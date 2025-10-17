import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com/")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com/")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        l = musicLibrary.m[song]
        webbrowser.open(l)


speak("Heyyy Jarvis is activeted")

if __name__ == "__Jarvis__":
    while True:
        r = sr.Recognizer()

        print("recoginzing....")
        try:
            with sr.Microphone() as s:
                print("Listening....")
                audio = r.listen(s,timeout=3,phrase_time_limit=2)
                w = r.recognize_google(audio)
            if (w.lower() =="jarvis"):
                speak("Yess Sir")
                    
                with sr.Microphone() as s:
                    print("I am listening")
                    audio = r.listen(s)
                    c = r.recognize_google(audio)
                        
                    process_command(c)
                        
        except Exception as e:
            print("Error!!! Please Say Something!!".format(e)) 