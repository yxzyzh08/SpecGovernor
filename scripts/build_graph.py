#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从解析的标记构建依赖图谱。

[ID: CODE-SCRIPT-003] [Implements: DESIGN-SCRIPT-GRAPH-001]
"""
import json
import os
import sys

# 设置 Windows 控制台编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def load_tags():
    """从 tags.json 加载标记。"""
    tags_file = '.specgov/index/tags.json'
    if not os.path.exists(tags_file):
        print(f"❌ 错误：未找到 {tags_file}")
        print("   请先运行: python scripts/parse_tags.py")
        exit(1)

    with open(tags_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['tags']


def build_graph(tags):
    """从标记构建依赖图谱。"""
    nodes = []
    edges = []

    # 创建节点
    for tag in tags:
        node = {
            'id': tag['id'],
            'type': tag['type'],
            'location': f"{tag['file']}#L{tag['line']}"
        }
        if 'module' in tag:
            node['module'] = tag['module']
        nodes.append(node)

    # 创建边
    for tag in tags:
        source_id = tag['id']

        # Implements 关系
        if 'implements' in tag:
            edges.append({
                'from': source_id,
                'to': tag['implements'],
                'relation': 'implements'
            })

        # Decomposes 关系
        if 'decomposes' in tag:
            edges.append({
                'from': source_id,
                'to': tag['decomposes'],
                'relation': 'decomposes'
            })

        # Designs-for 关系
        if 'designs_for' in tag:
            edges.append({
                'from': source_id,
                'to': tag['designs_for'],
                'relation': 'designs-for'
            })

        # Tests-for 关系
        if 'tests_for' in tag:
            edges.append({
                'from': source_id,
                'to': tag['tests_for'],
                'relation': 'tests-for'
            })

    return {'nodes': nodes, 'edges': edges}


def detect_circular_dependencies(graph):
    """使用 DFS 检测循环依赖。"""
    # 构建邻接表
    adj = {}
    for edge in graph['edges']:
        if edge['from'] not in adj:
            adj[edge['from']] = []
        adj[edge['from']].append(edge['to'])

    visited = set()
    rec_stack = set()
    cycles = []

    def dfs(node, path):
        visited.add(node)
        rec_stack.add(node)

        if node in adj:
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor, path + [neighbor])
                elif neighbor in rec_stack:
                    # 发现循环
                    try:
                        cycle_start = path.index(neighbor)
                        cycle = path[cycle_start:] + [neighbor]
                        if cycle not in cycles:
                            cycles.append(cycle)
                    except ValueError:
                        pass

        rec_stack.remove(node)

    for node_data in graph['nodes']:
        node = node_data['id']
        if node not in visited:
            dfs(node, [node])

    return cycles


def count_by_type(graph):
    """按类型统计节点。"""
    counts = {}
    for node in graph['nodes']:
        node_type = node['type']
        counts[node_type] = counts.get(node_type, 0) + 1
    return counts


def main():
    """主函数。"""
    print("━" * 60)
    print("Building dependency graph...")
    print("━" * 60)
    print()

    tags = load_tags()
    graph = build_graph(tags)

    print(f"✓ Created {len(graph['nodes'])} nodes")
    print(f"✓ Created {len(graph['edges'])} edges")
    print()

    # 检测循环依赖
    cycles = detect_circular_dependencies(graph)
    if cycles:
        print(f"⚠️  Detected {len(cycles)} circular dependencies:")
        for cycle in cycles[:5]:  # 只显示前5个
            print(f"   {' → '.join(cycle)}")
        if len(cycles) > 5:
            print(f"   ... and {len(cycles) - 5} more")
        print()
    else:
        print("✓ Detected 0 circular dependencies")
        print()

    # 保存图谱
    os.makedirs('.specgov/index', exist_ok=True)
    with open('.specgov/index/dependency-graph.json', 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    print("✓ Saved to .specgov/index/dependency-graph.json")
    print()

    # 统计信息
    counts = count_by_type(graph)
    print("📊 Statistics:")
    for node_type, count in sorted(counts.items()):
        print(f"  - {node_type}: {count}")
    print()

    return 0


if __name__ == '__main__':
    exit(main())
