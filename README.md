# PyImage-CLI
A command line interface to manipulate images
## 
The PyImage-CLI is a project made to solve basic image manipulation demands. It's build in Python and has the purpose to be easily accessible to developers, helping through theirs development working process (who hasn't ever browsed an image resizer or converter to use an image in a project?! lol).

## Overview:

![Welcome to PyImage](https://cdn.discordapp.com/attachments/778788148921761822/1103820145656336454/image.png)

## Functions
Here some functions and how to call'em:
| Function            | Command               | Description                                     | Argumments                                                                |
|---------------------|-----------------------|-------------------------------------------------|---------------------------------------------------------------------------|
| Resizer             |  `--resizer \| -r`    |  resize a local or url image                    | [1]: a image path locally on your PC or a URL to a image file             |
|                     |                       |                                                 | [2]: a desired height (integer) in pixels. (the resizer keeps proportion) |
| Converter           |  `--converter \| -c`  |  covert a image to PNG or JPEG.                 | [1]: a image path locally on your PC or a URL to a image file.            |
|                     |                       |                                                 | [2]: a desired format. [Accepted  Formats]: jpg | png                     |
| PNG Transparentizer |  `--png_t \| -pt`     |  turn white background in a png to transparent. | [1]: a image path locally on your PC or a URL to a image file.            |
| Help                |  `--help \| -h`       |  call help instructions                         | `--`                                                                      |

## How to use it:
Just use: `python pyimage.py`

**Recommendation:**

You can install pyinstaller with: `pip install pyinstaller` <br/>
And use `pyinstaller pyimage.py`

It'll convert this project in a executable. Therefore, you can add this new executable as a environment variable on PATH and use it at any place on your terminal :D (To be used as env variable, PyImage-CLI saves the result manipulated image on pwd)

## Tech Stack

- Python
