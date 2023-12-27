import speech_recognition as sr
import subprocess

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

def virtual_assistant():
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()

        if "exit" in command:
            speak("Goodbye!")
            break

        # Add your custom commands and functionalities here
        elif "who are you" in command:
            speak("I am your virtual assistant.")
        elif "open browser" in command:
            speak("Opening the browser...")
            # Add code to open the browser here
        else:
            speak("I'm sorry, I don't understand that command. Can you please repeat?")

if __name__ == "__main__":
    virtual_assistant()
