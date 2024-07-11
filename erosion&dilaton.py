
import cv2
import numpy as np

#Erosion---
#it erodes away the boundaries of foreground object
#kernal slides through all the image and all the pixel 
#from the original image conside 1 only if kernal's pixel is 1

img = cv2.imread(r"C:\Opencv_output\col_balls.jpg",0)
_,mask= cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2),np.uint8)# 5x5 kernel with full of ones. 
e = cv2.erode(mask,kernel) #optional parameters   iterations = 2

cv2.imshow("img",img) 
cv2.imshow("ker=",kernel)
cv2.imshow("mask==",mask)
cv2.imshow("erosion==",e)

#dilation-resolve the distortion in the image
#It is just opposite of erosion.

kernel = np.ones((3,3),np.uint8)# 5x5 kernel with full of ones.  
d = cv2.dilate(mask,kernel) #iterations = 2 (optional parameters) iterations = 2
cv2.imshow("dilate==",d)


#just all windows in one
# from matplotlib import pyplot as plt
# titles = ["img","mask","erosion","dilation"]
# images = [img,mask,e,d]
# for i in range(4):
#     plt.subplot(2, 2, i+1)
#     plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()