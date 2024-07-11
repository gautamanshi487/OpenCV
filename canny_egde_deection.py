import cv2
import numpy as np

img = cv2.imread(r"C:\Opencv_output\building.jpg")
# img = cv2.imread(r"C:\Opencv_output\strom_breaker.JPG")
img = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("img",img)

def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold", "Canny", 0, 255, nothing)

while True:
    a= cv2.getTrackbarPos('Threshold','Canny')
    
    print(a)
    result = cv2.Canny(img_gray,a,255)
    cv2.imshow("Canny",result)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
