import cv2
import numpy as np
import winsound
import threading 

kernel=np.ones((5,5),np.uint8)
cap=cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2()

def playSound():
    winsound.Beep(1000,2000)
    print("beeping")
while True:

    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)  #creates binary image of moving objects
    fgmask=cv2.erode(fgmask,kernel,iterations=1)  #erosion to remove noise
    counter=np.sum(fgmask==255)  #counts number of white pixels

    cv2.imshow('img',fgmask)
    cv2.imshow('frame',frame)

    if counter>50:  #sounds an alarm if the number of white pixels is greater than a certain limit
        # Run the playSound function on a separate thread as it is a blocking operation
        t = threading.Thread(target=playSound)
        t.start()
        

    if (cv2.waitKey(1) & 0xFF)==ord('q'):
        break

cap.release()
