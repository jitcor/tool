### 记录运行日志
```
sudo perf record -F 999 ./program 
```
> -F 指定采样频率  
> 运行后输出perf.data文件
### 分析perf.data
```
sudo perf report
```
- 输出结果如下：  
```
Samples: 5K of event 'cpu-clock', Event count (approx.): 5525525520
Overhead  Command  Shared Object      Symbol
  99.06%  sample   sample             [.] wasteTime
   0.69%  sample   sample             [.] number
   0.07%  sample   [kernel.kallsyms]  [k] __do_softirq
   0.04%  sample   [kernel.kallsyms]  [k] _raw_spin_unlock_irqrestore
   0.04%  sample   [kernel.kallsyms]  [k] run_timer_softirq
   0.04%  sample   libc-2.12.so       [.] malloc
   0.02%  sample   [kernel.kallsyms]  [k] _raw_spin_lock_irq
   0.02%  sample   [kernel.kallsyms]  [k] cursor_timer_handler
   0.02%  sample   [kernel.kallsyms]  [k] finish_task_switch
   0.02%  sample   libc-2.12.so       [.] _int_malloc
```
- 上面只能精确到函数级，若是要看更细粒度的，可以通过键盘上下键选择想看的函数，按ENTER进入  
```
Annotate wasteTime                --- 分析wasteTime函数中指令或者代码的性能
Zoom into sample(32477) thread    --- 聚焦到线程 sample(32477)
Zoom into sample DSO              --- 聚焦到动态共享对象sample(32477) 
Browse map details                --- 查看map
Run scripts for samples of thread [sample]--- 针对sample线程的采样运行脚本
Run scripts for samples of symbol [wasteTime] --- 针对函数的采样运行脚本   
Run scripts for all samples       --- 针对所有采样运行脚步
Switch to another data file in PWD --- 切换到当前目录中另一个数据文件
Exit
```
- 选中后ENTER进入
```
│    Disassembly of section .text:                              
       │                                                              
       │    08048424 <wasteTime>:                                      
       │    wasteTime():                                              
  0.04 │      push   %ebp                                              
       │      mov    %esp,%ebp                                        
  0.02 │      sub    $0x10,%esp                                        
       │      movl   $0x0,-0x8(%ebp)                                  
       │      movl   $0x0,-0x8(%ebp)                                  
       │   ┌──jmp    20                                                
 22.31 │16:│  mov    -0x8(%ebp),%eax                                  
  0.34 │   │  add    %eax,-0x4(%ebp)                                  
 26.32 │   │  addl   $0x1,-0x8(%ebp)                                  
  7.96 │20:└─→mov    -0x8(%ebp),%eax                                  
 42.54 │      cmp    0x8(%ebp),%eax                                    
       │    ↑ jl     16                                                
  0.24 │      mov    -0x4(%ebp),%eax                                  
  0.15 │      leave                                                       
  0.08 │      ret
```
> 若是只有汇编的话，可以加个-g附加调试信息  
- 或者直接执行`perf annotate --stdio --symbol=wastTime`即可进入上面最后一步  
### 参考
- [用Perf寻找程序中的性能热点](https://zhuanlan.zhihu.com/p/134721612)  
- [手把手教你系统级性能分析工具perf的介绍与使用（超详细）](https://zhuanlan.zhihu.com/p/471379451)
