import cv2
# import numpy as np

# # img = cv2.imread(r"C:\Users\anshika\Pictures\EE Department Farewell- 14-04-2024 (18).JPG")
# # img = np.zeros([512,512,3], np.uint8)*255
# img = np.ones([512,512,3], np.uint8)*255

# img = cv2.resize(img,(800,600))
# img = cv2.line(img,(0,0),(100,200),(15,230,240),5)
# img = cv2.arrowedLine(img,(100,200),(300,400),(240,230,15),5)
# img = cv2.rectangle(img,(50,100),(150,200),(20,230,15),-1)
# img = cv2.circle(img,(25,50),30,(150,100,180),6)
# font = cv2.FONT_ITALIC
# img = cv2.putText(img,"Batti_peeps",(20,500),font,2,(99, 209, 219),10,cv2.LINE_AA)
# img = cv2.ellipse(img,(200,300),(100,50),0,100,360,200,5)

# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows


#DRAW DATE AND TIME ON VIDEO#
import datetime #it is a type of module



cap = cv2.VideoCapture(r"C:\mine Videos\VID_20230525_224615.mp4")
# cap = cv2.VideoCapture(0)
print("width==",cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
print("height==",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("width==",cap.get(3))
print("height==",cap.get(4))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700,700))
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Height: " + str(cap.get(4))+ " Width: " + str(cap.get(3))
        frame = cv2.putText(frame,text,(100,100),font,1,(255,255,255),2,cv2.LINE_AA)
        
        date_data = "Date: " +str(datetime.datetime.now())
        frame = cv2.putText(frame,date_data,(50,50),font,1,(0,0,0),2,cv2.LINE_AA)
        frame = cv2.rectangle(frame,(50,100),(150,200),(20,230,15),-1)
        
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(25) & 0xFF == ord("z"):
            break
    else:
        break                    
        
cap.release()
cv2.destroyAllWindows()
            