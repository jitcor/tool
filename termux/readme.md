# 安装
https://f-droid.org/en/packages/com.termux/
# 设置代理
```
export http_proxy=http://127.0.0.1:1080
export https_proxy=http://127.0.0.1:1080
```
# 替换源
```
//todo
```
# 初始化
```
pkg update
```
# 查看默认账户
```
whoami
```
# ssh
```
# 安装
pkg install openssh

# 运行ssh服务端，默认8022端口
sshd
# 查看状态
nmap 127.0.0.1

# 停止运行
pkill sshd

# 初始化账户密码
passwd

# 电脑端连接
ssh username@x.x.x.x -p 8022
```


