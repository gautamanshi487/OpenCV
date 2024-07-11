import cv2
import numpy as np

## Mouse callback function

# def draw(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x,y),100,(125,0,255),5)     
#     if event == cv2.EVENT_RBUTTONDBLCLK:    
#         cv2.rectangle(img,(x,y),(x+100,y+75),(125,125,255),2)
# cv2.namedWindow(winname = "res")    
# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv2.setMouseCallback("res",draw)

# while True:
#     cv2.imshow("res",img)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cv2.destroyAllWindows()

#Create a function which help to find cordinate of any pixel

def mouse_event(event,x,y,flag,param):
    print("event==",event)
    print("x==",x)
    print("y==",y)
    print("flag==",flag)
    print("param==",param)
    font = cv2.FONT_HERSHEY_COMPLEX
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,", ",y)
        coordinate = " " +str(x)+ " , " +str(y)
        cv2.putText(img,coordinate,(x,y),font,1,(0,120,0),2)
        # cv2.imshow("image",img)

    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        color_bgr = " "+str(b)+ ", "+str(g)+ ", "+str(r)
        cv2.putText(img,color_bgr,(x,y),font,1,(100,120,200),2)
        # cv2.imshow("image",img)
        

# img = np.zeros((512,512,3),np.uint8)
img = cv2.imread(r"C:\mine Photos\InterIIT 2023\IMG_20231206_155508.jpg")
img = cv2.resize(img,(400,600))
cv2.namedWindow(winname = "Image")
cv2.setMouseCallback("Image",mouse_event)
    
while True:
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == 27:  # 27 means esc press krke window close kr skte ab
        break
            
cv2.destroyAllWindows()    
    
        
        
        

