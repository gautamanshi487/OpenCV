import cv2
import numpy as np
#GAUSSIAN PYRAMID--
#in 2 steps - pyrdown ya pyrup

#load image into gray scale
img = cv2.imread(r"C:\Opencv_output\avengers.jpg")
img = cv2.resize(img,(700,700))

# pd1 = cv2.pyrDown(img)
# pd2 = cv2.pyrDown(pd1)

# #pyrup
# #if we pyrup any pyrdown image both are not equal
# pu1 = cv2.pyrUp(pd2)

# #results------------------
# cv2.imshow("original==",img)
# cv2.imshow("pd1==",pd1)
# cv2.imshow("pd2==",pd2)
# cv2.imshow("pu1==",pu1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


#using loop---
img1 = img.copy()
data = [img1]

for i in range (4):
    img1 = cv2.pyrDown(img1)
    data.append(img1)
    cv2.imshow("Result"+str(i),img1)
    
cv2.imshow("original==",img)
cv2.waitKey(0)
cv2.destroyAllWindows() 