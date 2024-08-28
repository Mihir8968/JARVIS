import pyttsx3 #this library converts text to speech, offline
import speech_recognition as sr #sppech recognition module
# import pyaudio
import datetime

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
        audio = r.listen(source, timeout = 1, phrase_time_limit = 5)

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
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 5:
        speak("Good Afternood Sir")
    else :
        speak("Good Evening Sir")

    speak("How can I help you?")

if __name__ == "__main__":
    # speak("Good morning sir")
    # takeCommand()
    greet()
