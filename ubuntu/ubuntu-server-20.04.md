# 安装到笔记本
- 在https://next.itellyou.cn/ 下载iso文件
- 然后通过https://github.com/ventoy/Ventoy 刷入笔记本
- 执行`sudo su root`进入root账户
- 通过命令`ip addr`查看网卡名称为enp0s3
- 通过vim修改配置文件/etc/netplan/*.yaml
> yaml是专门用来写配置文件的语言：它对大小写敏感；使用缩进表示层级关系；缩进时不允许使用Tab键，只允许使用空格；缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
- 修改配置参考

1.静态IP

```python
# This is the network config written by 'subiquity'
network:
  ethernets:
    enp0s3:#配置的网卡名称,使用ifconfig -a查看得到
      dhcp4: no
      addresses: [192.168.1.6/24]
      optional: true
      gateway4: 192.168.1.1
      nameservers:
              addresses: [192.168.1.1,114.114.114.114]
  version: 2
```

2.动态IP

```python
# This is the network config written by 'subiquity'
network:
  ethernets:
    enp0s3:#配置的网卡名称,使用ifconfig -a查看得到
      dhcp4: true
      addresses: []
      optional: true
      nameservers:
              addresses: [114.114.114.114]
  version: 2
```

> 这里192.168.1.6为当前笔记本局域网IP地址，改为不与其他设备冲突的即可
- 执行命令`sudo netplan apply`应用更改
- 执行`ip addr`查看对应网卡状态
- 执行`export all_proxy=http://192.168.1.17:10809`
- 执行`export http_proxy=http://192.168.1.17:10809`
- 执行`export https_proxy=http://192.168.1.17:10809`
- 执行`wget https://raw.githubusercontent.com/Humenger/tool/master/IDEA/ssh-setup.sh`
- 执行`./ssh-setup.sh`开启ssh服务，默认端口22
- xshell，或IDEA里ssh连接即可
## 连接WLAN
* 连接前需要先通过上面的有线网连接方式连接到有线网下载一些东西，具体如下
* `sudo apt install net-tools`
* `sudo apt install wireless-tools`
* `sudo apt install wpasupplicant`
* `iwcondig` 查看有什么网卡，只要网卡名后面没显示`no wireless extensions`并且显示了详细的网卡信息的就是无线网卡，一般以'w'字母开头，我这里显示的网卡名字是`wlp3s0`
* 然后执行`sudo ip link set wlp3s0 up`这里wlp3s0为上面查询到的网卡名
* 如果该WLAN没加密，直接执行`sudo iw dev wlan0 connect wifi_name` 这里wifi_name专业术语叫ssid，其实就是平常手机wifi列表里看到的wifi名字
* 如果该WLAN是WEP协议，执行`sudo iw dev wlan0 connect wifi_name key 0:password` 这里wifi_name同上，password自然就是wifi密码
* 如果该WLAN是WPA或WPA2协议，就稍微复杂一点，具体步骤如下
* 执行`sudo vim /etc/wpasupplicant/wpa_supplicant.conf` 添加配置WPA文件
* 然后在该文件里输入以下内容
```conf
ctrl_interface=/var/run/wpa_supplicant

ap_scan=1

network={
        ssid="wifi_name"
        psk="password"
        priority=1
}
```
* 参数含义同上
* 然后执行命令`sudo wpa_supplicant -i wlp3s0 -c /etc/wpa_supplicant/wpa_supplicant.conf &` 开始连接WLAN，wlp3s0修改成上面获取的
* 通过iwconfig命令, 查看wlp3s0是否已经连接上相应wifi_name的WIFI, 或者通过ping尝试联网
* 参考：https://developer.aliyun.com/article/704878
## 笔记本关盖子不休眠
- 修改`/etc/systemd/logind.conf`的HandleLidSwitch的值为ignore，并去掉前面的注释
- 执行`service systemd-logind restart`重启服务以禁用笔记本的关闭盖子休眠功能
# 参考
https://www.bilibili.com/read/cv10613992/

https://blog.csdn.net/xiaoxiao133/article/details/82847936

https://www.cxyzjd.com/article/u014454538/88646689
