import common.msg_printer as msg_printer
import common.image_utils as image_utils
from PIL import Image

def _resize_img(img, img_height):
    width, height = img.size
    aspect_ratio = height / width
    img_width = int(img_height / aspect_ratio)
    return img.resize((img_width, img_height), Image.Resampling.LANCZOS)

def _save_img(img):
    file_name = "resized_image"
    output_file = image_utils.get_output_file(file_name)

    img.save(output_file)

def run():
    img_path = input("Enter with local path/url of image: \n")
    img_height = int(input("Enter with the desired height in pxl: \n"))

    img = image_utils.get_image(img_path)
    img = _resize_img(img, img_height)
    _save_img(img)

def run_args(args):
    try:
        msg_printer.resizer_intro()
        img_path = args[2]
        img_height = int(args[3])

        img = image_utils.get_image(img_path)
        img = _resize_img(img, img_height)
        _save_img(img)
        msg_printer.resizer_ending()
    except IndexError as err:
        print("It's missing a argument(s) to resize")
        pass

