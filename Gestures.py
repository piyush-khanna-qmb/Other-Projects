"""GESTURES CLASS"""
import serial
import time
import pyttsx3
import datetime

lefth= serial.Serial('COM16', baudrate= 9600, timeout=1)
righth= serial.Serial('COM17', baudrate= 9600, timeout=1)
engine= pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("Jarvis", voices[0].id)

def setVals(ardObj, a1,a2,a3,a4,a5,a6,stime):
    command= f"#1{chr(a1)}Z#2{chr(a2)}Z#3{chr(a3)}Z#4{chr(a4)}Z#5{chr(a5)}Z#6{chr(a6)}Z****"
    ardObj.write(command.encode())
    time.sleep(stime)

def Hi():
    setVals(lefth, 90, 90, 90, 90, 90, 90, 0.5)
    setVals(righth, 90, 90, 90, 90, 90, 90, 0.5)
    setVals(lefth, 160, 100, 120, 90, 90, 90, 0.2)
    setVals(righth, 40, 72, 67, 90, 90, 90, 0.2)
    setVals(lefth, 160, 100, 120, 90, 90, 125, 0.2)
    setVals(righth, 40, 72, 67, 90, 90, 125, 0.2)
    setVals(lefth, 160, 100, 120, 90, 90, 90, 0.2)
    setVals(righth, 40, 72, 67, 90, 90, 90, 0.2)
    setVals(lefth, 160, 100, 120, 90, 90, 125, 0.2)
    setVals(righth, 40, 72, 67, 90, 90, 125, 0.2)
    setVals(lefth, 160, 100, 120, 90, 90, 90, 0.2)
    setVals(righth, 40, 72, 67, 90, 90, 90, 0.2)
    setVals(lefth, 160, 100, 120, 90, 90, 125, 0.2)
    setVals(righth, 40, 72, 67, 90, 90, 125, 0.2)
    setVals(lefth, 160, 100, 120, 90, 90, 90, 0.2)
    setVals(righth, 40, 72, 67, 90, 90, 90, 0.2)
    setVals(lefth, 90, 90, 90, 90, 90, 90, 0.5)
    setVals(righth, 90, 90, 90, 90, 90, 90, 0.5)

def homePos(ard):
    give= f"#1ZZ#2ZZ#3ZZ#4ZZ#5ZZ#6ZZ****"
    ard.write(give.encode())

def churm(n=2):
    for i in range(n):
        giveR= f"#1ZZ#2ZZ#3ZZ#4ZZ#5ZZ#6{chr(130)}Z****"
        giveL = f"#1ZZ#2ZZ#3ZZ#4ZZ#5ZZ#6{chr(110)}Z****"
        lefth.write(giveL.encode())
        righth.write(giveR.encode())
        time.sleep(0.25)
        give= f"#1ZZ#2ZZ#3ZZ#4ZZ#5ZZ#6ZZ****"
        lefth.write(give.encode())
        righth.write(give.encode())   
        time.sleep(0.25)


def Wave():
    setVals(lefth, 90, 90, 90, 90, 90, 90, 0.4)
    setVals(lefth, 70, 50, 60, 70, 90, 90, 0.4)
    setVals(lefth, 70, 70, 40, 120, 90, 90, 0.4)
    setVals(righth, 120, 110, 130, 60, 90, 90, 0.4)
    setVals(lefth, 90, 90, 90, 90, 90, 90, 0.4)
    setVals(righth, 120, 120, 110, 110, 90, 90, 0.4)
    setVals(righth, 90, 90, 90, 90, 90, 90, 0.4)
def Hello():
    speak("Hello Baby")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    prahar= datetime.datetime.now().hour
    if 6<prahar<12:
        speak("A very Good morning gentlemen?")
    elif 12<prahar<15:
        speak("A very Good afternoon gentlemen?")
    else:
        speak("A very Good evening gentlemen?")
    speak("Nice to meet you")

def scan():
    homePos(lefth)
    homePos(righth)
    setVals(lefth, 180, 110, 100, 90, 90, 90, 1)
    setVals(righth, 90, 70, 70, 90, 90, 90, 1)
    setVals(lefth, 90, 110, 100, 90, 90, 90, 1)
    setVals(righth, 0, 70, 70, 90, 90, 90, 1)
    homePos(lefth)
    homePos(righth)
#
speak("Hello Baby")
homePos(righth)
homePos(lefth)
time.sleep(1)
print("Scanning...")
scan()
time.sleep(3)
greet()
Hi()
time.sleep(2)
homePos(righth)
homePos(lefth)
speak("Wave incoming")
Wave()
time.sleep(1.5)
churm(2)
time.sleep(1.5)
homePos(righth)
homePos(lefth)