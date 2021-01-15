import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import re

class Reno:
    def __init__(self):
        self.engine = pyttsx3.init()

        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            self.say("RENO sequence activated, Good Morning Sir")
            print("RENO sequence activated, Good Morning, Sir")
        elif hour >= 12 and hour < 18:
            self.say("RENO sequence activated, Good Afternoon Sir")
            print("RENO sequence activated, Good Afternoon, Sir")
        else:
            self.say("RENO sequence activated, Good Evening Sir")
            print("RENO sequence activated, Good Evening, Sir")

    def say(self, statement):
        self.engine.say(statement)
        self.engine.runAndWait()

    def initial(self):
        self.say("How can I help you?")
        print("How can I help you?")
    
    def goodbye(self):
        self.say('See you later Sir.')
        print('See you later, Sir.')

    def openApp(self, command):
        command = command.replace("open", "")

        if 'youtube' in command:
            webbrowser.open_new_tab("https://www.youtube.com")
            self.say("YouTube is open now")
            time.sleep(5)

        elif 'google' in command:
            webbrowser.open_new_tab("https://www.google.com")
            self.say("Google Chrome is open now")
            time.sleep(5)

        elif 'gmail' in command:
            webbrowser.open_new_tab("https://www.gmail.com")
            self.say("G-Mail is open now")
            time.sleep(5)

    def wikipedia(self, command):
        command = command.replace("wikipedia", "")
        self.say('Searching in  Wikipedia for' + command + '...')
        results = wikipedia.summary(command, sentences=3)
        results = re.sub(r'\([^()]*\)', '', results)
        self.say("According to Wikipedia, ")
        print(results)
        self.say(results)

    def getTime(self):
        hour = datetime.datetime.now().hour

        if hour >= 0 and hour < 12: meridiem = "am"
        else: meridiem = "pm"

        hour = hour % 12
        minute = datetime.datetime.now().minute
        strTime = str(f"{hour}:{minute} {meridiem}")
        self.say(f"It is {strTime}")
        print(f"It is {strTime}")