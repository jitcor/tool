# 配置环境
- ubuntu20.04-server(已切换清华镜像)
- 4 core
- 16G RAM
- 2T disk
- 物理主机
- 必备代理，速度够快，70Mb/s左右
- Pixel 2 XL 手机一部
- 配置proxychains

# 下载源码
```
sudo apt-get update

sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 libncurses5-dev lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig python

mkdir ~/bin
PATH=~/bin:$PATH

proxychains curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo

mkdir WORKING_DIRECTORY
cd WORKING_DIRECTORY

git config --global user.name Your Name
git config --global user.email you@example.com

# -b 后面代号选择，访问：https://source.android.com/setup/start/build-numbers#source-code-tags-and-builds
proxychains repo init -u https://android.googlesource.com/platform/manifest -b android-10.0.0_r2

# -j 的数字根据机器性能而定
proxychains repo sync -c -j8
```
# 导入设备驱动(可选，刷入真实设备需要)

- 访问 https://developers.google.com/android/drivers#taimenqp1a.190711.020 地址下载Pixel 2 XL对应版本驱动文件
- 将两个压缩包放入源码根目录
- 执行解压命令 `tar -zxvf xxxxx.tgz`
- 执行完后可在源码根目录下找到vector目录

# 构建源码
```
cd WORKING_DIRECTORY

sudo apt-get install libncurses5

export _JAVA_OPTIONS="-Xmx4g"

source build/envsetup.sh

lunch aosp_taimen-user

m 
```
> 这里循环执行m，报错就继续执行，有给修复提示，就按提示做，否则默认一直m，只要不是每次错误都一样
# 刷入镜像
```
cd WORKING_DIRECTORY/out/target/product/taimen/
fastboot flashall -w
```
# 定制
## root权限

# 参考
- https://source.android.com/setup/develop
- http://koifishly.com/2020/07/24/android/source-code/xia-zai-bian-yi-yun-xing-an-zhuo-yuan-ma/
- http://www.zhuoyue360.com/crack/34.html
