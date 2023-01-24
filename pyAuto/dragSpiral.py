import pyautogui as pag
import time
import pyttsx3

engine= pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("Jarvis", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def countDown(n, say=True):
    speed=0.3
    if say:
        speak("Starting countdown")
    while n:
        if say:
            speak(n)
        time.sleep(speed)
        n-=1
    speak("Fire")


def spiralSquare(edge=200):
    i=5
    while i<edge:
        pag.dragRel(i, 0)
        i+=5
        pag.dragRel(0, i)
        pag.dragRel(-i, 0)
        i+=5
        pag.dragRel(0, -i)   

if __name__=="__main__":
    print(__name__)
    countDown(5)
    spiralSquare()