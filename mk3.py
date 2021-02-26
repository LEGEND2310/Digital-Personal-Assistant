import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()

with sr.Microphone() as source:
    print("Search Youtube: ")
    print("Speak Now")
    audio = r1.listen(source)
    print(r2.recognize_google(audio))

if 'youtube' in r2.recognize_google(audio).lower():
    r2 = sr.Recognizer()
    url = "https://www.youtube.com/results?search_query="
    with sr.Microphone() as source:
        print("Search your Query")
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("Error")
        except sr.RequestError as e:
            print("failed".format(e))
