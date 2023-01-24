"""Working almost fine.
Major problem- key simulations continous hone ki jagah discrete ho rhe hain.
Press and hold key simulation hone ki jagah clearly dikh rha hai ki keys bhaari interval ke baad dabaai ja rhi hain  :( """

import serial
import pydirectinput as pdi
pdi.PAUSE =0
import time

# pdi.PAUSE = 0.02
ardObj = serial.Serial('COM7', baudrate=9600, timeout=None)
# while True:
#     got=ardObj.readline().decode().replace("\n", "").replace("\r", "")
#     print(got)
#     if "L" in got:
#         pdi.keyDown('left')
#     elif "R" in got:
#         pdi.keyDown('right')
#     else:
#         pdi.keyUp('left')
#         pdi.keyUp('right')



key = ""
while True:
    got = ardObj.readline().decode('ascii').replace("\n", "")
    if got:
        print(got)
        if "R" in got:
            key = "right"
        elif "L" in got:
            key = "left"
        elif "C" in got:
            pdi.keyUp('right')
            pdi.keyUp('left')

# for i in range(50):
#     pdi.keyDown('right')
# for i in range(50):
#     pdi.keyDown('left')
