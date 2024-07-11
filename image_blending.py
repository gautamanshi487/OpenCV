import cv2
import numpy as np

#read two different images of same channel
img1 = cv2.imread(r"C:\Opencv_output\roi_opr.jpg")
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread(r"C:\Opencv_output\bro_thor.jpg")
img2 = cv2.resize(img2,(500,700))

# cv2.imshow("thor==",img1)
# cv2.imshow("bro_thor==",img2)

# result = img2+img1 
# cv2.imshow("result is",result)

# result1 = cv2.add(img1,img2)   #chahe 2 pahle pass kra do
# cv2.imshow("result1 is",result1)

result2 = cv2.addWeighted(img1,0.8,img2,0.2,0)
cv2.imshow("result2 is = ",result2)
cv2.waitKey(0)
cv2.destroyAllWindows()