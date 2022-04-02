# 遍历所有包含自定内容的文件
```
# -n 显示行号 -C 5 也显示上下5行, -B 5 也显示上5行，-A 5 也显示下5行
find ./ -name "*.*" | xargs grep -n "for arch"
```
