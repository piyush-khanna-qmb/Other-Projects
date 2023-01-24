import speech_recognition as sr
import pyautogui

def scroll_down():
    pyautogui.scroll(-500)

def listen_for_scroll_down():
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening for scroll down command...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        if command:
            scroll_down()
            print(str(command))
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")

if __name__ == '__main__':
    while True:
        listen_for_scroll_down()
