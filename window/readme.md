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
