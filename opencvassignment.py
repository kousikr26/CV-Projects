import cv2
import numpy as np
import os
path="C:/Users/Kousik Rajesh/Documents/Python projects/opencv"
kernel=np.ones((5,5),np.uint8)
image=cv2.imread("45.png")
hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_red = np.array([170,0,0])
upper_red = np.array([179,255,255])
redmask = cv2.inRange(hsvimage, lower_red, upper_red)
redmask=cv2.erode(redmask,kernel,iterations=1)
redimage=cv2.bitwise_and(image,image,mask=redmask)
image2,cnts,hierarchy = cv2.findContours(redmask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    if len(approx)==3:
            text="triangle"
    elif len(approx)==4:
            text="quadrilateral"
    elif len(approx)==5:
            text="pentagon"
    else:
            text="circle"
    cv2.drawContours(redimage, [c], -1, (0, 255, 0), 2)
    cv2.putText(redimage, text, (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.imwrite(os.path.join(path , 'red.jpg'), redimage)
cv2.imshow("red",redimage)
k=cv2.waitKey(0)

image=cv2.imread("45.png")
lower_green = np.array([76,0,0])
upper_green = np.array([86,255,255])
greenmask = cv2.inRange(hsvimage, lower_green, upper_green)
greenmask=cv2.erode(greenmask,kernel,iterations=1)
greenimage=cv2.bitwise_and(image,image,mask=greenmask)
image,cnts,hierarchy = cv2.findContours(greenmask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    if len(approx)==3:
            text="triangle"
    elif len(approx)==4:
            text="quadrilateral"
    elif len(approx)==5:
            text="pentagon"
    else:
            text="circle"
    cv2.drawContours(greenimage, [c], -1, (0, 255, 0), 2)
    cv2.putText(greenimage, text, (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.imwrite(os.path.join(path , 'green.jpg'), greenimage)
cv2.imshow("green",greenimage)
k=cv2.waitKey(0)

image=cv2.imread("45.png")
lower_blue = np.array([99,0,0])
upper_blue = np.array([115,255,255])
bluemask = cv2.inRange(hsvimage, lower_blue, upper_blue)
bluemask=cv2.erode(bluemask,kernel,iterations=1)
blueimage=cv2.bitwise_and(image,image,mask=bluemask)
image2,cnts,hierarchy = cv2.findContours(bluemask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    if len(approx)==3:
            text="triangle"
    elif len(approx)==4:
            text="quadrilateral"
    elif len(approx)==5:
            text="pentagon"
    else:
            text="circle"
    cv2.drawContours(blueimage, [c], -1, (0, 255, 0), 2)
    cv2.putText(blueimage, text, (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.imwrite(os.path.join(path , 'blue.jpg'), blueimage)
cv2.imshow("blue",blueimage)
k=cv2.waitKey(0)

image=cv2.imread("45.png")
lower_yellow = np.array([23,60,0])
upper_yellow = np.array([31,255,255])
yellowmask = cv2.inRange(hsvimage, lower_yellow, upper_yellow)
yellowmask=cv2.erode(yellowmask,kernel,iterations=1)
yellowimage=cv2.bitwise_and(image,image,mask=yellowmask)
image2,cnts,hierarchy = cv2.findContours(yellowmask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    if len(approx)==3:
            text="triangle"
    elif len(approx)==4:
            text="quadrilateral"
    elif len(approx)==5:
            text="pentagon"
    else:
            text="circle"
    cv2.drawContours(yellowimage, [c], -1, (0, 255, 0), 2)
    cv2.putText(yellowimage, text, (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.imwrite(os.path.join(path , 'yellow.jpg'), yellowimage)
cv2.imshow("yellow",yellowimage)
k=cv2.waitKey(0)


image=cv2.imread("45.png")
lower_orange = np.array([10,96,0])
upper_orange = np.array([15,255,255])
orangemask = cv2.inRange(hsvimage, lower_orange, upper_orange)
orangemask=cv2.erode(orangemask,kernel,iterations=1)
orangeimage=cv2.bitwise_and(image,image,mask=orangemask)
image2,cnts,hierarchy = cv2.findContours(orangemask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    if len(approx)==3:
            text="triangle"
    elif len(approx)==4:
            text="quadrilateral"
    elif len(approx)==5:
            text="pentagon"
    else:
            text="circle"
    cv2.drawContours(orangeimage, [c], -1, (0, 255, 0), 2)
    cv2.putText(orangeimage, text, (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.imwrite(os.path.join(path , 'orange.jpg'), orangeimage)
cv2.imshow("orange",orangeimage)
k=cv2.waitKey(0)
