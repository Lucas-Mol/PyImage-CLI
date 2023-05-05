import common.msg_printer as msg_printer
import common.image_utils as image_utils
import image_modifiers.converter as converter

_BARELY_WHITE = 240

def _transparentizer_img(img):
    img = img.convert("RGBA")
    datas = img.getdata()
    new_data = from_white_pixel_to_transp(datas)

    img.putdata(new_data)
    return img

def _is_barely_white(data):
    if data is None:
        return True
    else:
        return data[0] >= _BARELY_WHITE and data[1] >= _BARELY_WHITE and data[2] >= _BARELY_WHITE

def from_white_pixel_to_transp(datas):
    new_data = []
    for item in datas:
        if _is_barely_white(item):
            new_data.append((_BARELY_WHITE, _BARELY_WHITE, _BARELY_WHITE, 0))
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

