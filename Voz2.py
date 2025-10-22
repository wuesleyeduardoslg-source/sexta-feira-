import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def falar(texto):
    engine.say(texto)
    engine.runAndWait()
