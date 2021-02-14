import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
from idlist import password,my_gmail,destination

p=password
g=my_gmail
d=destination

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            print('Recognizing...')
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', ' ')
                print(command)
    except:
        pass
    return command

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(g,p)
    server.sendmail(g,d,content)
    server.close()

def run_alexa():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', ' ')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M:%p')
            talk('Current time is ' + time)

        elif 'who is ' in command:
            person = command.replace('who is ', ' ')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif 'send email' in command:
            try:
                talk('What should i say?')
                content=take_command()
                to=d
                sendemail(to,content)
                talk('Email has been sent')
            except Exception as e:
                print(e)
                talk('Sorry,not able to send email')


        elif 'date' in command:
            talk('sorry, i have a headache')

        elif 'are you single' in command:
            talk('I am in a relationship with wifi')

        elif 'joke' in command:
            talk(pyjokes.get_joke())

        elif 'wish me' in command:
            hour=int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                talk('Good Morning!')
            elif hour>=12 and hour<18:
                talk('Good Afternoon!')
            else:
                talk('Good Night!')

            talk('How may i help you?')
        else:
            talk('Please say that command again.')


while True:
    run_alexa()
