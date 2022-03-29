# 安装
https://f-droid.org/en/packages/com.termux/
# 设置代理
```
export http_proxy=http://127.0.0.1:1080
export https_proxy=http://127.0.0.1:1080
```
# 替换源
```
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list

sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list

sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list

pkg update
```
# 查看软件所有有效版本
```
apt-cache madison software_name
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
# 自行编译包


