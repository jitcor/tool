Java.perform(function () {
    //tool
    var tool = {
        go: function (runnable) {
            try {
                runnable()
            } catch (e) {
                console.log(e)
            }
        },
        getStackTraceString: function () {
            return Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new())
        },
        StringMonitor:function (callback) {
            tool.api.StringBuffer.toString.implementation = function () {
                var string = this.toString()
                 if (callback != null) callback(string)
                return string
            }
            tool.api.StringBuilder.toString.implementation = function () {
                var string = this.toString()
                 if (callback != null) callback(string)
                return string
            }

        },
        AlgorithmMonitor: function (algorithm, callback) {
            tool.api.MessageDigest.digest.overload().implementation = function () {
                var bin = this.digest()
                if (algorithm == this.getAlgorithm()) {
                    if (callback != null) callback(bin)
                }
                return bin
            }
        },
        checkCast: function (sourceCls, targetCls) {
            try {
                return Java.cast(sourceCls, targetCls)
            } catch (e) {
                console.log(e)
                return sourceCls
            }
        }
        ,
        Hexdump: function (data) {
            try {
                return Java.use('org.lasinger.tools.hexdump.Hexdump').hexdump(data)
            } catch (e) {
                console.log(e);
                Java.openClassFile("/data/local/tmp/hexdump.dex").load();
                console.log("load hexdump.dex ok");
                return Java.use('org.lasinger.tools.hexdump.Hexdump').hexdump(data)
            }
        },
        Gson: function (object) {
            try {
                return Java.use('com.google.gson.Gson').$new().toJson(object)
            } catch (e) {
                console.log(e);
                Java.openClassFile("/data/local/tmp/gson.dex").load();
                console.log("load gson.dex ok");
                return Java.use('com.google.gson.Gson').$new().toJson(object)
            }
        },
        sleep: function sleep(numberMillis) {
            var now = new Date();
            var exitTime = now.getTime() + numberMillis;
            while (true) {
                now = new Date();
                if (now.getTime() > exitTime)
                    return;
            }
        },
        onJniLoad: function (callback) {
            return Interceptor.attach(this.libc.dlsym(), {
                onEnter: function (args) {
                    this.soPath = args[1].readCString()
                    // console.log("[call dlsym]", this.soPath)
                    if (this.soPath.indexOf("JNI_OnLoad") >= 0) {
                        tool.go(function () {
                            callback()
                        })
                    }
                },
                onLeave: function (retval) {
                }
            });
        },
        libc: {
            dlopen: function () {
                return Module.findExportByName("libc.so", "dlopen")
            },
            dlsym: function () {
                return Module.findExportByName("libc.so", "dlsym")
            },
            open: function () {
                return Module.findExportByName("libc.so", "open")
            }
        },
        api: {
            String: Java.use("java.lang.String"),
            application: Java.use("android.app.Application"),
            Toast: Java.use('android.widget.Toast'),
            System: Java.use('java.lang.System'),
            StringBuilder: Java.use('java.lang.StringBuilder'),
            StringBuffer: Java.use('java.lang.StringBuffer'),
            MessageDigest: Java.use('java.security.MessageDigest'),
            ActivityThread: Java.use("android.app.ActivityThread"),
            currentApplication: Java.use("android.app.ActivityThread").currentApplication(),
        },
        className: {
            String: "java.lang.String",
            application: "android.app.Application",
            Toast: 'android.widget.Toast',
            System: 'java.lang.System',
            MessageDigest: 'java.security.MessageDigest',
            ActivityThread: "android.app.ActivityThread",
        }
    }


});
