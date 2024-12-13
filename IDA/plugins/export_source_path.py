# -*- coding:utf-8 -*-
import os
import re

from idaapi import plugin_t
from idaapi import PLUGIN_PROC
from idaapi import PLUGIN_OK
import ida_nalt
import idaapi
import idautils
import idc
import time
from pathlib import Path


# 获取SO文件名和路径
def getSoPathAndName():
    fullpath = ida_nalt.get_input_file_path()
    filepath, filename = os.path.split(fullpath)
    return filepath, filename


# 获取代码段的范围
def getSegAddr():
    textStart = []
    textEnd = []

    for seg in idautils.Segments():
        if (idc.get_segm_name(seg)).lower() == '.text' or (
                idc.get_segm_name(seg)).lower() == 'text':
            tempStart = idc.get_segm_start(seg)
            tempEnd = idc.get_segm_end(seg)

            textStart.append(tempStart)
            textEnd.append(tempEnd)

    return min(textStart), max(textEnd)


def create_file(path: str):
    try:
        if os.path.exists(path):
            return
        if path[-1] == '/':
            if not os.path.exists(path):
                os.makedirs(path)
            return
        file_path = Path(path)
        if not file_path.parent.exists():
            file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch(exist_ok=True)
    except Exception as e:
        print(e)



def txt_to_path():
    dir = "./"
    for line in open(dir + "source_path.txt"):
        create_file(dir + line.strip())


def get_so_path_and_name():
    fullpath = ida_nalt.get_input_file_path()
    filepath, filename = os.path.split(fullpath)
    return filepath, filename


class PluginMain(plugin_t):
    flags = PLUGIN_PROC
    comment = "export_source_path"
    help = ""
    wanted_name = "export_source_path"
    wanted_hotkey = ""

    def init(self):
        print("export_source_path(v0.1) plugin has been loaded.")
        return PLUGIN_OK

    def run(self, arg):
        so_path,so_name = get_so_path_and_name()
        out_dir=so_path+os.sep+so_name+"_source_path"+os.sep
        sc = idaapi.string_info_t()
        for i in range(0, idaapi.get_strlist_qty()):
            idaapi.get_strlist_item(sc, i)
            text = idaapi.get_strlit_contents(sc.ea, sc.length, sc.type).decode()
            if re.compile(r"""^(?:
        (?=.*?/)                                # 有斜杠的情况
        (?:\.\.?/)*[A-Za-z0-9._-]+(?:/[A-Za-z0-9._-]+)*/*

        |

        (?!.*?/)                                # 无斜杠的情况
        [A-Za-z0-9._-]+\.[A-Za-z0-9]+
    )$""",re.VERBOSE).match(text):
                create_file(out_dir + text.strip())
                print("create file: ", text)
        print("The source path dir: %s" % out_dir)

    def term(self):
        pass


def PLUGIN_ENTRY():
    return PluginMain()
