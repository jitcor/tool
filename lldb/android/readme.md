# 环境配置
- 下载sdk
- 下载ndk
- lldb-server路径:sdk/lldb/3.1/android/{arch}/lldb-server
- lldb路径：sdk\ndk\23.0.7599858\toolchains\llvm\prebuilt\windows-x86_64\bin\lldb.cmd
# 配置lldb-server
```
adb push lldb-server /data/local/tmp/
adb shell su -c 'chmod +x ./data/local/tmp/lldb-server'
adb shell su -c './data/local/tmp/lldb-server platform --listen "*:1234" --server'
```
# 配置lldb
```
adb forward tcp:124 tcp:1234
lldb.cmd
platform list
platform select remote-android
platform connect connect://:1234
```
# 注入进程
```
platform process list
attach <pid>
```
> 获取进程pid: ps -A | grep \<packageName\>

# 具体调试
- 常用命令：wa,image,info,br
# 其它
## 常用命令
- help:查看所有帮助信息
## pycharm 导入lldb模块
ref:[pycharm下设置PYTHONPATH](https://blog.csdn.net/weixin_41698305/article/details/90902427)  
lldb模块路径：`sdk\ndk\23.0.7599858\toolchains\llvm\prebuilt\windows-x86_64\lib\python3.9\site-packages` 
- 直接在Window下python里import lldb会报找不到_lldb模块
- 可以在msys2命令行里启动pycharm.exe，然后在pycharm里正常编写代码即可(前提需要在msys2里用pacman先安装lldb)(若是pacman报密钥错误，不要搜解决方案，解决不了的，直接删除原来msys2，再[下载最新版msys2重新安装](https://www.msys2.org/)即可)(安装完成后再用[pacman更新](https://kaosx.us/docs/pacman/)下)
- 当然也可以再macOS里pycharm使用lldb，没什么坑
## python api for lldb
ref:[python-reference](https://lldb.llvm.org/use/python-reference.html)
## pycharm 编写lldb调试代码
```python
import os
import sys
import lldb

if __name__ == '__main__':
    os.system("D:\\tool\\AdbTool1.0.1\\adb forward tcp:8129 tcp:8129")
    os.popen("D:\\tool\\AdbTool1.0.1\\adb shell su -c './data/local/tmp/lldb-server platform --listen \"*:8129\" --server'")
    platform:lldb.SBPlatform=lldb.SBPlatform("remote-android")
    error:lldb.SBError=platform.ConnectRemote(lldb.SBPlatformConnectOptions("connect://:8129"))
    print("error3:",error.success)
    print("isConnect:",platform.IsConnected())
    env:lldb.SBEnvironment=platform.GetEnvironment()
    print(env.GetNumValues())
    print(platform.GetWorkingDirectory())
    error=platform.Run(lldb.SBPlatformShellCommand("attach 32742"))
    print(error)

```
## 参考
- [远程调试](https://lldb.llvm.org/use/remote.html)
- [lldb调试命令](https://lldb.llvm.org/use/map.html)
