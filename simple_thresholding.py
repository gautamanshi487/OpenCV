import cv2 
import numpy as np

img = cv2.imread(r"C:\Opencv_output\black_white.png",0)
# img = cv2.imread(r"C:\Users\anshika\Pictures\Camera Roll\WIN_20230427_16_05_51_Pro.jpg")
img = cv2.resize(img,(300,300))
cv2.imshow("data",img)

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("1 - THRESH_BINARY",th1)
cv2.imshow("2 -THRESH_BINARY_INV ", th2)
cv2.imshow("3- THRESH_TRUNC", th3)
cv2.imshow("4 - THRESH_TOZERO", th4)
cv2.imshow("5 - THRESH_TOZERO_INV", th5)
cv2.waitKey(0)
cv2.destroyAllWindows()