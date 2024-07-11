import cv2
import numpy as np

#read two different images of same channel
img1 = cv2.imread(r"C:\Opencv_output\roi_opr.jpg")
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread(r"C:\Opencv_output\bro_thor.jpg")
img2 = cv2.resize(img2,(500,700))

cv2.imshow("thor==",img1)
cv2.imshow("bro_thor==",img2)

#make trackbar using a function
def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)
cv2.namedWindow('win') #create track bar windows

cv2.createTrackbar('image_weight','win',1,100,blend)

switch = '0 : OFF \n 1 : ON'  #create switch for invoke the trackbars
cv2.createTrackbar(switch,'win',0,1,blend)  #create track bar for switch

while(1):
    i = cv2.getTrackbarPos('image_weight','win')
    s = cv2.getTrackbarPos(switch,'win')
    n = float(i/100)
    
    if s == 0:
        thor = img[:]
    else:
        thor = cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(thor, str(i), (20, 50), cv2.FONT_ITALIC,
                   2, (0, 125, 255), 2)
    cv2.imshow('thor',thor)

    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv2.waitKey(0)    
cv2.destroyAllWindows()















