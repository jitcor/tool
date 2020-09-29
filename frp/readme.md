# 服务端配置模板
```ini
[common]
bind_addr = 0.0.0.0
bind_port = 5443
dashboard_port = 6443
dashboard_user = admin
dashboard_pwd = 123456
token = token123456
max_pool_count = 50

```
# 客户端配置模板
```ini
[common]
server_addr = 47.242.68.11
server_port = 5443
token = token123456
[chp]
type = tcp
local_ip = 127.0.0.1
local_port = 4567
remote_port = 4567
```
# 安装服务端
- 服务端环境：ubuntu server
- 一键安装脚本[地址](https://github.com/MvsCode/frps-onekey)
- 不过他这个的配置是http的，不太适合我，可以等安装完后直接将/usr/local/frp/下的frps.ini配置文件的内容修改成上面的模板代码即可
- `frps start`(启动frp服务端)
- 在服务器控制台开启相应端口(这里需要开启的端口就是:5443,6443,4567)
# 安装客户端
- 下载客户端[地址](https://github.com/fatedier/frp/releases/tag/v0.34.0)
- `frpc.exe -c frpc.ini`(记得将配置文件修改成上面模板)
