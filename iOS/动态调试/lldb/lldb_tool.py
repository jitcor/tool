#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lldb
import re
import os
import shlex


def goto_main(debugger, command, result, internal_dict):
    """
    goto main
    """
    interpreter = lldb.debugger.GetCommandInterpreter()
    return_object = lldb.SBCommandReturnObject()  # 用来保存结果
    interpreter.HandleCommand('dis', return_object)  # 执行dis命令
    output = return_object.GetOutput();  # 获取反汇编后的结果

    br_index = output.rfind('br     x16')  # 查找最后的 bx x16
    br_index = br_index - 20  # 位置减去20
    addr_index = output.index('0x', br_index)  # 查找0x开头的字符串
    br_addr = output[br_index:br_index + 11]  # 找到之后偏移11位

    debugger.HandleCommand('b ' + br_addr)  # 添加断点
    debugger.HandleCommand('continue')  # 运行
    debugger.HandleCommand('si')  # 单步步入


def sql(debugger, command, result, internal_dict):
    """
    goto main
    """
    interpreter = lldb.debugger.GetCommandInterpreter()
    return_object = lldb.SBCommandReturnObject()  # 用来保存结果
    interpreter = lldb.debugger.GetCommandInterpreter()
    return_object = lldb.SBCommandReturnObject()  # 用来保存结果
    while True:
        interpreter.HandleCommand('register read x2', return_object)
        result: str = return_object.GetOutput()
        if result.find('x2 = 0x0000000000000001') > -1:
            interpreter.HandleCommand('register read x3', return_object)
            result: str = return_object.GetOutput()
            if re.search('x3 = 0x000000000000000[023]', result) is not None:
                print(result)
                break
                # interpreter.HandleCommand('memory read $x1', return_object)
                # result: str = return_object.GetOutput()
                # print(result)
                # if result.rfind('BE 9C BA 1A 84 29 24 79'.lower()) > -1:
                #     print('find db file')
                #     break
        debugger.HandleCommand('c')


def go_addr(debugger, command, result, internal_dict):
    """
    goto main
    """
    addr = shlex.split(command)[0]
    if not addr:
        print("Please inout address")
        return
    interpreter = lldb.debugger.GetCommandInterpreter()
    return_object = lldb.SBCommandReturnObject()  # 用来保存结果
    debugger.HandleCommand('br set -a %s' % addr)
    debugger.HandleCommand('c')
    interpreter.HandleCommand('br list', return_object)
    output = return_object.GetOutput()
    groups = re.findall('\n([0-9]+)', output)
    groups.reverse()
    print('index:', groups[0])
    debugger.HandleCommand('br del %s' % groups[0])


def get_aslr():
    interpreter = lldb.debugger.GetCommandInterpreter()
    return_object = lldb.SBCommandReturnObject()

    interpreter.HandleCommand('image list -o -f', return_object)  # 执行image list -o -f命令
    output = return_object.GetOutput();  # 获取命令的返回值
    match = re.match(r'.+(0x[0-9a-fA-F]+)', output)  # 正则匹配(0x开头)
    if match:
        return match.group(1)
    else:
        return None


def aslr(debugger, command, result, internal_dict):
    """
    get ASLR offset
    """
    aslr = get_aslr()
    print("ASLR offset is:", aslr)


def breakpoint_address(debugger, command, result, internal_dict):
    """
    breakpoint aslr address
    """
    fileoff = shlex.split(command)[0]  # 获取输入的参数
    if not fileoff:
        print('Please input the address!')
        return

    aslr = get_aslr()
    if aslr:
        # 如果找到了ASLR偏移，就设置断点
        debugger.HandleCommand('br set -a "%s+%s"' % (aslr, fileoff))
    else:
        print('ASLR not found!')


def __lldb_init_module(debugger: lldb.SBCommandInterpreter, internal_dict):
    debugger.HandleCommand('command script add -f lldb_tool.aslr aslr')
    debugger.HandleCommand('command script add -f lldb_tool.goto_main gm')
    debugger.HandleCommand('command script add -f lldb_tool.breakpoint_address ba')
    debugger.HandleCommand('command script add -f lldb_tool.go_addr goaddr')
    debugger.HandleCommand('command script add -f lldb_tool.sql sql')
    debugger.HandleCommand('platform select remote-ios')
    debugger.HandleCommand('process connect connect://127.0.0.1:1234')
    # debugger.HandleCommand('ba 0x16EEC74')
    # debugger.HandleCommand('ba 0x3102C10')
    # debugger.HandleCommand('ba 0x3102660')
    # debugger.HandleCommand('ba 0x310294c')
    # debugger.HandleCommand('ba 0x24D00FC')
    debugger.HandleCommand('ba 0x24D0230')

    print('lldb_tool is finish')
