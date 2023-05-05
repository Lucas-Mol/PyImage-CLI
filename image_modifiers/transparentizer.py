import common.msg_printer as msg_printer
import common.image_utils as image_utils
import image_modifiers.converter as converter

_WHITE = 255

def _transparentizer_img(img):
    img = img.convert("RGBA")
    datas = img.getdata()
    new_data = []

    for item in datas:
        if item[0] == _WHITE and item[1] == _WHITE and item[2] == _WHITE:
            new_data.append((_WHITE, _WHITE, _WHITE, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img

def _save_img(img):
    file_name = "transparent_image"
    output_file = image_utils.get_output_file(file_name)

    img.save(output_file, format="PNG")

def run():
    img_path = input("Enter with local path/url of image: \n")

    msg_printer.transparentizer_intro()
    img = image_utils.get_image(img_path)
    img = _transparentizer_img(img)
    _save_img(img)
    msg_printer.transparentizer_ending()

def run_args(args):
    try:
        msg_printer.transparentizer_intro()
        img_path = args[2]

        img = image_utils.get_image(img_path)
        img = _transparentizer_img(img)
        _save_img(img)
        msg_printer.transparentizer_ending()
    except IndexError as err:
        print("It's missing a argument(s) to resize")
        pass

