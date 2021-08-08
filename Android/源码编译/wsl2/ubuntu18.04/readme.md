# 所需资料
- WSL2
- Ubuntu18.04

# 具体步骤
参考https://www.vectoros.club/post/fe9083b4.html
## 问题
### /usr/bin/env: ‘python’: No such file or directory
- If Python 3 is not installed, install it: `apt-get install python3`
- If Python 3 has been installed, run these commands: `whereis python3`
- Then we create a symlink to it: `sudo ln -s /usr/bin/python3 /usr/bin/python`

# 参考
