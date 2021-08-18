# 所需资料
- WSL2
- Ubuntu18.04

# 具体步骤
 ~~参考https://www.vectoros.club/post/fe9083b4.html~~

参考https://blog.csdn.net/weixin_42695485/article/details/108655661
## 关于源码同步问题
可以参考https://mirrors.tuna.tsinghua.edu.cn/help/AOSP/ \
直接下载aosp-latest.tar文件，然后解压repo sync同步 \
同步后，直接`repo init -b android-4.4.4_r1 --depth=1`即可取出代码
## `repo sync` success result
```
Checking out: 100% (677/677), done in 9m34.823s
repo sync has finished successfully.
```
## `make` 成功返回
```
#### build completed successfully (04:08:18 (hh:mm:ss)) ####
```
# 问题
## 大小写敏感问题
- 管理员cmd命令开启大小写敏感`fsutil.exe file setCaseSensitiveInfo <path> enable`
> ~~这里的路径不能偷懒，直接设定AOSP和CCACHE的上级目录，而应该分别设定~~ \
> 实测发现原来是Window系统版本的问题，老版本虽然可以设置大小写敏感，但是子目录无法继承，新版虽然已创建的子目录也无法继承，但新创建的子目录可以继承
### /usr/bin/env: ‘python’: No such file or directory
- ~~If Python 3 is not installed, install it: `apt-get install python3`~~
- ~~If Python 3 has been installed, run these commands: `whereis python3`~~
- ~~Then we create a symlink to it: `sudo ln -s /usr/bin/python3 /usr/bin/python`~~
- 直接`sudo apt install python`
### Unable to fully sync the tree
```
Checking out files: 100% (17/17), done.
Checking out files: 100% (2255/2255), done.
Checking out: 100% (677/677), done in 2h17m6.703s

error: Unable to fully sync the tree.
error: Downloading network changes failed.
Try re-running with "-j1 --fail-fast" to exit at the first error.
```
根据提示执行`repo sync -j1 --fail-fast`即可
### Exited sync due to fetch errors.
```
error: Exited sync due to fetch errors.
Local checkouts *not* updated. Resolve network issues & retry.
`repo sync -l` will update some local checkouts.
```
根据提示执行`repo sync -l`
### Failed to listen for path logs: listen unix out/.path_interposer_log: bind: operation not supported
将源码放在WSL的文件系统里，不要放在Window文件系统里
### FAILED: setup-jack-server
参考https://segmentfault.com/a/1190000039970343 \
`/etc/java-8-openjdk/security/java.security`文件里属性jdk.tls.disabledAlgorithms去掉TLSv1, TLSv1.1参数，然后`aosp/prebuilts/sdk/tools/` 目录下执行`./jack-admin kill-server && ./jack-admin start-server` 成功。
### SyntaxError: invalid syntax
python3->python2
# 参考
- https://blog.csdn.net/u013427969/article/details/114371933
- https://blog.csdn.net/weixin_42695485/article/details/108655661
- https://ckcat.github.io/2019/11/03/%E7%BC%96%E8%AF%91Android%E7%B3%BB%E7%BB%9F/
