from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import webbrowser as web


def WhatsappMsg(name,message):
    startfile("C:\\Users\\HP\\AppData\\Local\\WhatsApp\\app-2.2314.11\\WhatsApp.exe")

    sleep(25)  

    click(x=176, y=140)

    sleep(2)

    write(name)
     
    sleep(1)

    click(x=159, y=289)
    
    sleep(1)

    click(x=724, y=987)

    write(message)

    press('enter')

def WhatsappCall(name):
    startfile("C:\\Users\\HP\\AppData\\Local\\WhatsApp\\app-2.2314.11\\WhatsApp.exe")

    sleep(25)  


    click(x=176, y=140)

    sleep(2)

    write(name)
     
    sleep(1)

    click(x=159, y=289)
    
    sleep(1)
    
    click(x=1718, y=82)
    
def WhatsappvCall(name):
    startfile("C:\\Users\\HP\\AppData\\Local\\WhatsApp\\app-2.2314.11\\WhatsApp.exe")

    sleep(25)  


    click(x=176, y=140)

    sleep(2)

    write(name)
     
    sleep(1)

    click(x=159, y=289)
    
    sleep(1)
    
    click(x=1648, y=72)

def Autotype(sentence):
    write(sentence)

# def sendwhatsmsg(phone_no,message):
#             Message = message
#             wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+ Message )
#             sleep(25)
#             pyautogui.press('enter')
