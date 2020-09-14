# 目的
在macOS 使用lldb借助USB接口传输ssh通信协议远程调试iphone app
# 测试环境
- iphone6 12.4(已越狱)
- macOS 10.15.5 Catalina
- lldb 1103.0.22.4
# 步骤[<sup>1</sup>](#ref.1)
- `iproxy 2222 22`:端口转发
- 打开一个新命令窗口
- `ssh -p 2222 root@127.0.0.1`:执行后进入到iphone命令窗口
- `debugserver -x backboard *:1234 /path/to/app/executable`:先启动进程然后注入，注入后会挂起进程
- or `./debugserver *:1234 -a "YourAPPName"`:注入已运行进程
- 打开一个新命令窗口
- `iproxy 1234 1234`
- 打开一个新命令窗口
- `lldb`(执行后进入lldb命令窗口)
- `platform select remote-ios`
- `process connect connect://localhost:1234`[<sup>q1</sup>](#q.1)
- 接下来就可以输入调试命令操作了
# 调试
- `c`:继续运行
- `r`:重启
- `si`:指令级步入
- `ni`:指令级步过
- `return`:退出子函数
- `breakpoint set -a 0x012345`:在函数地址下断
- `dis -a 0x12345`:从某地址开始反汇编
- `image list`:获取执行文件基址
- or `image list -f -o WhatsApp`:增加过滤选项
# 问题
- q1.`error: rejecting incoming connection from ::ffff:127.0.0.1 (expecting ::1)`<a id="q.1"/> \
将*:1234中的'*'改成127.0.0.1[<sup>2</sup>](#ref.2) \
- 
# 参考
- [1] [2018-08-10更新-LLDB常用命令--飘云整理](https://www.dllhook.com/post/51.html)<a id="ref.1"/>
- [2] [IOS越狱12.4之后debugger使用lldb连不上](https://www.ioshacker.net/thread-148-1-1.html)<a id="ref.2"/>

