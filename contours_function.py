import cv2
import numpy as np

# img = cv2.imread(r"C:\Opencv_output\shapes.png")
# img = cv2.resize(img,(600,700))
# img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# ret,thresh = cv2.threshold(img1,220,255,cv2.THRESH_BINARY_INV)

# #findcontour(img,contour_retrival_mode,method)
# cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# #Here cnts is a list of contours. ANd each contour is an array with x, y cordinate   
# #hier variable called hierarchy and it contain image information.
# print("Number of contour==",cnts,"\n total contour==",len(cnts))
# print("Hierarchy==\n",hier)

# # loop over the contours
# for c in cnts:
#     # compute the center of the contour
#     #an image moment is a certain particular weighted average (moment) of the image pixels
#     M = cv2.moments(c)
#     print("M==",M)
#     cX = int(M["m10"] / M["m00"])
#     cY = int(M["m01"] / M["m00"])
#     # draw the contour and center of the shape on the image
#     cv2.drawContours(img, [c], -1, (0, 255, 0), 2) #-1 means sbke around ban jae contour,2 thickness
#     cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
#     cv2.putText(img, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
# cv2.imshow("original===",img)
# cv2.imshow("gray==",img1)
# cv2.imshow("thresh==",thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



img = cv2.imread(r"C:\Opencv_output\shapes.png")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1,220,255,cv2.THRESH_BINARY_INV)

#findcontour(img,contour_retrival_mode,method)
cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Here cnts is a list of contours. ANd each contour is an array with x, y cordinate   
#hier variable called hierarchy and it contain image information.
# print("Number of contour==",cnts,"\n total contour==",len(cnts))
# print("Hierarchy==\n",hier)

area1 = []

# loop over the contours
for c in cnts:
    # compute the center of the contour
    #an image moment is a certain particular weighted average (moment) of the image pixels
    M = cv2.moments(c)
    # print("M==",M)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    area = cv2.contourArea(c)
    area1.append(area)
    
    if area<10000:
    
        epsilon = 0.1*cv2.arcLength(c,True)
        data = cv2.approxPolyDP(c,epsilon,True)
        hull = cv2.convexHull(data)
        x,y,w,h = cv2.boundingRect(hull)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(125,10,20),5)
    
        print("epsilon===",epsilon)
        print("data===",data)
        print("hull===",hull)
        
        # draw the contour and center of the shape on the image
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2) #-1 means sbke around ban jae contour,2 thickness
    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
    cv2.imshow("original===",img)
    cv2.imshow("gray==",img1)
    cv2.imshow("thresh==",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()