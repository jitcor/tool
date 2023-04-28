import asyncio
import os
import re
import sys
import threading
import time

import lldb
import paramiko


def enter_console(command_interpreter: lldb.SBCommandInterpreter, ):
    while True:
        command = input("(lldb) ")
        if command == "q":
            return
        print(exec_lldb(command_interpreter, command))


def hexdump(command_interpreter: lldb.SBCommandInterpreter, pointer: int, size: int) -> str:
    return exec_lldb(command_interpreter, "memory read %s %s" % (pointer, pointer + size))


def get_dylib_base(command_interpreter: lldb.SBCommandInterpreter, so_name: str) -> int:
    result = exec_lldb(command_interpreter, "image list")
    print(result)
    return int(re.split(r" +", re.findall(r"\[.*/%s " % so_name, result)[0])[3], 16)


def get_pointer_value(command_interpreter: lldb.SBCommandInterpreter, pointer: int) -> int:
    result = exec_lldb(command_interpreter, "memory read -fx -c1 %s" % pointer)
    print(result)
    return int(result.split(' ')[1], 16)


def exec_lldb(command_interpreter: lldb.SBCommandInterpreter, command: str) -> str:
    ci_result = lldb.SBCommandReturnObject()
    command_interpreter.HandleCommand(command, ci_result)
    process: lldb.SBProcess = command_interpreter.GetProcess()
    if not ci_result.Succeeded():
        print("exec_lldb: ",ci_result)
        return ""
    return ci_result.GetOutput()



def do_task(debugger: lldb.SBDebugger):
    # try:
    debugger.SetAsync(False)
    ci: lldb.SBCommandInterpreter = debugger.GetCommandInterpreter()
    plat: lldb.SBPlatform = debugger.GetSelectedPlatform()
    print("ci IsActive:",ci.IsActive())
    print("ci IsValid:",ci.IsValid())
    print("plat IsValid:",plat.IsValid())
    print("plat IsConnected:",plat.IsConnected())
    # pid = re.split(' +', result)[1]
    # exec_lldb(ci, "attach " + pid)
    #
    # exec_lldb(ci,"image list")
    base = get_dylib_base(ci, "dylib name")
    print("base:", hex(base))
    #
    # # enter_console(ci)
    #
    # print(hexdump(ci, base + 0xa5910, 1024))
    #
    # exec_lldb(ci,
    #           "memory read %s %s -outfile ./test.bin --binary -force" % (base + 0xa5910, base + 0xa5910 + 47308 * 5))
    # # exec_lldb(ci,"br set -a %s"%(base+0x2991c))
    #
    # # tmp=ci.GetProcess().ReadMemory(base,1000000,error)
    # # print(error)
    # # data=bytearray(tmp)
    # # index=data.find(bytes({0x11,0x00,0x3D,0xC1}))
    # # print(index)
    #
    # enter_console(ci)
    #
    # # except Exception as e:
    # #     print(e)
    # exec_lldb(ci, "detach")


def start_lldb_server():
    ssh = paramiko.SSHClient()
    key = paramiko.AutoAddPolicy()
    ssh.set_missing_host_key_policy(key)
    ssh.connect('127.0.0.1', 2222, 'root', 'alpine', timeout=5)
    stdin, stdout, stderr = ssh.exec_command(
        'debugserver 127.0.0.1:1234 -a "app name"')

    start_lldb_client()

    for i in stdout.readlines():
        print(i)
    for i in stderr.readlines():
        print(i)
    for i in stderr.readlines():
        print(i)
    print("debugserver end...")


def start_lldb_client():

    debugger: lldb.SBDebugger = lldb.SBDebugger.Create()
    target:lldb.SBTarget=debugger.CreateTarget("")
    listener=lldb.SBListener()
    error=lldb.SBError()
    target.ConnectRemote(listener,"connect://127.0.0.1:1234",None,error)

    do_task(debugger)

    debugger.Clear()
    lldb.SBDebugger.Destroy(debugger)

if __name__ == '__main__':

    # run shell: iproxy 2222 22
    # run shell: iproxy 1234 1234

    threading.Thread(target=start_lldb_server).start()

