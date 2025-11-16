#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 git diff 和依赖图谱分析文件变更的影响。

[ID: CODE-SCRIPT-004] [Implements: DESIGN-SCRIPT-IMPACT-001]
"""
import json
import subprocess
import argparse
import re
import os
import sys

# 设置 Windows 控制台编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

TAG_PATTERN = r'\[ID:\s*([A-Z0-9-]+)\]'


def get_changed_lines(filepath):
    """使用 git diff 获取变更的行号。"""
    try:
        result = subprocess.run(
            ['git', 'diff', 'HEAD', filepath],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        diff = result.stdout

        # 解析 diff 以查找变更的行
        changed_lines = []
        current_line = 0
        for line in diff.split('\n'):
            if line.startswith('@@'):
                # 从 @@ -a,b +c,d @@ 中提取行号
                match = re.search(r'\+(\d+)', line)
                if match:
                    current_line = int(match.group(1))
            elif line.startswith('+') and not line.startswith('+++'):
                changed_lines.append(current_line)
                current_line += 1
            elif not line.startswith('-'):
                current_line += 1

        return changed_lines
    except Exception as e:
        print(f"Error running git diff: {e}")
        return []


def find_changed_tags(filepath, changed_lines):
    """在变更的行中查找标记。"""
    changed_tags = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                if line_num in changed_lines or not changed_lines:  # 如果没有 git diff，解析所有行
                    match = re.search(TAG_PATTERN, line)
                    if match:
                        changed_tags.append(match.group(1))
    except Exception as e:
        print(f"Error reading file: {e}")

    return changed_tags


def load_graph():
    """加载依赖图谱。"""
    graph_file = '.specgov/index/dependency-graph.json'
    if not os.path.exists(graph_file):
        print(f"❌ 错误：未找到 {graph_file}")
        print("   请先运行: python scripts/parse_tags.py && python scripts/build_graph.py")
        exit(1)

    with open(graph_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_downstream(graph, source_ids):
    """查找所有下游节点（BFS）。"""
    # 构建邻接表（反向，用于下游）
    adj = {}
    for edge in graph['edges']:
        # 下游：如果 A implements B，则 B 影响 A
        target = edge['from']
        source = edge['to']
        relation = edge['relation']

        if source not in adj:
            adj[source] = []
        adj[source].append((target, relation))

    # 从 source_ids 开始 BFS
    queue = [(sid, None) for sid in source_ids]
    visited = set(source_ids)
    affected = []

    while queue:
        node_id, reason = queue.pop(0)

        if node_id in adj:
            for neighbor, relation in adj[node_id]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    affected.append((neighbor, f"{relation.capitalize()} {node_id}"))
                    queue.append((neighbor, f"{relation} {node_id}"))

    return affected


def get_node_info(graph, node_id):
    """获取节点信息。"""
    for node in graph['nodes']:
        if node['id'] == node_id:
            return node
    return None


def main():
    """主函数。"""
    parser = argparse.ArgumentParser(description='分析文件变更的影响')
    parser.add_argument('--changed', required=True, help='变更的文件路径')
    args = parser.parse_args()

    print("━" * 60)
    print("🔍 Impact Analysis Report")
    print("━" * 60)
    print()
    print(f"Analyzing: {args.changed}")
    print()

    # 获取变更的行
    changed_lines = get_changed_lines(args.changed)
    if not changed_lines:
        print("ℹ️  No git diff found, analyzing all tags in the file...")
        changed_lines = []  # Empty list will cause parse to check all lines

    # 查找变更的标记
    changed_tags = find_changed_tags(args.changed, changed_lines)
    if not changed_tags:
        print("No traceability tags found in changed lines")
        return 0

    # 加载图谱
    graph = load_graph()

    # 查找下游节点
    affected = find_downstream(graph, changed_tags)

    # 打印报告
    print(f"变更的节点 ({len(changed_tags)}):")
    for tag_id in changed_tags:
        node = get_node_info(graph, tag_id)
        if node:
            print(f"  • {tag_id} ({node['type']}) at {node['location']}")
        else:
            print(f"  • {tag_id} (not found in graph)")
    print()

    if affected:
        print(f"受影响的节点 ({len(affected)}):")
        for node_id, reason in affected:
            node = get_node_info(graph, node_id)
            if node:
                print(f"  ⚠️  {node_id} ({node['type']}) at {node['location']}")
                print(f"      原因：{reason}")
        print()
    else:
        print("✓ 无下游节点受影响")
        print()

    print("建议的行动：")
    if affected:
        print("  1. Review and update affected documents")
        print("  2. Run tests for affected code")
        print("  3. Update dependency graph (python scripts/parse_tags.py && python scripts/build_graph.py)")
    else:
        print("  无需额外行动")
    print()

    print("━" * 60)
    print()
    print("⏱️  Time: < 10 seconds")
    print("💰 Cost: $0 (graph query only)")
    print()

    return 0


if __name__ == '__main__':
    exit(main())
