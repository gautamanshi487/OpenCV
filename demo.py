import cv2
import numpy as np

# img1=cv2.imread(r"C:\Users\anshika\Pictures\EE Department Farewell- 14-04-2024 (18).JPG",1)
# img1=cv2.resize(img1,(1100,700))
# print(img1)
# cv2.imshow("original",img1)
# cv2.waitKey()
# cv2.destroyAllWindows()

# img2=cv2.imread(r"C:\Users\anshika\Pictures\EE Department Farewell- 14-04-2024 (18).JPG",0)
# img2=cv2.resize(img2,(1100,700))
# print(img2)
# cv2.imshow("gray scale",img2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# img3=cv2.imread(r"C:\Users\anshika\Pictures\EE Department Farewell- 14-04-2024 (18).JPG",-1)
# img3=cv2.resize(img3,(1100,700))
# print(img3)
# cv2.imshow("unchanged",img3)
# cv2.waitKey()
# cv2.destroyAllWindows()

# Image conversion project coloured image into grayscale.
# path = input(r"Enter the path and name of image=")
# print("You enter this=",path)

# Now read image
img1=cv2.imread(r"C:\Users\anshika\Pictures\EE Department Farewell- 14-04-2024 (18).JPG",0) 
img1=cv2.resize(img1,(1100,700))    
# img1=cv2.flip(img1,0)
cv2.imshow("converted image",img1)

k = cv2.waitKey(0)
if k==ord("z"):
    cv2.imwrite(r"C:\Users\anshika\Desktop\Robotics Project\open cv\output.png",img1)
    # print("saved.")
else:
    cv2.destroyAllWindows()