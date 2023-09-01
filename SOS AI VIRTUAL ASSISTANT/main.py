import operator
import random
import sys
import openai as openai
import pyttsx3 #pip install pyttsx3
import requests
import speech_recognition as sr #pip install speechRecognition
import datetime
import openai
from config import api_key
import speedtest
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import psutil
from bs4 import BeautifulSoup
from requests import get
from instaloader import instaloader
from selenium import webdriver
from time import sleep
import pyautogui
import numpy as np
import pywhatkit as kit
import html5lib
import speedtest_cli
from twilio.rest import Client

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)




def ai(prompt):
    openai.api_key = api_key
    text = f"Open AI Response for Prompt: {prompt} \n ***********************\n\n"


    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    print(response["choices"][0]["text"])
    speak(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

        with open(f"Openai/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
            f.write(text)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am SOS AI Assistant Sir. Please tell me how may I help you")

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
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('singhmanrajarora@gmail.com', 'Manraj@111')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

chatStr=""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = api_key
    chatStr += f"Divjot: {query}\n SOS AI: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]



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

        elif 'thanks' in query or 'thank you' in query or 'thank u' in query:
            speak("You are welcome sir, I am always here to help you, Its my pleasure")
            print("You are welcome sir, I am always here to help you, Its my pleasure")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\hp\\Music\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'scribble.io' in query:
            webbrowser.open("https://skribbl.io/")

        elif 'email to divjot' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aroradivjotsingh@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend divjot. I am not able to send this email")

        elif "instagram profile" in query or "profile on instagram" in query:
                speak("sir please enter the user name correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                sleep(5)
                speak("sir would you like to download profile picture of this account.")
                condition = takeCommand().lower()
                if "yes" in condition:

                 mod = instaloader.Instaloader()  # pip install instadownloader
                 mod.download_profile(name, profile_pic_only=True)
                 speak("i am done sir, profile picture is saved in our main folder. now i am ready")

        elif "take screenshot" in query or "take a screenshot" in query:

           speak("sir, please tell me the name for this screenshot file")
           name=takeCommand().lower()
           speak("please sir hold the screen for few seconds, i am taking sreenshot")
           sleep(3)
           img = pyautogui.screenshot()
           img.save(f"{name}.png")
           speak("i am done sir, the screenshot is saved in our main folder")

        elif 'alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 12:
                music_dir = 'C:\\Users\\hp\\Music\\Songs'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        # elif 'some calculation' or 'calculate' in query:
        #     r=sr.Recognizer()
        #     with sr.Microphone() as source:
        #         print("Listening... ")
        #         r.adjust_for_ambient_noise(source)
        #         audio = r.listen(source)
        #     my_string = r.recognize_google(audio)
        #     print(my_string)
        #     def get_operator_fn(op):
        #         return {
        #             'plus 'or '+' : operator.add,#plus
        #             '-' : operator.add,#minus
        #             'x' : operator.add,#multiplied by
        #             'divided' :operator.__truediv__, #divided by
        #         }[op]
        #     def eval_binary_expr(op1, oper, op2): #5 plus 8
        #         op1,op2 = int(op1), int(op2)
        #         return get_operator_fn(oper)(op1, op2)
        #     speak("Your Result is")
        #     speak(eval_binary_expr(*(my_string.split())))

        elif 'whatsapp message' in query:
            speak("Please enter the number to whom you want to send the message")
            msg_num = takeCommand().lower()
            speak("Please enter the message you want to send")
            msg = takeCommand().lower()
            kit.sendwhatmsg("+91" + msg_num, msg,  datetime.datetime.now().hour, datetime.datetime.now().minute + 3)

        elif 'play song on youtube' in query:
            speak("Please enter the song name")
            song = takeCommand().lower()
            kit.playonyt(song)

        elif 'on Google' in query:
            speak("sir what do you want to search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'temperature' in query:
            speak("Please Repeat again")
            search = takeCommand().lower()
            url = f"https://google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div",class_ ="BNeawe").text
            speak(f"current {search} is {temp}")

        elif 'how much power left' in query or 'battery' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Hi sir Your laptop has {percentage} percent battery")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")
            print(f"Your IP Address is {ip}")

        elif 'internet speed' in query or 'net speed' in query:
            speak("sure please wait for 1-2 minutes")
            print("sure please wait for 1-2 minutes")
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Your Downloading Speed is {dl} bit per second and Your Upload speed is {up} bit per seconds")
            print(f"Your Downloading Speed is {dl} bit per second and Your Upload speed is {up} bit per seconds")

        elif 'send sms' in query:
            speak("Please Enter the number where you want to send sms")
            msg_number = takeCommand().lower()
            speak("Please enter the message you want to send")
            msgg = takeCommand().lower()
            account_sid = 'AC1ca967fde5d2d1a88223eca5c5550904'
            auth_token = '3d7bfd456b3b093cf540c79e85dab07'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body= msgg,
                from_='+12055494417',
                to='+91'+ msg_number
            )

            print(message.sid)

        elif 'voice call' in query:
            speak("Please Enter the number whom you want to call")
            call_num = takeCommand().lower()
            msgg = takeCommand().lower()
            account_sid = 'AC1ca967fde5d2d1a88223eca5c5550904'
            auth_token = '3d7bfd456b3b093cf540c79e85dab07'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                twiml= '<Response><SayThis Is A Call From SOS AI </Say></Response>',
                from_='+12055494417',
                to='+91'+ call_num
            )

            print(message.sid)

        elif 'volume up' in query:
            pyautogui.press("volumeup")


        elif 'volume down' in query:
            pyautogui.press("volumedown")


        elif 'volume mute' in query:
            pyautogui.press("volumemute")

        elif 'Using Artificial Intelligence'.lower() in query.lower() or 'Using AI'.lower() in query.lower():
            ai(prompt=query)


        elif 'shutdown the system' in query:
            os.system("shutdown /s /t 5")

        elif 'stop' in query or 'end' in query or 'finish' in query:
            exit()

        else:
            chat(query)
