import subprocess
import speech_recognition as sr

# ...

def open_website(url):
    try:
        subprocess.run(["open", url])
        print(f"Opening {url}...")
    except Exception as e:
        print(f"An error occurred: {e}")

# ...
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



def virtual_assistant():
    # ...

    while True:
        command = listen()

        if 'youtube' in command:
            open_website("https://www.youtube.com")

        elif 'google' in command:
            open_website("https://www.google.com")

        elif 'stack overflow' in command:
            open_website("https://stackoverflow.com")

        elif 'facebook' in command:
            open_website("https://www.facebook.com")

if __name__ == "__main__":
    virtual_assistant()

