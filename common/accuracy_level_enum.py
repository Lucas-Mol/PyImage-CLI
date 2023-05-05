from enum import Enum

class AccuracyLevel(Enum):
    JUST = (0, "just", 255)
    MEDIUM =  (1, "medium", 225)
    ALL =   (2, "all", 200)

    def __init__(self, number, argument, level_value):
        self.number = number
        self.argument = argument
        self.level_value = level_value

    @classmethod
    def _get_by_number_atr(self, number):
        for option in self:
            if option.number == number:
                return option
        return None
    
    @classmethod
    def _get_by_argument_atr(self, argument):
        for option in self:
            if option.argument == argument:
                return option
        return None
    
    @classmethod
    def get_by_command(self, command):
        option = self._get_by_argument_atr(command)
        if option is None:
            option = self._get_by_number_atr(int(command))
        if option is None:
             raise ValueError(f"{command} is not valid!")
        else:
            return option   


