import cv2 as c
# import pyautogui as p
# import numpy as np

# resolution = p.size()

# fn_input = input("Enter any file name and path")
# fps=25.0

# fourcc = c.VideoWriter_fourcc(*"XVID")
# output = c.VideoWriter(fn_input,fourcc,fps,resolution)

# c.namedWindow("Live Recording",c.WINDOW_NORMAL)
# c.resizeWindow("Live Recording",(600,400))
# while True:
#     img = p.screenshot()
#     screenshot_capture = np.array(img)
#     screenshot_capture = c.cvtColor(screenshot_capture,c.COLOR_BGR2RGB)
    
#     output.write(screenshot_capture)
#     c.imshow("Live Recording",screenshot_capture)
#     if c.waitKey(1) & 0xFF == ord("z"):
#         break

# output.release()
# c.destroyAllWindows()

vidcap = c.VideoCapture(r"C:\Users\anshika\Desktop\Robotics Project\test2.mp4")
ret,image = vidcap.read()

count = 0
while True:
    if ret == True:
        c.imwrite(r"C:\Users\anshika\Desktop\Robotics Project\open cv\frames\imgN%d.jpg"%count,image)
        vidcap.set(c.CAP_PROP_POS_MSEC,(count**100))  #speed of capturing video
        ret,image = vidcap.read()           #dubara capture kr rhe h loop k andar qki vo agli image capture hoti rhe lopp infitine tk chlega jb tk video end hogi ya z press krne tk chlega
        image = c.resize(image,(600,400))
        c.imshow("res",image)
        print(count)
        count += 1
        if c.waitKey(1) & 0xFF == ord("z"):
            break
            c.destroyAllWindows()

vidcap.release()
c.destroyAllWindows()
        
