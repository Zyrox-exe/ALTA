import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

# Rate and Volume
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)

# Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Text to Speech
def speak(text):
    """Used to Speak whatever text is passed to it"""
    engine.say(text)
    engine.runAndWait()


def greet_user():
    """Greet User According to the time"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning, Sir {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon, Sir {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening, Sir {USERNAME}")
    speak(f"I am {BOTNAME}, How may I assist you?")

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone as source:
        print('Listening......')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        if not "exit" in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 or hour < 6:
                speak("Good night sir, take care!")
            else:
                speak("Have a good day sir!")
            exit()
        except Exception:
            speak('Sorry, I could not understand. Could you say that again?')
            query = 'None'
        return query