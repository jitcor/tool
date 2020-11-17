直接参考https://github.com/ihbing/ShiLuLib 配置即可
# 具体步骤
- Android Studio 创建一个工程
- 在工程里再创建一个lib模块
- 顶级build.gradle添加       classpath 'com.novoda:bintray-release:0.8.0'
```
注意版本对应关系
AndroidStudio3.1.4 com.novoda:bintray-release:0.8.0
AndroidStudio3.4.2 com.novoda:bintray-release:0.9.1
```
- 对应lib库里build.gradle添加
```
apply plugin: 'com.novoda.bintray-release'//添加
···
publish {
    userOrg = 'ihbing'
    groupId = 'com.ihbing'
    artifactId = 'ShiLuLib'
    publishVersion = '0.1.0'
    desc = 'ShiLu\'s lib'
    website = 'https://github.com/ihbing/ShiLuLib'
}
```
- 编译通过后，通过git 上传到github里
- 在github里创建一个发布版本,tag里不要加前缀v，直接版本号即可
- 然后访问https://jitpack.io/#ihbing/ShiLuLib获取依赖链接
