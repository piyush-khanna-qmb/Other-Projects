
"""Going on right track
Ek ek karke stream aa rha hai data ka. Values bhi discrete dikh rhi hain arduino se aati hui.
FUNCTIONS TO MAKE:
1. highMag(got): takes string 'got' and returns the highest magnitude digit in complete string
-> Will be called from inside if got: 

2. mostRecentCommand(got): ek given steering ke chakkar me sabse end me konsi command hui, vo dega
-> ex- returns 0,1,2 for left or center or right

3. MapSpeed(mag): returns time.sleep ki value for particular magnitude

EXECUTION:
Got ke andar check kar lenge, 
if MRC== centre
    pass
elif MRC== right:
    keyDown(right)
else:
    keyDown(left)
time.sleep(MagSpeed(highMag(got)))

"""



from cv2 import waitKey
import serial
import sys
sys.path.append("G:/Commands/PythonProject/")
from baap import *
import pydirectinput as pdi
import re

def mostrecentMagnitude(got):
    digits= re.findall(r"\d+", got)
    print(digits[-1])

def mostRecentCommand(got):
    pos= ["left" , "centre", "right"]
    Occ=[]
    for i in pos:
        p=got.rfind(i)
        Occ.append(p)
    j = [i for i in range(len(Occ)) if Occ[i]==max(Occ)][0]
    return j

def mapSpeed(mag):
    pass

ardObj=serial.Serial('COM7', baudrate=9600, timeout=0.01)
key=""
MRC=1
ttt=0.22

while True:
    got= ardObj.readline().decode('ascii')
    if got:
        MRC=mostRecentCommand(got)
        print(MRC)
    if MRC== 1:
        pdi.keyUp("right")
        pdi.keyUp("left")
    elif MRC== 2:
        pdi.keyDown("right")
        time.sleep(ttt)
    elif MRC== 0:
        pdi.keyDown("left")
        time.sleep(ttt)    # time.sleep(mapSpeed(highMag(got)))
    if waitKey(1) & 0xff ==ord('t'):
        ttt=0.2
