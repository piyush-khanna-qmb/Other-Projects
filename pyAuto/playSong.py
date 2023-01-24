import cv2
import pyautogui as pag
import dragSpiral as dg
from dragSpiral import *

pag.PAUSE= 0
temp= cv2.imread("pyAuto/duckhunt/face.png")
temp_gray= cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)
tH, tW= temp_gray.shape
tmx= tW//2
tmy= tH//2
# print(tH, tW)
#Main window dimensions->
x, y, w, h= 180, 0, 1000, 600
# countDown(0, 0.4)
speak("Starting")
while True:
    pag.screenshot("pyAuto/temps/image.png", (x, y, w, h))
    im= cv2.imread("pyAuto/temps/image.png")
    im_gray= cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    result= cv2.matchTemplate(im_gray, temp_gray, cv2.TM_CCOEFF_NORMED)
    mV, MV, mL, ML= cv2.minMaxLoc(result)
    if MV>=0.54:
        pag.click(x= ML[0]+x+ tmx, y= ML[1]+ y+ tmy)
        im= cv2.rectangle(im, ML, (ML[0]+tW, ML[1]+tH), (0,0,255), -1)
# cv2.waitKey(0)

# cv2.imshow("Hi", temp)


