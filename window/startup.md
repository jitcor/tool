# ~~在系统启动时运行~~
~~把脚本放入如下目录即可~~
```
C:\Windows\System32\GroupPolicy\Machine\Scripts\Startup\
```
~~如果不行，就按照如下方法添加~~

![image](https://user-images.githubusercontent.com/27600008/133868796-b4a718db-5163-41c8-89c2-18155330e59c.png)

> ~~其中gpedit是错的，应该是gpedit.msc才对~~

# ~~在用户登录时启动~~ (这个才是真正的在系统系统时运行)
把脚本放在`shell:startup`目录下即可

