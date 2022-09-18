# vdex转dex for android8.+
`./vdexExtractor -i xxx.vdex`
# cdex转dex for android9及以上
若vdex文件是安卓8.0~8.1提取出来的，那么就大功告成了，但是vdex文件如果是安卓9或者以上的，执行命令后会转换出cdex文件，此时需要用到cdexExtractor \
`./cdexExtractor /sdcard/test.cdex`
# vdexExtractor地址
https://github.com/anestisb/vdexExtractor
# oat/odex 转dex
```bash
java -jar baksmali-2.5.2.jar x  D:\*********\*.odex(oat)
```
```bash
java -jar smali-2.5.2.jar ass -o classes.dex out
```
# 参考
- [dex2oat 原理和慢的原因](https://blog.csdn.net/long375577908/article/details/78190422?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166347240016800192296324%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166347240016800192296324&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-1-78190422-null-null.142^v47^pc_rank_34_default_2,201^v3^add_ask&utm_term=dex2oat%20%E6%85%A2&spm=1018.2226.3001.4187)
- [安卓.odex文件的反编译](https://blog.csdn.net/qq_33163046/article/details/120729670?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-120729670-blog-107669242.pc_relevant_multi_platform_featuressortv2dupreplace&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-120729670-blog-107669242.pc_relevant_multi_platform_featuressortv2dupreplace&utm_relevant_index=5)
