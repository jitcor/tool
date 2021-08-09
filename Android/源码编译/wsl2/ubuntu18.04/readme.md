# 所需资料
- WSL2
- Ubuntu18.04

# 具体步骤
参考https://www.vectoros.club/post/fe9083b4.html
## success result
```
Checking out: 100% (677/677), done in 9m34.823s
repo sync has finished successfully.
```
## 问题
### /usr/bin/env: ‘python’: No such file or directory
- If Python 3 is not installed, install it: `apt-get install python3`
- If Python 3 has been installed, run these commands: `whereis python3`
- Then we create a symlink to it: `sudo ln -s /usr/bin/python3 /usr/bin/python`
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
# 参考
https://blog.csdn.net/u013427969/article/details/114371933
