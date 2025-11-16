#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 Markdown 和代码文件中解析可追溯性标记。

[ID: CODE-SCRIPT-002] [Implements: DESIGN-SCRIPT-PARSER-001]
"""
import os
import re
import json
import sys
from pathlib import Path

# 设置 Windows 控制台编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

TAG_PATTERNS = {
    'id': r'\[ID:\s*([A-Z0-9-]+)\]',
    'implements': r'\[Implements:\s*([A-Z0-9-]+)\]',
    'decomposes': r'\[Decomposes:\s*([A-Z0-9-]+)\]',
    'designs_for': r'\[Designs-for:\s*([A-Z0-9-]+)\]',
    'tests_for': r'\[Tests-for:\s*([A-Z0-9-]+)\]',
    'module': r'\[Module:\s*([A-Za-z0-9-]+)\]'
}


def scan_files(root_dirs=None):
    """扫描所有 Markdown 和代码文件。"""
    if root_dirs is None:
        root_dirs = ['docs', 'src']

    files = []
    for root_dir in root_dirs:
        if not os.path.exists(root_dir):
            continue
        for filepath in Path(root_dir).rglob('*'):
            if filepath.is_file() and (
                filepath.suffix in ['.md', '.py', '.ts', '.tsx', '.js', '.jsx', '.java', '.go', '.c', '.cpp', '.h']
            ):
                files.append(str(filepath))
    return files


def parse_file(filepath):
    """从单个文件中解析可追溯性标记。"""
    tags = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # 查找 ID 标记
                id_match = re.search(TAG_PATTERNS['id'], line)
                if id_match:
                    tag_id = id_match.group(1)
                    tag_entry = {
                        'id': tag_id,
                        'file': filepath,
                        'line': line_num,
                        'type': infer_type(tag_id)
                    }

                    # 在同一行查找关系标记
                    for rel_type, pattern in TAG_PATTERNS.items():
                        if rel_type in ['id', 'module']:
                            continue
                        match = re.search(pattern, line)
                        if match:
                            tag_entry[rel_type] = match.group(1)

                    # 查找模块标记
                    module_match = re.search(TAG_PATTERNS['module'], line)
                    if module_match:
                        tag_entry['module'] = module_match.group(1)

                    tags.append(tag_entry)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

    return tags


def infer_type(tag_id):
    """从 ID 前缀推断标记类型。"""
    if tag_id.startswith('RD-'):
        return 'requirement'
    elif tag_id.startswith('PRD-FEAT-'):
        return 'feature'
    elif tag_id.startswith('PRD-US-'):
        return 'user_story'
    elif tag_id.startswith('DESIGN-ARCH-'):
        return 'architecture'
    elif tag_id.startswith('DESIGN-API-'):
        return 'api_design'
    elif tag_id.startswith('DESIGN-DB-'):
        return 'database_design'
    elif tag_id.startswith('DESIGN-'):
        return 'design'
    elif tag_id.startswith('TEST-CASE-'):
        return 'test_case'
    elif tag_id.startswith('TEST-'):
        return 'test'
    elif tag_id.startswith('CODE-'):
        return 'code'
    else:
        return 'unknown'


def main():
    """主函数。"""
    print("━" * 60)
    print("Parsing traceability tags...")
    print("━" * 60)
    print()

    files = scan_files()
    print(f"✓ Scanning {len(files)} files")

    all_tags = []
    for filepath in files:
        tags = parse_file(filepath)
        all_tags.extend(tags)

    # 统计标记
    id_count = len(all_tags)
    implements_count = sum(1 for t in all_tags if 'implements' in t)
    decomposes_count = sum(1 for t in all_tags if 'decomposes' in t)
    designs_for_count = sum(1 for t in all_tags if 'designs_for' in t)
    tests_for_count = sum(1 for t in all_tags if 'tests_for' in t)

    # 保存到 JSON
    output = {'tags': all_tags}
    os.makedirs('.specgov/index', exist_ok=True)
    with open('.specgov/index/tags.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print()
    print(f"✓ Found {id_count} [ID: XXX] tags")
    print(f"✓ Found {implements_count} [Implements: XXX] tags")
    print(f"✓ Found {decomposes_count} [Decomposes: XXX] tags")
    print(f"✓ Found {designs_for_count} [Designs-for: XXX] tags")
    print(f"✓ Found {tests_for_count} [Tests-for: XXX] tags")
    print()
    print(f"✓ Saved to .specgov/index/tags.json")
    print()

    # 按类型统计
    type_counts = {}
    for tag in all_tags:
        tag_type = tag['type']
        type_counts[tag_type] = type_counts.get(tag_type, 0) + 1

    if type_counts:
        print("📊 Statistics by type:")
        for tag_type, count in sorted(type_counts.items()):
            print(f"  - {tag_type}: {count}")
        print()

    return 0


if __name__ == '__main__':
    exit(main())
