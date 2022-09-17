from multiprocessing.dummy.connection import Listener
import pyttsx3
import speech_recognition as sr
import pywhatkit 
import datetime
import wikipedia
import pyjokes
import os
import webbrowser

Listener  = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        talk("Good Morning")
    elif hour >=12 and hour < 18:
        talk("Good afternoon")
    else:
        talk("Good Evening")

wishMe()

engine.say("I am your Alexa")
engine.say("How can i help you")
engine.runAndWait()



def listen():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voice = Listener.listen(source)
            command = Listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa",'')
                # print(command)
    except:
        pass
    return command


def run_alexa():
    command = listen()
    print(command)

    if "play" in command:
        song = command.replace("play",'')
        talk("playing"+ song)
        pywhatkit.playonyt(song)
    
    # elif "play music" in command:
        
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is:"+ time)
    
    elif "who is" in command:
        person = command.replace("who is",'')
        print("Searching in wikipedia.......")
        info  = wikipedia.summary(person,2)
        print(info)
        talk("According to wikipedia:"+ info)
    
    elif "joke" in command:
        jokes = pyjokes.get_joke()
        print(jokes)
        talk(jokes)
    
    elif "open youtube" in command:
        print("opening youtube")
        webbrowser.open("youtube.com")
    
    elif "open google" in command:
        print("opening google")
        webbrowser.open("google.com")
    
    elif "open stackoverflow" in command:
        print("opening stackoverflow")
        webbrowser.open("stackoverflow.com")
    
    elif "open gmail" in command:
        print("opening gmail")
        webbrowser.open("gmail.com")

    elif "Thank you" in command:
        print("Mention not")
        talk("Mention not")
    
    # elif "stop" in command:
    #     return command
    
    else:
        talk("Can you plese repeat it again")
# while True:
#     command = run_alexa()
#     if "stop" in command:
#         break

run_alexa()



