import cv2
import numpy as np
import pymouse

cap=cv2.VideoCapture(0)#video capture from internal/external cam

kernel=np.ones((5,5),np.uint8)#kernel for erosion

'''
#FOR EXTERNAL CAM
lower_red1 = np.array([0,160,0])#hsv values for red mask
upper_red1 = np.array([10,250,255])
#hsv values will be different for different cameras objects and lighting
lower_red2 = np.array([170,160,0])
upper_red2 = np.array([180,250,255])
'''

#FOR INTERNAL CAM
#these values are found after intensive experimentation 
lower_red1 = np.array([1,0,0])#hsv values for red mask
upper_red1 = np.array([3,255,255])
#hsv values will be different for different cameras objects and lighting
lower_red2 = np.array([170,0,0])
upper_red2 = np.array([180,255,255])
#internal cam is a bit jittery FIX IT




def find_ball(img_hsv):
    

    mask0 = cv2.inRange(img_hsv, lower_red1, upper_red1)


   # mask1 = cv2.inRange(img_hsv, lower_red2, upper_red2)
    mask = mask0#binary image of red objects

    cv2.imshow('redmaskbef',mask)

    mask=cv2.erode(mask,kernel,iterations=2)#erosion to remove noise
    #reduce dilations if not found necessary
    mask=cv2.dilate(mask,kernel,iterations=2)
    
    im2,contours,hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#magic that finds contours
    cv2.imshow('redmask',mask)

    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(frame, contours, -1, 255, 3)

        #find the biggest area
        c = max(contours, key = cv2.contourArea)

        M = cv2.moments(c)
        #finds centre
        object_x = int(M["m10"] / M["m00"])
        object_y = int(M["m01"] / M["m00"])

        
        #640x480 ext cam
        screensize_x=pymouse.PyMouse().screen_size()[0]
        screensize_y=pymouse.PyMouse().screen_size()[1]

        height,width = mask.shape
        #0.8,0.2 were chosen by experimentation
        thresh_max_x=int(0.8*width)
        thresh_max_y=int(0.8*height)
        thresh_min_x=int(0.2*width)
        thresh_min_y=int(0.2*height)
        
        if object_x>thresh_max_x:
            mouse_x=0#thresholding so you dont have to cram the object against the edge to move the mouse to corners
        elif object_x<thresh_min_x:
            mouse_x=screensize_x
        else:
            mouse_x=int(np.interp(object_x,[thresh_min_x,thresh_max_x],[screensize_x,0]))#mapping of image coordinates to screen coordinates
        if object_y>thresh_max_y:
            mouse_y=screensize_y
        elif object_y<thresh_min_y:
            mouse_y=0
        else:
            
            mouse_y=int(np.interp(object_y,[thresh_min_y,thresh_max_y],[0,screensize_y]))
        
        pymouse.PyMouse().move(mouse_x,mouse_y)



lower_green=np.array([41,0,0])
upper_green=np.array([80,255,255])

def find_click(img_hsv):
    green_mask=cv2.inRange(img_hsv, lower_green, upper_green)
    cv2.imshow('greenmaskbef',green_mask)

    green_mask=cv2.erode(green_mask,kernel,iterations=2)#erosion to remove noise
    #reduce dilations if not found necessary
    green_mask=cv2.dilate(green_mask,kernel,iterations=2)    
    im2,contours,hierarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#magic that finds contours
    cv2.imshow('greenmask',green_mask)


while True:

    _,frame=cap.read()

    img_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    find_ball(img_hsv)
    cv2.imshow('original',frame)
    find_click(img_hsv)
    
    k=cv2.waitKey(1) & 0xff
    if k==27 or k==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()#doesnt fking work
