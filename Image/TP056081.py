import cv2
from image import *

# Reading the image
img = cv2.imread('Media/40.jpg')
img1 = cv2.imread('Media/sailing_star.jpg')

img = blend_image(img, img1, 160, 80)
img = increase_brightness(img, 1.9)
img = sharpen_image(img)
img = rotate_image(img, 10)

cv2.imshow("My Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
