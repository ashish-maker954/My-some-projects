import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Asish sir!")

    elif hour>=12 and hour<14:
        speak("Good Afternoon Ashish sir!")   

    else:
        speak("Good Evening Ashish sir!")  

    speak("I am Jarvis Ai of Ashish . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('asthaetah.ak@gmail.com', '@INDALSINGH2008')
    server.sendmail('asthaetah.ak@gamil.com',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open stackover flow' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        
        elif 'hari' in query:
            webbrowser.open("https://www.youtube.com/watch?v=aqvDTCpNRek&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")

        elif 'upload video' in query:
            webbrowser.open("https://studio.youtube.com/channel/UCULU_dtIrAqkCbGuoLM5YlQ/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D")


        elif 'play music' in query:
            music_dir = 'D:\Ashtech'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\91945\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open mamu' in query:
            mamuPath = "C:\Program Files (x86)\Microvirt\MEmu\MEmu.exe"
            os.startfile(mamuPath)

        elif 'open chrome'in query:
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chromePath)

        elif 'open fast typing' in query:
            fastPath = "C:\\Program Files (x86)\\TypingMaster10\\tmaster.exe"
            os.startfile(fastPath)
        
        elif 'email to dad' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "asthaetah@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry my friend Ashish bhai. I am not able to sent this email")
        
        elif 'owner' in query:
            speak("Ashish sir is my owner he developed me and i am the ai of Ashish!")

        elif 'pratham' in query:
            speak("hello pratham parmar i know you are ashish best friend ")

        elif 'father' in query:
            speak("hello Mr.Indal Singh  i know you are father of Ashish sir ")

        elif 'kushagra' in query:
            speak("hello kushagra  i know you are brother of Ashish sir ")

        elif 'mother' in query:
            speak("hello Mrs.vijaylakshami  i know you are mother of Ashish sir and you are so good in world")

        elif 'uncle' in query:
            speak("hello mr.ravi prakash i know you are the uncle of Ashish congratulation for buying new car and i know you are the best buissnessman of galaxy industries")

        elif 'who are you' in query:
          speak("i am jarvis the ai of ashish he design me")
       
        elif 'something about bad' in query:
         speak("kushagra is very bad and never able to pass iit")

        


        




        

        
    