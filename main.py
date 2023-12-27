import operator
import random
import sys
import keyboard
import openai as openai
import pyttsx3 #pip install pyttsx3
import requests
import speech_recognition as sr #pip install speechRecognition
import datetime
import openai
import translator
from word2number import w2n
from config import api_key
import speedtest
import wikipedia #pip install wikipedia
import os
import tkinter as tk
import random
import time
from os import system
import cv2
import smtplib
import psutil
from bs4 import BeautifulSoup
from requests import get
from instaloader import instaloader
from time import sleep
import pyautogui
import numpy as np
import pywhatkit as kit
import html5lib
import speedtest_cli
# from twilio.rest import Client
import PyPDF2
import subprocess
from bardapi import BardCookies
import setuptools

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voice', voices[0].id)
recognizer = sr.Recognizer()

chatStr = ""
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


def open_app(app_name):
    try:
        subprocess.run(["open", "-a", app_name])
        print(f"Opening {app_name}...")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("Please Repeat the name of application")
    speak("Please Repeat the name of application")
    app_name = listen().lower()
    open_app(app_name)

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry("420x500")

        self.canvas = tk.Canvas(self.master, bg="black", width=400, height=400)
        self.canvas.pack()

        self.canvas.create_rectangle(0, 0, 400, 400, outline="white")

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.is_paused = False

        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", fg="white", bg="black")
        self.score_label.pack()

        self.high_score_label = tk.Label(self.master, text=f"High Score: {self.get_high_score()}", fg="white", bg="black")
        self.high_score_label.pack()

        self.start_time = time.time()

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.pack()

        self.pause_button = tk.Button(self.master, text="Pause/Resume", command=self.toggle_pause)
        self.pause_button.pack()

        self.master.bind("<Key>", self.change_direction)

        self.update()

    def create_food(self):
        x = random.randrange(1, 39) * 10
        y = random.randrange(1, 39) * 10
        return self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="red")

    def move(self):
        if not self.is_paused:
            head = list(self.snake[0])

            if self.direction == "Up":
                head[1] -= 10
            elif self.direction == "Down":
                head[1] += 10
            elif self.direction == "Left":
                head[0] -= 10
            elif self.direction == "Right":
                head[0] += 10

            self.snake.insert(0, tuple(head))

            if self.snake[0] == (self.canvas.coords(self.food)[0], self.canvas.coords(self.food)[1]):
                self.canvas.delete(self.food)
                self.food = self.create_food()
                self.score += 1
                self.update_score()
            else:
                self.canvas.delete(self.snake[-1])
                self.snake.pop()

            if self.is_game_over():
                self.game_over()

            self.draw_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(
                segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green", tags="snake"
            )

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if (
                (event.keysym == "Up" and self.direction != "Down")
                or (event.keysym == "Down" and self.direction != "Up")
                or (event.keysym == "Left" and self.direction != "Right")
                or (event.keysym == "Right" and self.direction != "Left")
            ):
                self.direction = event.keysym

    def update(self):
        self.move()
        if not self.is_game_over() and not self.is_paused:
            self.master.after(100, self.update)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
        high_score = self.get_high_score()
        self.high_score_label.config(text=f"High Score: {high_score}")

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")
            self.update()

    def restart_game(self):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.is_paused = False
        self.start_time = time.time()
        self.update_score()
        self.update()

    def game_over(self):
        end_time = time.time()
        play_time = round(end_time - self.start_time, 2)
        high_score = self.get_high_score()

        if self.score > high_score:
            self.set_high_score(self.score)
            self.canvas.create_text(
                200, 240, text=f"Congratulations!\nNew High Score: {self.score}", font=("Helvetica", 16), fill="white"
            )
        else:
            self.canvas.create_text(
                200, 240, text=f"High Score: {high_score}", font=("Helvetica", 16), fill="white"
            )

        self.canvas.create_text(
            200, 180, text=f"Game Over\nScore: {self.score}\nTime: {play_time} seconds", font=("Helvetica", 16), fill="white"
        )

        self.master.after_cancel(self.update)

    def is_game_over(self):
        if any(
            [
                self.snake[0][0] < 0,
                self.snake[0][0] >= 400,
                self.snake[0][1] < 0,
                self.snake[0][1] >= 400,
                self.snake[0] in self.snake[1:],
            ]
        ):
            return True
        return False

    def get_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                high_score = int(file.read())
        except FileNotFoundError:
            high_score = 0
        return high_score

    def set_high_score(self, score):
        with open("high_score.txt", "w") as file:
            file.write(str(score))

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://open.er-api.com/v6/latest"

    def get_exchange_rate(self, base_currency, target_currency):
        params = {'apikey': self.api_key, 'base': base_currency}
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            exchange_rate = data['rates'].get(target_currency)
            if exchange_rate:
                return exchange_rate
            else:
                print(f"Currency code '{target_currency}' not found.")
                return None
        else:
            print("Failed to fetch exchange rates.")
            return None

    def convert(self, numamount, base_currency, target_currency):
        exchange_rate = self.get_exchange_rate(base_currency, target_currency)

        if exchange_rate is not None:
            converted_amount = numamount * exchange_rate
            return converted_amount
        else:
            return None

def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        quote_data = response.json()
        return f'"{quote_data["content"]}" - {quote_data["author"]}'
    else:
        return "Failed to fetch a quote."


def guess_number_game():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            elif abs(target_number - guess) <= 10:
                print("You're close! Keep trying.")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                break
            # Provide feedback when the guess is close

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def currency_converter():
    api_key = 'ca6bed7a7193138ee549fcb5'  # Replace with your actual API key
    currency_converter = (CurrencyConverter(api_key))

    print("Enter the amount to convert:")
    amount = input()
    numamount = w2n.word_to_num(amount)

    print("Enter the source currency code like INR, USD:")
    source_currency = input().upper()

    print("Enter the target currency code like INR, USD:")
    target_currency = input().upper()

    converted_amount = currency_converter.convert(numamount, source_currency, target_currency)

    if converted_amount is not None:
        print(f"{numamount} {source_currency} is equivalent to {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed")


def open_website(url):
    try:
        subprocess.run(["open", url])
        print(f"Opening {url}...")
    except Exception as e:
        print(f"An error occurred: {e}")

def speak(text):
    subprocess.run(["say", text])

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""


# def bardchat():
#         cookie_dict = {
#             "__Secure-1PSID": "bQhuVisizX6gmibLTAyPNMPbm7CdwC9mKI7NY2BCyCFg2G6HN1vMtA7KxVoMPgYAc0Z44w.",
#             "__Secure-1PSIDTS": "sidts-CjEB3e41hTLESRukhfkjDV2L50qZ0JqxzG_R7bMl8l_4nkywGAEm3FfCzz8nhseX36G1EAA",
#             "__Secure-1PSIDCC": "ACA-OxMad6pjXJ2tYFDrIxUE2NQnjNHYo2WB2DJaM5oWPk4nxb4LyqLijsfCrj-ewB47-LpLKQPr"
#         }
#         bard = BardCookies(cookie_dict=cookie_dict)
#
#         while True:
#             speak("Enter The Query : ")
#             Query = listen().lower()
#             Reply = bard.get_answer(Query)['content']
#             speak(Reply)
#             print(Reply)
#             if Query == "quit" or "stop":
#                  break
#             else:
#                 continue

def face_recognization():
    def setup_camera():
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            print("Error: Could not open webcam.")
            exit()
        cam.set(3, 640)
        cam.set(4, 480)
        return cam

    def detect_faces(image, scaleFactor=1.2, minNeighbors=5, minSize=None):
        return faceCascade.detectMultiScale(image, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)

    def recognize_faces(cam, recognizer, names, faceCascade, font, minW, minH):
        while True:
            ret, img = cam.read()
            if not ret:
                print("Error: Failed to capture frame.")
                break

            converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detect_faces(converted_image, scaleFactor=1.2, minNeighbors=5,
                                 minSize=(int(minW), int(minH)))

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])

                if 0 <= id < len(names):
                    recognized_name = names[id]
                    accuracy_percent = round(100 - accuracy)
                else:
                    recognized_name = "unknown"
                    accuracy_percent = round(100 - accuracy)

                cv2.putText(img, recognized_name, (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                # cv2.putText(img, f"{accuracy_percent}%", (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

                if accuracy_percent >= 50:
                    virtual_assistant()

            cv2.imshow('camera', img)

            k = cv2.waitKey(10) & 0xff
            if k == 27:
                break

        print("Thanks for using this program, have a good day.")
        cam.release()
        cv2.destroyAllWindows()

    if __name__ == "__main__":
        trainer_path = 'trainer/trainer.yml'

        if os.path.exists(trainer_path):
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read(trainer_path)

            cascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)
            font = cv2.FONT_HERSHEY_SIMPLEX

            id = 2
            names = ['', 'divjot']

            cam = setup_camera()

            minW = 0.1 * cam.get(3)
            minH = 0.1 * cam.get(4)

            recognize_faces(cam, recognizer, names, faceCascade, font, minW, minH)
        else:
            virtual_assistant()

def get_weather(city):
    api_key = 'df7f1c701223ebc643d34779916590cb'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(base_url)
    data = response.json()

    if data['cod'] == '404':
        return 'City not found'

    weather_description = data['weather'][0]['description']
    temperature_kelvin = data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15

    return f'The weather in {city} is {weather_description}. Temperature: {temperature_celsius:.2f}°C'

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    data = response.json()

    if data["type"] == "twopart":
        return f"{data['setup']} {data['delivery']}"
    elif data["type"] == "single":
        return data["joke"]
    else:
        return "Failed to fetch a joke."

def get_news():
    api_key = '7065166e0987403daf07aeb05ce82154'
    base_url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}'
    response = requests.get(base_url)
    data = response.json()

    if data['status'] == 'ok':
        articles = data['articles']
        headlines = [article['title'] for article in articles]
        return '\n'.join(headlines)
    else:
        return 'Unable to fetch news'

def get_health_tips():
    url = "https://example-health-tips-api.com/tips"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "tips" in data:
        return data["tips"]
    else:
        return "Failed to fetch health tips."

def add_task(todo_list):
    speak('Sure, what task would you like to add?')
    new_task = listen()
    todo_list.append_task(new_task)

def get_tasks(todo_list):
    tasks = todo_list.get_tasks()
    if tasks:
        speak('Here are your tasks:')
        for task in tasks:
            speak(task)
    else:
        speak('You have no tasks.')

def virtual_assistant():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am SOS A.I Assistant Sir. Please tell me how may I help you")

    while True:
        command = listen()

        def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('singhmanrajarora@gmail.com', 'Manraj@111')
            server.sendmail('youremail@gmail.com', to, content)
            server.close()

        #
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
            speak(response["choices"][0]["text"])
            chatStr += f"{response['choices'][0]['text']}\n"
            return response["choices"][0]["text"]

        def pdf_reader():
            book = open('py3.pdf, rb')
            pdfReader = PyPDF2.PDFfileReader(book)
            pages = pdfReader.num_pages()
            speak(f"Total Number Of Pages in This pdf/book {pages}")
            speak("sir please enter the page number i have to read ")
            pg = int(input("Please enter the page number: "))
            page = pdfReader.get_page(pg)
            text = page.extractText()
            speak(text)

        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'thanks' in command or 'thank' in command or 'thank u' in command:
            speak("You are welcome sir, I am always here to help you, Its my pleasure")
            print("You are welcome sir, I am always here to help you, Its my pleasure")
            speak("Do You need any help")
            yes_no = listen().lower()
            if "yes" in yes_no:
                print("How Can I help you?")
                speak("How Can I help you?")
                listen()
            else:
                exit()

        elif 'youtube' in command:
            open_website("https://www.youtube.com")

        elif 'google' in command:
            open_website("https://www.google.com")

        elif 'stack overflow' in command:
            open_website("https://stackoverflow.com")

        elif 'facebook' in command:
            open_website("https://www.facebook.com")

        elif 'play music' in command:
            music_dir = 'C:\\Users\\hp\\Music\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'funny' in command:
            speak("Hahaha! Glad You liked it")

        elif 'joke' in command:
            joke = get_joke()
            speak(joke)
            print(joke)

        elif 'quote' in command:
            quote = get_random_quote()
            print("Random Inspirational Quote:")
            speak("Random Inspirational Quote:")
            print(quote)
            speak(quote)

        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'currency' in command:
            currency_converter()

        elif 'health' in command:
            health_tips = get_health_tips()

            if isinstance(health_tips, list):
                for tip in health_tips:
                    speak(tip)
                    print(tip)
            else:
                speak("I am not professional health advisor visit doctor" + health_tips)
                print("I am not professional health advisor visit doctor" + health_tips)

        elif 'code' in command:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'scribble.io' in command:
            open_website("stackoverflow.com")

        elif 'email to divjot' in command:
            try:
                speak("What should I say?")
                content = listen()
                to = "aroradivjotsingh@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend divjot. I am not able to send this email")

        elif "instagram profile" in command or "profile on instagram" in command:
            speak("sir please enter the user name correctly.")
            name = input("Enter username here:")
            open_website(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            sleep(5)
            speak("sir would you like to download profile picture of this account.")
            condition = listen().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()  # pip install instadownloader
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder. now i am ready")

        elif "screenshot" in command or "take a screenshot" in command:
            speak("sir, please tell me the name for this screenshot file")
            name = listen().lower()
            speak("please sir hold the screen for few seconds, i am taking sreenshot")
            sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder")

        elif 'alarm' in command:
            nn = int(datetime.datetime.now().hour)
            if nn == 12:
                music_dir = 'C:\\Users\\hp\\Music\\Songs'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'snake game' in command:
            root = tk.Tk()
            game = SnakeGame(root)
            root.mainloop()

        elif 'whatsapp message' in command:
            speak("Please enter the number to whom you want to send the message")
            msg_num = listen().lower()
            speak("Please enter the message you want to send")
            msg = listen().lower()
            kit.sendwhatmsg("+91" + msg_num, msg, datetime.datetime.now().hour, datetime.datetime.now().minute + 3)

        elif 'play song on youtube' in command:
            speak("Please enter the song name")
            song = list().lower()
            kit.playonyt(song)

        elif 'game' in command:
            guess_number_game()

        elif 'on Google' in command:
            speak("sir what do you want to search on google")
            cm = listen().lower()
            open_website(f"{cm}")

        elif 'oh' or 'great' or 'yes' in command:
            speak("Haha! Congrats You won the game")

        elif 'temperature' in command:
            speak("Please Repeat the city name again")
            search = listen().lower()
            url = f"https://google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif 'how much power left' in command or 'battery' in command:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Hi sir Your laptop has {percentage} percent battery")

        elif 'ip address' in command:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")
            print(f"Your IP Address is {ip}")

        elif 'news' in command:
            news_headlines = get_news()
            print(news_headlines)

        elif 'internet speed' in command or 'net speed' in command:
            speak("sure please wait for 1-2 minutes")
            print("sure please wait for 1-2 minutes")
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Your Downloading Speed is {dl} bit per second and Your Upload speed is {up} bit per seconds")
            print(f"Your Downloading Speed is {dl} bit per second and Your Upload speed is {up} bit per seconds")

        # elif 'send sms' in query:
        #     speak("Please Enter the number where you want to send sms")
        #     msg_number = takeCommand().lower()
        #     speak("Please enter the message you want to send")
        #     msgg = takeCommand().lower()
        #     account_sid = 'AC1ca967fde5d2d1a88223eca5c5550904'
        #     auth_token = '3d7bfd456b3b093cf540c79e85dab07'
        #     client = Client(account_sid, auth_token)
        #
        #     message = client.messages \
        #         .create(
        #         body= msgg,
        #         from_='+12055494417',
        #         to='+91'+ msg_number
        #     )
        #
        #     print(message.sid)
        #
        # elif 'voice call' in query:
        #     speak("Please Enter the number whom you want to call")
        #     call_num = takeCommand().lower()
        #     msgg = takeCommand().lower()
        #     account_sid = 'AC1ca967fde5d2d1a88223eca5c5550904'
        #     auth_token = '3d7bfd456b3b093cf540c79e85dab07'
        #     client = Client(account_sid, auth_token)
        #
        #     message = client.messages \
        #         .create(
        #         twiml= '<Response><SayThis Is A Call From SOS AI </Say></Response>',
        #         from_='+12055494417',
        #         to='+91'+ call_num
        #     )
        #
        #     print(message.sid)

        elif 'volume up' in command:
            pyautogui.press("volumeup")

        elif 'who are you' in command:
            speak("Myself S O S A I ASSISTANT How may i help you")

        elif 'volume down' in command:
            pyautogui.press("volumedown")

        elif 'volume mute' in command:
            pyautogui.press("volumemute")

        elif 'Using Artificial Intelligence'.lower() in command.lower() or 'Using AI'.lower() in command.lower():
            ai(prompt=command)

        elif 'pdf' in command:
            pdf_reader()

        # elif 'super' or 'chat' in command:
        #     bardchat()

        elif 'app' in command:
            main()

        elif 'translate' in command:
            speak('What phrase would you like to translate?')
            phrase = listen()
            speak('To which language would you like to translate it?')
            target_language = listen().lower()
            translated_phrase = translator.translate(phrase, target_language)
            speak(f'Translation: {translated_phrase}')

        elif 'add task' in command:
            add_task()

        elif 'tasks' in command:
            get_tasks()

        elif 'weather' in command:
            speak("Can you repeat the city name please")
            print("Can you repeat the city name please")
            weather_info = get_weather(city=listen())
            print(weather_info)
            speak(weather_info)

        # elif 'website' in command:
        #     website_url = listen().lower()
        #     open_website("https://"+website_url)

        elif 'shutdown the system' in command:
            os.system("shutdown /s /t 5")

        elif 'stop' in command or 'end' in command or 'finish' in command:
            exit()

        # else:
        #     chat(command)

if __name__ == "__main__":
    # face_recognization()
    virtual_assistant()