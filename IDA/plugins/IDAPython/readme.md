# 文档
- IDAPython 官方文档：https://www.hex-rays.com/wp-content/static/products/ida/support/idapython_docs/

# 小知识点
- 常用api：[api](./../../api/)
## idapython 如何快速加载已更改模块/脚本
- idapythonrc.py
> window: %appdata%/Hex-Rays/IDA Pro/idapythonrc.py
```python
import idaapi
import sys
import importlib #only python3.4+
print("hello,idapython!")
sys.path.append(r"F:/project/python/idapro/ida-script-test/") # project dir

```
- 重新打开IDA
- 首次加载模块/脚本，python命令行输入如下代码
```python
import arm_unicorn # module name
```
- 更改模块/脚本后，python命令行输入如下代码
```python
importlib.reload(arm_unicorn) ; importlib.reload(arm_unicorn)
```
> 执行两次，是因为，需要先解除上次加载的代码
## dump 整个so文件
```python
size=ida_nalt.retrieve_input_file_size()
so_bin=idc.get_bytes(0,size)
```
# 第三方开发教程
refs:[编写IDApython的PY插件](https://cryzlasm.github.io/2017/11/24/%E7%BC%96%E5%86%99IDApython%E7%9A%84PY%E6%8F%92%E4%BB%B6/)
