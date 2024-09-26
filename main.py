import datetime
import os
import random
import smtplib
import subprocess
import time
import tkinter as tk
import webbrowser
from contextvars import Token
from math import sqrt
from time import sleep
from tkinter import messagebox
from tkinter import ttk, filedialog, scrolledtext
import PyPDF2
import cv2
import geocoder
from gtts import gTTS
import os
# from test import numbe
import folium
import google.generativeai as genai
import mediapipe as mp
import notification
import openai as openai
import phonenumbers
import psutil
import pyautogui
import pywhatkit
import pywhatkit as kit
import requests
import speech_recognition as sr  # pip install speechRecognition
import speedtest
import wikipedia
import wikipedia as googleScrap
from bs4 import BeautifulSoup
from instaloader import instaloader
from plyer import notification  # pip install plyer
from pygments.lexers import PythonLexer
from pygments.token import Token
from requests import get
from ttkthemes import ThemedStyle
from word2number import w2n
from config import api_key

# todo: Main Code Starts here:

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voice', voices[0].id)
recognizer = sr.Recognizer()

def tracker():

    Key = "6d6f969fd9024ac8afde957f0c86a5ba"

    number = input("Enter phone number with country code:")
    check_number = phonenumbers.parse(number)
    number_location = geocoder.description_for_number(check_number, "en")
    print(number_location)

    from phonenumbers import carrier
    service_provider = phonenumbers.parse(number)
    print(carrier.name_for_number(service_provider, "en"))

    from opencage.geocoder import OpenCageGeocode
    geocoder = OpenCageGeocode(Key)

    query = str(number_location)
    results = geocoder.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(lat, lng)

    map_location = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=number_location).add_to(map_location)
    map_location.save("mylocation.html")

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


def virtual_mouse():
    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    index_y = 0
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        index_x = screen_width / frame_width * x
                        index_y = screen_height / frame_height * y

                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width / frame_width * x
                        thumb_y = screen_height / frame_height * y
                        print('outside', abs(index_y - thumb_y))
                        if abs(index_y - thumb_y) < 20:
                            pyautogui.click()
                            pyautogui.sleep(1)
                        elif abs(index_y - thumb_y) < 100:
                            pyautogui.moveTo(index_x, index_y)
        cv2.imshow('Virtual Mouse', frame)
        cv2.waitKey(1)

def open_app(app_name):
    try:
        subprocess.run(["open", "-a", app_name])
        print(f"Opening {app_name}...")
    except Exception as e:
        print(f"An error occurred: {e}")

def debug_code(code):
    try:
        # Create a dictionary for the local and global variables
        local_vars = {}
        global_vars = {}

        # Execute the code
        exec(code, global_vars, local_vars)

        # Return the result
        result = f"Execution Result: {local_vars}"
    except Exception as e:
        # If an error occurs during execution, return the error message
        result = f"Error: {str(e)}"

    return result

# def get_random_quote():
#     # API endpoint for fetching a random quote
#     api_url = "https://api.quotable.io/random"
#
#     try:
#         # Make a GET request to the API
#         response = requests.get(api_url)
#
#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Parse the JSON response
#             quote_data = response.json()
#
#             # Extract the quote and author
#             quote = quote_data.get("content")
#             author = quote_data.get("author")
#
#             # Print the quote
#             print(f'"{quote}" - {author}')
#         else:
#             print(f"Failed to fetch a random quote. Status Code: {response.status_code}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

def main():
    print("Please Repeat the name of application")
    speak("Please Repeat the name of application")
    app_name = listen().lower()
    open_app(app_name)

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry("500x500")

        self.canvas = tk.Canvas(self.master, bg="black", width=400, height=360)
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

        self.pause_button = tk.Button(self.master, text="Pause/Resume", command=self.toggle_pause)
        self.pause_button.pack()

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.pack()

        self.reset_button = tk.Button(self.master, text="Reset High Score", command=self.reset_high_score)
        self.reset_button.pack()

        self.master.bind("<Key>", self.change_direction)

        self.update()

    def reset_high_score(self):
        response = messagebox.askyesno("Reset High Score",
                                       "Are you sure you want to reset the high score? This action cannot be undone.")
        if response:
            self.set_high_score(0)
            self.update_score()
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
        self.direction = "Right"
        self.score = 0
        self.is_paused = False
        self.start_time = time.time()

        # Clear the canvas
        self.canvas.delete("all")

        # Recreate the background rectangle
        self.canvas.create_rectangle(0, 0, 400, 400, outline="white")

        # Recreate the score label
        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", fg="white", bg="black")
        self.score_label.pack()

        # Update the high score label
        high_score = self.get_high_score()
        self.high_score_label.config(text=f"High Score: {high_score}")

        # Recreate the food object
        self.food = self.create_food()

        # Check if the snake is not empty before accessing its coordinates
        if self.snake:
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

    def reset_high_score(self):
        response = messagebox.askyesno("Reset High Score", "Are you sure you want to reset the high score?")
        if response:
            self.set_high_score(0)
            self.update_score()
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

def search_google(query):
    google_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(google_url)

def search_youtube(query):
    youtube_url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(youtube_url)

class ModernCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Modern Calculator")

        # Apply a themed style
        style = ThemedStyle(self.master)
        style.set_theme("plastik")

        # Entry widget
        self.entry = ttk.Entry(self.master, font=('Arial', 16), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('(', 3, 4),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3), (')', 4, 4),
        ]

        for (text, row, col) in buttons:
            btn = ttk.Button(self.master, text=text, style="TButton", command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)

        # Configure row and column weights so that they expand proportionally
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

        # Memory
        self.memory = None

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == 'C':
            self.entry.delete(0, tk.END)
        elif text == 'sqrt':
            value = float(self.entry.get())
            result = sqrt(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + str(text))

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

def Quiz():
        questions = {
            "What is the capital of France?": "paris",
            "Who wrote 'Romeo and Juliet'?": "shakespeare",
            "What is the largest mammal on Earth?": "blue whale",
            "What country has the highest life expectancy?": "hong kong",
            "Where would you be if you were standing on the Spanish Steps?": "rome",
            "Which language has more native speakers: English or Spanish?": "spanish",
            "What is the most common surname in the United States?": "smith",
            "What disease commonly spread on pirate ships?": "scurvy",
            "Who was the Ancient Greek God of the Sun?": "apollo",
            "What was the name of the crime boss who was head of the feared Chicago Outfit?": "al capone",
            "What year was the United Nations established?": "1945",
            "Who has won the most total Academy Awards?": "walt disney",
            "What artist has the most streams on Spotify?": "drake",
            "How many minutes are in a full week?": "10,080",
            "What car manufacturer had the highest revenue in 2020?": "volkswagen",
            "How many elements are in the periodic table?": "118",
            "What company was originally called 'Cadabra'?": "amazon",
            "How many faces does a Dodecahedron have?": "12",
            "Queen guitarist Brian May is also an expert in what scientific field?": "astrophysics",
            "Aureolin is a shade of what color?": "yellow",
            "How many ghosts chase Pac-Man at the start of each game?": "4",
            "What Renaissance artist is buried in Rome's Pantheon?": "raphael",
            "What shoe brand makes the 'Mexico 66'?": "onitsuka tiger",
            "What game studio makes the Red Dead Redemption series?": "rockstar games",
            "Who was the last Tsar of Russia?": "nicholas ii",
            "What character have both Robert Downey Jr. and Benedict Cumberbatch played?": "sherlock holmes",
            "What country drinks the most coffee per capita?": "finland",
            "Which planet in the Milky Way is the hottest?": "venus",
            "What is the 4th letter of the Greek alphabet?": "delta",
            "What sports car company manufactures the 911?": "porsche",
            "What city is known as 'The Eternal City'?": "rome",
            "Roald Amundsen was the first man to reach the South Pole, but where was he from?": "norway",
            "What is the highest-rated film on IMDb as of January 1st, 2022?": "the shawshank redemption",
            "Who discovered that the earth revolves around the sun?": "nicolaus copernicus",
            "What company was initially known as 'Blue Ribbon Sports'?": "nike",
            "What art form is described as 'decorative handwriting or handwritten lettering'?": "calligraphy",
            "Which planet has the most moons?": "saturn",
            "What country has won the most World Cups?": "brazil",
            "Complete the following lyrics - 'I should have changed that stupid lock.....'": "i should have made you leave your key",
            "Kratos is the main character of what video game series?": "god of war",
            "In what country would you find Mount Kilimanjaro?": "tanzania",
            "What is a group of pandas known as?": "an embarrassment",
            "What European country experienced the highest rate of population decline from 2015 - 2020?": "lithuania",
            "How many bones do we have in an ear?": "3",
            "Who famously crossed the Alps with elephants on the way to war with the Romans?": "hannibal",
            "True or False: Halloween originated as an ancient Irish festival.": "true",
            "What Netflix show had the most streaming views in 2021?": "squid game",
            "Which Grammy-nominated New York rapper died in April of 2021?": "dmx",
            "What software company is headquartered in Redmond, Washington?": "microsoft",
            "What is the largest Spanish-speaking city in the world?": "mexico city",
            "What is the world's fastest bird?": "the peregrine falcon",
            "In what country is the Chernobyl nuclear plant located?": "ukraine",
            "The Parthenon Marbles are controversially located in what museum?": "the british museum",
            # ... add more questions here
        }

        score = 0

        for question, correct_answer in questions.items():
            speak(question)
            user_answer = listen()

            if user_answer is not None and user_answer == correct_answer:
                speak("Correct!")
                score += 1
            elif user_answer == "quit":
                speak("Quitting the quiz. Your final score is {} out of {}.".format(score, len(questions)))
                break
            else:
                speak(f"Wrong! The correct answer is {correct_answer}.")

        speak(f"You scored {score} out of {len(questions)}.")


def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        quote_data = response.json()
        return f'"{quote_data["content"]}" - {quote_data["author"]}'
    else:
        return "Failed to fetch a quote."

def play_song(category):
    songs = {
        "pop": "https://www.youtube.com/watch?v=3tmd-ClpJxA",  # Example song link
        "rock": "https://www.youtube.com/watch?v=3tmd-ClpJxA",  # Replace with actual links
        "hip hop": "https://www.youtube.com/watch?v=3tmd-ClpJxA",
        # Add more categories and songs here
    }

    category_lower = category.lower()

    if category_lower in songs:
        song_url = songs[category_lower]
        speak(f"Playing a {category_lower} song.")
        webbrowser.open(song_url)
        speak("Enjoy The music")
        exit()
    else:
        speak(f"Sorry, I don't have songs for the {category_lower} category.")

def rock_stone_paper_scissor_game():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while (i < 5):
        speak('choose = ("rock", "paper", "scissors")')
        choose = ("rock", "paper", "scissors")  # Tuple
        com_choose = random.choice(choose)
        query = listen().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper"):
            if (com_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score + 1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1

    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")

def guess_number_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")

    while True:
        try:
            # Get user input for the guess
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            # Compare the guess with the target number
            if guess < target_number:
                print("low! Try again.")
            elif guess > target_number:
                print("high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
                break

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
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")

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


class CodeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Feature-Rich IDE")

        # Menu Bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New File", command=self.new_file)
        self.file_menu.add_command(label="Open File", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)

        # Edit Menu (Add more features as needed)

        # Code Editor
        self.code_editor = scrolledtext.ScrolledText(self.root, wrap="word", undo=True)
        self.code_editor.pack(expand="yes", fill="both")

        # Button Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=5)

        # Run Button
        self.run_button = ttk.Button(button_frame, text="Run", command=self.run_code)
        self.run_button.pack(side="left", padx=5)

        # Save Button
        self.save_button = ttk.Button(button_frame, text="Save", command=self.save_file)
        self.save_button.pack(side="left", padx=5)

        # Open Button
        self.open_button = ttk.Button(button_frame, text="Open File", command=self.open_file)
        self.open_button.pack(side="left", padx=5)

        # Syntax Highlighting Tags
        self.code_editor.tag_configure("keyword", foreground="blue")
        self.code_editor.tag_configure("string", foreground="orange")
        self.code_editor.tag_configure("comment", foreground="gray")

        # Binding for Syntax Highlighting
        self.code_editor.bind("<KeyRelease>", self.update_syntax_highlighting)

        # Autocompletion
        self.autocomplete_list = ["if", "else", "while", "for", "def", "class", "import", "from", "True", "False", "None"]
        self.autocomplete_popup = AutocompletePopup(self.root, self.code_editor, self.autocomplete_list)

        # Variable to store the last cursor position
        self.last_cursor_position = "1.0"

        # Auto-save interval in milliseconds (adjust as needed)
        self.auto_save_interval = 60000  # 1 minute

        # Schedule auto-save
        self.root.after(self.auto_save_interval, self.auto_save)

    def new_file(self):
        self.code_editor.delete(1.0, tk.END)
        self.root.title("Feature-Rich IDE - Untitled")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".py",
                                                filetypes=[("Python files", "*.py"), ("All files", "*.*")])
        if file_path:
            self.code_editor.delete(1.0, tk.END)
            with open(file_path, "r") as file:
                self.code_editor.insert(tk.END, file.read())
            self.root.title(f"Feature-Rich IDE - {file_path}")

    def save_file(self):
        # Save existing file
        if hasattr(self, 'current_file'):
            with open(self.current_file, "w") as file:
                file.write(self.code_editor.get(1.0, tk.END))
        # If it's a new file, ask for a file name
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".py",
                                                  filetypes=[("Python files", "*.py"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.code_editor.get(1.0, tk.END))
            self.current_file = file_path
            self.root.title(f"Feature-Rich IDE - {file_path}")

    def run_code(self):
        # Clear previous output
        self.clear_output()

        code = self.code_editor.get(1.0, tk.END)
        try:
            result = subprocess.run(["python3", "-c", code], capture_output=True, text=True, timeout=5)
            self.display_output(result)
        except subprocess.TimeoutExpired:
            self.code_editor.insert(tk.END, "\nError: Execution timed out.", "comment")
        except subprocess.CalledProcessError as e:
            self.code_editor.insert(tk.END, f"\nError: {e}", "comment")

    def display_output(self, result):
        # Output tab
        output_frame = ttk.Frame(self.root)
        output_frame.pack(side="bottom", fill="both", expand=True)

        # Add a scrolled text widget (output) to the Output tab
        output_widget = scrolledtext.ScrolledText(output_frame, wrap="word", undo=True)
        output_widget.pack(expand="yes", fill="both")

        # Highlight stdout and stderr
        for line in result.stdout.splitlines():
            output_widget.insert(tk.END, line + "\n", "comment")

        for line in result.stderr.splitlines():
            output_widget.insert(tk.END, line + "\n", "comment")

        # Scroll to the end
        output_widget.yview(tk.END)

        self.root.update()

    def clear_output(self):
        # Clear previous output
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Frame) and widget != self.code_editor:  # Exclude the code editor from destruction
                widget.destroy()

    def update_syntax_highlighting(self, event=None):
        code = self.code_editor.get(1.0, tk.END)
        self.code_editor.tag_remove("keyword", 1.0, tk.END)
        self.code_editor.tag_remove("string", 1.0, tk.END)
        self.code_editor.tag_remove("comment", 1.0, tk.END)

        for tag, start, end in self.syntax_highlighting(code):
            self.code_editor.tag_add(tag, start, end)

        # Autocompletion
        self.autocomplete_popup.update()

        # Remember the current cursor position
        self.last_cursor_position = self.code_editor.index(tk.CURRENT)

    def syntax_highlighting(self, code):
        lexer = PythonLexer()
        for token, value in lexer.get_tokens(code):
            start = f"1.{value[0]}"
            end = f"1.{value[1]}"
            if token in Token.Keyword:
                yield "keyword", start, end
            elif token in Token.String:
                yield "string", start, end
            elif token in Token.Comment:
                yield "comment", start, end

        # Restore the cursor position
        self.code_editor.mark_set(tk.CURRENT, self.last_cursor_position)

    def auto_save(self):
        # Auto-save the code
        if hasattr(self, 'current_file'):
            with open(self.current_file, "w") as file:
                file.write(self.code_editor.get(1.0, tk.END))

        # Schedule the next auto-save
        self.root.after(self.auto_save_interval, self.auto_save)


class AutocompletePopup:
    def __init__(self, root, text_widget, autocomplete_list):
        self.root = root
        self.text_widget = text_widget
        self.autocomplete_list = autocomplete_list

        self.popup_menu = tk.Menu(self.root, tearoff=0)

        # Bind to the text widget
        self.text_widget.bind("<KeyRelease>", self.show_popup)
        self.text_widget.bind("<Return>", self.insert_selected)

    def show_popup(self, event):
        # Get the current word
        current_word = self.get_current_word()

        # Remove previous menu items
        self.popup_menu.delete(0, tk.END)

        if current_word:
            # Filter autocomplete list based on the current word
            matches = [word for word in self.autocomplete_list if word.startswith(current_word)]
            if matches:
                for match in matches:
                    self.popup_menu.add_command(label=match, command=lambda m=match: self.insert_completion(m))

                # Display the popup menu below the current word
                x, y, _, _ = self.text_widget.bbox(tk.SEL_FIRST)
                x += self.text_widget.winfo_rootx() + 2
                y += self.text_widget.winfo_rooty() + self.text_widget.winfo_height() + 2
                self.popup_menu.post(int(x), int(y))

    def get_current_word(self):
        cursor_index = self.text_widget.index(tk.INSERT)
        line, col = map(int, cursor_index.split("."))
        line_text = self.text_widget.get(f"{line}.0", f"{line}.end")
        current_word = ""

        for char in reversed(line_text[:col]):
            if char.isalpha() or char.isdigit() or char == "_":
                current_word = char + current_word
            else:
                break

        return current_word

    def insert_completion(self, word):
        current_word = self.get_current_word()

        # Delete the current word
        self.text_widget.delete(tk.SEL_FIRST, tk.INSERT)

        # Insert the selected word
        self.text_widget.insert(tk.INSERT, word)

    def insert_selected(self, event):
        # Insert the selected word when Enter key is pressed
        selected_index = self.popup_menu.index(tk.ACTIVE)
        selected_word = self.popup_menu.entrycget(selected_index, "label")
        self.insert_completion(selected_word)

        # Close the popup menu
        self.popup_menu.delete(0, tk.END)

    def update(self):
        # Update the autocomplete popup based on the current word
        self.show_popup(None)


def face_recognization():
    def setup_camera():
        cam = cv2.VideoCapture(1)
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
    api_key = 'enter your'
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
    base_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(base_url)
    data = response.json()

    if data['status'] == 'ok':
        articles = data['articles']
        headlines = [article['title'] for article in articles]
        return '\n'.join(headlines)
    else:
        return 'Unable to fetch news'

#//////////////////////////////////////////////////////////////////////////////
def gemini(query):
    genai.configure(api_key="AIzaSyAl0DXSVxsJmO2kZC74aa4uK2COHmFJMsc")
    query = query.lower()
    # Set up the model
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    prompt_parts = [ str(listen())
                     ]

    response = model.generate_content(prompt_parts)
    speak(response.text)
    print(response.text)
    # ////////////////////////////////////////////////////////////////////////
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

def IPL_SCORE():
    url = "https://www.cricbuzz.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
    team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
    team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
    team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

    a = print(f"{team1} : {team1_score}")
    b = print(f"{team2} : {team2_score}")

    notification.notify(
        title="IPL SCORE :- ",
        message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
        timeout=15
    )

def greet_me():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am S.O.S.A.I Assistant Sir. Please tell me how may I help you")

def virtual_assistant():

    while True:
        command = listen()

        def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('', '')
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

        # elif 'thanks' in command or 'thank' in command or 'thank u' in command:
        #     speak("You are welcome sir, I am always here to help you, Its my pleasure")
        #     print("You are welcome sir, I am always here to help you, Its my pleasure")
        #     speak("Do You need any help")
            # yes_no = listen().lower()
            # if "yes" in yes_no:
            #     print("How Can I help you?")
            #     speak("How Can I help you?")
            #     listen()
            # else:
            #     speak("okay sir bye see you again")
            #     print("okay sir bye see you again")
            #     exit()

        elif 'open youtube' in command:
            open_website("https://www.youtube.com")

        elif 'open google' in command:
            open_website("https://google.com/")

        elif 'stack overflow' in command:
            open_website("https://stackoverflow.com")

        elif 'facebook' in command:
            open_website("https://www.facebook.com")

        elif 'music' in command:
            speak("Welcome! Choose a category to play a song. Categories include pop, rock, hip hop, etc.")
            chosen_category = input("Enter a category: ")
            play_song(chosen_category)

        elif 'funny' in command:
            speak("Hahaha! Glad You liked it")

        elif 'joke' in command:
            joke = get_joke()
            speak(joke)
            print(joke)

        # elif 'quote' in command:
        #     quote = get_random_quote()
        #     print("Random Inspirational Quote:")
        #     speak("Random Inspirational Quote:")
        #     print(quote)
        #     speak(quote)

        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'currency' in command:
            currency_converter()

        # elif 'health' in command:
        #     health_tips = get_health_tips()
        #
        #     if isinstance(health_tips, list):
        #         for tip in health_tips:
        #             speak(tip)
        #             print(tip)
        #     else:
        #         speak("I am not professional health advisor visit doctor" + health_tips)
        #         print("I am not professional health advisor visit doctor" + health_tips)

        elif 'code' in command:
            from code import code
            code_to_debug = code()

            debug_result = debug_code(code_to_debug)
            print(debug_result)

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

        elif 'number' in command:
            guess_number_game()

        elif 'quiz' in command:
            Quiz()

        elif 'on Google' in command:
            command = command.replace("SOS AI", "")
            command = command.replace("google search", "")
            command = command.replace("google", "")
            speak("This is what I found on google")

            try:
                pywhatkit.search(command)
                result = googleScrap.summary(command, 1)
                speak(result)

            except:
                speak("No speakable output available")

        # elif 'oh' or 'great' or 'yes' in command:
        #     speak("Haha! Congrats You won the game")

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
            speak(news_headlines)
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

        elif 'mouse' in command:
            virtual_mouse()

        elif 'pointer' in command:
            virtual_mouse()

        elif 'volume up' in command:
            pyautogui.press("volumeup")

        # elif 'are you' in command:
        #     speak("Myself S.O.S.A I ASSISTANT How may i help you")

        elif 'volume down' in command:
            pyautogui.press("volumedown")

        elif 'volume mute' in command:
            pyautogui.press("volumemute")

        elif 'Using Artificial Intelligence'.lower() in command.lower() or 'Using AI'.lower() in command.lower():
            ai(prompt=command)

        elif 'pdf' in command:
            pdf_reader()

        elif 'game' in command:
            rock_stone_paper_scissor_game()

        elif 'search on youtube' in command:
            speak("Can you repeat? What do you want to search on youutube")
            search_query = listen()
            search_youtube(search_query)

        elif 'calculator' in command:
            root = tk.Tk()
            calculator = ModernCalculator(root)
            root.mainloop()

        elif 'search on google' in command:
            speak("Can you repeat? What do you want to search on google")
            search_query = listen()
            search_google(search_query)

        # elif 'super' or 'chat' in command:
        #     bardchat()

        elif 'app' in command:
            main()

        # elif 'translate' in command:
        #     translategl()

        elif 'voice to text' in command:
            speak("Okay Can you speak what do you want to convert")
            speech = listen()
            speak(speech)


        elif 'add task' in command:
            add_task()

        elif 'ide' in command:
            root = tk.Tk()
            root.geometry("800x600")  # Set initial window size
            code_editor = CodeEditor(root)
            root.mainloop()

        elif 'tasks' in command:
            get_tasks()

        elif 'track' in command:
            tracker()

        elif 'weather' in command:
            speak("Can you repeat the city name please")
            print("Can you repeat the city name please")
            weather_info = get_weather(city=listen())
            print(weather_info)
            speak(weather_info)

        elif "click my photo" in command:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(2)
            speak("SMILE")
            pyautogui.press("enter")

        elif 'advance' in command:
            gemini()

        # elif 'quote' in command:
        #     get_random_quote()

        elif 'ipl' in command:
            IPL_SCORE()

        # elif 'website' in command:
        #     website_url = listen().lower()
        #     open_website("https://"+website_url)

        elif 'shutdown the system' in command:
            os.system("shutdown /s /t 5")

        elif 'stop' in command or 'end' in command or 'finish' in command:
            exit()

        else:
            gemini(command)

if __name__ == "__main__":
    # face_recognization()
    # greet_me()
    virtual_assistant()