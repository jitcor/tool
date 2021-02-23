# 默认vmoptions
```
-Xms256m
-Xmx1280m
-XX:ReservedCodeCacheSize=240m
-XX:+UseConcMarkSweepGC
-XX:SoftRefLRUPolicyMSPerMB=50
-Dsun.io.useCanonCaches=false
-Djava.net.preferIPv4Stack=true
-Djna.nosys=true
-Djna.boot.library.path=

-da

```
# 内存优化
```
-Xms1024m
-Xmx2048m
-XX:ReservedCodeCacheSize=480m
-XX:+UseConcMarkSweepGC
-XX:SoftRefLRUPolicyMSPerMB=50
-Dsun.io.useCanonCaches=false
-Djava.net.preferIPv4Stack=true
-Djna.nosys=true
-Djna.boot.library.path=

-da

```
# 参考
- 1.[IntelliJ IDEA 参数配置、内存及性能、卡顿优化](http://www.w3capi.com/mcms/content/id/64/cid/26.html)
