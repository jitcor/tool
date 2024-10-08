# 获取当前界面UI信息
./dump_ui.js
# frida-ios-hook
https://github.com/noobpk/frida-ios-hook

# 安装指定版本frida server
[iOS iphone 7 手动安装Frida指定版本(老版本) 这里以15.1.2版本为例](https://blog.csdn.net/qq_26914291/article/details/129031855)

# 代码片段

## 获取未导出符号的函数(偏移)地址

```js
DebugSymbol.fromName('SSL_CTX_set_keylog_callback').address.sub(Module.findBaseAddress('libboringssl.dylib'))
```

> https://github.com/frida/frida/issues/541



## 获取iOS路径

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
## dump iOS系统库
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

# 提取TLS key log
https://github.com/jankais3r/Frida-iOS-15-TLS-Keylogger  
〉这个仅适配了iOS 15，若是其它版本，需要自行适配

又找到一个：https://codeshare.frida.re/@vadim-a-yegorov/universalkeylogger/

> 这个支持更多版本：12～15，但对libboringssl.dylib的初始加载时机是采用循环检测，有可取之处，但容易漏掉最开始执行的日志

```js
/**
 * Android, iOS (12.0-15.7.3), Linux universal SSLKEYLOG dumper.
 *
 * Usage:
 * 
 *   # For iOS and mac:
 *   rvictl -s [UDID]
 *   # Then open Wireshark and select rvi0
 * 
 *   # For iOS and not mac:
 *   git clone https://github.com/gh2o/rvi_capture
 *   ./rvi_capture/rvi_capture.py - | wireshark -k -i -
 * 
 *   # For Android
 *   androiddump --extcap-interface=android-wifi-tcpdump --capture --fifo=&1 | wireshark -k -i -
 * 
 *   # For Linux
 *   tcpdump
 * 
 *   # Dumping SSLKEYLOG
 *   frida --codeshare vadim-a-yegorov/universalkeylogger -f YOUR_BINARY -U --no-pause > sslkeylog.log
 *   
 *   # Then in Wireshark TLS settings load "sslkeylog.log" file
 * 
 * Vadim A. Yegorov
 * https://gist.github.com/vadim-a-yegorov/9d4fbcdfec055373656daa9bc97063ac
 */


/**
 * Sleep
 */
async function sleep(seconds = 0) {
    await new Promise(r => setTimeout(r, seconds * 1000))
}


/**
 * Logging function, reads null terminated string from address in line.
 */
function keyLogger(ssl, line) {
    const keylog = new NativePointer(line).readCString()
    console.log(keylog)
}
const keyLogCallback = new NativeCallback(keyLogger, 'void', ['pointer', 'pointer'])


/**
 * Start logging libboringssl.dylib TLS keys. Should be called before resuming the binary.
 */
function startSystemTLSKeyLogger() {
    const moduleName = "libboringssl.dylib"

    // iOS version
    const deviceSystemVersion = ObjC.classes.UIDevice.currentDevice().systemVersion()
    const deviceSystemVersionMajor = deviceSystemVersion.floatValue() ^ 0

    // Offset of keylog_callback pointer in SSL struct
    // Derived from dissassembly of ssl_log_secret in ssl_lib.c (libboringssl.dylib) on iOS
    const CALLBACK_OFFSET = {
        12: 0x2A8,
        13: 0x2C0,
        14: 0x2B8,
        15: 0x2F8
    }[deviceSystemVersionMajor]
    if (!CALLBACK_OFFSET) {
        throw new Error(`iOS ${deviceSystemVersion} isn't supported yet.`)
    }

    // Intercept
    const SSL_CTX_set_info_callback = Module.findExportByName(moduleName, "SSL_CTX_set_info_callback");
    Interceptor.attach(SSL_CTX_set_info_callback, {
        onEnter: function(args) {
            const ssl = new NativePointer(args[0])
            const callback = new NativePointer(ssl).add(CALLBACK_OFFSET)
            callback.writePointer(keyLogCallback)
        }
    })
    send(`Module ${moduleName} SSL logging started.`)
}


/**
 * Start logging TLS keys. Should be called before resuming the binary.
 */
function startTLSKeyLogger(moduleName) {
    if (moduleName === "libboringssl.dylib") {
        return startSystemTLSKeyLogger()
    }
    const SSL_CTX_new = Module.findExportByName(moduleName, "SSL_CTX_new")
    const SSL_CTX_set_keylog_callback = Module.findExportByName(moduleName, "SSL_CTX_set_keylog_callback")
    if (!SSL_CTX_set_keylog_callback) {
        return
    }
    Interceptor.attach(SSL_CTX_new, {
        onLeave: function(retval) {
            const ssl = new NativePointer(retval)
            if (!ssl.isNull()) {
                const SSL_CTX_set_keylog_callbackFn = new NativeFunction(SSL_CTX_set_keylog_callback, 'void', ['pointer', 'pointer'])
                SSL_CTX_set_keylog_callbackFn(ssl, keyLogCallback)
            }
        }
    })
    send(`Module ${moduleName} SSL logging started.`)
}


(async function() {
    // Wait for environment (for iOS)
    if (Process.platform === "darwin") {
        while (true) {
            try {
                Module.ensureInitialized("libboringssl.dylib")
                break
            } catch {
                await sleep(0)
            }
        }
    }
    send("Loaded!")

    if (Process.platform === "darwin") {
        startTLSKeyLogger("libboringssl.dylib")
    }

    const modules = Process.enumerateModules()
    for (const module of modules) {
        if (module.name === "libboringssl.dylib") {
            continue
        }

        startTLSKeyLogger(module.name)
    }
})()
```



## 优化版

>  理论支持所有iOS版本，也不再手动获取指针，也没有上面循环检测会漏掉部分日志问题

```js
/**
 * Optimized version (from: github/jitcor): Directly obtain the function pointer of 
 * `SSL_CTX_set_keylog_callback` via code, eliminating the need for manual handling.
 *
 * This is based on https://codeshare.frida.re/@andydavies/ios-tls-keylogger/
 * but does not require the binary to use `SSL_CTX_set_info_callback` etc.
 * Instead it directly hooks `SSL_CTX_new` to find the pointer to each
 * SSL_CTX and then directly calls `SSL_CTX_set_keylog_callback`.
 * This method requires that you can find the the pointers to both
 * `SSL_CTX_new` and `SSL_CTX_set_keylog_callback` which might not
 * always be possible.
 *
 * This is based on work by Andy Davies
 *  Copyright (c) 2019 Andy Davies, @andydavies, http://andydavies.me
 *
 * The rest is his work
 *  Copyright (c) 2020 Hugo Tunius, @k0nserv, https://hugotunius.se
 *
 * Andy's original code is released under MIT License and my modifications
 * are likewise MIT licensed.
 *
 * A full writeup is available on my blog
 * https://hugotunius.se/2020/08/07/stealing-tls-sessions-keys-from-ios-apps.html
 */

Module.load("/usr/lib/libboringssl.dylib");
function startTLSKeyLogger(SSL_CTX_new, SSL_CTX_set_keylog_callback) {
    function keyLogger(ssl, line) {
        console.log(new NativePointer(line).readCString());
    }
    const keyLogCallback = new NativeCallback(keyLogger, 'void', ['pointer', 'pointer']);

    Interceptor.attach(SSL_CTX_new, {
        onLeave: function(retval) {
            const ssl = new NativePointer(retval);

            if (!ssl.isNull()) {
                const SSL_CTX_set_keylog_callbackFn = new NativeFunction(SSL_CTX_set_keylog_callback, 'void', ['pointer', 'pointer']);
                SSL_CTX_set_keylog_callbackFn(ssl, keyLogCallback);
            }
        }
    });
}
startTLSKeyLogger(Module.findExportByName("libboringssl.dylib","SSL_CTX_new"),DebugSymbol.fromName('SSL_CTX_set_keylog_callback').address);


```

wireshark 导入keylog教程：https://wiki.wireshark.org/TLS#tls-decryption

# 待解决问题
1. frida spawn方式拦截子进程  
2. frida spawn方式拦截依赖库报unable to find module  
    这个可能涉及到iOS的依赖库加载机制，和frida 注入机制，但这两个学习成本有点高，临时解决方案就是主动加载依赖库或者延时hook
3. 
