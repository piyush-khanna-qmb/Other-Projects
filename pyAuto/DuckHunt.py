import os
import cv2
import pyautogui as pag
import time
import pyttsx3
import speech_recognition as sr

engine= pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("Jarvis", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


time.sleep(2)
pag.PAUSE=0
temp= cv2.imread("pyAuto/temp.png")
temp_gray= cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)
temp_h, temp_w =temp_gray.shape

speak("Ready to shoot!")

x, y, w, h= 0, 0, 1366, 768

while True:
    pag.screenshot("pyAuto/temps/image.png", (x,y,w,h))
    ss= cv2.imread("pyAuto/temps/image.png")
    ss_gray= cv2.cvtColor(ss, cv2.COLOR_RGB2GRAY)

    while True:
        #cv2.imshow("hello", ss_gray)
        result= cv2.matchTemplate(ss_gray, temp_gray, cv2.TM_CCOEFF_NORMED)
        mV, MV, mL, ML= cv2.minMaxLoc(result)

        if MV>=0.6:
            speak("Yes")
            print(ML)
            pag.moveTo(ML[0], ML[1])
            pag.doubleClick()
            ss_gray= cv2.rectangle(ss_gray, (ML[0], ML[1]), (ML[0]+ temp_w, ML[1]+temp_h), (0,0,255),-1)
            cv2.imshow("track", ss_gray)
        else:
            speak("No")
            break
    os.remove("pyAuto/temps/image.png")