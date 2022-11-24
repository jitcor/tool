import pydevd_pycharm

import ida_funcs
import ida_kernwin
import ida_ua
import idaapi
import idc
import unicorn

class ToClang(ida_kernwin.action_handler_t):
    def __init__(self, message):
        ida_kernwin.action_handler_t.__init__(self)
        self.message = message

    def activate(self, ctx):
        print("ToClang ok")
        ea = idc.here()
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
        custom_code=""
        while cur_addr<= pfn.end_ea:
            next_addr=idc.next_head(cur_addr, pfn.end_ea)
            asm_size=next_addr-cur_addr
            asm=idc.generate_disasm_line(cur_addr,0)
            m=idc.print_insn_mnem(cur_addr)
            # print("process asm: ", asm)
            if m=="ADD":
                opt = idc.get_operand_type(cur_addr, 0)
                op1 = idc.print_operand(cur_addr, 0)
                op2 = idc.print_operand(cur_addr, 1)
                op2_value=idc.get_operand_value(cur_addr,1)
                op3 = idc.print_operand(cur_addr, 2)
                op3_value=idc.get_operand_value(cur_addr,2)
                print("process 0x%x asm: %s op2_value: %d op3_value: %d"%(cur_addr,asm,op2_value,op3_value))
                if op3 is "":
                    print("%s=%s+%s" % (op1, op1, op2))
                elif op3.startswith("#"):
                    print("%s=%s+%s" % (op1, op2, op3[1:]))
                else:
                    print("%s=%s+%s" % (op1, op2, op3))
            elif m=="SUB":

                pass
            cur_addr = next_addr

        return 1

    def update(self, ctx):
        return ida_kernwin.AST_ENABLE_FOR_WIDGET if ctx.widget_type == ida_kernwin.BWN_DISASM else ida_kernwin.AST_DISABLE_FOR_WIDGET

hooks = None
act_name = "ToClang"
if __name__ == '__main__':
    if ida_kernwin.register_action(ida_kernwin.action_desc_t(
            act_name,
            "To Clang",
            ToClang("developer")
    )):
        print("register toClang action ok")
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