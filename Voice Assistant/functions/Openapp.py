import subprocess
import speech_recognition as sr

# Your existing functions and modules...

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

def open_app(app_name):
    try:
        subprocess.run(["open", "-a", app_name])
        print(f"Opening {app_name}...")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Open App Program")
    app_name = input("Enter the name of the application you want to open: ")
    open_app(app_name)

def virtual_assistant():
    # Your existing virtual assistant code...

    while True:
        command = listen()

        if 'open' in command:
            main()  # Call the open app program

        # Add other commands and functionalities as needed...

if __name__ == "__main__":
    virtual_assistant()
