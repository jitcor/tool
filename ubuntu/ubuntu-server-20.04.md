# 安装到笔记本
- 在https://next.itellyou.cn/ 下载iso文件
- 然后通过https://github.com/ventoy/Ventoy 刷入笔记本
- 执行`sudo su root`进入root账户
- 通过命令`ip addr`查看网卡名称为enp0s3
- 通过vim修改配置文件/etc/netplan/*.yaml
> yaml是专门用来写配置文件的语言：它对大小写敏感；使用缩进表示层级关系；缩进时不允许使用Tab键，只允许使用空格；缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
- 修改配置参考
```
# This is the network config written by 'subiquity'
network:
  ethernets:
    enp0s3:
      dhcp4: no
      addresses: [192.168.1.6/24]
      optional: true
      gateway4: 192.168.1.1
      nameservers:
              addresses: [192.168.1.1,114.114.114.114]
  version: 2
```
> 这里192.168.1.6为当前笔记本局域网IP地址，可改为不与其他设备冲突的即可
- 执行命令`sudo netplan apply`应用更改
- 执行`ip addr`查看对应网卡状态
- 执行`export all_proxy=http://192.168.1.17:10809`
- 执行`export http_proxy=http://192.168.1.17:10809`
- 执行`export https_proxy=http://192.168.1.17:10809`
- 执行`wget https://raw.githubusercontent.com/Humenger/tool/master/IDEA/ssh-setup.sh`
- 执行`./ssh-setup.sh`开启ssh服务，默认端口22
- xshell，或IDEA里ssh连接即可
- 修改`/etc/systemd/logind.conf`的HandleLidSwitch的值为ignore，并去掉前面的注释
- 执行`service systemd-logind restart`重启服务以禁用笔记本的关闭盖子休眠功能
# 参考
https://www.bilibili.com/read/cv10613992/
https://blog.csdn.net/xiaoxiao133/article/details/82847936
