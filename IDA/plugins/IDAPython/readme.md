# ARM

# 小知识点
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

