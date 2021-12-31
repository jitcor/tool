# 解BL锁
- 开启oem
- fastboot oem unlock
> 注：解BL锁后，Wlan无法正常使用了，即使完全还原也不行，可能需要升级到最新版固件包才能解决(更新:据酷安网友说需要刷persist分区才行，具体待测试)
# Magisk
- 下载OTA包[https://www.h2os.com/download.](https://www.h2os.com/download.)
- 解包提取boot.img
- Magisk 对boot.img打补丁
- fastboot boot magisk_patch.img
- 后面按提示操作即可
> 该机型在重启手机后，会恢复boot.img，所以在每次重启之后都要进入fastboot，重新刷一次magisk boot补丁。
> 
> 至于模块重启生效问题，可以等安装完模块，直接强制重启到fastboot，然后再重新刷一次magisk boot补丁再重启即可。
> 
> OTA包需要通过系统更新刷入。
# 解包提取boot.img
- 下载解包工具https://gist.github.com/ius/42bd02a5df2226633a342ab7a9c60f15
- 包含两个py文件payload_dumper.py，update_metadata_pb2.py
- 或者直接当前目录下载即可
- pip3 install protobuf
- python payload_dumper.py payload.bin (payload.bin从固件包里提取即可)
# 固件救砖
> 一次刷boot.img不小心执行了错误的命令:`fastboot flash boot magisk_patch.img`(正确的是`fastboot boot magisk_patch.img`)，导致变砖，当然还能通过音量+和电源键进入fastboot模式刷固件也可以解决，不过固件包没找到，需要重新下载，那多麻烦，又发现固件救砖包倒还在，那就试下这个9008救砖吧

- 禁用驱动签名检查
- 装9008驱动
- 关机
- 按住音量上键
- 点击start
- 连接电脑
- 等待自动识别，并刷入固件
- 完成图

![image](https://user-images.githubusercontent.com/27600008/147733462-207872e5-21f5-4df6-92c7-320ae7c5ad16.png)


# 全部资料
https://cloud.189.cn/t/jAJJBjbM7f6z (访问码:5l7k)


