

# VVaannchoooooooooooooooooo!!!1
#COMPLETELY AND PERFECTLY WORKING MODEL FOR ALL THE COMPONENTS OF NFS SIMULATOR!


import serial
import pydirectinput as pdi
import time

ardObj=serial.Serial('COM7', baudrate=9600, timeout=None)
# TotalOperationsLength= 3    #Gear, LCR, Up, down, nitro
key=keyPrev= 1
pdi.PAUSE= 0.02
lastdir="C"
while True:
    got= ardObj.readline().decode('ascii').replace("\n", "").replace("\r", "")
    print(got)
    gearnum= got[1]
    spos= got[2]
    upSt= got[3]
    downSt= got[4]
    nitroSt = got[5]

    ###########--------GearBox Operations-------###########

    if gearnum== "R":
        while c < 10:
            pdi.press("space")
            c += 1
    elif gearnum== "1":
        key = 1
    elif gearnum == "2":
        key = 2
    elif gearnum == "3":
        key = 3
    elif gearnum == "4":
        key = 4
    elif gearnum=="5":
        key = 5
    elif gearnum == "6":
        key = 6
    elif gearnum == "7":
        key = 7
    elif gearnum == "N":
        key = keyPrev = 1

    if keyPrev != key:
        c = 0
        if key > keyPrev:
            for _ in range(key - keyPrev):
                pdi.press("shiftleft")

        elif keyPrev > key:
            for _ in range(keyPrev - key):
                pdi.press("ctrlleft")

    keyPrev = key
    ###########--------/GearBox Operations-------###########

    ###########--------Steering Position-------###########

    if "L" in spos:
        for _ in range(2):
            pdi.keyDown('left', _pause=False)
            time.sleep(0.02)
    elif "R" in spos:
        for _ in range(2):
            pdi.keyDown("right", _pause=False)
            time.sleep(0.02)
    else:
        if lastdir != 'C':      #Ek baar hi release honge
            pdi.keyUp('left')
            pdi.keyUp('right')

    lastdir= spos

    ###########--------/Steering Position-------###########

    ###########--------Valves-------###########
    if upSt== "0":
        for _ in range(2):
            pdi.keyDown('up', _pause=False)
            time.sleep(0.02)
    else:
        pdi.keyUp('up')

    if downSt== "0":
        for _ in range(2):
            pdi.keyDown('down', _pause=False)
            time.sleep(0.02)
    else:
        pdi.keyUp('down')

    if nitroSt== "0":
        for _ in range(2):
            pdi.keyDown('x', _pause=False)
            time.sleep(0.02)
    else:
        pdi.keyUp('x')

    ###########--------/Valves-------###########
