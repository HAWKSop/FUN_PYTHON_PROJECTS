import os
import webbrowser
import pyautogui as pg
import time
from gtts import gTTS
import speech_recognition as sr


t = 1                       #use for looping


voice = sr.Recognizer()     #voice recoginiser
s = "en"                    #lang that is going to use in conversion and voice


#speech recognition
#vtt means voice to text
def vtt (b): 
    with sr.Microphone() as source :
        
        audio = voice.record(source, duration= 5)
        Text = voice.recognize_google(audio,language="en")
        print(Text) 
    return Text

#voice provider
# ttv means text to voice

def ttv(x):
    s = "en"                    #lang that is going to use in conversion and voice
    c = gTTS(text=x,lang=s)
    c.save("new.mp3")

    os.system("start new.mp3")


#main programm
a=None



t="Can i know your name "
ttv(t)
name1 = vtt(a)
b = None

t1= "hello" + name1 + "how can i help you"
ttv(t1)


name = str("wtxhawks")
pasw = str("wtf123")



def login(name, pasw):
    time.sleep(3)
    pg.press('tab')
    pg.write(name)
    pg.press('tab')
    pg.write(pasw)
    pg.press('enter')
    time.sleep(5)
    pg.press('tab')
    pg.press('tab')
    pg.press('enter')


c= str(vtt(b))
if c == ("open insta"):


    webbrowser.open("https://www.instagram.com", new = 2)
    login(name,pasw)

'''while t==1:
    
   
   
    if start1 == "y" or "Y":
        m="I am fine what about you"
        vtt(b)
        
        print(b)
        
        n="i am also fine how's your day going"
        ttv(n)

   


    elif start1 == "n" or "N":
        print ("exiting.....")
        t=2
    
    
    else:
        print("wrong input\n exiting...  in 2sec")
        time.sleep(2)
        t=2'''
     
    