
from gtts import gTTS
import os

name =input("Enter your name = ")

a = "hello" + name + "how can i help you"

#a = input("Enter your sentences =")
b = "en"

c = gTTS(text=a,lang=b)
c.save("new.mp3")

os.system("start new.mp3")



#this programm is orginally belongs to Ayush Ranjan bauri