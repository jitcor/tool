# 配置环境
- ubuntu20.04-server
- 4 core
- 16G RAM
- 2T disk
- 物理主机
- 必备代理，速度够快，70Mb/s左右
- Pixel 2 XL 手机一部
# 下载源码
```
sudo apt-get update

sudo apt-get install git-core gnupg flex bison build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 libncurses5-dev lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig python

mkdir ~/bin
PATH=~/bin:$PATH

curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo

mkdir WORKING_DIRECTORY
cd WORKING_DIRECTORY

git config --global user.name Your Name
git config --global user.email you@example.com

repo init -u https://android.googlesource.com/platform/manifest -b android-10.0.0_r2

repo sync -c -j8
```
# 构建源码
```
cd WORKING_DIRECTORY

sudo apt-get install libncurses5

export _JAVA_OPTIONS="-Xmx4g"

source build/envsetup.sh

lunch aosp_taimen-user

#这里循环执行m，报错就继续执行，有给修复提示，就按提示做，否则默认一直m，只要不是每次错误都一样
m 
```
