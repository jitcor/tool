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
            ActivityThread: Java.use("android.app.ActivityThread"),
            currentApplication: Java.use("android.app.ActivityThread").currentApplication()
        }
    }

});
