# Window 
- WSL1不支持
- Docker桌面版会强制安装到C盘
- 可以直接在WSL2里像在Linux里安装一样
- 尽量把文件放在WSL发行版文件系统里，一可以提高性能，二减少一些兼容性问题的出现(毕竟WSL与Window的文件系统还是不一样的)

# WSL2 安装Docker
参考https://zhuanlan.zhihu.com/p/148511634
## Install
```
curl -fsSL https://get.docker.com -o get-docker.sh
//sleep20s
sudo sh get-docker.sh
sudo service docker start
```
## Check 
```
service docker status
ps aux|grep docker
```
## Pull Test
```
docker pull busybox
docker images
```
> 注意：不同于完全linux虚拟机方式，WLS2下通过apt install docker-ce命令安装的docker无法启动，因为WSL2方式的ubuntu里面没有systemd。上述官方get-docker.sh安装的docker，dockerd进程是用ubuntu传统的init方式而非systemd启动的。

# Linux
## Ubuntu
### 安装
```
cd <work dir>
proxychains curl https://get.docker.com/ -o install.sh
chmod +x ./install.sh
sudo proxychains ./install.sh
```
> 若要更改docker数据目录，参见：[./change-docker-root.md](./change-docker-root.md)
### 拉取镜像
```
sudo docker pull <image name>
```
### 运行镜像
```
sudo docker run -it <image name>
```
### 常用命令
```
# 查看已运行镜像
sudo docker ps

# 查看已安装镜像
sudo docker ps --all

# ssh 连接docker端口映射 , 10022主机端口，22容器里端口 run 创建一个以test1命名的容器并运行
sudo docker run -it -p 10022:22 --name test1 ubuntu:18.04
# 允许ssh以root登录
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
# 重启ssh
service ssh restart
# 容器启动时自启ssh
echo "service ssh start" >> ~/.bashrc
# 设置root密码
passwd root
# 本地访问容器ssh
ssh root@x.x.x.x -p 10022

# 启动一个以test1命名的容器
sudo docker start -a -i test1

```
# 参考
- [ssh连接docker容器；docker容器设置root密码](https://blog.csdn.net/winter2121/article/details/118223637)
