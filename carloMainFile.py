# GUI libraries
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import QThread
from carloMainGui import Ui_mainGUIfile

# add above library
import sys
# pip insall pyttsx3 ==text data into speech using python
import pyttsx3
import datetime
import speech_recognition as sr              # pip install Speech regognition
import smtplib
# from secrets import senderemail, epwd, to
from email.message import EmailMessage
from email import message
import pyautogui  # pip install pyautogui
import webbrowser as wb
import webbrowser as web
from time import sleep
import wikipedia  # pip install wikipedia
import pywhatkit  # pip install pywhatkit
import requests
# pip install newsapi  &  pip install newsapi-python
from newsapi import NewsApiClient
import clipboard  # pip  install clipboard
import os
import pyjokes
import time as tt
import psutil  # pip insatll psutil
import json
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread,
                          QThreadPool, pyqtSignal)
from PyQt5.QtGui import *  # pip install pyqt5
from PyQt5.QtWidgets import *  # pip install pyqt5-tools
from PyQt5.uic import loadUiType
# from carloui import Ui_MainWindow
from keyboard import press  # pip install keyboard
from keyboard import press_and_release
import openai  # pip install openai
from apikey import api_data
import serial


engine = pyttsx3.init()
engine.setProperty("rate", 190)


def speak(audio):
    ui.updateMoviesDynamically("speaking")
    engine.say(audio)
    engine.runAndWait()


Ser = serial.Serial('COM7', baudrate=9600)

now = datetime.datetime.now()
# dd/mm/YY H:M:S
date = now.strftime("%d %m %Y")

time = now.strftime("%H:%M:%S")

openai.api_key = api_data  # openai key

completion = openai.Completion()


def Reply(question):
    prompt = question
    response = completion.create(
        prompt=prompt, engine="text-davinci-002", stop=['\Chando'], max_tokens=100)
    answer = response.choices[0].text.strip()
    return answer


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good Evening")
    else:
        speak("Good Night")


def wishme():
    speak("welcome back sir !")
    # speak("today is date")
    # speak(date)
    # speak("now the current time is ")
    # speak(time)
    greeting()
    speak("carlo at Your service please tell how can i help you sir ?")


def takeCommandCMD(self):
    self.query = input("please tell me how can i help you ?\n")
    return self.query


def searchgoogle(self):
    speak('what should i search for?')
    google = self.takeCommandMic()
    wb.open('https://www.google.com/search?q='+google)


def news(self):
    newsapi = NewsApiClient(api_key='61c569a352404934a47c6e3d96159d0d')
    speak("What topic you need the news about?")
    topic = self.takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']

    for x, y in enumerate(newsdata):
        ui.terminalPrint(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))

        speak("Thats is for now ill update in some time")


def text2speech():
    text = clipboard.paste()
    ui.terminalPrint(text)
    speak(text)


def screenshot():
    name_img = tt.time()
    name_img = 'D:\\Projects\\AI\\sreenshots\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)
    speak("percent")


class carloMain(QThread):
    def __init__(self):
        super(carloMain, self).__init__()

    def run(self):
        self.runCarlo()

    def takeCommandMic(self):
        ui.updateMoviesDynamically("listening")

        r = sr.Recognizer()
        with sr.Microphone() as source:

            ui.terminalPrint("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            ui.terminalPrint("Recognizing...")
            self.query = r.recognize_google(audio, language="en-IN")
            ui.terminalPrint(self.query)
        except Exception as e:
            print(e)
            # speak("Say that again please...")
            return "None"
        return self.query

    def runCarlo(self):
        wishme()

        # # wakeword = "carlo"
        while True:

            self.query = self.takeCommandMic().lower()
            # query = word_tokenize(query)
            # ui.terminalPrint(query)
            # wishme()
            # if wakeword in query:
            if "date" in self.query:
                speak(date)

            elif 'hey carlo' in self.query or 'he kar lo' in self.query or 'a kar lo' in self.query or 'hi kar lo' in self.query:
                speak("how may i help you sir!")

            elif 'hay kar lo' in self.query or 'kar lo' in self.query or 'karlo' in self.query or 'hay kar lo' in self.query:
                speak("how may i help you sir!")

            elif 'hey ka rlo' in self.query:
                speak("how may i help you sir!")

            elif 'hey kar lo' in self.query:
                speak("how may i help you sir!")

            elif 'what are you doing' in self.query:
                speak("I am doing nothing sir.")

            elif 'how are you' in self.query:
                speak("i am fine ,what about you sir!")

            elif 'what is your name' in self.query or 'whats your name' in self.query:
                speak("hello! I am Carlo")

            elif 'thanks' in self.query or 'thank' in self.query:
                speak("Welcome sir!")

            elif 'who are you' in self.query:
                speak("i am carlo your persnol assistant")
            elif 'time' in self.query:
                speak(time)

            elif "whatsapp message" in self.query:
                speak("To who you want send ?")
                Name = self.takeCommandMic()
                speak(f"Whats the message for {Name}")
                MSG = self.takeCommandMic()
                from automations import WhatsappMsg
                WhatsappMsg(Name, MSG)

            elif "whatsapp call" in self.query:
                speak("To who you want to call?")
                Name = self.takeCommandMic()
                from automations import WhatsappCall
                WhatsappCall(Name)

            elif "whatsapp video call" in self.query:
                speak("To who you want to call?")
                Name = self.takeCommandMic()
                from automations import WhatsappvCall
                WhatsappvCall(Name)

            elif "search app" in self.query:
                speak("Which app to open you want ?")
                App = self.takeCommandMic()
                from autosytems import AutoSearchApp
                AutoSearchApp(App)

            elif "search settings" in self.query:
                speak("Which settings to open you want ?")
                Set = self.takeCommandMic()
                from autosytems import AutoSearchsettings
                AutoSearchsettings(Set)

            elif "wikipedia" in self.query:
                speak('searching on wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                self.result = wikipedia.summary(self.query, sentences=3)
                ui.terminalPrint(self.result)
                speak(self.result)

            elif "type here" in self.query:
                speak("okay start typing")
                Type = self.takeCommandMic()
                from automations import Autotype
                Autotype(Type)

            elif 'google' in self.query:
                speak('searching on google...')
                searchgoogle(self)

            elif 'new tab' in self.query:
                press_and_release('ctrl + t')

            elif 'close tab' in self.query:
                press_and_release('ctrl + w')

            elif 'new window' in self.query:
                press_and_release('ctrl + n')

            elif 'incognito' in self.query:

                press_and_release('Ctrl + Shift + n')

            elif 'switch tab' in self.query:
                tab = self.query.replace("switch tab ", "")
                Tab = tab.replace("to", "")
                num = Tab
                bb = f'ctrl + {num}'
                press_and_release(bb)

            elif 'close this window' in self.query:
                press_and_release('Alt + F4')

            elif 'search bar' in self.query:
                press_and_release('Ctrl + e')

            elif 'okay search' in self.query:
                press_and_release('enter')

            elif 'find here' in self.query:
                press_and_release('Ctrl + f')

            elif 'youtube' in self.query:
                speak("what should i search for on youtube?")
                topic = self.takeCommandMic()
                pywhatkit.playonyt(topic)

            elif 'pause' in self.query:

                press('space bar')

            elif 'resume' in self.query:

                press('space bar')

            elif 'full screen' in self.query:

                press('f')

            elif 'film screen' in self.query:

                press('t')

            elif 'skip' in self.query:

                press('l')

            elif 'back' in self.query:

                press('j')

            elif 'increase' in self.query:

                press_and_release('SHIFT + .')

            elif 'decrease' in self.query:

                press_and_release('SHIFT + ,')

            elif 'previous' in self.query:

                press_and_release('SHIFT + p')

            elif 'next' in self.query:

                press_and_release('SHIFT + n')

            elif 'mute' in self.query:

                press('m')

            elif 'unmute' in self.query:

                press('m')

            # elif 'weather' in self.query:
            #     url ='https://api.openweathermap.org/data/2.5/weather?q=oras&units=imperial&appid=d3db12fe162386b9cc1d240f20a84c57'
            #     res = requests.get(url)
            #     data = res.json()

                # weather = data ['weather'][0]['main']
                # temp = data['main']['temp']
                # desp = data ['weather'][0]['description']

                # temp = round((temp-32)*5/9)

                # ui.terminalPrint(weather)
                # ui.terminalPrint(temp)
                # ui.terminalPrint(desp)

                # speak('Temperature : {} degree celcius'.format(temp))
                # speak('The weather is {}'.format(desp))

            # elif "news" in self.query:
            #     news(self)

            elif 'read' in self.query:
                text2speech()

            elif 'my document' in self.query:
                os.system(
                    'explorer c://{}'.format(self.query.replace('Open', '')))

            elif 'open vs code' in self.query:
                codepath = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
                os.startfile(codepath)

            elif 'open ms word' in self.query:
                codepath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
                os.startfile(codepath)

            elif 'open excel' in self.query:
                codepath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
                os.startfile(codepath)

            elif 'open powerpoint' in self.query:
                codepath = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
                os.startfile(codepath)

            elif 'open spotify' in self.query:
                codepath = 'C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.209.743.0_x86__zpdnekdrzrea0\\Spotify.exe'
                os.startfile(codepath)

            elif 'search song' in self.query or 'search music' in self.query:
                speak("Which song you want to listen?")
                Music = self.takeCommandMic()
                from autosytems import Automusic
                Automusic(Music)

            elif 'open calculator' in self.query:
                codepath = 'C:\\Windows\\System32\\calc.exe'
                os.startfile(codepath)

            elif 'open notepad' in self.query:
                codepath = 'C:\\Windows\\System32\\notepad.exe'
                os.startfile(codepath)

            elif 'open chrome' in self.query:
                codepath = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
                os.startfile(codepath)

            elif 'open discord' in self.query:
                codepath = 'C:\\Users\\HP\\AppData\\Local\\Discord\\app-1.0.9007\\Discord.exe'
                os.startfile(codepath)

            elif 'open telegram' in self.query:
                codepath = 'C:\\Program Files\\WindowsApps\\TelegramMessengerLLP.TelegramDesktop_4.7.1.0_x64__t4vj0pshhgkwm\\Telegram.exe'
                os.startfile(codepath)

            elif 'open control panel' in self.query:
                codepath = 'C:\\Windows\\System32\\control.exe'
                os.startfile(codepath)

            elif 'open cmd' in self.query:
                codepath = 'C:\\Windows\\System32\\cmd.exe'
                os.startfile(codepath)

            elif 'open whatsapp' in self.query:
                codepath = 'C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
                os.startfile(codepath)

            elif 'joke' in self.query:
                speak(pyjokes.get_joke())

            elif 'screenshot' in self.query:
                speak("okay sir!")
                screenshot()

            elif 'remember that' in self.query:
                speak("What should i remember?")
                data = self.takeCommandMic()
                speak("you said me to remember that"+data)
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()

            elif 'do you know anything' in self.query:
                remember = open('data.txt', 'r')
                speak("you told me to remember that "+remember.read())

            elif 'cpu' in self.query:
                cpu()

            elif 'battery' in self.query:
                cpu()

            elif "offline" in self.query:
                speak("ok sir!")
                (self.close)
            elif "goodbye" in self.query:
                speak("ok sir!")
                (self.close)
            elif "good bye" in self.query:
                speak("ok sir!")
                (self.close)
            elif "quick settings" in self.query:
                from autosytems import QuickSet
                QuickSet()

            elif "minimise tab" in self.query or "minimise this tab" in self.query or "minimise window" in self.query:
                from autosytems import autominimise
                autominimise()

            elif "on wifi" in self.query or "turn on wifi" in self.query:
                from autosytems import wifiAuto
                wifiAuto()

            elif "on Wi-Fi" in self.query:
                speak("okay sir! turnning on Wi-Fi")
                from autosytems import wifiAuto
                wifiAuto()

            elif "turn off wifi" in self.query:
                speak("okay sir! turnning off Wi-Fi")
                from autosytems import wifiAuto
                wifiAuto()
            elif "turn off Wi-Fi" in self.query:
                speak("okay sir! turnning off Wi-Fi")
                from autosytems import wifiAuto
                wifiAuto()

            elif "on bluetooth" in self.query:
                speak("okay sir! turnning on bluetooth")
                from autosytems import bluetoothAuto
                bluetoothAuto()

            elif "off bluetooth" in self.query:
                speak("okay sir! turnning off bluetooth")
                from autosytems import bluetoothAuto
                bluetoothAuto()

            elif "shutdown pc" in self.query or "shutdown computer" in self.query:
                from autosytems import Autoshutdown
                Autoshutdown()

            elif "take picture" in self.query or "take photo" in self.query or "take a picture" in self.query or "take a photo" in self.query:
                speak("okay sir!")
                from autosytems import AutoCamera
                AutoCamera()

            elif "restart pc" in self.query or "restart computer" in self.query:
                from autosytems import Autorestart
                Autorestart()

            elif 'on light' in self.query or 'onlight' in self.query:
                speak("turning on light")
                Ser.write(b'N')
            elif 'off light' in self.query or 'offlight' in self.query:
                speak("turning off light")
                Ser.write(b'Y')
            elif 'on fan' in self.query:
                speak("turning on fan")
                Ser.write(b'O')
            elif 'off fan' in self.query:
                speak("turning off fan")
                Ser.write(b'F')

            elif 'on device 1' in self.query or 'on device one' in self.query:
                speak("turning on device one")
                Ser.write(b'N')
            elif 'off device 1' in self.query or 'off device one' in self.query:
                speak("turning off device one")
                Ser.write(b'Y')

            elif 'on device to' in self.query or 'on device two' in self.query or 'on device tu' in self.query:
                speak("turning on device two")
                Ser.write(b'O')
            elif 'off device to' in self.query or 'off device two' in self.query or 'on device tu' in self.query:
                speak("turning off device two")
                Ser.write(b'F')

            elif self.query:
                if len(self.query) > 20:
                    ans = Reply(self.query)
                    ui.terminalPrint(ans)
                    speak(ans)
                elif len(self.query) == 0:
                    speak("say something")


startExecution = carloMain()


class guiOfCarlo(QWidget):
    def __init__(self):
        super(guiOfCarlo, self).__init__()
        self.carloUI = Ui_mainGUIfile()
        self.carloUI.setupUi(self)
        self.runAllMovies()
        self.carloUI.pushButton.clicked.connect(self.taskExecution)
        self.carloUI.pushButton_2.clicked.connect(self.close)

    def taskExecution(self):
        startExecution.start()

    def runAllMovies(self):

        # self.carloUI.label_2 = QtGui.QMovie("./../../../../hp/idle.gif")
        self.carloUI.movie = QtGui.QMovie("idle.gif")
        self.carloUI.label_2.setMovie(self.carloUI.movie)
        self.carloUI.movie.start()

        self.carloUI.movie = QtGui.QMovie("speak.gif")
        self.carloUI.label.setMovie(self.carloUI.movie)
        self.carloUI.movie.start()

    def updateMoviesDynamically(self, state):
        if state == "listening":
            self.carloUI.label_2.raise_()
            self.carloUI.label.hide()
        #   self.carloUI.movie.start()
            self.carloUI.label_2.show()

        elif state == "speaking":
            self.carloUI.label.raise_()
            self.carloUI.label_2.hide()
        #   self.carloUI.movie.start()
            self.carloUI.label.show()

    def terminalPrint(self, text):

            self.carloUI.plainTextEdit.appendPlainText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = guiOfCarlo()
    ui.show()
    sys.exit(app.exec_())
