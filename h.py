import webbrowser
import pyautogui as pg

import time
name = input("Enter username = ")
pasw = input("ENter password = ")

webbrowser.open("https://www.instagram.com", new = 2)

def login(name, pasw):
    time.sleep(2)
    pg.press('tab')
    pg.write(name)
    pg.press('tab')
    pg.write(pasw)
    pg.press('enter')
login(name,pasw)
