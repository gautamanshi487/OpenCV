import cv2
import numpy as np

img = cv2.imread(r"C:\Opencv_output\logo.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img1,50,255,cv2.THRESH_BINARY)      #we also can use 0 in place of cv2.THRESH_BINARY

#findcontour
contours,hierachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(contours,len(contours))

# drawcontours
img = cv2.drawContours(img,contours,-1,(25,100,50),4)

cv2.imshow("original===",img)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)
cv2.waitKey(0)
cv2.destroyAllwindow()

