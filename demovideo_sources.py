import cv2

# mobile_camera="http://172.20.10.5:8080/video"
# cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cap.open(mobile_camera)

# print("check==",cap.isOpened()) 

# fourcc = cv2.VideoWriter_fourcc(*"XVID")                      
# #It contain 4 parameter,name,codec,fps,resolution
# output = cv2.VideoWriter(r"C:\Users\anshika\Desktop\Robotics Project\open cv\hero.mp4",fourcc,20.0,(640,480))

    
# while cap.isOpened():                                                    
#     ret,frame = cap.read()                     
#     if ret == True:           
#         frame = cv2.resize(frame,(640,480))                        
#         cv2.imshow("frame",frame)
#         output.write(frame)                          
#         if cv2.waitKey(1) & 0xFF == ord("z"):
#             break
        
# cap.release()
# output.release()   
# cv2.destroyAllWindows()

#CAPTURE VIDEO FROM YOUTUBE
import pafy

url_external_video="https://youtu.be/pDc9civaqHE?si=PpN3nvbzrsC821l4"
data = pafy.new(url_external_video)
data = data.getbest(preftype = "mp4")
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url_external_video)
print("check==",cap.isOpened()) 

# fourcc = cv2.VideoWriter_fourcc(*"XVID")                      
# #It contain 4 parameter,name,codec,fps,resolution
# output = cv2.VideoWriter(r"C:\Users\anshika\Desktop\Robotics Project\open cv\hero.mp4",fourcc,20.0,(640,480))

while(cap.isOpened()):                                                   
    ret,frame = cap.read()                     
    if ret == True:           
        frame = cv2.resize(frame,(640,480)) 
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)                   
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        # output.write(frame)                          
    if cv2.waitKey(1) & 0xFF == ord("z"):
        break
        
cap.release()
# output.release()   
cv2.destroyAllWindows()