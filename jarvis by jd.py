import pyttsx3
import speech_recognition as sr
import random
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):   
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("goood afternoon!") 
    else:
        speak("good evening!")
    speak("i am jarvis sir please tell me how may i help you")               
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('harshshah4014@gmail.com','potatodj@')
    server.sendmail('harshshah4648@gmail.com',to,content)
    server.close()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
       
     
        audio =r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
     print(e)
        
     speak("say again it ")    
        
     return "none"
    return query    
if __name__ == "__main__":
    wishMe()     
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("goolge.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music'  in query:
            music_dir='D:\\new songs'   
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'send mail' in query:
            try:
                speak("what should i say!")
                content=takecommand()
                to = "harshshah4648@gmail.com"
                sendEmail(to,content)
                speak("email as been sent!")
            except Exception as e:
                print(e)
                speak("sorry email is not send")
        elif 'who are you' in query:
            jarvis=("i am jarvis and i am here to spread love")
            print(jarvis)
            speak(jarvis)        
        elif 'quit' in query:
            file_dir = 'D:\\jarvis'
            jd = ("bye sir have a great day")
            print(jd)
            speak(jd)

            os._exit(file_dir)    
        elif ' open game  ' in query:
            print("opening gta 5")
            speak(print)
            game_code="C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(game_code)           



    
                 
     

   


 