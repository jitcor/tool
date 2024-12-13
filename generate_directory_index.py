import os

def has_readme(directory):
    """检查目录中是否存在 README.md（不区分大小写）"""
    for item in os.listdir(directory):
        if item.lower() == 'readme.md':
            return True
    return False

def generate_markdown_index(base_path, current_path='.', level=0, exclude_dirs=None):
    """递归生成 Markdown 目录索引，只包含包含 README.md 的目录，并链接到目录本身"""
    if exclude_dirs is None:
        exclude_dirs = ['.git', '.github', 'node_modules', '__pycache__']

    markdown = ""
    full_path = os.path.join(base_path, current_path)
    try:
        items = sorted(os.listdir(full_path))
    except PermissionError:
        return markdown

    for item in items:
        item_path = os.path.join(full_path, item)
        relative_path = os.path.join(current_path, item)
        if os.path.isdir(item_path) and item not in exclude_dirs:
            if has_readme(item_path):
                indent = '  ' * level
                # 确保目录路径以 '/' 结尾
                link = relative_path.replace('\\', '/').rstrip('/') + '/'
                markdown += f"{indent}- [{item}]({link})\n"
                # 递归查找子目录
                markdown += generate_markdown_index(base_path, relative_path, level + 1, exclude_dirs)
    return markdown

def main():
    base_path = '.'  # 仓库根目录
    start_marker = '<!-- DIRECTORY INDEX START -->'
    end_marker = '<!-- DIRECTORY INDEX END -->'

    directory_index = generate_markdown_index(base_path)

    directory_section = f"{start_marker}\n## 目录索引\n{directory_index}{end_marker}\n"

    readme_path = 'README.md'

    # 读取现有 README.md 内容
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    else:
        readme_content = ''

    # 替换或添加目录索引部分
    if start_marker in readme_content and end_marker in readme_content:
        # 替换现有的目录索引
        parts = readme_content.split(start_marker)
        if len(parts) > 1:
            before = parts[0]
            after = parts[1].split(end_marker, 1)[1] if end_marker in parts[1] else ''
            new_readme = before + directory_section + after
        else:
            new_readme = readme_content + "\n" + directory_section
    else:
        # 添加目录索引到 README.md
        new_readme = readme_content + "\n" + directory_section

    # 写回 README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_readme)

    print("README.md 已更新目录索引。")

if __name__ == "__main__":
    main()
