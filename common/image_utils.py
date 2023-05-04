import os
from urllib.request import urlopen
from io import BytesIO
from PIL import Image

def _is_URL(path):
    return path.startswith("http" or "\"http")

def get_image(img_path):
    if _is_URL(img_path):
        response = urlopen(img_path)
        return Image.open(BytesIO(response.read())).convert("RGB")
    else:
        return Image.open(img_path).convert("RGB")


def get_output_file(name):
    output_file = os.path.join(os.getcwd(), f"{name}.jpg")

    if os.path.exists(output_file):
        i = 1
        output_file_no_extension = output_file[:-4]
        while os.path.exists(f"{output_file_no_extension}_{i}.jpg"):
            i += 1
        output_file = f"{output_file_no_extension}_{i}.jpg"
    return output_file

def get_output_file_ext(name, desired_extension):
    output_file = os.path.join(os.getcwd(), f"{name}." + desired_extension)

    if os.path.exists(output_file):
        i = 1
        output_file_no_extension = output_file[:-4]
        while os.path.exists(f"{output_file_no_extension}_{i}.{desired_extension}"):
            i += 1
        output_file = f"{output_file_no_extension}_{i}.{desired_extension}"
    return output_file