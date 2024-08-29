import pyttsx3 #this library converts text to speech, offline
import speech_recognition as sr #sppech recognition module
import datetime
import os
import webbrowser as wb
import pywhatkit as pw

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id) 
# print(voices[1].id)

def speak(audio): #function to speak
    engine.say(audio)
    engine.runAndWait()

def takeCommand(): #takes audio command from user and converts it to text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout = 1000, phrase_time_limit = 5)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said : {query}")
    except Exception as e:
        speak("Please say that again")
        return "none"
    return query

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning mihhir sir. how may i help you?")
    elif hour >= 12 and hour < 17:
        speak("good afternoon mihhir sir. how may i help you?")
    else :
        speak("good evening mihhir sir. how may i help you?")

if __name__ == "__main__":
    query = takeCommand().lower()
    if "jarvis" in query:
        greet()
        while(True):
            query = takeCommand().lower()
            if "stop" in query:
                speak("Good bye sir")
                break
            elif "open notepad" in query: #open notepad
                path = "C:\\Windows\\notepad.exe"
                speak("sure sir, opening notepad")
                os.startfile(path)
            elif "open ms word" in query:
                path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
                speak("sure sir, opening m.s. word")
                os.startfile(path)
            elif "open command prompt" in query:
                speak("sure sir, opening command prompt")
                os.system("start cmd")
            elif "open youtube" in query:
                speak("sure sir, opening youtube")
                wb.open("https://www.youtube.com/")
            elif "open linkedin" in query:
                speak("sure sir, opening linkedin")
                wb.open("https://www.linkedin.com/in/mihiranand21/")
            elif "open google" in query:
                speak("Sir, what do you want me to search?")
                search = takeCommand().lower()
                wb.open(f"{search}")
            elif "time" in query:
                min = datetime.datetime.now().minute
                hour = datetime.datetime.now().hour
                if hour > 12:
                    hour -= 12
                speak(f"Sir, it is currently {min} past {hour}")
            elif "play on youtube" in query:
                speak("Sir, what do you want me to play?")
                cm = takeCommand().lower()
                pw.playonyt(cm)
