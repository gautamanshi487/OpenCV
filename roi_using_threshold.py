#In this we try to perfrom roi extraction any shaped object
import cv2
import numpy as np

# Load two images
img1 = cv2.imread(r"C:\Opencv_output\hero1.jpg")
img2 = cv2.imread(r"C:\Opencv_output\strom_breaker.JPG")
 
img1 = cv2.resize(img1,(1024,650))
img2 = cv2.resize(img2,(600,650))

#I want to fix img2 data into img1
r,c,ch = img2.shape
#here first(y,x)
roi = img1[0:r,0:c]
#S1-image in grayscale..then only masking
img_gry = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#S2-mask create
_,mask = cv2.threshold(img_gry,50,255,cv2.THRESH_BINARY)
#S3-inverse mask---remove background
mask_inv = cv2.bitwise_not(mask)
#S4-put mask into roi--put axe on roi
img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
#S5-now bitwise bt mask and img_gry to get only region of storm breaker
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

res = cv2.add(img1_bg,img2_fg)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow(" Step -1 gry==",img_gry)
cv2.imshow("Step -2 Mask===",mask)
cv2.imshow("Step -3 Mask_inv",mask_inv)
cv2.imshow("Step -4 Mask_bg",img1_bg)
cv2.imshow("Step -5 Mask fg",img2_fg)
cv2.imshow("res ",res)

final = img1
final[0:r,0:c] = res

cv2.imshow("Final image",final)

cv2.waitKey(0)
cv2.destroyAllWindows()