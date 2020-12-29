# 参考
[python3.6和pip3：Ubuntu下安装升级与踩坑之路](https://blog.csdn.net/ccgshigao/article/details/108212828?ops_request_misc=%25257B%252522request%25255Fid%252522%25253A%252522160922128216780276310289%252522%25252C%252522scm%252522%25253A%25252220140713.130102334.pc%25255Fblog.%252522%25257D&request_id=160922128216780276310289&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v1~rank_blog_v1-4-108212828.pc_v1_rank_blog_v1&utm_term=python3.6)
# 具体步骤
```
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update 
sudo apt-get install python3.6
#删除原来的软连接
rm -rf /usr/bin/python3
 
#建立新的软连接
ln -s /usr/bin/python3.6m /usr/bin/python3
 
#重新测试python3版本
python3 -V
#用pip安装很多python的package都会依赖python-dev包
sudo apt install -y python3.6-dev
#安装pip3
sudo apt install -y python3-pip 
#查看pip3版本 
pip3 -V
```
