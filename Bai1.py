from cv2 import cv2
img = cv2.imread('Picture1.jpg')
# mau than nhiet
img= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# mau xam
img = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
cv2.imshow("image",img)
# Cat anh
img2 = img[200:500,100:600]

cv2.imshow("image2",img2)
cv2.waitKey()