import speech_recognition as sr
import  pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyjokes
import webbrowser as wb

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace("assistant","")
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = listen_command()
    if "play" in command:
        song = command.replace("play","")
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'wiki' in command:
        person = command.replace('wiki', '')
        person = person.replace('search','')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        url = "http://google.com/search?q="
        wb.get().open_new(url+command)
        talk("Here are the results from Google.")

run_alexa()