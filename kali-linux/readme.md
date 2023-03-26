# 简介
# 下载
## WSL
https://docs.microsoft.com/zh-cn/windows/wsl/install-manual#downloading-distributions
- 天翼云盘：https://cloud.189.cn/t/ZVVFBvJfUJne (访问码:9yfk)
## VMware虚拟机版
https://www.kali.org/get-kali/#kali-virtual-machines
> 天翼云备份：https://cloud.189.cn/t/INzIFjABbqam (访问码:k8l8)
## Linux版
# 安装
## VMware虚拟机版
- VMware工具下载安装
> 天翼云盘：https://cloud.189.cn/t/Qnay6n6jARvi (访问码:2dew)
- 解压上面下载的kali的VMware虚拟机版压缩包
- VMware里->打开虚拟机->选择解压后的文件夹里的对应的虚拟机入口文件(我这里后缀.vmx)
- 即可运行虚拟机了
## WSL

# 配置
## 默认账户
参考https://www.kali.org/docs/introduction/default-credentials/
> 我这里VMware虚拟机的默认账户是kali kali

# 问题
* An error occurred during the signature verification.
```
W: An error occurred during the signature verification. The repository is not updated and the previous 
index files will be used. GPG error: http://mirrors.jevincanders.net/kali kali-rolling InRelease: The 
following signatures were invalid: EXPKEYSIG ED444FF07D8D0BF6 Kali Linux Repository <devel@kali.org>
W: Failed to fetch http://http.kali.org/kali/dists/kali-rolling/InRelease  The following signatures 
were invalid: EXPKEYSIG ED444FF07D8D0BF6 Kali Linux Repository <devel@kali.org>
W: Some index files failed to download. They have been ignored, or old ones used instead.
```
解决方案(ref:[apt-get-update-issue-in-kali](https://superuser.com/questions/1644520/apt-get-update-issue-in-kali))
```bash
# download
wget http://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_2022.1_all.deb
# install
sudo dpkg -i kali-archive-keyring_2022.1_all.deb
# remove downloaded file again
rm kali-archive-keyring_2022.1_all.deb
# update
sudo apt-get update
```
