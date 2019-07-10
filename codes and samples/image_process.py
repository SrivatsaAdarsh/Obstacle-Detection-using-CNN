import time
import cv2
import sys
import os,os.path


path = sys.argv[1]
data_path=sys.argv[2]

fpsLimit = 0.8 
index = 0 	
currentFrame=0
intframe =0

startTime = time.time()
# Playing video from file:
cap = cv2.VideoCapture(str(path))

try:
    if not os.path.exists('data_path'):
        os.makedirs('data_path')
except OSError:
    print ('Error: Creating directory of data')

while(True):
    ret = cap.set(1,index)	
    ret1,frame = cap.read()
    if ret == False or ret1 == False:
           break
    nowTime = time.time()
    if (int(nowTime - startTime)) > fpsLimit:
        temp = cv2.resize(frame,(400,400))
        for intframe in range(4):
             if intframe == 0:
                 t = temp[0:200,0:200]
             if intframe == 1:
                 t = temp[200:400,0:200]
             if intframe ==2:
                 t = temp[0:200,200:400]
             if intframe == 3:
                 t = temp[200:400,200:400]
                 
             # Saves image of the current frame in jpg file
             cv2.waitKey(2)
             name = str(data_path) + str(currentFrame) + '.jpg'
             print ('Creating...image' + str(currentFrame) )
             cv2.imwrite(name, t)
             currentFrame += 1
        intframe=0
        index+=100
        startTime = time.time() # reset time

cap.release()
cv2.destroyAllWindows()
