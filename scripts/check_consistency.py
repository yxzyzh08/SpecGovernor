#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为指定需求收集完整依赖链上下文。

[ID: CODE-SCRIPT-005] [Implements: DESIGN-SCRIPT-CONSISTENCY-001]
"""
import json
import argparse
import os
import sys

# 设置 Windows 控制台编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def load_graph():
    """加载依赖图谱。"""
    graph_file = '.specgov/index/dependency-graph.json'
    if not os.path.exists(graph_file):
        print(f"❌ 错误：未找到 {graph_file}")
        print("   请先运行: python scripts/parse_tags.py && python scripts/build_graph.py")
        exit(1)

    with open(graph_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_dependency_chain(graph, scope_id):
    """找到指定 ID 的完整依赖链（上游和下游）。"""
    chain = {'upstream': [], 'downstream': []}

    # 构建邻接表
    downstream_adj = {}  # id -> [依赖它的节点]
    upstream_adj = {}    # id -> [它依赖的节点]

    for edge in graph['edges']:
        source = edge['from']
        target = edge['to']
        relation = edge['relation']

        # 下游：source 依赖 target，所以 target 的下游包含 source
        if target not in downstream_adj:
            downstream_adj[target] = []
        downstream_adj[target].append((source, relation))

        # 上游：source 依赖 target，所以 source 的上游包含 target
        if source not in upstream_adj:
            upstream_adj[source] = []
        upstream_adj[source].append((target, relation))

    # BFS 查找上游（scope_id 实现了哪些节点）
    visited_up = set()
    queue_up = [scope_id]
    while queue_up:
        node_id = queue_up.pop(0)
        if node_id in visited_up:
            continue
        visited_up.add(node_id)

        if node_id in upstream_adj:
            for target, relation in upstream_adj[node_id]:
                if target not in visited_up:
                    chain['upstream'].append((target, relation))
                    queue_up.append(target)

    # BFS 查找下游（哪些节点实现了 scope_id）
    visited_down = set()
    queue_down = [scope_id]
    while queue_down:
        node_id = queue_down.pop(0)
        if node_id in visited_down:
            continue
        visited_down.add(node_id)

        if node_id in downstream_adj:
            for source, relation in downstream_adj[node_id]:
                if source not in visited_down:
                    chain['downstream'].append((source, relation))
                    queue_down.append(source)

    return chain


def get_node_info(graph, node_id):
    """获取节点信息。"""
    for node in graph['nodes']:
        if node['id'] == node_id:
            return node
    return None


def extract_content(filepath, line_num, context_lines=20):
    """从文件中提取内容，以 line_num 为中心。"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 查找包含标记的区域（向前向后扩展）
        start = max(0, line_num - context_lines)
        end = min(len(lines), line_num + context_lines)

        # 尝试找到章节边界（以 ## 或 # 开头）
        for i in range(line_num - 1, max(0, line_num - 50), -1):
            if lines[i].startswith('##') or (lines[i].startswith('#') and not lines[i].startswith('###')):
                start = i
                break

        for i in range(line_num, min(len(lines), line_num + 50)):
            if (lines[i].startswith('##') or lines[i].startswith('#')) and i > line_num:
                end = i
                break

        content = ''.join(lines[start:end])
        return content.strip()

    except Exception as e:
        return f"Error reading file: {e}"


def build_context(graph, scope_id, chain):
    """构建上下文文件内容。"""
    context = []

    context.append("━" * 60)
    context.append(f"# Consistency Check Context for {scope_id}")
    context.append("━" * 60)
    context.append("")

    # 添加上游节点（scope_id 实现了什么）
    if chain['upstream']:
        context.append("## Upstream Dependencies (What this implements)")
        context.append("")
        for i, (node_id, relation) in enumerate(chain['upstream'], 1):
            node = get_node_info(graph, node_id)
            if node:
                context.append(f"### {i}. {node_id} ({node['type']})")
                context.append(f"**Source**: {node['location']}")
                context.append(f"**Relation**: {scope_id} {relation} {node_id}")
                context.append("")

                # 提取内容
                file_path, line_str = node['location'].split('#L')
                line_num = int(line_str)
                content = extract_content(file_path, line_num)
                context.append(content)
                context.append("")
                context.append("---")
                context.append("")

    # 添加当前节点
    current_node = get_node_info(graph, scope_id)
    if current_node:
        context.append(f"## Current Node: {scope_id} ({current_node['type']})")
        context.append(f"**Source**: {current_node['location']}")
        context.append("")

        file_path, line_str = current_node['location'].split('#L')
        line_num = int(line_str)
        content = extract_content(file_path, line_num)
        context.append(content)
        context.append("")
        context.append("---")
        context.append("")

    # 添加下游节点（谁实现了 scope_id）
    if chain['downstream']:
        context.append("## Downstream Dependencies (What implements this)")
        context.append("")
        for i, (node_id, relation) in enumerate(chain['downstream'], 1):
            node = get_node_info(graph, node_id)
            if node:
                context.append(f"### {i}. {node_id} ({node['type']})")
                context.append(f"**Source**: {node['location']}")
                context.append(f"**Relation**: {node_id} {relation} {scope_id}")
                context.append("")

                # 提取内容
                file_path, line_str = node['location'].split('#L')
                line_num = int(line_str)
                content = extract_content(file_path, line_num)
                context.append(content)
                context.append("")
                context.append("---")
                context.append("")

    context.append("━" * 60)

    return '\n'.join(context)


def estimate_tokens(text):
    """粗略估计 token 数（1 token ≈ 4 字符）。"""
    return len(text) // 4


def main():
    """主函数。"""
    parser = argparse.ArgumentParser(
        description='为指定需求收集完整依赖链上下文'
    )
    parser.add_argument('--scope', required=True, help='要检查的需求 ID（如 RD-REQ-005）')
    parser.add_argument('--output', default='context.md', help='输出文件路径')
    args = parser.parse_args()

    print(f"🔍 收集 {args.scope} 的依赖链上下文...")
    print()

    # 加载图谱
    graph = load_graph()

    # 验证 scope_id 存在
    node = get_node_info(graph, args.scope)
    if not node:
        print(f"❌ 错误：找不到 {args.scope}")
        return 1

    # 查找依赖链
    chain = find_dependency_chain(graph, args.scope)

    # 构建上下文
    context_content = build_context(graph, args.scope, chain)

    # 估计 tokens
    token_count = estimate_tokens(context_content)

    # 检查 token 限制
    if token_count > 5000:
        print(f"⚠️  警告：上下文过大（约 {token_count} tokens），超过 5K 限制")
        print("   考虑使用更具体的 scope 或减少 context_lines")
        print()

    # 保存到文件
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(context_content)

    # 统计信息
    print(f"✓ 收集了 {args.scope} 的依赖链")
    print(f"✓ 找到 {len(chain['upstream'])} 个上游依赖")
    print(f"✓ 找到 {len(chain['downstream'])} 个下游依赖")
    print(f"✓ 生成上下文文件：{args.output}（约 {token_count} tokens）")
    print(f"✓ 保存到 {args.output}")
    print()
    print("📚 下一步：")
    print("  1. 打开 Claude Code")
    print("  2. 加载 .specgov/prompts/consistency-checker.md")
    print(f"  3. 提供 {args.output} 内容")
    print("  4. Claude Code 将检查一致性并输出报告")
    print()
    print("⏱️  时间：< 5 秒")
    print("💰 成本：$0（本地上下文构建）")
    print()

    return 0


if __name__ == '__main__':
    exit(main())
