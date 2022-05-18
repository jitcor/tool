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
> 获取进程pid: ps -A | grep <packageName>

# 具体调试

## 参考
- [远程调试](https://lldb.llvm.org/use/remote.html)
