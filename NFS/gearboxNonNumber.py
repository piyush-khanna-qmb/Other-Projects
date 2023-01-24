# Pehla gear by default Neutral ki jagah 1 hoga.
# Efficient gameplay ke liye ye zyada kaargar hai.
# Neutral functionality ka use gaadi thukne pe gear reseting me use ayega

"""Gaadi thukte hi vo by default 1 gear me aa jaati hai. Is waqt GearN daal do, kaam paintis!"""

#---------ACTUAL WORKING MODEL FOR NFS SIMULATION----------
"""---------------------COMPLETED! WORKING SUCCESSFULLY!-----------------------"""


import serial
import sys
sys.path.append("G:/Commands/PythonProject/")
from baap import *
import pydirectinput as pdi

pdi.PAUSE=0.1
ardObj=serial.Serial('COM7', baudrate=9600, timeout=0.2)
keyPrev=key=1
c=0
while True:
    got= ardObj.readline().decode('ascii')
    # print(got)
    if got=="":
        time.sleep(1)
        continue
    
    if "GearR" in got:
        while c<10:
            pdi.press("space")
            c+=1
    if "Gear1" in got:
        key=1
    elif "Gear2" in got:
        key=2
    elif "Gear3" in got:
        key=3
    elif "Gear4" in got:
        key=4
    elif "Gear5" in got:
        key=5
    elif "Gear6" in got:
        key=6
    elif "Gear7" in got:
        key=7
    elif "GearN" in got:
        key=keyPrev= 1

    if keyPrev!=key:
        # print(str(got), end="- ")
        c=0
        if key>keyPrev:
            for _ in range(key-keyPrev):
                # print("Up ", end=" ")
                pdi.press("shiftleft")
                # time.sleep(0.2)
            # print()
        elif keyPrev>key:
            for _ in range(keyPrev- key):
                # print("Down ", end=" ")
                pdi.press("ctrlleft")
                # time.sleep(0.2)
            # print()

    keyPrev=key