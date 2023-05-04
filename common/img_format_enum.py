from enum import Enum

class FormatOptions(Enum):
    PNG =   (1, "png", "PNG")
    JPEG =  (2, "jpg", "JPEG")

    def __init__(self, number, extension, format):
        self.number = number
        self.extension = extension
        self.format = format

    @classmethod
    def get_by_number(self, number):
        for option in self:
            if option.number == number:
                return option
        raise ValueError(f"{number} isn't valid")
    
    @classmethod
    def get_by_extension(self, extension):
        for option in self:
            if option.extension == extension:
                return option
        raise ValueError(f"{extension} isn't valid")


