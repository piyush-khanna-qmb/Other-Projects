import pyautogui as pag
import time

print("Waiiting 5 secs")
time.sleep(5)
for i in range(100):
    pag.typewrite("Bundelkhandi aur Paancha party dedo kanjaro!!")
    pag.press('enter')
