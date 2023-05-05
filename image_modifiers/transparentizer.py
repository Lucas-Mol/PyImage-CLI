import common.msg_printer as msg_printer
from common.accuracy_level_enum import AccuracyLevel
import common.image_utils as image_utils

def _transparentizer_img(img, accuracy_level):
    img = img.convert("RGBA")
    datas = img.getdata()

    accuracy_level_enum = AccuracyLevel.get_by_command(accuracy_level)
    new_data = from_white_pixel_to_transp(datas, accuracy_level_enum.level_value)

    img.putdata(new_data)
    return img

def _is_barely_white(data, level_value):
    if data is None:
        return True
    else:
        return data[0] >= level_value and data[1] >= level_value and data[2] >= level_value

def from_white_pixel_to_transp(datas, level_value):
    new_data = []
    for item in datas:
        if _is_barely_white(item, level_value):
            new_data.append((level_value, level_value, level_value, 0))
        else:
            new_data.append(item)
    return new_data

def _save_img(img):
    file_name = "transparent_image"
    desired_format = "png"
    output_file = image_utils.get_output_file_ext(file_name, desired_format)

    img.save(output_file, format="PNG")

def run():
    img_path = input("Enter with local path/url of image: \n")
    accuracy_level = input("Enter with accuracy level ('all', 'medium' or 'just' white): \n")

    msg_printer.transparentizer_intro()
    img = image_utils.get_image(img_path)
    img = _transparentizer_img(img, accuracy_level)
    _save_img(img)
    msg_printer.transparentizer_ending()

def run_args(args):
    try:
        msg_printer.transparentizer_intro()
        img_path = args[2]
        accuracy_level = args[3]

        img = image_utils.get_image(img_path)
        img = _transparentizer_img(img, accuracy_level)
        _save_img(img)
        msg_printer.transparentizer_ending()
    except IndexError as err:
        print("It's missing a argument(s) to transparentizer")
        pass

