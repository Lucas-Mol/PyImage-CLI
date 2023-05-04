import common.msg_printer as msg_printer
import common.image_utils as image_utils
from common.img_format_enum import FormatOptions


def _save_img(img, desired_extension):
    file_name = "converted_image"
    output_file = image_utils.get_output_file_ext(file_name, desired_extension)

    format_enum = FormatOptions.get_by_extension(desired_extension)
    img.save(output_file, format=format_enum.format)

def run():
    img_path = input("Enter with local path/url of image: \n")
    desired_extension = input("Enter with the desired desired extension: \n")

    img = image_utils.get_image(img_path)
    _save_img(img, desired_extension)

def run_args(args):
    try:
        msg_printer.converter_intro()
        img_path = args[2]
        desired_extension = args[3]

        img = image_utils.get_image(img_path)
        _save_img(img, desired_extension)
        msg_printer.converter_ending()
    except IndexError as err:
        print("It's missing a argument(s) to convert")
        pass

