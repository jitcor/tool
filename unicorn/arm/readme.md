# 编译unicorn arm版
- 下载源码
```
# 我下载时的commit id:c10639fd4658a852049546162d116b123e2b1ec2
git clone https://github.com/unicorn-engine/unicorn.git
```
- 将以下构建脚本放入项目根目录，然后修改相应路径，最后执行即可
```sh
# build.sh

rm -rf build

mkdir build

cd build

export JAVA_HOME=/data/tool/android/android-10.0.0_r2/prebuilts/jdk/jdk8/linux-x86

export NDK=/data/tool/sdk/sdk/ndk-bundle

export ABI=armeabi-v7a

export MINSDKVERSION=16

export PATH=$PATH:$JAVA_HOME:/data/tool/sdk/sdk/cmake/3.18.1/bin:$NDK/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin

echo "exec cmake..."

cmake .. -DCMAKE_TOOLCHAIN_FILE=$NDK/build/cmake/android.toolchain.cmake -DANDROID_ABI=$ABI -DANDROID_NATIVE_API_LEVEL=$MINSDKVERSION

echo "exec make..."

make

cd ../

echo "finish"

```
# 调用unicorn
```c

```
# 运行
```sh

adb push test001 /data/local/tmp/

adb push libunicorn.so /data/local/tmp/

adb shell

cd /data/local/tmp/

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/local/tmp/

./test001

```
