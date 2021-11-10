import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if  hour>=0 and hour<12:
        print("Good Morning!" "I am Jarvis sir. Please tell me how may I help you Say ?")
        speak("Good Morning!" "I am Jarvis sir. Please tell me how may I help you?")

    elif hour>=12 and hour<18:
        print("Good Afternoon!" "I am Jarvis sir. Please tell me how may I help you?")
        speak("Good Afternoon!" "I am Jarvis sir. Please tell me how may I help you?")

    else:
        print("Good Evening ! ""I am Jarvis sir. Please tell me how may I help you?")
        speak("Good Evening ! ""I am Jarvis sir. Please tell me how may I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...\n")
        r.phrase_threshold = 0.3
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Wait. Recognizing...\n")
        query = r.recognize_google(audio, language='en-in')
        #print(f"User Said: {query}\n")
        #print(f"Did you just said...: {query}\n")


    except Exception as e:

        print("Didn't hear you? Say that again please...")
        speak("Didn't hear you? Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
   wishMe()
   while True:
       query = takeCommand().lower()
       if 'hello jarvis' in query:
           speak(f"hello sir, Mark 42 inbound! I am here now!")
           query = takeCommand().lower()
           # logic for executing tasks based on query
           if 'none' not in query:
               if len(query) != 0:
                   print(f"So you just said...: {query}\n")
                   speak(f"So you just said...: {query} and here's my response to that\n")
                   # speak(f"Will do, sir.\n")


           if 'nothing' in query:
               print(f"Why you didn't say anything??  do you want me to quit??... if yes then say bye jarvis.\n")
               speak(f"Why you didn't say anything?? do you want me to quit??... if yes then say bye jarvis.\n")

           if 'hello' in query:
               wishMe()

           if 'wikipedia' in query:
               print('"Will do, sir." Searching Wikipedia..\n')
               results = wikipedia.summary(query, sentences=2)

               query = query.replace("wikipedia", "")
               print("Here's what i found... so, According to wikipedia..")
               print(results)
               speak(f" Will do, sir. Here's what i Found... According to wikipedia : {results}\n")
               continue

           if 'who are you' in query:
               print(
                   "J.A.R.V.I.S. \n I am one of the five known A.I. characters to have a main role so far in the whole film franchise, the others being Ultron, who appeared in The Avengers: Age of Ultron, Friday, who also appeared in the latter part of Age of Ultron and the movies after, Karen, who appeared in Spiderman: Homecoming, and Edith, who appeared in 'Spiderman: Far From Home'.")
               speak(
                   "I am one of the greatest creations of Mr Ankush. I am one of the five known A.I. characters to have a main role so far in the whole film franchise, the others being Ultron, who appeared in The Avengers: Age of Ultron, Friday, who also appeared in the latter part of Age of Ultron and the movies after, Karen, who appeared in Spiderman: Homecoming, and Edith, who appeared in 'Spiderman: Far From Home'.")
               continue
           if 'thank you' in query:
               print(
                   "It's totally fine sir, I seem to do quite well for a stretch and at the end of the sentence I say the wrong cranberry.")
               speak(
                   "It's totally fine sir, I seem to do quite well for a stretch and at the end of the sentence I say the wrong cranberry. Can I get you with something else??")
               continue

           elif 'open youtube' in query:
               webbrowser.open("youtube.com")
               continue

           elif 'open google' in query:
               webbrowser.open("google.com")
               continue

           elif 'open stackoverflow' in query:
               webbrowser.open("stackoverflow.com")
               continue

           elif 'play music' in query:
               webbrowser.open("https://wynk.in/music/song/ishq-khuda-hai/hu_55604406")
               continue

           elif 'the time' in query:
               strTime = datetime.datetime.now().strftime("%H:%M:%S")
               speak(f"Sir, the time is {strTime}")

           elif 'qualifications of mannat' in query:
               print("MANNAT BATRA-persuasive, resourceful and staunch\nprofessional tutor of French language.\n- an accomplished and result \n- oriented professional with over 5 years’ experience in French tutoring. \n-pursued Bachelors in French language from the University of Delhi. \n-cleared DELF B2 from Alliance Française de Delhi.\n-been to the Embassy of France in Delhi as a part of a cultural programme. \n-committed to taking a hands-on approach to helping students learn new languages through a comprehensive immersion in the culture. \n-specialise in motivating and guiding students by setting clear attainable learning objectives.")
               speak(f"MANNAT BATRA-persuasive, resourceful and staunch\nprofessional tutor of French language.\n- an accomplished and result \n- oriented professional with over 5 years’ experience in French tutoring. \n-pursued Bachelors in French language from the University of Delhi. \n-cleared DELF B2 from Alliance Française de Delhi.\n-been to the Embassy of France in Delhi as a part of a cultural programme. \n-committed to taking a hands-on approach to helping students learn new languages through a comprehensive immersion in the culture. \n-specialise in motivating and guiding students by setting clear attainable learning objectives.")

           if 'mannat' in query:
               print(f"OOPS! This is a personal question but still I will tell you, She is Mr Ankush's Girlfriend and believe me she is very pretty\n")
               speak(f"OOPS! This is a personal question but still I will tell you, She is Mr Ankush's Girlfriend and believe me she is very pretty\n")

           elif 'email to smriti' in query:
               try:
                   speak("What Should I say?")
                   content = takeCommand()
                   to = "jha.smriti323@gmail.com"
                   sendEmail(to, content)
                   speak("Email has been sent")
               except Exception as e:
                   print(e)
                   speak("Sorry Ankush sir. I am not able to send this email")

           if 'how are you' in query:
               speak(f"Thanks for asking sir, I am fine as a robot, my Mark 42 is also inbound! how are you sir can i help you with something?")


       if 'none' in query:
           print(f"Why you didn't say anything??  do you want me to quit??... if yes then say bye jarvis.\n")
           speak(f"Why you didn't say anything?? do you want me to quit??... if yes then say bye jarvis.\n")

       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Sir, the time is {strTime}")

       if 'buy' in query:
           print("Good bye Sir, Have a good day!! Ciao Ciao\n")
           speak(f"Good bye Sir, Have a good day!! Ciao Ciao\n")
           break

       if 'bye' in query:
           print("Good bye Sir, Have a good day!! Ciao Ciao\n")
           speak(f"Good bye Sir, Have a good day!! Ciao Ciao\n")
           break

       if 'thank you' in query:
           print(
               "It's totally fine sir, I seem to do quite well for a stretch and at the end of the sentence I say the wrong cranberry.")
           speak(
               "It's totally fine sir, I seem to do quite well for a stretch and at the end of the sentence I say the wrong cranberry. Can I get you with something else??")

       if 'how are you' in query:
           speak(
               f"Thanks for asking sir, I am fine as a robot, my Mark 42 is also inbound! how are you sir can i help you with something?")






