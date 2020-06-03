import cv2
from matplotlib import pyplot as plt

img = cv2.imread("picsart.jpg")
#gray = cv2.imread('picsart.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(img)