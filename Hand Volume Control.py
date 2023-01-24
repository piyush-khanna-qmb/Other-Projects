import cv2
import HandTrackingModule as htm
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange= volume.GetVolumeRange()
minVol=volRange[0]
maxVol=volRange[1]

cam=cv2.VideoCapture(0)
width, height= 1020, 720
detector= htm.handDetector(maxHands=4, detectionCon=0.7)
cam.set(3, width)
cam.set(4, height)

while True:
    ignore, frame=cam.read()
    frame= detector.findHands(frame)
    pList= detector.findPosition(frame, draw=False)
    if len(pList)!=0:
        x1,y1= pList[4][1], pList[4][2]
        x2,y2= pList[8][1], pList[8][2]
        cx,cy = (x1+x2)//2, (y1+y2)//2
        cv2.circle(frame, (x1,y1), 10, (125,0,0), -1)
        cv2.circle(frame, (x2,y2), 10, (125,0,0), -1)
        cv2.line(frame, (x1,y1), (x2,y2), (125,0,0), 2)
        dist=int(math.hypot(x2-x1, y2-y1))
        vol= np.interp(dist, (15,170), (minVol, maxVol))
        volume.SetMasterVolumeLevel(vol, None)

        if dist<15:
            cv2.circle(frame, (cx,cy), 10, (0,255,0), -1)
        elif dist>170:
            cv2.circle(frame, (cx,cy), 10, (0,0,255), -1)
        else:
            cv2.circle(frame, (cx,cy), 10, (125,0,0), -1)
        
    cv2.imshow("Volume Controller", frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cam.release()