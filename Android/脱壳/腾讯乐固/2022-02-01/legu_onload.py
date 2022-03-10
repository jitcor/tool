# import unicorn.arm_const
import re

import unicorn

import idc



javavm_func_name_list = ['reserved0',
                         'reserved1',
                         'reserved2',
                         'DestroyJavaVM',
                         'AttachCurrentThread',
                         'DetachCurrentThread',
                         'GetEnv',
                         'AttachCurrentThreadAsDaemon']

javaenv_func_name_list = ['reserved0',
                          'reserved1',
                          'reserved2',
                          'reserved3',
                          'GetVersion',
                          'DefineClass',
                          'FindClass',
                          'FromReflectedMethod',
                          'FromReflectedField',
                          'ToReflectedMethod',
                          'GetSuperclass',
                          'IsAssignableFrom',
                          'ToReflectedField',
                          'Throw',
                          'ThrowNew',
                          'ExceptionOccurred',
                          'ExceptionDescribe',
                          'ExceptionClear',
                          'FatalError',
                          'PushLocalFrame',
                          'PopLocalFrame',
                          'NewGlobalRef',
                          'DeleteGlobalRef',
                          'DeleteLocalRef',
                          'IsSameObject',
                          'NewLocalRef',
                          'EnsureLocalCapacity',
                          'AllocObject',
                          'NewObject',
                          'NewObjectV',
                          'NewObjectA',
                          'GetObjectClass',
                          'IsInstanceOf',
                          'GetMethodID',
                          'CallObjectMethod',
                          'CallObjectMethodV',
                          'CallObjectMethodA',
                          'CallBooleanMethod',
                          'CallBooleanMethodV',
                          'CallBooleanMethodA',
                          'CallByteMethod',
                          'CallByteMethodV',
                          'CallByteMethodA',
                          'CallCharMethod',
                          'CallCharMethodV',
                          'CallCharMethodA',
                          'CallShortMethod',
                          'CallShortMethodV',
                          'CallShortMethodA',
                          'CallIntMethod',
                          'CallIntMethodV',
                          'CallIntMethodA',
                          'CallLongMethod',
                          'CallLongMethodV',
                          'CallLongMethodA',
                          'CallFloatMethod',
                          'CallFloatMethodV',
                          'CallFloatMethodA',
                          'CallDoubleMethod',
                          'CallDoubleMethodV',
                          'CallDoubleMethodA',
                          'CallVoidMethod',
                          'CallVoidMethodV',
                          'CallVoidMethodA',
                          'CallNonvirtualObjectMethod',
                          'CallNonvirtualObjectMethodV',
                          'CallNonvirtualObjectMethodA',
                          'CallNonvirtualBooleanMethod',
                          'CallNonvirtualBooleanMethodV',
                          'CallNonvirtualBooleanMethodA',
                          'CallNonvirtualByteMethod',
                          'CallNonvirtualByteMethodV',
                          'CallNonvirtualByteMethodA',
                          'CallNonvirtualCharMethod',
                          'CallNonvirtualCharMethodV',
                          'CallNonvirtualCharMethodA',
                          'CallNonvirtualShortMethod',
                          'CallNonvirtualShortMethodV',
                          'CallNonvirtualShortMethodA',
                          'CallNonvirtualIntMethod',
                          'CallNonvirtualIntMethodV',
                          'CallNonvirtualIntMethodA',
                          'CallNonvirtualLongMethod',
                          'CallNonvirtualLongMethodV',
                          'CallNonvirtualLongMethodA',
                          'CallNonvirtualFloatMethod',
                          'CallNonvirtualFloatMethodV',
                          'CallNonvirtualFloatMethodA',
                          'CallNonvirtualDoubleMethod',
                          'CallNonvirtualDoubleMethodV',
                          'CallNonvirtualDoubleMethodA',
                          'CallNonvirtualVoidMethod',
                          'CallNonvirtualVoidMethodV',
                          'CallNonvirtualVoidMethodA',
                          'GetFieldID',
                          'GetObjectField',
                          'GetBooleanField',
                          'GetByteField',
                          'GetCharField',
                          'GetShortField',
                          'GetIntField',
                          'GetLongField',
                          'GetFloatField',
                          'GetDoubleField',
                          'SetObjectField',
                          'SetBooleanField',
                          'SetByteField',
                          'SetCharField',
                          'SetShortField',
                          'SetIntField',
                          'SetLongField',
                          'SetFloatField',
                          'SetDoubleField',
                          'GetStaticMethodID',
                          'CallStaticObjectMethod',
                          'CallStaticObjectMethodV',
                          'CallStaticObjectMethodA',
                          'CallStaticBooleanMethod',
                          'CallStaticBooleanMethodV',
                          'CallStaticBooleanMethodA',
                          'CallStaticByteMethod',
                          'CallStaticByteMethodV',
                          'CallStaticByteMethodA',
                          'CallStaticCharMethod',
                          'CallStaticCharMethodV',
                          'CallStaticCharMethodA',
                          'CallStaticShortMethod',
                          'CallStaticShortMethodV',
                          'CallStaticShortMethodA',
                          'CallStaticIntMethod',
                          'CallStaticIntMethodV',
                          'CallStaticIntMethodA',
                          'CallStaticLongMethod',
                          'CallStaticLongMethodV',
                          'CallStaticLongMethodA',
                          'CallStaticFloatMethod',
                          'CallStaticFloatMethodV',
                          'CallStaticFloatMethodA',
                          'CallStaticDoubleMethod',
                          'CallStaticDoubleMethodV',
                          'CallStaticDoubleMethodA',
                          'CallStaticVoidMethod',
                          'CallStaticVoidMethodV',
                          'CallStaticVoidMethodA',
                          'GetStaticFieldID',
                          'GetStaticObjectField',
                          'GetStaticBooleanField',
                          'GetStaticByteField',
                          'GetStaticCharField',
                          'GetStaticShortField',
                          'GetStaticIntField',
                          'GetStaticLongField',
                          'GetStaticFloatField',
                          'GetStaticDoubleField',
                          'SetStaticObjectField',
                          'SetStaticBooleanField',
                          'SetStaticByteField',
                          'SetStaticCharField',
                          'SetStaticShortField',
                          'SetStaticIntField',
                          'SetStaticLongField',
                          'SetStaticFloatField',
                          'SetStaticDoubleField',
                          'NewString',
                          'GetStringLength',
                          'GetStringChars',
                          'ReleaseStringChars',
                          'NewStringUTF',
                          'GetStringUTFLength',
                          'GetStringUTFChars',
                          'ReleaseStringUTFChars',
                          'GetArrayLength',
                          'NewObjectArray',
                          'GetObjectArrayElement',
                          'SetObjectArrayElement',
                          'NewBooleanArray',
                          'NewByteArray',
                          'NewCharArray',
                          'NewShortArray',
                          'NewIntArray',
                          'NewLongArray',
                          'NewFloatArray',
                          'NewDoubleArray',
                          'GetBooleanArrayElements',
                          'GetByteArrayElements',
                          'GetCharArrayElements',
                          'GetShortArrayElements',
                          'GetIntArrayElements',
                          'GetLongArrayElements',
                          'GetFloatArrayElements',
                          'GetDoubleArrayElements',
                          'ReleaseBooleanArrayElements',
                          'ReleaseByteArrayElements',
                          'ReleaseCharArrayElements',
                          'ReleaseShortArrayElements',
                          'ReleaseIntArrayElements',
                          'ReleaseLongArrayElements',
                          'ReleaseFloatArrayElements',
                          'ReleaseDoubleArrayElements',
                          'GetBooleanArrayRegion',
                          'GetByteArrayRegion',
                          'GetCharArrayRegion',
                          'GetShortArrayRegion',
                          'GetIntArrayRegion',
                          'GetLongArrayRegion',
                          'GetFloatArrayRegion',
                          'GetDoubleArrayRegion',
                          'SetBooleanArrayRegion',
                          'SetByteArrayRegion',
                          'SetCharArrayRegion',
                          'SetShortArrayRegion',
                          'SetIntArrayRegion',
                          'SetLongArrayRegion',
                          'SetFloatArrayRegion',
                          'SetDoubleArrayRegion',
                          'RegisterNatives',
                          'UnregisterNatives',
                          'MonitorEnter',
                          'MonitorExit',
                          'GetJavaVM',
                          'GetStringRegion',
                          'GetStringUTFRegion',
                          'GetPrimitiveArrayCritical',
                          'ReleasePrimitiveArrayCritical',
                          'GetStringCritical',
                          'ReleaseStringCritical',
                          'NewWeakGlobalRef',
                          'DeleteWeakGlobalRef',
                          'ExceptionCheck',
                          'NewDirectByteBuffer',
                          'GetDirectBufferAddress',
                          'GetDirectBufferCapacity']

class_list = [0]
field_list = [0]
method_list = [0]
object_list = [0]
chars_dict = {0}
fd_list=[0]

def func_mem_invalid_handle(uc, type, address, size, value, user_data):
    print 'func_mem_invalid_handle:', type, hex(address), hex(size), hex(value), user_data
    return False


def func_mem_valid_handle(uc, type, address, size, value, user_data):
    print 'func_mem_valid_handle:', type, hex(address), hex(size), hex(value), hex(func_to_int(uc.mem_read(address,size)))


def func_alloc_mem_valid_handle(uc, type, address, size, value, user_data):
    print 'func_alloc_mem_valid_handle:', type, hex(address), hex(size), hex(value),
    offset = address - user_data
    if offset == 0x2b8:
        print 'init_0'
    elif offset == 0x254:
        print 'ro.build.version.sdk_int'
    elif offset == 0x260:
        print 'dex_count'
    else:
        print hex(offset)
        uc.emu_stop()


def func_code_handle(uc, address, size, user_data):
    print 'func_code_handle:', hex(address), idc.generate_disasm_line(address, 0)


def func_uc_read_str(addr):
    s_len = 0
    while uc.mem_read(addr + s_len, 1)[0] != 0:
        s_len += 1
    return str(uc.mem_read(addr, s_len))


def func_block_handle(uc, address, size, user_data):
    # print 'func_block_handle:', hex(address), '/' * 8,
    r0 = uc.reg_read(unicorn.arm_const.UC_ARM_REG_R0)
    r1 = uc.reg_read(unicorn.arm_const.UC_ARM_REG_R1)
    r2 = uc.reg_read(unicorn.arm_const.UC_ARM_REG_R2)
    r3 = uc.reg_read(unicorn.arm_const.UC_ARM_REG_R3)
    lr = uc.reg_read(unicorn.arm_const.UC_ARM_REG_LR)
    sp = uc.reg_read(unicorn.arm_const.UC_ARM_REG_SP)
    if address == 0x1D48:
        global mm_last
        addr = mm_last
        size = r0 * r1
        size = (size / 0x1000 + (1 if size % 0x1000 else 0)) * 0x1000
        mm_last += size
        uc.mem_map(addr, size)

        print 'calloc(', hex(r0), ',', hex(r1), ') --->', hex(addr)
        uc.hook_add(unicorn.UC_HOOK_MEM_VALID, func_alloc_mem_valid_handle, user_data=addr, begin=addr, end=mm_last)

        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, addr)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
    elif address == 0X1D3C:
        s0 = func_uc_read_str(r0)
        s1 = func_uc_read_str(r1)

        result = cmp(s0, s1)
        print 'strcmp(', s0, ',', s1, ') --->', result
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, result)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0X1CF4:
        uc.mem_write(r0, func_to_bytes(0, r1))
        print '__aeabi_memclr(', hex(r0), ',', hex(r1), ')'
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0X1D00:
        prop_name = func_uc_read_str(r0)
        if prop_name == 'ro.build.version.release':
            prop_val = '8.1.0'
            uc.mem_write(r1, bytes(prop_val))
        else:
            prop_val = 'unknown prop .....'
            uc.emu_stop()
        print '__system_property_get(', prop_name, ',', hex(r1), ') --->', prop_val
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0X1D18:
        format_str = func_uc_read_str(r2)
        op_chs = re.findall(r'%(\S)', format_str)
        arg_list = []
        arg_val = []
        if len(op_chs) > 0:
            arg_val.append(hex(r3))
            if op_chs[0] == 'd':
                arg_list.append(r3)
            elif op_chs[0] == 's':
                arg_list.append(func_uc_read_str(r3))
            else:
                arg_list.append('errrr:' + op_chs[0])
                uc.emu_stop()
            offset = 0
            for op in op_chs[1:]:
                if op == 'd':
                    arg = func_to_int(uc.mem_read(sp + offset, 4))
                    arg_list.append(arg)
                    arg_val.append(hex(arg))
                    offset += 4
                elif op == 's':
                    arg = func_to_int(uc.mem_read(sp + offset, 4))
                    arg_list.append(func_uc_read_str(arg))
                    arg_val.append(hex(arg))
                    offset += 4
                else:
                    arg_list.append('errrr:' + op)
                    uc.emu_stop()
                    break

        ret = format_str % tuple(arg_list)
        uc.mem_write(r0, bytes(ret))
        # print 'snprintf(', hex(r0), ',', hex(r1), ',', format_str, ',', op_chs, arg_val, arg_list, ') --->', ret
        print 'snprintf(', ') --->', ret
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, len(ret))
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0x1d24:
        format_str = func_uc_read_str(r1)
        op_chs = re.findall(r'%(\S)', format_str)
        arg_list = []
        arg_val = []
        if len(op_chs) > 0:
            arg_val.append(hex(r2))
            if op_chs[0] == 'd':
                arg_list.append(r2)
            elif op_chs[0] == 's':
                arg_list.append(func_uc_read_str(r2))
            else:
                arg_list.append('errrr:' + op_chs[0])
                uc.emu_stop()

            if len(op_chs) > 1:
                arg_val.append(hex(r3))
                if op_chs[1] == 'd':
                    arg_list.append(r3)
                elif op_chs[1] == 's':
                    arg_list.append(func_uc_read_str(r3))
                else:
                    arg_list.append('errrr:' + op_chs[1])
                    uc.emu_stop()

                offset = 0
                for op in op_chs[2:]:
                    if op == 'd':
                        arg = func_to_int(uc.mem_read(sp + offset, 4))
                        arg_list.append(arg)
                        arg_val.append(hex(arg))
                        offset += 4
                    elif op == 's':
                        arg = func_to_int(uc.mem_read(sp + offset, 4))
                        arg_list.append(func_uc_read_str(arg))
                        arg_val.append(hex(arg))
                        offset += 4
                    else:
                        arg_list.append('errrr:' + op)
                        uc.emu_stop()
                        break

        ret = format_str % tuple(arg_list)
        uc.mem_write(r0, bytes(ret))
        # print 'snprintf(', hex(r0), ',', format_str, ',', op_chs, arg_val, arg_list, ') --->', ret
        print 'snprintf(', ') --->', ret
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, len(ret))
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0X1F668:
        print 'call init_ctx --->', hex(address)
        ctx_addr = r2
        uc.mem_write(ctx_addr + 0, bytes('/data/app/com.baidu.homework-ynm_loH-SSolI21s3Wbc0A==/base.apk'))
        uc.mem_write(ctx_addr + 0x254, func_to_bytes(27, 4))
        uc.mem_write(ctx_addr + 0x260, func_to_bytes(9, 4))

        last_offset = 0x300

        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
    elif address == 0x1E224:
        print 'call BuglyLog.i --->', func_uc_read_str(r1)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0x1d30:
        print 'access --->', func_uc_read_str(r0), hex(r1)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0xcea8:
        print 'call load --->',hex(address)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0x1d84:
        path=func_uc_read_str(r0)
        fd=-1
        if path.startswith('/data/data/com.baidu.homework/files/prodexdir'):
            r_path=path.replace('/data/data/com.baidu.homework/files','/Users/lll19/Downloads/legu')
            fd=len(fd_list)
            fd_list.append(open(r_path,'rb'))
        else:
            uc.emu_stop()
        print 'open',path, hex(r1),' --->',fd
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, fd)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0x1f88:
        content=bytes(fd_list[r0].read(r2))
        uc.mem_write(r1,content)
        print 'read',r0, hex(r2),' --->',len(content)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, len(content))
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0x3004c:
        fd_list[r0].close()
        print 'close',r0
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0x1DEA0:
        path = '/data/data/com.baidu.homework/files'
        uc.mem_write(r1, bytes(path))
        print 'call get_files_dir --->', path
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
        uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        # uc.emu_stop()
    elif address == 0X1E108:
        print 'call get_sdk_int '
    elif address == 0X2B604:
        print 'call decode_toversion --->',hex(address)
    elif address == 0x3A62:
        print 'call decode_toversion --->',uc.mem_read(0x36A8C,0x10)
        # uc.emu_stop()  # AWB8Aak4h1vFZZEn
    elif address == 0x1de78:
        print 'call get_prodexdir '
    elif address in (0x1de82, 0x1de94L,0x2b612L,0x2b616L,0x2b624L,0x2b642L,0x2b656L,0x2b63cL,
                     0x2b658L,0x2b662L):
        # print
        pass
    elif javavm_func_start <= address < javavm_func_end:
        func_name = javavm_func_name_list[(address - javavm_func_start) / 4]
        if func_name == 'GetEnv':
            print func_name, '(', hex(r0),',', hex(r1),',', hex(r2), ') --->', hex(javaenv_start)
            uc.mem_write(r1, func_to_bytes(javaenv_start, 4))
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        else:
            print func_name
            uc.emu_stop()
    elif javaenv_func_start <= address < javaenv_func_end:
        func_name = javaenv_func_name_list[(address - javaenv_func_start) / 4]
        if func_name == 'FindClass':
            class_id = len(class_list)
            class_name = idc.get_strlit_contents(r1)
            class_list.append(class_name)
            print func_name, '(', class_name, ') --->', hex(class_id)
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, class_id)
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        elif func_name == 'RegisterNatives':
            print func_name, '(', hex(r1),',', hex(r2),',', hex(r3), ') --->', class_list[r1]
            for i in range(r3):
                item_addr = r2 + 0xc * i
                print idc.get_strlit_contents(idc.get_wide_dword(item_addr)), idc.get_strlit_contents(
                    idc.get_wide_dword(item_addr + 4)), hex(idc.get_wide_dword(item_addr + 8))
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        elif func_name == 'GetStaticFieldID':
            field_id = len(field_list)
            class_name = class_list[r1]
            field_name = idc.get_strlit_contents(r2)
            field_sig = idc.get_strlit_contents(r3)
            field_list.append(field_name + ':' + field_sig)
            print func_name, '(', class_name, field_name, field_sig, ') --->', hex(field_id)
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, field_id)
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
        elif func_name == 'GetStaticObjectField':
            object_id = len(object_list)
            class_name = class_list[r1]
            field_str = field_list[r1]
            field = class_name + '->' + field_str
            if field == 'com/wrapper/proxyapplication/WrapperProxyApplication->tinkerApp:Ljava/lang/String;':
                object_list.append('tinker not support')
            else:
                # object_list.append('unknown field ..........................')
                uc.emu_stop()
            print func_name, '(', class_name, field_str, ') --->', hex(object_id)
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, object_id)
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
            # uc.emu_stop()
        elif func_name == 'GetStringUTFChars':
            obj = object_list[r1]
            print func_name, '(', r1,',', r2, ') --->', obj
            global mm_last
            addr = mm_last
            size = len(obj) + 1
            size = (size / 0x1000 + (1 if size % 0x1000 else 0)) * 0x1000
            mm_last += size
            uc.mem_map(addr, size)
            uc.mem_write(addr, bytes(obj))
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, addr)
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
            # uc.emu_stop()
        elif func_name == 'ReleaseStringUTFChars':
            obj = object_list[r1]
            print func_name, '(', hex(r1),',', hex(r2), ') --->', obj
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
            # uc.emu_stop()
        elif func_name == 'DeleteLocalRef':
            print func_name, '(', hex(r1), ')'
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, 0)
            uc.reg_write(unicorn.arm_const.UC_ARM_REG_PC, lr)
            # uc.emu_stop()
        else:
            print func_name
            uc.emu_stop()
    elif address < func_start or address >= func_end:
        print
        uc.emu_stop()
    # else:
    #     print


def func_to_bytes(n, to_len):
    bytes_list = []
    while n:
        bytes_list.append(chr(n & 0xff))
        n >>= 8
    bb = [chr(0) for i in range(len(bytes_list), to_len)]
    bytes_list.extend(bb)
    return bytes(''.join(bytes_list))


def func_to_int(barr):
    val = 0
    for item in enumerate(barr):
        val |= item[1] << (item[0] * 8)
    return val


print '\n' * 100
# bin_len: 0x37000L
# stack_top: 0x37000L
# stack_bottom: 0x137000L
# javavm_start: 0x237000L


bin_len = idc.prev_addr(idc.BADADDR)
bin_len = (bin_len / 0x1000 + (1 if bin_len % 0x1000 else 0)) * 0x1000
print 'bin_len:', hex(bin_len)
bin_path = 'C:\\Users\\lll19\\Downloads\\legu\\elf_bin'
# idc.savefile(bin_path, 0, 0, bin_len)

f_bin = open(bin_path, 'rb')
bin_bytes = bytes(f_bin.read())
f_bin.close()

# func_start = 0x258E8
func_start = 0x2710
func_end = idc.find_func_end(func_start)

stack_size = 0x100000
stack_top = bin_len
stack_bottom = stack_top + stack_size

javavm_start = stack_bottom
javavm_buf_len = 0x1000
javavm_end = javavm_start + javavm_buf_len

javaenv_start = javavm_end
javaenv_buf_len = 0x1000
javaenv_end = javaenv_start + javaenv_buf_len

mm_last = javaenv_end

uc = unicorn.Uc(unicorn.UC_ARCH_ARM, unicorn.UC_MODE_THUMB)

uc.mem_map(0, bin_len)
uc.mem_write(0, bin_bytes)

print 'stack_top:', hex(stack_top)
print 'stack_bottom:', hex(stack_bottom)
uc.mem_map(stack_top, stack_size)
uc.reg_write(unicorn.arm_const.UC_ARM_REG_SP, stack_bottom)

print 'javavm_start:', hex(javavm_start)
uc.mem_map(javavm_start, javavm_buf_len)
bytes_list = []
bytes_list.append(func_to_bytes(javavm_start + 4 + 4, 4))
bytes_list.append(func_to_bytes(0, 4))
javavm_func_start = javavm_start + (2 + 8) * 4
javavm_func_end = javavm_func_start + 8 * 4
for i in range(8):
    bytes_list.append(func_to_bytes(javavm_func_start + i * 4, 4))
uc.mem_write(javavm_start, bytes(''.join(bytes_list)))
# b= uc.mem_read(javavm_start,8*4*2)
# for i in b:
#     print hex(i),


print 'javaenv_start:', hex(javaenv_start)
uc.mem_map(javaenv_start, javaenv_buf_len)
bytes_list = []
bytes_list.append(func_to_bytes(javaenv_start + 4, 4))
javaenv_func_start = javaenv_start + (1 + 232) * 4
javaenv_func_end = javaenv_func_start + 232 * 4
for i in range(232):
    bytes_list.append(func_to_bytes(javaenv_func_start + i * 4, 4))
uc.mem_write(javaenv_start, bytes(''.join(bytes_list)))

uc.reg_write(unicorn.arm_const.UC_ARM_REG_R0, javavm_start)
uc.reg_write(unicorn.arm_const.UC_ARM_REG_R1, javavm_start + 4)

uc.reg_write(unicorn.arm_const.UC_ARM_REG_LR, 0)

uc.hook_add(unicorn.UC_HOOK_MEM_INVALID, func_mem_invalid_handle)
# uc.hook_add(unicorn.UC_HOOK_MEM_VALID, func_mem_valid_handle, begin=0, end=bin_len)
# uc.hook_add(unicorn.UC_HOOK_CODE, func_code_handle)
uc.hook_add(unicorn.UC_HOOK_BLOCK, func_block_handle)

uc.emu_start(func_start + 1, func_end)

print 'end.....'
