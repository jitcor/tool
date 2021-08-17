
# !/bin/bash

version="0.0.1"

echo "Aosp compile Version:$version"

echo "设置工作目录:(默认~/Android/)"
read WorkDirectory

echo "选择要编译的Android版本:"
echo "1.Android-8.1.0_r1(默认)"
echo "2.Android-9.0.0_r1"
read AndroidVersionIndex

echo "选择镜像源:"
echo "1.清华源(默认)"
echo "2.谷歌官方源(需魔法)"
echo "3.科大源"
read SourceUrlIndex

echo "选择编译版本:"
echo "1.aosp_arm-eng(默认)"
read CompileVersionIndex

echo "输入make编译并行数:(默认4)"
read JobCount

AndroidVersion="Android-8.1.0_r1"
SourceUrl="https://mirrors.tuna.tsinghua.edu.cn/git/git-repo"
CompileVersion="aosp_arm-eng"

if [ "$WorkDirectory" = "" ]
then
  WorkDirectory='~/Android/'
fi

if [ ! -d "$WorkDirectory" ]; then
  mkdir -p "$WorkDirectory"
fi
echo "已创建工作目录:$WorkDirectory"


case $AndroidVersionIndex in
     2) AndroidVersion="Android-9.0.0_r1"
     ;;
     *) AndroidVersion="Android-8.1.0_r1"
     ;;
esac

case $CompileVersionIndex in
     2) CompileVersion="aosp_arm64-debug"
     ;;
     *) CompileVersion="aosp_arm-eng"
     ;;
esac

if [ "$JobCount" = "" ]
then 
   JobCount=4
fi

apt-get update

yes | apt-get install openjdk-8-jdk

apt-get -y install git-core gnupg flex bison build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig


case $SourceUrlIndex in
     2) echo "not implement :2"
     ;;
     3) echo "not implement :2"
     ;;
     *)
       #echo "编译命令：cd $WorkDirectory && curl https://mirrors.tuna.tsinghua.edu.cn/git/git-repo -o repo && chmod +x repo && export REPO_URL='https://mirrors.tuna.tsinghua.edu.cn/git/git-repo/' && wget -c https://mirrors.tuna.tsinghua.edu.cn/aosp-monthly/aosp-20200101.tar && tar xf aosp-20200101.tar && cd aosp && repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest -b $AndroidVersion && repo sync -n -j1; while [ $? -ne 0 ]; do echo \"======sync failed, re-sync again======\"; repo sync -n -j1 ; done && repo sync -l ; while [ $? -ne 0 ]; do echo \"======2sync failed, re-sync again======\"; repo sync -l  ; done && source build/envsetup.sh && lunch $CompileVersion && make -j$JobCount"
       cd $WorkDirectory && curl https://mirrors.tuna.tsinghua.edu.cn/git/git-repo -o repo && chmod +x repo && export REPO_URL='https://mirrors.tuna.tsinghua.edu.cn/git/git-repo/' && wget -c https://mirrors.tuna.tsinghua.edu.cn/aosp-monthly/aosp-20200101.tar && tar xf aosp-20200101.tar && cd aosp && repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest -b $AndroidVersion && repo sync -n -j1; while [ $? -ne 0 ]; do echo "======sync failed, re-sync again======"; repo sync -n -j1 ; done && repo sync -l ; while [ $? -ne 0 ]; do echo "======2sync failed, re-sync again======"; repo sync -l  ; done && source build/envsetup.sh && lunch $CompileVersion && sed -i 's/jdk.tls.disabledAlgorithms=SSLv3, TLSv1 TLSv1.1,/jdk.tls.disabledAlgorithms=SSLv3,/g' /etc/java-8-openjdk/security/java.security && cd prebuilts/sdk/tools/ && ./jack-admin kill-server && ./jack-admin start-server && cd ../../../ && make -j$JobCount
     ;;
esac
