import os
import re
import sys
import lldb


def enter_console(command_interpreter: lldb.SBCommandInterpreter, ):
    while True:
        command = input("(lldb) ")
        if command == "q":
            return
        print(exec_lldb(command_interpreter, command))


def hexdump(command_interpreter: lldb.SBCommandInterpreter, pointer: int, size: int) -> str:
    return exec_lldb(command_interpreter, "memory read %s %s" % (pointer, pointer + size))


def get_so_base(command_interpreter: lldb.SBCommandInterpreter, so_name: str) -> int:
    result = exec_lldb(command_interpreter, "image list")
    return int(re.split(r" +", re.findall(r"\[.*?\\%s" % so_name, result)[0])[-2], 16)


def get_pointer_value(command_interpreter: lldb.SBCommandInterpreter, pointer: int) -> int:
    result = exec_lldb(command_interpreter, "memory read -fx -c1 %s" % pointer)
    print(result)
    return int(result.split(' ')[1], 16)


def exec_lldb(command_interpreter: lldb.SBCommandInterpreter, command: str) -> str:
    ci_result = lldb.SBCommandReturnObject()
    command_interpreter.HandleCommand(command, ci_result)
    process:lldb.SBProcess=command_interpreter.GetProcess()
    if not ci_result.Succeeded():
        print(ci_result)
        return ""
    return ci_result.GetOutput()


def exec_android_shell(platform: lldb.SBPlatform, command: str) -> str:
    command: lldb.SBPlatformShellCommand = lldb.SBPlatformShellCommand(command)  # (shell) android shell env
    error = platform.Run(command)
    if not error.Success():
        print(error)
        return ""
    return command.GetOutput()


def do_task(debugger: lldb.SBDebugger):
    # try:
    debugger.SetAsync(False)
    ci :lldb.SBCommandInterpreter= debugger.GetCommandInterpreter()
    plat:lldb.SBPlatform=debugger.GetSelectedPlatform()

    result = exec_android_shell(plat, "system/bin/ps -A | grep xxxxx | grep -v xxx")
    print(result)
    pid = re.split(' +', result)[1]
    exec_lldb(ci, "attach " + pid)

    base = get_so_base(ci, "libxxxxxx.so")
    print("base:", hex(base))

    # enter_console(ci)

    print(hexdump(ci,base+0xa5910,1024))

    exec_lldb(ci,"memory read %s %s -outfile ./test.bin --binary -force"%(base+0xa5910,base+0xa5910+47308*5))
    # exec_lldb(ci,"br set -a %s"%(base+0x2991c))

    # tmp=ci.GetProcess().ReadMemory(base,1000000,error)
    # print(error)
    # data=bytearray(tmp)
    # index=data.find(bytes({0x11,0x00,0x3D,0xC1}))
    # print(index)

    enter_console(ci)

    # except Exception as e:
    #     print(e)
    exec_lldb(ci, "detach")


if __name__ == '__main__':
    os.popen(
        r"D:\tool\AdbTool1.0.1\adb shell su -c './data/local/tmp/lldb-server p --server --listen unix-abstract:///data/local/tmp/debug.sock'")

    platform: lldb.SBPlatform = lldb.SBPlatform("remote-android")

    error = platform.ConnectRemote(lldb.SBPlatformConnectOptions("unix-abstract-connect:///data/local/tmp/debug.sock"))
    print(error)

    debugger: lldb.SBDebugger = lldb.SBDebugger.Create()
    debugger.SetSelectedPlatform(platform)

    do_task(debugger)

    platform.DisconnectRemote()
    platform.Clear()
    debugger.Clear()
    lldb.SBDebugger.Destroy(debugger)
