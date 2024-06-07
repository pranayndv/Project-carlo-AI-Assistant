import os
import speech_recognition as sr 

def takeCommandMic():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-IN")
                print(query)
            except Exception as e:
                print(e)
                print("Say that again please...")
                return "None"
            return query

while True:
      
      wake_Up = takeCommandMic()
      if 'wake up' in wake_Up:
            os.startfile('D:\\Projects\\AI\\carloAI\\carlo.py')

      else:
            print("Nothing.....")


            # C:\Users\HP\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup