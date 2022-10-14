from pickle import TRUE
import cv2
import numpy as np
from PIL import ImageEnhance, Image, ImageFilter
from matplotlib import pyplot as plt
# plt.style.use('seaborn')

# https://blog.csdn.net/hua_you_qiang/article/details/118683134
# convert PIL to numpy


def PILToNumpy(img):
    img = np.array(img)
    return img


def numpyToPIL(img):
    img = Image.fromarray(np.uint8(img))
    return img


# https://stackoverflow.com/questions/32609098/how-to-fast-change-image-brightness-with-python-opencv


def increase_brightness(img, factor=2.5):
    # https://pythonexamples.org/python-pillow-adjust-image-brightness/
    img = numpyToPIL(img)
    enhancer = ImageEnhance.Brightness(img)

    im_output = enhancer.enhance(factor)
    img = np.array(im_output)
    return img


# blend image
def blend_image(img1, img2):
    img1 = numpyToPIL(img1)
    img2 = numpyToPIL(img2)

    img2 = img2.resize((img1.width, img1.height))
    # add alpha channel
    img1.putalpha(100)

    img2.putalpha(150)

    composite_img = Image.alpha_composite(img2, img1)
    img = PILToNumpy(composite_img)
    return img


# rotate image
def rotate_image(img, angle=45):
    img = numpyToPIL(img)
    img = img.rotate(angle, expand=TRUE)
    img = PILToNumpy(img)
    return img


# https: // www.askpython.com/python/examples/denoising-images-in-python
def denoise_seaborn(img):
    dst = cv2.fastNlMeansDenoisingColored(img, None, 11, 6, 7, 21)

    row, col = 1, 2
    fig, axs = plt.subplots(row, col, figsize=(15, 10))
    fig.tight_layout()
    return cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)


# sharpen image
# https://pythontic.com/image-processing/pillow/sharpen-filter
def sharpen_image(img):
    img = numpyToPIL(img)
    img = img.filter(ImageFilter.SHARPEN)
    img = PILToNumpy(img)
    return img
