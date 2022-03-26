# 配置环境
- ubuntu20.04-server(已切换清华镜像)
- 4 core
- 8G RAM
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

proxychains curl https://storage.googleapis.com/git-repo-downloads/repo -o ~/bin/repo
chmod a+x ~/bin/repo

mkdir WORKING_DIRECTORY
cd WORKING_DIRECTORY

git config --global user.name Your Name
git config --global user.email you@example.com

# -b 后面代号选择，访问：https://source.android.com/setup/start/build-numbers#source-code-tags-and-builds
proxychains repo init -u https://android.googlesource.com/platform/manifest -b android-10.0.0_r2
# 使用清华源init
# proxychains repo init -u https://mirrors.tuna.tsinghua.edu.cn/git/AOSP/platform/manifest -b android-10.0.0_r2

# -j 的数字根据机器性能而定
proxychains repo sync -c -j8
# 使用清华源sync
# repo sync -c -j8
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
# 编译Pixel 2 XL内核
> 内核源码并不在aosp里，需要单独下载 \
> 各个机型的内核不一样，具体参看：https://source.android.google.cn/setup/build/building-kernels?hl=zh-cn
## 下载源码
```
mkdir android-msm-wahoo-4.4-android10-qpr3

cd android-msm-wahoo-4.4-android10-qpr3

proxychains repo init -u https://android.googlesource.com/kernel/manifest -b android-msm-wahoo-4.4-android10-qpr3

proxychains repo sync -c -j8
```
## 编译源码
```
# openssl/bio.h file not found
sudo apt-get install libssl-dev

# soong_zip: cammand not found
export PATH=/mnt/d/tool/android/android-10.0.0_r2/out/soong/host/linux-x86/bin:$PATH

build/build.sh
```
## 替换aosp内核
> aosp里替换上面编译后的内核，这里通过环境变量TARGET_PREBUILT_KERNEL指定，方便动态切换内核，具体看：https://source.android.google.cn/setup/build/building-kernels?hl=zh-cn#running
```
cd android-10.0.0_r2

# 先初始化aosp编译环境，具体看上面构建aosp源码步骤

export TARGET_PREBUILT_KERNEL=/mnt/d/tool/android/kernel/android-msm-wahoo-4.4-android10-qpr3/out/android-msm-wahoo-4.4/dist/Image.lz4-dtb

m bootimage
```
> 之后按上面的<刷入镜像>步骤正常刷入即可
# 定制
- 修改代码
- `m <target module>`
- `make snod` (编译system.img，忽略依赖)
- `m`
- 定制时系统日志检查`dmesg | grep <tag>` or `cat /proc/kmsg | grep <tag>`
## audit2allow运行环境修复
```
sudo apt-get install python2
rm -rf /usr/bin/python
sudo ln -s /usr/bin/python2 /usr/bin/python
```
## root权限
// 看参考
## 默认开启USB调试(persist.sys.usb.config依然为none，防止检测usb连接)

- 开启USB调试
```java
//android-10.0.0_r2/frameworks/base/services/core/java/com/android/server/adb/AdbService.java#119
                // mAdbEnabled = containsFunction(
                //         SystemProperties.get(USB_PERSISTENT_CONFIG_PROPERTY, ""),
                //         UsbManager.USB_FUNCTION_ADB);
                mAdbEnabled = true;

```
- 自动处理USB验证
```java
//android-10.0.0_r2/frameworks/base/packages/SystemUI/src/com/android/systemui/usb/UsbDebuggingActivity.java#onCreate()
   @Override
    public void onCreate(Bundle icicle) {
        //......
        setupAlert();
        //....
        mAlert.getButton(BUTTON_POSITIVE).setOnTouchListener(filterTouchListener);
        //add code
        try {
            IBinder b = ServiceManager.getService(ADB_SERVICE);
            IAdbManager service = IAdbManager.Stub.asInterface(b);
            service.allowDebugging(true, mKey);
        } catch (Exception e) {
            Log.e(TAG, "Unable to notify Usb service", e);
        }
        finish();
    }

```
## 制作releasekey
- 源码根目录下创建create_key.sh
```
#create_key.sh
subject='/C=CN/ST=Shanghai/L=Shanghai/O=marto/OU=marto/CN=marto.cc/emailAddress=android@marto.cc'
for x in releasekey platform shared media networkstack;
do
  ./development/tools/make_key ~/.android-certs/$x "$subject";
done

```
- 源码根目录执行`cp -r ~/.android-certs/releasekey.* build/target/product/security/`
- `testkey`->`releasekey`
```mk
# build/core/config.mk

# The default key if not set as LOCAL_CERTIFICATE
ifdef PRODUCT_DEFAULT_DEV_CERTIFICATE
  DEFAULT_SYSTEM_DEV_CERTIFICATE := $(PRODUCT_DEFAULT_DEV_CERTIFICATE)
else
  DEFAULT_SYSTEM_DEV_CERTIFICATE := build/target/product/security/releasekey
endif
.KATI_READONLY := DEFAULT_SYSTEM_DEV_CERTIFICATE
```
```mk
# build/core/Makefile

# The "test-keys" tag marks builds signed with the old test keys,
# which are available in the SDK.  "dev-keys" marks builds signed with
# non-default dev keys (usually private keys from a vendor directory).
# Both of these tags will be removed and replaced with "release-keys"
# when the target-files is signed in a post-build step.
ifeq ($(DEFAULT_SYSTEM_DEV_CERTIFICATE),build/target/product/security/releasekey)
BUILD_KEYS := release-keys
else
BUILD_KEYS := dev-keys
endif

```
- `m -j4`重新编译
## 修改设备属性
## 隐藏BL解锁
## 系统属性访问trace
```cpp
//bionic/libc/bionic/system_property_api.cpp

#include <async_safe/log.h>

__BIONIC_WEAK_FOR_NATIVE_BRIDGE
const prop_info* __system_property_find(const char* name) {
  char value[PROP_VALUE_MAX] = {0};
  system_properties.Get(name, value);
   async_safe_format_log(ANDROID_LOG_ERROR,
             "marto","call __system_property_find %s -> %s",name,value);
  return system_properties.Find(name);
}

__BIONIC_WEAK_FOR_NATIVE_BRIDGE
int __system_property_read(const prop_info* pi, char* name, char* value) {
  int ret= system_properties.Read(pi, name, value);
  async_safe_format_log(ANDROID_LOG_ERROR,
             "marto","call __system_property_read %s -> %s",name,value);
  return ret;
}

__BIONIC_WEAK_FOR_NATIVE_BRIDGE
int __system_property_get(const char* name, char* value) {
  int ret= system_properties.Get(name, value);
  async_safe_format_log(ANDROID_LOG_ERROR,
             "marto","call __system_property_get %s -> %s",name,value);
  return ret;
}


```
## 开启应用debuggable(ro.debuggable依然为0)
```java
//frameworks/base/core/java/android/content/pm/PackageParser.java#parseBaseApplication()

       // if (sa.getBoolean(
       //         com.android.internal.R.styleable.AndroidManifestApplication_debuggable,
       //         false)) {
            ai.flags |= ApplicationInfo.FLAG_DEBUGGABLE;
            // Debuggable implies profileable
            ai.privateFlags |= ApplicationInfo.PRIVATE_FLAG_PROFILEABLE_BY_SHELL;
       // }

```
## 修改屏幕默认休眠时间(单位：ms)
```xml
<!-- frameworks/base/packages/SettingsProvider/res/values/defaults.xml  -->
    <integer name="def_screen_off_timeout">36000000</integer>
```
## 屏幕锁定默认为“无”
```xml
<!-- frameworks/base/packages/SettingsProvider/res/values/defaults.xml  -->
<bool name="def_lockscreen_disabled">true</bool>
```
## 修改默认语言为中文
```shell
# build/tools/buildinfo.sh

# ..........

echo "# end build properties"

echo "# custom build properties"

echo "# default language"
echo "ro.product.locale=zh_CN"
echo "ro.product.locale.language=zh"
echo "ro.product.locale.region=CN"
echo "persist.sys.language=zh"
echo "persist.sys.country=CN"
echo "persist.sys.timezone=Asia/Shanghai"


echo "# end custom build properties"

```
## ptrace trace
```cpp
//bionic/libc/bionic/ptrace.cpp

#include <async_safe/log.h>

long ptrace(int req, ...) {
  //......
  
  va_end(args);
  
  async_safe_format_log(ANDROID_LOG_ERROR,
             "marto","call ptrace pid:%d,addr:0x%p",pid,addr);

  long result = __ptrace(req, pid, addr, data);
  if (is_peek && result == 0) {
    return peek_result;
  }
  return result;
}

```
## getenforce 强制返回Enforcing
```cpp
//external/toybox/toys/android/getenforce.c

void getenforce_main(void)
{
  if (!is_selinux_enabled()) puts("Disabled");
  else {
    int ret = security_getenforce();

    if (ret == -1) perror_exit("Couldn't get enforcing status");
    //else puts(ret ? "Enforcing" : "Permissive");
    else puts(ret ? "Permissive" : "Enforcing");
  }
}

```
# 参考
- https://source.android.com/setup/develop
- http://koifishly.com/2020/07/24/android/source-code/xia-zai-bian-yi-yun-xing-an-zhuo-yuan-ma/
- http://www.zhuoyue360.com/crack/34.html
- https://www.jianshu.com/p/bb5325760506
- https://source.android.com/devices/tech/ota/sign_builds
- https://source.android.com/devices/bootloader/locking_unlocking?hl=zh-cn
- https://blog.csdn.net/qq_35003588/article/details/99567368
- https://balalals.cn/archives/aosp%E6%9B%B4%E6%94%B9%E9%BB%98%E8%AE%A4%E8%AF%AD%E8%A8%80%E6%97%B6%E5%8C%BA%E9%97%AE%E9%A2%98
- [SELinux政策文件](https://source.android.com/security/selinux/implement)
- https://www.modb.pro/db/375240
- https://blog.csdn.net/zxc99408267/article/details/80789670
- https://www.shuzhiduo.com/A/gVdnOvYlzW/
- https://blog.51cto.com/u_15315240/3212141
- http://www.juneleo.cn/47a3736f9762/
