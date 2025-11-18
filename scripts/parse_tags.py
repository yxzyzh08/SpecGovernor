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
        # 默认扫描根目录、docs 和 src
        root_dirs = ['.']

    # 排除目录列表
    exclude_dirs = ['archives', 'v2-backup', '.git', 'node_modules', '__pycache__', '.specgov', '.claude', 'reviews']

    files = []
    for root_dir in root_dirs:
        if not os.path.exists(root_dir):
            continue

        # 如果是根目录，先添加根目录下的直接 .md 文件
        if root_dir == '.':
            for filepath in Path(root_dir).glob('*.md'):
                if filepath.is_file():
                    files.append(str(filepath))

        # 然后递归扫描子目录
        for filepath in Path(root_dir).rglob('*'):
            # 跳过排除的目录
            if any(exclude_dir in filepath.parts for exclude_dir in exclude_dirs):
                continue
            if filepath.is_file() and (
                filepath.suffix in ['.md', '.py', '.ts', '.tsx', '.js', '.jsx', '.java', '.go', '.c', '.cpp', '.h']
            ):
                # 避免重复添加根目录的 .md 文件
                filepath_str = str(filepath)
                if filepath_str not in files:
                    files.append(filepath_str)
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
    # v3.0: PRD 标记（业务需求和产品功能）
    if tag_id.startswith('PRD-MODULE-'):
        return 'module'
    elif tag_id.startswith('PRD-GOAL-'):
        return 'goal'
    elif tag_id.startswith('PRD-USER-'):
        return 'user'
    elif tag_id.startswith('PRD-REQ-'):
        return 'requirement'  # v3.0: 业务需求（原 RD-REQ-XXX）
    elif tag_id.startswith('PRD-NFR-'):
        return 'non_functional_requirement'
    elif tag_id.startswith('PRD-FEAT-'):
        return 'feature'  # 产品功能
    elif tag_id.startswith('PRD-US-'):
        return 'user_story'
    elif tag_id.startswith('PRD-EPIC-'):
        return 'epic'
    elif tag_id.startswith('PRD-SCENARIO-'):
        return 'scenario'
    elif tag_id.startswith('PRD-TRACE-'):
        return 'traceability'
    elif tag_id.startswith('PRD-STRUCTURE-'):
        return 'document_structure'
    elif tag_id.startswith('PRD-SUMMARY-'):
        return 'summary'
    elif tag_id.startswith('PRD-METRICS-'):
        return 'metrics'
    elif tag_id.startswith('PRD-NEXT-'):
        return 'next_steps'
    elif tag_id.startswith('PRD-VISION-'):
        return 'vision'
    # Design 标记
    elif tag_id.startswith('DESIGN-ARCH-'):
        return 'architecture'
    elif tag_id.startswith('DESIGN-API-'):
        return 'api_design'
    elif tag_id.startswith('DESIGN-DB-'):
        return 'database_design'
    elif tag_id.startswith('DESIGN-'):
        return 'design'
    # Test 标记
    elif tag_id.startswith('TEST-CASE-'):
        return 'test_case'
    elif tag_id.startswith('TEST-PERF-'):
        return 'performance_test'
    elif tag_id.startswith('TEST-'):
        return 'test'
    # Code 标记
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

    # 提取模块信息并更新 project-config.json（仅适用于大项目）
    update_project_modules(all_tags)

    return 0


def update_project_modules(all_tags):
    """从标记中提取模块信息并更新 project-config.json。"""
    config_path = '.specgov/project-config.json'

    # 检查配置文件是否存在
    if not os.path.exists(config_path):
        return

    # 读取当前配置
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except Exception as e:
        print(f"⚠️  Warning: Could not read {config_path}: {e}")
        return

    # 仅处理大项目（双层文档结构）
    if config.get('document_structure') != 'two-tier':
        return

    # 提取所有模块标记（PRD-MODULE-XXX）- v3.0 更新
    module_tags = [tag for tag in all_tags if tag.get('type') == 'module' and tag['id'].startswith('PRD-MODULE-')]

    if not module_tags:
        return

    # 构建模块列表
    modules = []
    for tag in module_tags:
        # 从 PRD-MODULE-USER 提取 "USER"
        module_id = tag['id'].replace('PRD-MODULE-', '')
        module_name = module_id.title()  # USER -> User

        module_info = {
            'id': module_id,
            'name': module_name,
            'tag': tag['id'],
            'file': tag.get('file', ''),
            'line': tag.get('line', 0)
        }
        modules.append(module_info)

    # 更新配置文件
    old_modules = config.get('modules', [])
    config['modules'] = modules

    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

        if modules:
            print("📦 Updated project modules:")
            for module in modules:
                print(f"  - {module['name']} ({module['id']}) in {module['file']}:{module['line']}")
            print(f"✓ Updated {len(modules)} modules in {config_path}")
            print()
    except Exception as e:
        print(f"⚠️  Warning: Could not update {config_path}: {e}")
        print()


if __name__ == '__main__':
    exit(main())
