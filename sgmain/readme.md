# 模拟加载libsgmain.so
```java
public void sgmain(){
        String libDir=getApplicationInfo().nativeLibraryDir;
        String sgmainPath=libDir+"/libsgmain.so";
        String sgmainOptDir=getDir("sgmain",MODE_PRIVATE).getAbsolutePath();
        log("path:"+sgmainPath);
        PathClassLoader sgmainClassLoader=new PathClassLoader(sgmainPath,sgmainOptDir,getClassLoader());
        try {
            log("sgmain classloader:"+sgmainClassLoader);
            Class<?> sgmainCls=sgmainClassLoader.loadClass("com.alibaba.wireless.security.mainplugin.SecurityGuardMainPlugin");
            log("main class:"+sgmainCls);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }


    }
```
> 测试失败，无法找到类，但换成我自己创建的apk却是可以的，初步猜测应该是该dex里调用了主程序了的类文件，而我没加载主程序，导致找不到类
