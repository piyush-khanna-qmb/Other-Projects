
"""-----------------DICTATION MODE FOR ABDUL-------------------"""

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

def s2t():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=800
        r.pause_threshold=1
        audio= r.listen(source)

    try:
        query= r.recognize_google(audio, language="en-in")
        print("Recognized:", query)
        return query
    
    except Exception as e:
        return "none"

if __name__=="__main__":
    speak("ready for command")
    while True:
        sf= False
        txt= s2t().lower()

        if txt=="none":
            speak("Couldn't get what you said. Please repeat or ask to stop")
            continue
        if txt=="stop":
            speak("Exiting")
            break

        if "next line" in txt:
            txt= txt.replace("next line", "NL")
        
        if "send and stop" in txt:
            txt= txt.replace("send and stop", "SAS")

        txtArr= txt.split()
        if txtArr[-1]=="send":   #Taaki send last me ho tabhi send ho, varna treat as common text
            sf=True
            k=txtArr.pop()
        
        for word in txtArr:
            if word=="NL":
                pag.keyDown('shift')
                pag.press('enter')
                pag.keyUp('shift')
                continue

            if word=="SAS":
                pag.press('enter')
                speak("Message typed and sent. Exiting.")
                exit()

            pag.typewrite(word)
            pag.press('space')

        if sf==True:
            pag.press('enter')
            speak("Message typed and sent successfully")
        else:
            speak("Written. Next?")