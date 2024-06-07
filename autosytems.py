from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
import os
from time import sleep

def QuickSet():  
    sleep(1) 
    click(x=1724, y=1071)
    
def wifiAuto():
    sleep(1) 
    click(x=1724, y=1071)
    sleep(1)
    click(x=1534, y=448)
    sleep(1) 
    click(x=1724, y=1071)

def bluetoothAuto():
    sleep(1) 
    click(x=1724, y=1071)
    sleep(1)
    click(x=1671, y=451)
    sleep(1) 
    click(x=1724, y=1071)

def AutoSearchApp(app):
    sleep(1) 
    click(x=712, y=1058)
    sleep(1)
    write(app)
    sleep(1)
    click(x=749, y=273)

def Autoshutdown():
    sleep(1)
    press_and_release('Win')
    sleep(1)
    click(x=1257, y=957)
    sleep(1)
    click(x=1234, y=864)
    click(x=1234, y=864)
    
def Autorestart():
    sleep(1)
    press_and_release('Win')
    sleep(1)
    click(x=1257, y=957)  
    sleep(1)
    click(x=1208, y=911)
    click(x=1208, y=911)

def AutoSearchsettings(set):
    sleep(1) 
    click(x=712, y=1058)
    sleep(1)
    write(set)
    sleep(1)
    click(x=749, y=273)

def AutoCamera():
    sleep(1) 
    click(x=712, y=1058)
    sleep(1)
    write('camera')
    sleep(1)
    click(x=749, y=273)
    sleep(0.5) 
    click(x=1861, y=527)
    click(x=1861, y=527)
    click(x=1861, y=527)
    
def autominimise():
    sleep(1)
    click(x=1777, y=13)

def Automusic(music):
    sleep(10)
    click(x=127, y=151)
    sleep(2)
    click(x=633, y=91)
    sleep(1)
    write(music)
    sleep(5)
    click(x=1042, y=302)
    click(x=1042, y=302)
    click(x=1042, y=302)

