import cv2
## This below code is used for capture a video and show it.

# cap=cv2.VideoCapture(r"C:\Users\anshika\Pictures\Camera Roll\WIN_20240506_13_45_58_Pro.mp4")
# print("cap",cap)

# while True:
#     ret,frame = cap.read() 
#     frame = cv2.resize(frame,(700,450))
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("frame",frame)
#     cv2.imshow("gray",gray)
      
#     k=cv2.waitKey(25)
#     if k==ord("z") & 0xFF:
#         break
    
# cap.release()
# cv2.destroyAllWindows()



#**Now capture the video from webcam and save into memory**

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# DIVX,XVID,MJPG,X264,WMV1,WMV2

fourcc = cv2.VideoWriter_fourcc(*"XVID")                       #format is XVID (suggested format)
#It contain 4 parameter,name,codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

#this is for capture frames from webcam and then stored frames in frame and read
# it if boolean value of ret is true means frames are captured by webcam then
# show frames and if pressed z then stopped showing frames captured by webcam.

print(cap)     
while cap.isOpened():                                                    
    ret,frame = cap.read()                     
    if ret == True:                                                 
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame= cv2.flip(frame,-1)                            #to flip the video 
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        output.write(frame)                              #depends on you what frames do you write in output and those 
                                                        #are passes to output videowrite line31 and for grayscale you have to specify there a 0 also.)
        if cv2.waitKey(1) & 0xFF == ord("z"):
            break
        
cap.release()
output.release()    #used so that video saved and not get corrupted
cv2.destroyAllWindows()

#End