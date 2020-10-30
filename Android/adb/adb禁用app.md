- 源码解析参考https://lishuaiqi.top/2018/09/17/PMS12-enable_disableThroughAdb/#2-3-setEnabledSetting-%E6%A0%B8%E5%BF%83%E5%85%A5%E5%8F%A3
- 通过阅读源码可以知道
- shell必须有android.Manifest.permission.CHANGE_COMPONENT_ENABLED_STATE 权限否则会报以下错误
> Error: java.lang.SecurityException: Permission Denial: attempt to change component state from pid=xxx, uid=2000, package uid=xxxx
- shell不能使用pm disable 命令禁用组件，只能使用pm disbale-user，否则会报以下错误
> Error: java.lang.SecurityException: Shell cannot change component state for xxxx/xxxxx to 2
