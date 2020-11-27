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
        ClassLoaderMonitor: function (callback) {
            tool.api.ContextWrapper.attachBaseContext.implementation = function (content) {
                if (callback != null) {
                    callback(content.getClassLoader())
                }
                return this.attachBaseContext(content)
            }
            tool.api.ClassLoader.$init.overload('java.lang.ClassLoader').implementation = function (clsLoader) {
                if (callback != null) {
                    callback(clsLoader)
                }
                return this.$init(clsLoader)
            }
        },
        hookAllMethod: function (targetClass, targetMethod, hookImpl) {
            var hook = (typeof targetClass) == "string" ? Java.use(targetClass) : targetClass;
            var overloadCount = hook[targetMethod].overloads.length;

            console.log("[hookAllMethod] " + targetMethod + " [" + overloadCount + " overload(s)]");

            for (var i = 0; i < overloadCount; i++) {
                hook[targetMethod].overloads[i].implementation = hookImpl
            }
        },
        getStackTraceString: function () {
            return Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new())
        },
        getNativeStackTrace: function (content) {
            return Thread.backtrace(content, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\n');
        },
        StringMonitor: function (callback) {
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
        FileMonitor: function (callback) {
            tool.hookAllMethod(tool.api.File, '$init', function () {
                var retval = this['$init'].apply(this, arguments); // rare crash (Frida bug?)
                // console.log("[File]", this.path)
                if (callback != null) callback(this.path.value)
                return retval
            })
        },
        FileMonitorNative: function (keyToTrace, callback) {
            var hook = {
                onEnter: function (args) {
                    var fileName = Memory.readCString(args[0]);
                    // var trace = Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\n');
                    if (fileName.indexOf(keyToTrace) > -1) {
                        if (callback != null) callback(fileName)
                        console.log('[native stack]\n' +
                            Thread.backtrace(this.context, Backtracer.ACCURATE)
                                .map(DebugSymbol.fromAddress).join('\n') + '\n');
                    }
                },
                onLeave: function (retval) {
                }
            }
            Interceptor.attach(tool.libc.open(), hook);
            Interceptor.attach(tool.libc.open64(), hook);
            Interceptor.attach(tool.libc.fopen(), hook);

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
        },
        WriteFile: function (filePath) {

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
        FridaTool: function () {
            try {
                return Java.use('org.ihbing.frida.FridaTool')
            } catch (e) {
                console.log(e);
                Java.openClassFile("/data/local/tmp/fridatool.dex").load();
                console.log("load fridatool.dex ok");
                return Java.use('org.ihbing.frida.FridaTool')
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
        traceMethod: function (targetClassMethod, printBacktrace) {
            var delim = targetClassMethod.lastIndexOf(".");
            if (delim === -1) return;

            var targetClass = targetClassMethod.slice(0, delim)
            var targetMethod = targetClassMethod.slice(delim + 1, targetClassMethod.length)

            var hook = Java.use(targetClass);
            var overloadCount = hook[targetMethod].overloads.length;

            console.log("Tracing " + targetClassMethod + " [" + overloadCount + " overload(s)]");

            for (var i = 0; i < overloadCount; i++) {

                hook[targetMethod].overloads[i].implementation = function () {
                    console.warn("\n*** entered " + targetClassMethod);

                    // print backtrace
                    if (printBacktrace == true) {
                        Java.perform(function () {
                            var bt = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
                            console.log("\nBacktrace:\n" + bt);
                        });

                    }

                    // print args
                    if (arguments.length) console.log();
                    for (var j = 0; j < arguments.length; j++) {
                        console.log("arg[" + j + "]: " + arguments[j]);
                    }

                    // print retval
                    var retval = this[targetMethod].apply(this, arguments); // rare crash (Frida bug?)
                    console.log("\nretval: " + retval);
                    console.warn("\n*** exiting " + targetClassMethod);
                    return retval;
                }
            }
        },
        traceClass: function (targetClass, printBacktrace) {
            function uniqBy(array, key) {
                var seen = {};
                return array.filter(function (item) {
                    var k = key(item);
                    return seen.hasOwnProperty(k) ? false : (seen[k] = true);
                });
            }

            //Java.use是新建一个对象哈，大家还记得么？
            var hook = Java.use(targetClass);
            //利用反射的方式，拿到当前类的所有方法
            var methods = hook.class.getDeclaredMethods();
            //建完对象之后记得将对象释放掉哈
            hook.$dispose;
            //将方法名保存到数组中
            var parsedMethods = [];
            methods.forEach(function (method) {
                parsedMethods.push(method.toString().replace(targetClass + ".", "TOKEN").match(/\sTOKEN(.*)\(/)[1]);
            });
            //去掉一些重复的值
            var targets = uniqBy(parsedMethods, JSON.stringify);
            //对数组中所有的方法进行hook，traceMethod也就是第一小节的内容
            targets.forEach(function (targetMethod) {
                tool.traceMethod(targetClass + "." + targetMethod, printBacktrace);
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
            },
            open64: function () {
                return Module.findExportByName("libc.so", "open64")
            },
            fopen: function () {
                return Module.findExportByName("libc.so", "fopen")
            },
        },
        api: {
            File: Java.use("java.io.File"),
            String: Java.use("java.lang.String"),
            ContextWrapper: Java.use("android.content.ContextWrapper"),
            ClassLoader: Java.use("java.lang.ClassLoader"),
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
