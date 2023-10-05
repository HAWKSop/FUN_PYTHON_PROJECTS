import webbrowser
import pyautogui as pg

name = input("Enter username = ")
pasw = input("ENter password = ")

webbrowser.open("https://www.instagram.com", new = 2)

def login(name, pasw):
        pg.click('Phone number, username, or email')
        pg.write(name)
        pg.click('Password')
        pg.write(pasw)
