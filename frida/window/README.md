# 脚本
### 拦截任意进程执行的命令行数据
```python
# coding=utf-8
import frida
import sys


def on_message(message, data):
    type = message["type"]
    msg = message
    if type == "send":
        msg = message["payload"]
    elif type == 'error':
        msg = message['stack']
    else:
        msg = message
    print(msg)

#输出frida版本
print('frida version:'+frida.__version__)
# 获取设备
device = frida.get_local_device()
# 注入进程
process=device.attach("HiSuite.exe")
js = open("_agent.js").read()
script = process.create_script(js)
# 绑定函数
script.on('message', on_message)
# 加载脚本
script.load()
print("FridaDebugTool running....")
# 执行脚本
sys.stdin.read()
```
```js
var popen=Module.getExportByName(null,"_popen")
var CreateProcess=Module.getExportByName(null,"CreateProcessW")
console.log('popen.base:',popen)
console.log('CreateProcess.base:',CreateProcess)
Interceptor.attach(CreateProcess,{
    // Interceptor.attach(adb_command,{
    onEnter:function (args){
        console.log('CreateProcess:\n',args[1].readUtf16String())
        // console.log('CreateProcess:\n',hexdump(args[1]))
    },
    onLeave:function (retval){}

})

```
