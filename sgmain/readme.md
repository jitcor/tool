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
这里直接加载SecurityGuardMainPlugin以及同包下的R类会报错，而加载同dex下的com.taobao.dp.util.ZipUtils类却不会报错\
进一步分析，可以发现ZipUtils类所在包只有它一个类，并且其仅调用了系统Api\
所以可以得出结论：若同包下任一类调用了未加载的类，则该包下的所有类都将无法正常加载
