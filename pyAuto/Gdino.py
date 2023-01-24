
"""-------------------------COMPLETED-------------------------"""


import pyautogui as pag
from dragSpiral import *
import cv2

temp=cv2.imread("pyAuto/dino/dino.png")
tH, tW, rgb= temp.shape       
x,y,w,h= 150, 80, 840, 545

pag.PAUSE=0
time.sleep(4)

while True:
    pag.screenshot("pyAuto/dino/image.png")
    image= cv2.imread("pyAuto/dino/image.png")
    result= cv2.matchTemplate(image, temp, cv2.TM_CCOEFF_NORMED)
    mV, MV, ml, ML= cv2.minMaxLoc(result)
    if MV<0.95:
        pag.press('space')