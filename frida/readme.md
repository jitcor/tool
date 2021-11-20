# 版本对应
| frida    | frida-tools |
| :----:   | :----:      |
| 12.7.22  | 5.2.0       |

一键查看对应版本https://github.com/frida/frida/releases/tag/12.7.22
# 安装frida
```
..\python3.6.8\Scripts>pip3.6 install frida==12.7.22  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```
# 安装frida-tools
```
..\python3.6.8\Scripts>pip3.6 install frida-tools==5.2.0  -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```
# 安装多个Python版本问题
设置pythonpath为当前要用的版本路径即可
# 重新编译Frida
```
$ git clone https://github.com/frida/frida.git

$ cd frida

$ make

$ export ANDROID_NDK_ROOT=/Users/{username}/Library/Android/sdk/ndk/22.0.6917172/

$ sudo apt-get install npm

$ sudo apt install python3-pip

$ pip3 install colorama prompt-toolkit pygments

$ rm -rf build

$ make core-android-x86_64

$ make core-android-x86

# 最后生成的文件在 build/frida-android-x86 build/frida-android-x86_64 
# 如果需要调整编译参数，在releng/setup-env.sh中进行调整 比如: meson_common_flags="['-g']"
```
