import cv2
import numpy as np

frame = cv2.imread(r"C:\Opencv_output\color_balls.jpg")
while True:
    #HUE SATURATION VALUE             
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_v = np.array([110,50,50])
    u_v = np.array([130,235,225])
    #create mask
    mask = cv2.inRange(hsv, l_v, u_v)
    
    #filter mask with image
    
    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

# frame = cv2.imread(r"C:\Opencv_output\color_balls.jpg")

# cap = cv2.VideoCapture(0)
# def nothing(x):
#     pass

# cv2.namedWindow("Color Adjustments")
# cv2.createTrackbar("Lower_H", "Color Adjustments", 0, 255, nothing)
# cv2.createTrackbar("Lower_S", "Color Adjustments", 0, 255, nothing)
# cv2.createTrackbar("Lower_V", "Color Adjustments", 0, 255, nothing)

# cv2.createTrackbar("Upper_H", "Color Adjustments", 255, 255, nothing)
# cv2.createTrackbar("Upper_S", "Color Adjustments", 255, 255, nothing)
# cv2.createTrackbar("Upper_V", "Color Adjustments", 255, 255, nothing)

# while True:
#     _,frame = cap.read()
#     frame = cv2.resize(frame,(400,400))

#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     l_h = cv2.getTrackbarPos("Lower_H", "Color Adjustments")
#     l_s = cv2.getTrackbarPos("Lower_S", "Color Adjustments")
#     l_v = cv2.getTrackbarPos("Lower_V", "Color Adjustments")

#     u_h = cv2.getTrackbarPos("Upper_H", "Color Adjustments")
#     u_s = cv2.getTrackbarPos("Upper_S", "Color Adjustments")
#     u_v = cv2.getTrackbarPos("Upper_V", "Color Adjustments")

#     lower_bound = np.array([l_h,l_s,l_v])
#     upper_bound = np.array([u_h,u_s,u_v])
     
#     mask = cv2.inRange(hsv,lower_bound,upper_bound)

#     result = cv2.bitwise_and(frame,frame,mask=mask)

#     cv2.imshow("Original Frame", frame)
#     cv2.imshow("Masking", mask)
#     cv2.imshow("Result", result)

#     key = cv2.waitKey(25) &0xFF
#     if key == 27:
#         break
    
# cap.release()
# cv2.destroyAllWindows()
