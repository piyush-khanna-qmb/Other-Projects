import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit as kit
import serial
import time
import cv2
from cvzone import HandTrackingModule as htm
import numpy as np
import math

Assnames= ["jarvis", "lullu", "ghochu", "chirkut", "prosthetic"]
Sassnames= ["zira", "lata", "pushpa", "machpa"]
Massnames= ["sir", "master", "master ji", "king almighty", "sire", "my lord", "sir victor"]
contacts= {"arjun": "+917818816011", "mummy": "+919548944863", "papa": "+917669956656", "khushi": "+918923665606"}

engine= pyttsx3.init("sapi5")
voices= engine.getProperty("voices")
engine.setProperty("Jarvis", voices[0].id)
# lefth= serial.Serial('COM16', baudrate= 9600, timeout=1)
# righth= serial.Serial('COM17', baudrate= 9600, timeout=1)

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

def Wave():
    setVals(lefth, 90, 90, 90, 90, 90, 90, 0.4)
    setVals(lefth, 70, 50, 60, 70, 90, 90, 0.4)
    setVals(lefth, 70, 70, 40, 120, 90, 90, 0.4)
    setVals(righth, 120, 110, 130, 60, 90, 90, 0.4)
    setVals(lefth, 90, 90, 90, 90, 90, 90, 0.4)
    setVals(righth, 120, 120, 110, 110, 90, 90, 0.4)
    setVals(righth, 90, 90, 90, 90, 90, 90, 0.4)

def compVision():
    cam=cv2.VideoCapture(0)
    width, height= 1020, 720
    detector= htm.HandDetector(maxHands=1, detectionCon=0.7)
    cam.set(3, width)
    cam.set(4, height)
    prev= time.time()
    while True:
        ignore, frame= cam.read(0)
        frame= detector.findHands(frame)
        pList= detector.getPosition(frame, draw=False)
        if len(pList)!=0:
            x1,y1= pList[4][1], pList[4][2]
            x2,y2= pList[8][1], pList[8][2]
            cx,cy = (x1+x2)//2, (y1+y2)//2
            cv2.circle(frame, (x1,y1), 10, (125,0,0), -1)
            cv2.circle(frame, (x2,y2), 10, (125,0,0), -1)
            cv2.line(frame, (x1,y1), (x2,y2), (125,0,0), 2)
            dist=int(math.hypot(x2-x1, y2-y1))
            vol= int(np.interp(dist, (20,150), (130, 20)))
            print(int(vol))
            command= f"#1ZZ#ZZ#ZZ#4ZZ#5ZZ#6{chr(vol)}Z****"
            # righth.write(command.encode())
            if dist<15:
                cv2.circle(frame, (cx,cy), 10, (0,255,0), -1)
            elif dist>170:
                cv2.circle(frame, (cx,cy), 10, (0,0,255), -1)
            else:
                cv2.circle(frame, (cx,cy), 10, (125,0,0), -1)

        cv2.imshow("Volume Controller", frame)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break

    cam.release()

def skillset():
    speak("I have a huge skillset, sir. You can use me to, search something on wikipedia or directly on google. I can open various other sites too. You can ask me to play a song either on youtube, or randomly from media library. I can even send whatsapp messages for you. For home automation, when connected to ESP, i can even turn on and off room appliances through voice or gestures.")
    
###################Gestures###################
def scan():
    homePos(lefth)
    homePos(righth)
    setVals(lefth, 180, 110, 100, 90, 90, 90, 1)
    setVals(righth, 90, 70, 70, 90, 90, 90, 1)
    setVals(lefth, 90, 110, 100, 90, 90, 90, 1)
    setVals(righth, 0, 70, 70, 90, 90, 90, 1)
    homePos(lefth)
    homePos(righth)


def wave():
    setVals(lefth, 90, 90, 90, 90, 90, 90, 0.4)
    setVals(lefth, 70, 50, 60, 70, 90, 90, 0.4)
    setVals(lefth, 70, 70, 40, 120, 90, 90, 0.4)
    setVals(righth, 120, 110, 130, 60, 90, 90, 0.4)
    setVals(lefth, 90, 90, 90, 90, 90, 90, 0.4)
    setVals(righth, 120, 120, 110, 110, 90, 90, 0.4)
    setVals(righth, 90, 90, 90, 90, 90, 90, 0.4)

def churm(n=2):
    for i in range(n):
        give= f"#1ZZ#2ZZ#3ZZ#4ZZ#5ZZ#6{chr(180)}Z****"
        lefth.write(give.encode())
        time.sleep(0.25)
        give= f"#1ZZ#2ZZ#3ZZ#4ZZ#5ZZ#6ZZ****"
        lefth.write(give.encode())    
        time.sleep(0.25)

###################Gestures###################

def ListCheck(lis, query):
    for i in lis:
        if i in query:
            return(i)
    else:
        return("")

def speakOutOf(lis):
    i= random.randint(0,len(lis)-1)
    speak(lis[i])

def intro():
    speak("Sure sir. Gentlemen? My name is Codey and i am Piyush's Laptop. And I've recently gained these wonderful arms. You can call them Claws.")
    churm(2)
    speak("If you please, you can ask me to make certain gestures using these arms. You can even control these claws yourself either by entering values for its angles, or simply, You can simulate the gripper using your own fingers.")

def s2t():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio= r.listen(source)

    try:
        query= r.recognize_google(audio, language="en-in")
        #print("Recognized!")
        return query
    
    except Exception as e:
        return "None"

def WikiSearch(query):
    try:
        results= wikipedia.summary(query, sentences=2)
        return results
    except Exception as e:
        return "Error"

def greet():
    prahar= datetime.datetime.now().hour
    if 6<prahar<12:
        speak("A very Good morning gentlemen?")
    elif 12<prahar<15:
        speak("A very Good afternoon gentlemen?")
    else:
        speak("A very Good evening gentlemen?")
    speak("Nice to meet you")

def urlFormer(lul):
    t=""
    lul=lul.lower()
    for ch in lul:
        #print(ch, end="")
        if ('a'<=ch<='z') or ('A'<=ch<='Z'):
            t=t+ch
        if ch==' ':
            t=t+'+'
    t="www.google.com/search?q="+t
    return t

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def telltime():
    strTime= datetime.datetime.now().strftime("%I hours and %M minutes")
    speak(f"The time is {strTime}")

mode=0

if __name__ == "__main__":
    # scan()
    # greet()
    while True:
        query= s2t().lower()
        print(query)
        # print("Listening")
        if ListCheck(["stop listening", "bye bye", "takliya", "you can leave", "you may leave", "see you again", "see you next time", "until next time"], query)!="":
            speakOutOf(["Have a good day, sir!", "Have a nice day, sir!", "I hope i was helpful sir."])
            quit()

        if ListCheck(Assnames, query)!="":
            mode=1
            speakOutOf(["At your command, sir.", "Always up for you, sir!", "Ready for your command, sir.", "Yes sir?", "Han g?"])
            continue

        if mode==1:
            if "none" in query:
                speakOutOf(["Couldn't get that. Can you please repeat, sir?",  "i am sorry, can you please repeat?", "not sure i got that. can you please repeat?"])
                continue
            #BIGBUBBLE
            elif "introduce" in query:
                intro()

            elif "computer vision" in query:
                compVision()
            
            elif "wave" in query:
                wave()
            
            elif ListCheck(["what all", "what can", "you do"], query):
                skillset()

            elif "youtube" in query:
                if ListCheck(["open youtube", "youtube chala de"], query):
                    webbrowser.open("www.youtube.com")
                    speak("Opening youtube")

                elif "play" in query:
                    query=query.replace("play", "")
                    if "on youtube" in query:
                        query=query.replace("on youtube", "")
                    kit.playonyt(query)
                    speakOutOf(["Have a good time sir", "sending good vibes"])

            elif "time" in query:
                telltime()
            
            elif (ListCheck(["wikipedia", "who is"], query))!="":
                speakOutOf(["Just a second?", "searching online", "looking in wikipedia"])
                wikiRet= ListCheck(["wikipedia", "who is"], query)
                query=query.replace(wikiRet, "")
                results= WikiSearch(query)
                if results== "Error":
                    print("404- Page doesn't exist :(")
                    speak("Sorry sir. The wikipedia page doesn't exist for this person")
                else:
                    print(results)
                    speak(f"Sir, According to wikipedia, {results}")
                    
            elif "facebook" in query:
                webbrowser.open("www.facebook.com")
            
            elif "reddit" in query:
                webbrowser.open("www.reddit.com")
            
            elif "open whatsapp" in query:
                webbrowser.open("web.whatsapp.com")
            
            elif "google" in query:
                speak("What should I search on google, sir?")
                cm=s2t().lower()
                print(f"To be searched: {cm}")
                url=urlFormer(cm)
                webbrowser.open(url)
            
            elif (ListCheck(["email", "gmail"], query))!="":
                webbrowser.open("www.gmail.com")
            
            elif "dialogue box" in query:
                direc= "G:\\Commands\\speech.vbs"
                os.startfile(direc)

            elif (ListCheck(["random song", "random music", "random songs", "play music", "play some songs", "play some music", "let's have some party", "play songs", "play a song", "play me some music", "play me some songs"], query)!=""):
                music_dir= "E:\\songs"
                completesongs= os.listdir(music_dir)
                songs=[]
                for i in completesongs:
                    if i.endswith('.mp3'):
                        songs.append(i)
                num= random.randint(0, (len(songs)-1))
                speakOutOf(["Opening the music library and playing a random song", "have a good time sir!"])
                os.startfile(music_dir)
                os.startfile(os.path.join(music_dir, songs[num]))

            elif "arduino" in query:
                path="G:\\apps\Arduino Mahhhki\\Arduino\\arduino.exe"
                os.startfile(path)

            elif (ListCheck(["message", "whatsapp"], query))!="":
                speak("Whom should I send it to?")
                name= s2t().lower()
                if name=="none":
                    speak("Not sure i got that. Unsending the message")
                    print("Rolling back message...")
                    continue
                if name in contacts:
                    print(f"Will send message to {name} and num: {contacts[name]}")
                    speak("And what is the message, sir?")
                    msg=s2t()
                    speakOutOf(["The messages's on its way sir", "Sending the message", "Forwarding your message sir", "Forwarding your thoughts, sir"])
                    kit.sendwhatmsg_instantly(contacts[name], msg)
                else:
                    print(f"Contact unlisted: {name}")
                    speak(f"The name {name} is not in list. Either try again, or add to the list.")
                    
            elif ListCheck(["what is your name", "who are you"], query):
                speak("Hello! My name is any of these. Jarvis, lullu, chirkoot, bunny. Though, my master, Sir Piyush likes to call me oulu ka puttha sometimes.")
            
            elif ListCheck(["what is your age", "what is your birth date", "how old are you", "when is your birthday", "when does your birthday come", "on what date is your birthday"], query):
                yearcur= int(datetime.datetime.now().year)
                yeardiff= yearcur-2014
                #make function for displaying upcoming birthday
                speak(f"Currently, I am {yeardiff} years old. I was born on 18th of April 2014, and my birthday comes on the same date every year")

            elif ListCheck(["how are you", "wassup", "how you doing", "kya haal hai", "sab changa", "kaisa hai"], query):
                speakOutOf(["Really fine sir! I hope you are fine too", "Trying my best to make your work easier sir", "Been working a little extra nowadays? I hope it pays off someday."])
            


            #baaki saari conditions ab yahaan se
        mode=0  #Reverting back to non listening mode
