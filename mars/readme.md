mars是腾讯微信开源的消息通讯框架
# 编译demo
- 下载1.3.0发布版https://github.com/Tencent/mars/releases/tag/v1.3.0
- 用AndroidStudio 3.1.4打开 marsSampleChat 开始build(测试用AndroidStudio 4.1虽然也会编译通过，但很多文件打开都会报红，可能新版编辑器编码问题)
- 期间可能会报No toolchains found in the NDK toolchains folder for ABI with prefix: mipsel-linux-android问题
- 具体解决办法就是将ndk版本切换为官方使用版本ndk-r16b(这里我用的r17,应该是只要保证ndk/toolchains/下有 mipsel-linux-android-xx文件夹就行)
- 然后将Apk安装在两个或多个手机上(聊天室只有一个人看不到效果)，或者换个包名在一个手机上安装两个Apk(虽然也能正常进行通讯，但会出现看到自己发送的消息再发送给自己的情况)
- 然后用PyCharm2019 pro打开samples/Server工程
- 将python版本调整到2.7版本
- 运行start_server.py文件，等待构建完成，可能会比较漫长
- 运行成功后，在其间打开的一个窗口中会打印如下日志，表示启动成功
```
Building 85% > :server:jettyRun > Running at http://localhost:8080//
```
- 然后将两部或多部手机通过USB连接PC
- 分别对两部或多部手机执行如下命令
```bat
adb reverse tcp:8080 tcp:8080
adb reverse tcp:8081 tcp:8081
```
- 然后启动各自手机上的apk，正常情况下，会出现一个转圈，转圈后出现三个按钮，就是对应三个聊天室了，在两部或多部手机在同一聊天室里输入消息文字即可进行聊天了
- 测试还挺快，几乎零延迟
