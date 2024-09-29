# 获取当前界面UI信息
./dump_ui.js
# frida-ios-hook
https://github.com/noobpk/frida-ios-hook

# 安装指定版本frida server
[iOS iphone 7 手动安装Frida指定版本(老版本) 这里以15.1.2版本为例](https://blog.csdn.net/qq_26914291/article/details/129031855)

# 获取iOS路径
```oc
//tmp路径
function iOSNSTemporaryDirectory(){
    try {
        // @ts-ignore
        var NSTemporaryDirectory = new NativeFunction(ptr(Module.findExportByName("Foundation", "NSTemporaryDirectory")), 'pointer', []);
        // @ts-ignore
        let path = new ObjC.Object(NSTemporaryDirectory());
        // @ts-ignore
        return new ObjC.Object(NSTemporaryDirectory()).UTF8String();
    }catch (e){
        return "";
    }
}
```
# dump iOS系统库
```oc
// @ts-ignore
const cc=Process.getModuleByAddress(Module.findExportByName(null,"CC_SHA1"));
console.log("path:",cc.path);
console.log("size:",cc.size);
console.log("base:",cc.base);

function iOSNSTemporaryDirectory(){
    try {
        // @ts-ignore
        var NSTemporaryDirectory = new NativeFunction(ptr(Module.findExportByName("Foundation", "NSTemporaryDirectory")), 'pointer', []);
        // @ts-ignore
        let path = new ObjC.Object(NSTemporaryDirectory());
        // @ts-ignore
        return new ObjC.Object(NSTemporaryDirectory()).UTF8String();
    }catch (e){
        return "";
    }
}
// @ts-ignore
function iOSDumpMemory(address,size,name){
    let outFile=new File(iOSNSTemporaryDirectory()+"/"+name,"wb");
    // @ts-ignore
    outFile.write(ptr(address).readByteArray(size))
    outFile.flush();
    outFile.close();
}
iOSDumpMemory(cc.base,cc.size,"libName");
```
> 实测可以dump出来，但是IDA无法识别，可能需要修复头，具体后面再研究吧  
> 这里直接按路径找，是找不到系统库的，只能二进制dump

# 提取TLS证书
https://github.com/jankais3r/Frida-iOS-15-TLS-Keylogger  
〉这个仅适配了iOS 15，若是其它版本，需要自行适配
