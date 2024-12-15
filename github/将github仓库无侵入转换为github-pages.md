# 将github仓库无侵入转换为github-pages

啥叫无侵入？

就是在转换为github-pages后，通过github仓库依然可以正常查看readme.md

第一先开启github pages

jekyll-gh-pages.yml

第二开启github action



## 建立readme.md索引

```python
import os
import urllib.parse

def has_readme(directory):
    """检查目录中是否存在 README.md（不区分大小写）"""
    for item in os.listdir(directory):
        if item.lower() == 'readme.md':
            return True
    return False

def is_markdown_file(filename):
    """检查文件是否为 Markdown 文件（不区分大小写）"""
    return filename.lower().endswith('.md')

def generate_markdown_index(base_path, current_path='.', level=0, exclude_dirs=None):
    """
    递归生成 Markdown 目录索引，包含：
    - 仅包含 README.md 的目录，链接指向目录本身。
    - 其他 Markdown 文件，链接指向文件本身，链接文本为文件名（不含 .md）。
    """
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
        relative_path = os.path.join(current_path, item).replace('\\', '/')
        if os.path.isdir(item_path) and item not in exclude_dirs:
            if has_readme(item_path):
                indent = '  ' * level
                # 确保目录路径以 '/' 结尾，并进行 URL 编码
                dir_link = urllib.parse.quote(relative_path.rstrip('/') + '/')
                markdown += f"{indent}- 📁 [{item}/]({dir_link})\n"
                # 递归查找子目录
                markdown += generate_markdown_index(base_path, relative_path, level + 1, exclude_dirs)
            else:
                indent = '  ' * level
                # 不包含 README.md 的目录，仅显示目录名称，不包含链接
                markdown += f"{indent}- 📁 {item}/\n"
                # 递归查找子目录
                markdown += generate_markdown_index(base_path, relative_path, level + 1, exclude_dirs)
        elif os.path.isfile(item_path) and is_markdown_file(item) and item.lower() != 'readme.md':
            indent = '  ' * level
            # 文件名不包含后缀
            file_name = os.path.splitext(item)[0]
            # 进行 URL 编码
            file_link = urllib.parse.quote(relative_path)
            markdown += f"{indent}- 📄 [{file_name}]({file_link})\n"

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

```

github action:

```yaml
name: Update README Directory Index

on:
  push:
    branches:
      - main  # 根据你的默认分支名称调整
  schedule:
    - cron: '0 0 * * 7'  # 每周一次（可选）

jobs:
  update-readme:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Run directory index script
        run: python generate_directory_index.py

      - name: Commit and Push changes
        uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: "🛠️ 自动更新目录索引"
          file_pattern: "README.md"
```



但现在有一个问题：readme.md里的.md后缀，不会替换成.html或空

问题探究：

相关issue: [reason for blacklisting plugins?](https://github.com/github/pages-gem/issues/926)

​      ^ TODO:  该issue下给出了一个绕过白名单限制的解决方案，后面有时间可以研究下

相关issue: [Links with titles not handled properly](https://github.com/github/pages-gem/issues/876)

​         ^ 据该issue提示：问题出在jekyll-relative-links这个插件上，版本为0.6.1，但其已在[0.7.0](https://github.com/benbalter/jekyll-relative-links/releases/tag/v0.7.0)版本已修复，但官方一直不处理

经过分析提交记录，发现Pages-gem v229~v230已经更新到了0.7.0，但在v231又降回去了，commit: [pages-gem/commit/c29f89c3c](https://github.com/github/13c55cfc4aec49d58089a58c123e980)

​        ^ 因此现在只要在action里指定该[Pages-gem v230](https://github.com/github/pages-gem/releases/tag/v230)，也就是[Jekyll-build-pages v1.0.11](https://github.com/actions/jekyll-build-pages/releases/tag/v1.0.11)版本：

```yaml
uses: actions/jekyll-build-pages@v1.0.11
```



