
import ida_funcs
import ida_kernwin
import ida_ua
import idaapi
import idc
import unicorn


def unicorn_exec(asm_bin:bytes):
    ADDRESS=0x8000
    STACK_BASE=0x0
    STACK_SIZE=0x7000
    MEM_SIZE=20 * 1024 * 1024 #20M
    #asm_bin = bytes.fromhex("f0b503af8db00a9201b420bca92080002968")
    bin_len = len(asm_bin)
    #init
    uc = unicorn.Uc(unicorn.UC_ARCH_ARM, unicorn.UC_MODE_THUMB)

    #sp
    sp=STACK_SIZE
    uc.mem_map(STACK_BASE,STACK_SIZE)
    uc.reg_write(unicorn.arm_const.UC_ARM_REG_SP,sp)

    #call
    uc.mem_map(ADDRESS,MEM_SIZE)
    uc.mem_write(ADDRESS,asm_bin)
    uc.emu_start(ADDRESS|1,ADDRESS+bin_len)

    #result
    print("default value:r0-r12=0,r13(sp)=0x%x,r14(lr)=0,r15(pc)=0x%x"%(STACK_SIZE,ADDRESS))
    print("r0: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R0))
    print("r1: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R1))
    print("r2: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R2))
    print("r3: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R3))
    print("r4: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R4))
    print("r5: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R5))
    print("r6: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R6))
    print("r7: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R7))
    print("r8: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R8))
    print("r9: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R9))
    print("r10: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R10))
    print("r11: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R11))
    print("r12: 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R12))
    sp_=uc.reg_read(unicorn.arm_const.UC_ARM_REG_R13)
    print("r13(sp): 0x%x(%s)"%(sp_,hex(sp_-STACK_SIZE)))
    print("r14(lr): 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R14))
    print("r15(pc): 0x%x"%uc.reg_read(unicorn.arm_const.UC_ARM_REG_R15))

class ToUnicorn(ida_kernwin.action_handler_t):
    def __init__(self, message):
        ida_kernwin.action_handler_t.__init__(self)
        self.message = message

    def activate(self, ctx):
        print("ToUnicorn ok")
        ea = idc.here()
        next_addr = idc.next_head(ea)

        pfn=ida_funcs.get_fchunk(ea)
        if pfn is None:
            print("No function at 0x%x!"%pfn)
            return 1
        print("current chunk boundaries: 0x%x..0x%x" % (pfn.start_ea, pfn.end_ea))
        cur_addr =pfn.start_ea
        #pydevd_pycharm.settrace('localhost', port=5070, stdoutToServer=True, stderrToServer=True)
        print("o_near:",idc.o_near)
        print("o_reg:",idc.o_reg)
        print("o_imm:",idc.o_imm)
        print("o_mem:",idc.o_mem)
        asm_bin = idc.get_bytes(cur_addr, next_addr - cur_addr)
        bin_len=len(asm_bin)
        print("bin_len:%d"%bin_len)
        print("bin_hex:%s"%asm_bin.hex())

        # unicorn
        unicorn_exec(asm_bin)

        return 1

    def update(self, ctx):
        return ida_kernwin.AST_ENABLE_FOR_WIDGET if ctx.widget_type == ida_kernwin.BWN_DISASM else ida_kernwin.AST_DISABLE_FOR_WIDGET

hooks = None
act_name = "ToUnicorn"
if __name__ == '__main__':
    if ida_kernwin.register_action(ida_kernwin.action_desc_t(
            act_name,
            "To Unicorn",
            ToUnicorn("developer")
    )):
        print("register toUnicorn action ok")
        if ida_kernwin.attach_action_to_menu("Edit/Export data", act_name, ida_kernwin.SETMENU_APP):
            print("Attached to menu.")
        else:
            print("Failed attaching to menu.")


        class Hooks(ida_kernwin.UI_Hooks):
            def finish_populating_widget_popup(self, widget, popup):
                # We'll add our action to all "IDA View-*"s.
                # If we wanted to add it only to "IDA View-A", we could
                # also discriminate on the widget's title:
                #
                #  if ida_kernwin.get_widget_title(widget) == "IDA View-A":
                #      ...
                #
                if ida_kernwin.get_widget_type(widget) == ida_kernwin.BWN_DISASM:
                    ida_kernwin.attach_action_to_popup(widget, popup, act_name, None)


        hooks = Hooks()
        hooks.hook()
    else:
        print("Action found; unregistering.")
        # No need to call detach_action_from_menu(); it'll be
        # done automatically on destruction of the action.
        if ida_kernwin.unregister_action(act_name):
            print("Unregistered.")
        else:
            print("Failed to unregister action.")
        if hooks is not None:
            hooks.unhook()
            hooks = None