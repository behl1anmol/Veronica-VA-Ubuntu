import speech_recognition
from gtts import gTTS
from subprocess import getoutput

# Microphone Input Part
recognizer = speech_recognition.Recognizer()


def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,0.5)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        return "didn't get you"
    except speech_recognition.RequestError as e:
        return "Connection problem"


# Voice Output Function
def speak(text):
    try:
        path = '/home/anmol/VA/speeches/nancy.mp3'
        tts = gTTS(text, lang="hi")
        tts.save(path)
        getoutput("mpg123 " + path)
    except Exception as ex:
        print(ex)
