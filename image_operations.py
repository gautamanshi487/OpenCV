import cv2
import numpy as np

# img = cv2.imread(r"C:\mine Photos\InterIIT 2023\IMG_20231215_184304.jpg")
# img = cv2.resize(img,(500,400))

# print("shape==",img.shape)
# print("no. of pixels==",img.size)
# print("datatype==",img.dtype)
# print("Imagetype==",type(img))
# # print(cv2.split(img)) 
# b,g,r = cv2.split(img)

# # cv2.imshow("blue",b)
# # cv2.imshow("green",g)
# # cv2.imshow("red",r)
# # cv2.imshow("cat",img)

# mr1 = cv2.merge((r,g,b))
# cv2.imshow("rgb",mr1)

# mr2 = cv2.merge((g,b,r))
# cv2.imshow("gbr",mr2)


# cv2.waitKey(0)
# cv2.destroyAllWindows                      

##NOW WORK ON PIXEL VALUE-

img = cv2.imread(r"C:\mine Photos\InterIIT 2023\IMG_20231215_184304.jpg")
img = cv2.resize(img,(500,400))
cv2.imshow("cat==",img)

#access a particular pixel value(means its color value)
px = img[250,300]
print("The pixel value of that coordinate==",px)

blue = img[250,300,0]
print("the pixel having blue color==",blue)
green = img[250,300,1]
print("the pixel having green color==",green)
red = img[250,300,2]
print("the pixel having red color==",red)


cv2.waitKey()