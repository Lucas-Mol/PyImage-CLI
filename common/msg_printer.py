from common.function_opts_enum import FunctionOptions

def ascii_art_intro():
    print(" -------------------------------------------------------- ")
    print(" -------------------------------------------------------- ")
    print(" ---   _____       _____                              --- ")
    print(" ---  |  __ \     |_   _|                             --- ")
    print(" ---  | |__) |   _  | |  _ __ ___   __ _  __ _  ___   --- ")
    print(" ---  |  ___/ | | | | | | '_ ` _ \ / _` |/ _` |/ _ \  --- ")
    print(" ---  | |   | |_| |_| |_| | | | | | (_| | (_| |  __/  --- ")
    print(" ---  |_|    \__, |_____|_| |_| |_|\__,_|\__, |\___|  --- ")
    print(" ---          __/ |                       __/ |       --- ")
    print(" ---         |___/                       |___/        --- ")
    print(" -------------------------------------------------------- ")
    print(" -------------------------------------------------------- ")  
    print(" ------------------ Welcome to PyImage ------------------ ") 
    print(" -------------------------------------------------------- ")    
    print("")



def no_args_msg():
    print(" -------------------------------------------------------- ")  
    print(" ------ You've not call me with function arguments ------ ") 
    print(" ---------  Please, choose a function below: ------------ ")
    print("")
    print(f"{FunctionOptions.RESIZER.number}- Resizer ({FunctionOptions.RESIZER.command} | {FunctionOptions.RESIZER.cmd})")
    print(f"{FunctionOptions.CONVERTER.number}- Converter ({FunctionOptions.CONVERTER.command} | {FunctionOptions.CONVERTER.cmd})")
    print(f"{FunctionOptions.PNG_TRANSPARENTIZER.number}- PNG transparentizer ({FunctionOptions.PNG_TRANSPARENTIZER.command} | {FunctionOptions.PNG_TRANSPARENTIZER.cmd})")
    print(f"{FunctionOptions.HELP.number}- Help ({FunctionOptions.HELP.command} | {FunctionOptions.HELP.cmd})")
    print(f"{FunctionOptions.EXIT.number}- Exit")
    print(" -------------------------------------------------------- ")  


def ending_msg():
    print("")
    print(" -------------------------------------------------------- ")  




def resizer_intro():
    print(" -------------------------------------------------------- ")
    print(" --------------------- Resizing... ---------------------- ")
    print(" -------------------------------------------------------- ")
    print("")

def resizer_ending():
    print(" -------------------------------------------------------- ")
    print(" ---------------- Resized successfully! ----------------- ")
    print(" -------------------------------------------------------- ")

def converter_intro():
    print(" -------------------------------------------------------- ")
    print(" -------------------- Converting... --------------------- ")
    print(" -------------------------------------------------------- ")
    print("")

def converter_ending():
    print(" -------------------------------------------------------- ")
    print(" --------------- Converted successfully! ---------------- ")
    print(" -------------------------------------------------------- ")

def transparentizer_intro():
    print(" -------------------------------------------------------- ")
    print(" ------------------ Transparentizer... ------------------ ")
    print(" -------------------------------------------------------- ")
    print("")

def transparentizer_ending():
    print(" -------------------------------------------------------- ")
    print(" ------------ Transparentized successfully! ------------- ")
    print(" -------------------------------------------------------- ")

def helper():
    print(" -------------------------------------------------------- ")
    print(" ----------------------- Help --------------------------- ")
    print(" -------------------------------------------------------- ")
    print("- Commands: ")
    print("")
    print("--resizer (-r): resize a local or url image.                     REQUIRED ARGS:  [1]: a image path locally on your PC or a URL to a image file.")
    print("                                                                                 [2]: a desired height (integer) in pixels. (the resizer keeps proportion)")
    print("--converter (-c): covert a image to PNG or JPEG.                 REQUIRED ARGS:  [1]: a image path locally on your PC or a URL to a image file.")
    print("                                                                                 [2]: a desired format. [Accepted  Formats]: jpg | png")
    print("--png_t (-pt): turn white background in a png to transparent.    REQUIRED ARGS:  [1]: a image path locally on your PC or a URL to a image file.")
    print("--help (-h): call help instructions")
    

