import cv2

img = cv2.imread('photo.jpg')
gray = cv2.imread('photo.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Nature Image',img)
cv2.imshow('Gray Nature Image',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
