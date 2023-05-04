import sys
import common.msg_printer as msg_printer
from common.function_opts_enum import FunctionOptions

def _no_args():
    return len(sys.argv) < 2

def _choose_options():
    msg_printer.no_args_msg()
    option = int(input())
    option_enum = FunctionOptions.get_by_number(option)
    option_enum._class.run()

def _check_function():
    function_cmd = sys.argv[1]
    try:
        function_enum = FunctionOptions.get_by_command(function_cmd)
        function_enum._class.run_args(sys.argv)
    except ValueError as err:
        print(err.args[0])
        pass


def init():
    msg_printer.ascii_art_intro()
    if _no_args():
        _choose_options()
    else:
        _check_function()
    msg_printer.ending_msg()
        

if __name__ == '__main__':
    init()
