import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday = pyttsx3.init()
voices = friday.getProperty('voices')
friday.setProperty('voice', voices[1].id)

def speak(audio):
    print("AI Nhà làm:" + audio)
    friday.say(audio)
    friday.runAndWait()

def get_time():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("Now it's " + Time)

def welcome():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 10:
        speak("Good morning, Boss")
    elif 10 <= hour < 13:
        speak("Good afternoon, Boss")
    elif 13 <= hour < 19:
        speak("Good evening, Boss")
    else:
        speak("Good night, Boss")
    

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 1
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='vn')
        print("Boss: " + query)
    except sr.UnknownValueError:
        print("Please repeat or type the command:")
        query = str(input("Your order is: "))
    return query

if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "open google" in query:
            speak("What should I search, boss?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here are your results for {search} on Google.")
        elif "open youtube" in query:
            speak("What should I search on YouTube, boss?")
            search = command().lower()
            url = f"https://www.youtube.com/results?search_query={search}"
            wb.get().open(url)
            speak(f"Here are your results for {search} on YouTube.")
        elif "music" in query:
            meme = r"D:\python\music.mp4"  # Sửa định dạng của hình ảnh thành "png"
            os.startfile(meme)
        elif "what time" in query:
            get_time()
        elif "hello" in query:
            speak("How can I help you?")
        elif "gril" in query:
            speak("Girls are strange and unpredictable creatures")
        elif "get out" in query:
            speak("AI is quitting, boss. Goodbye, boss.")
            quit()
