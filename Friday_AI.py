import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voice,id)
engine.setProperty('voice' , voices[1].id)


def speak(audio):
    engine.say (audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour  >=0 and hour <12:
        speak ("Very Good Mornin")

    elif hour>= 12 and hour < 18:
        speak ("Good Afternoon Ji")


    else :
        speak ("Good Evening ")

    
    speak (" I am Friday. A artificail Intelligent speak recogniser made by Dheeraj, Please tell me how may i help you.")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("i am listning......")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
            print('recognizing')
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")

    except Exception as e:
            #print (e)

            print("Say that again please.....")
            return "None"

    return query


if __name__ == "__main__":
    wishMe()
    

    while True:
        query = takecommand().lower()

    #All Logic Based on query to perform task
        if 'wikipedia' in query:
            speak('searching Wikipedia......')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary (query, sentences=2)
            speak("According to Wikipedia")
            print (results)
            speak (results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com") 

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            music_dir = 'D:\\music'    
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak (f"Hello the time is {strtime}")
            print (strtime)

        elif 'open code editor' in query:
            codepath = "C:\\Users\\Dheeraj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'quit exit' in query:
            exit(speak)
            exit(takecommand)
            
