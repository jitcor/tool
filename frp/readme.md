# 服务端配置模板
```ini
[common]
bind_addr = 0.0.0.0
bind_port = xxxx
dashboard_port = xxxx
dashboard_user = xxxx
dashboard_pwd = xxxxxx
token = xxxxxx
max_pool_count = 50

```
# 客户端配置模板
```ini
[common]
server_addr = xx.xx.xx.xx
server_port = xxx
token = xxxxxx
[chp]
type = tcp
local_ip = 127.0.0.1
local_port = xxxx
remote_port = xxxx
```
# Window 远程桌面配置模板
```ini
[common]
server_addr = xx.xx.xx.xx
server_port = xxxx
token = xxxxx
[chp]
type = tcp
local_ip = 127.0.0.1
local_port = 3389
remote_port = xxxx
```
# 安装服务端
- 服务端环境：ubuntu server
- 一键安装脚本[地址](https://github.com/MvsCode/frps-onekey)
- 不过他这个的配置是http的，不太适合我，可以等安装完后直接将/usr/local/frp/下的frps.ini配置文件的内容修改成上面的模板代码即可,然后根据自己需要进行修改
- `frps start`(启动frp服务端)
- 在服务器控制台开启相应端口(这里需要开启的端口就是:5443,6443,4567)
> 后台启动服务参考systemctl命令
# 安装客户端
- 下载客户端[地址](https://github.com/fatedier/frp/releases/tag/v0.34.0)
- `frpc.exe -c frpc.ini`(记得将配置文件修改成上面模板)
# 本地开启http服务
- 这里我使用的python代码借助FastApi框架开启的
- 具体代码如下
```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=4567)

```
- FastApi 具体使用参考[地址1](https://fastapi.tiangolo.com/zh/)
# 远程访问
- 访问`http://xx.xx.xx.xx:4567/`
- 正常情况下就会打印`Hello World`
