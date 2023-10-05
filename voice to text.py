
import speech_recognition as sr

voice = sr.Recognizer()
with sr.Microphone() as source :
    print("how can i help you")
    audio = voice.record(source, duration= 5)
    Text = voice.recognize_google(audio,language="en")
    print(Text)
