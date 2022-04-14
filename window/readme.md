# 如何解决C盘频繁报红问题
mklink /d C:\Users\$(user) H:\Users\$(user) (需先移动$(user)目录，再mklink链接)
# window强制/频繁更新问题
windowUpdateBlocker
# WindowDefender问题
DefenderControl
# 启动大小写敏感
- 以管理员方式启动cmd
- cd 到目标目录
- 执行 `fsutil.exe file SetCaseSensitiveInfo ./ enable`开启当前目录的大小写敏感
- 执行 `fsutil.exe file queryCaseSensitiveInfo ./` 查询当前目录的大小写敏感状态
> 注意：当某目录开启大小写敏感后，在该目录下的所有可执行文件，在cmd控制台中必须要输入带后缀的文件名才能正常调用
# VT-x已开启但CPU-V和模拟器显示未开启
管理员方式执行以下命令，重启电脑即可
```
bcdedit /set hypervisorlaunchtype off
```
# Window端口转发
```
netsh interface portproxy add v4tov4  listenaddress=localaddress listenport= localport connectaddress=destaddress  connectport=destport protocol=tcp
```
# 远程桌面无法共享剪切板
请查看本地或远程设备的进程列表是否有rdpclip.exe，没有则\[任务管理器->文件->新建任务\]输入rdpclip，确定即可
- 一键重启脚本
```bat
taskkill /im rdpclip.exe -f
rdpclip.exe

```
# 休眠/睡眠后自动唤醒问题
- 执行以下命令获取最后唤醒详情
```
powercfg /lastwake
```
> 若是设备唤醒，可在设备管理器里的设备>属性>电源管理>取消勾选“允许此设备唤醒计算机” \
> 注意，若是网卡驱动唤醒的，取消勾选会导致无法远程连接到已休眠的目标机器 
- 定时唤醒计算机看[wakeup.md](./wakeup.md) \
参考：https://zhuanlan.zhihu.com/p/93306740
