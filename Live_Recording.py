import pyautogui as p
import cv2 as c
import numpy as np

#Create resolution
rs = p.size()

#filename in which we store recording
fn = input("Please Enter any file name and Path: ")
#Fix the frame rate
fps = 20.0
fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)

#create recording module
c.namedWindow("LIve_Recording",c.WINDOW_NORMAL)

#Resize the window
resizeWindow = ("Live",(600,400))

while True:
    img = p.screenshot() #image
    f = np.array(img) #convert image into array
    f = c.cvtColor(f,c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("screenshot", f)
    if c.waitKey(1) == ord("E"):
        break

c.destroyAllWindows()