# 安装
https://f-droid.org/en/packages/com.termux/
# 设置代理
```
export http_proxy=http://127.0.0.1:1080
export https_proxy=http://127.0.0.1:1080
```
# ~~替换源~~ 
```
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list

sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list

sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list

pkg update
```
# 替换源
> 新版增加了GUI选择源界面，很方便
```
termux-change-repo
pkg update -y
```
# 查看软件所有有效版本
```
apt-cache madison software_name
```
# 初始化
```
pkg update -y
```
# 查看默认账户
```
whoami
```
# ssh
```
# 安装
pkg install openssh -y

# 运行ssh服务端，默认8022端口
sshd
# 查看状态
pkg install nmap
nmap 127.0.0.1

# 停止运行
pkill sshd

# 初始化账户密码
passwd

# 电脑端连接
ssh username@x.x.x.x -p 8022
```
# 自动登录
```
echo <rsa_pub_data> > ~/.ssh/authorized_keys
# 权限配置
drwx------ 2 u0_a278 u0_a278 3452 Sep 21 15:44 .ssh
-rw------- 1 u0_a278 u0_a278    0 Sep 21 15:44 authorized_keys
# 客户端配置
# 文件：~/.ssh/config
Host 127.0.0.1
    HostName 127.0.0.1
    User u0_a278
    Port 8022
    IdentityFile C:\Users\shlu\.ssh\id_rsa
```
# scp
```
scp xxx.file a0_u108@127.0.0.1:~/
```
# adb端口转发
```
adb -s cccc forward tcp:8022 tcp:8022
adb -s cccc forward tcp:9022 tcp:9022
```
# vscode
```
# 安装虚拟root
pkg install proot-distro
# 安装debian
proot-distro install debian
# 登录debian
proot-distro login debian
# 更新软件
apt update
# 安装openssh
apt install -y openssh-server
# 修改/etc/ssh/sshd_config文件里Port端口
#Port 22
Port 9022
/etc/init.d/ssh restart
# 客户端配置
# 文件：~/.ssh/config
Host 127.0.0.1
    HostName 127.0.0.1
    User root
    Port 9022
    IdentityFile C:\Users\shlu\.ssh\id_rsa
# 连接
ssh -p 9022 127.0.0.1

```
# 自行编译包
https://github.com/termux/termux-packages/wiki/Build-environment

