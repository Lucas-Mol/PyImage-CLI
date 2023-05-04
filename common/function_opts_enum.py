import sys
from enum import Enum
from image_modifiers import resizer, converter, transparentizer
import common.exit as exit
import common.helper as helper

class FunctionOptions(Enum):
    RESIZER =             (1, "--resizer",   "-r",  resizer)
    CONVERTER =           (2, "--converter", "-c",  converter)
    PNG_TRANSPARENTIZER = (3, "--png_t",     "-pt", transparentizer)
    HELP =                (4, "--help",      "-h",  helper)
    EXIT =                (0, ""           , "",    exit)

    def __init__(self, number, command, cmd, _class):
        self.number = number
        self.command = command
        self.cmd = cmd
        self._class = _class

    @classmethod
    def get_by_number(self, number):
        for option in self:
            if option.number == number:
                return option
        raise ValueError(f"{number} isn't valid")
    
    @classmethod
    def _get_by_command_atr(self, command):
        for option in self:
            if option.command == command:
                return option
        return None
    
    @classmethod
    def _get_by_cmd_atr(self, cmd):
        for option in self:
            if option.cmd == cmd:
                return option
        return None
    
    @classmethod
    def get_by_command(self, command):
        option = self._get_by_command_atr(command)
        if option is None:
            option = self._get_by_cmd_atr(command)
        if option is None:
             raise ValueError(f"{command} is not valid!")
        else:
            return option        
