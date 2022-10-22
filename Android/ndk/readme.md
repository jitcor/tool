# 常用代码
```c
#include <sys/system_properties.h>

            __system_property_get("","asdfsd");

```
# jniLibs 问题
### 直接点击run运行，报找不到so文件问题？
直接添加如下代码即可，当然abiFilters需要跟你的jniLibs目录下的架构匹配  
```gradle
android {

    defaultConfig {

        ndk {
            abiFilters 'armeabi-v7a'
            ldLibs "log", "z", "m"
        }
    }
}
```
