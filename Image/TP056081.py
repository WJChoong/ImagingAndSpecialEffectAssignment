import cv2
from image import *

# Reading the image
img = cv2.imread('Media/40.jpg')
# img = resize(img)

img = increase_brightness(img, 2.6)
img = sharpen_image(img)
img = rotate_image(img, 10)

cv2.imshow("My Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
