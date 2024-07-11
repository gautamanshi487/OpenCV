import cv2
import numpy as np


img1 = cv2.imread(r"C:\mine Photos\InterIIT 2023\IMG_20231214_225814.jpg")
img1 = cv2.resize(img1,(500,600))
#creating image border 
# brdr = cv2.copyMakeBorder(img1,50,50,85,85,cv2.BORDER_REPLICATE)
brdr = cv2.copyMakeBorder(img1,10,10,5,5,cv2.BORDER_CONSTANT,value = [255,0,125])

cv2.imshow("res",brdr)

cv2.waitKey(0)
cv2.destroyAllWindows()