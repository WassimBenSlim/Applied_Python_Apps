import cv2
import numpy as np

#read video file
new_capture = cv2.VideoCapture('PythonApps\Video.mp4')

#check if file is opened successfully
if(new_capture.isOpened()==False):
    print("Error for opening the video file")

#reading the video to comeplete
while(new_capture.isOpened()):
    ret, frame = new_capture.read()
    if ret == True :
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) and cv2.getWindowProperty('Frame', cv2.WND_PROP_VISIBLE) <1:
            break
    else:
        break

#release when eveything is completed
new_capture.release()
cv2.destroyAllWindows() #close all frames