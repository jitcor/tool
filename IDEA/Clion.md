# WSL+Clion
- 进入wsl 选择一个目录作为工作目录
- cd 到该目录
- 执行·sudo apt-add-repository -r ppa:gophers/archive·
- 执行`sudo apt update -q`
- 执行`sudo apt list --upgradable`
- 执行
```
sudo apt update
sudo apt upgrade
```
- 将以下脚本放入sh文件中并执行
```sh
#!/bin/bash
set -e

SSHD_LISTEN_ADDRESS=0.0.0.0

SSHD_PORT=2222
SSHD_FILE=/etc/ssh/sshd_config
SUDOERS_FILE=/etc/sudoers
  
# 0. update package lists
sudo apt-get update

# 0.1. reinstall sshd (workaround for initial version of WSL)
sudo apt remove -y --purge openssh-server
sudo apt install -y openssh-server

# 0.2. install basic dependencies
sudo apt install -y cmake gcc clang gdb valgrind build-essential

# 1.1. configure sshd
sudo cp $SSHD_FILE ${SSHD_FILE}.`date '+%Y-%m-%d_%H-%M-%S'`.back
sudo sed -i '/^Port/ d' $SSHD_FILE
sudo sed -i '/^ListenAddress/ d' $SSHD_FILE
sudo sed -i '/^UsePrivilegeSeparation/ d' $SSHD_FILE
sudo sed -i '/^PasswordAuthentication/ d' $SSHD_FILE
echo "# configured by CLion"      | sudo tee -a $SSHD_FILE
echo "ListenAddress ${SSHD_LISTEN_ADDRESS}"	| sudo tee -a $SSHD_FILE
echo "Port ${SSHD_PORT}"          | sudo tee -a $SSHD_FILE
echo "UsePrivilegeSeparation no"  | sudo tee -a $SSHD_FILE
echo "PasswordAuthentication yes" | sudo tee -a $SSHD_FILE
# 1.2. apply new settings
sudo service ssh --full-restart
  
# 2. autostart: run sshd 
sed -i '/^sudo service ssh --full-restart/ d' ~/.bashrc
echo "%sudo ALL=(ALL) NOPASSWD: /usr/sbin/service ssh --full-restart" | sudo tee -a $SUDOERS_FILE
cat << 'EOF' >> ~/.bashrc
sshd_status=$(service ssh status)
if [[ $sshd_status = *"is not running"* ]]; then
  sudo service ssh --full-restart
fi
EOF
  

# summary: SSHD config info
echo 
echo "SSH server parameters ($SSHD_FILE):"
echo "ListenAddress ${SSHD_LISTEN_ADDRESS}"
echo "Port ${SSHD_PORT}"
echo "UsePrivilegeSeparation no"
echo "PasswordAuthentication yes"

```
- 成功返回如下
- ![image](https://user-images.githubusercontent.com/27600008/124688573-92787680-df09-11eb-8a3a-2ad3fafb610e.png)
- ssh 连接地址ssh://127.0.0.1:2222
- ssh 连接账户密码就是wsl账户密码
- 可以先用xshell尝试下

# Clion部分
- ![image](https://user-images.githubusercontent.com/27600008/124693387-f0a95780-df11-11eb-8960-e3589223340d.png)
- ![image](https://user-images.githubusercontent.com/27600008/124693499-23ebe680-df12-11eb-9b1a-d52a8368f13c.png)
- 填写完Credentials，其他的会自动获取
- ![image](https://user-images.githubusercontent.com/27600008/124693619-5a296600-df12-11eb-8127-d2371b100d08.png)
- 若是出现如上图错误，请选择Environmnet为其它的选项
- ![image](https://user-images.githubusercontent.com/27600008/124693853-b2f8fe80-df12-11eb-82cb-5ebf7f9d6c74.png)
- 然后开始新建的c项目编译运行吧



