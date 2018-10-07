


#!/usr/bin/python3
import notify2, nautilus, sys
import tkinter as tk
#from notification import veronica_notify
#from re import match,search
from os import chdir
from saavn import open_saavn
from random import choice
from wolfwiki import search
import random
from settings import LOG_DIR, LOGO_PATH, veronica_notify
from datetime import datetime
from meaning import getMeaning
from browse import get_address
from youtube import url_Open
from search import get_result
from lyrics import lyrics_down
from AudioIO import speak, listen
from youtubemp3 import youtube_mp3
from youtubemp4 import youtube_mp4
from defaultsearch import get_result_google
#from subprocess import getoutput


def update_log(text):   # Updating Microphone Log
    chdir('/home/anmol/VA/Documents/VLOG')
    with open('microphone_log.txt', 'a') as f:
        f.write(str(datetime.utcnow()) + " " + text + '\n')


class StopApp(tk.Tk):   # Pause Nancy code
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Nancy Stopped")
        self.button = tk.Button(self, text="Start Nancy", bg="#09C889", fg="white", command=self.on_button)
        self.button.pack()

    def on_button(self):
        self.destroy()





def main(text):

    update_log(text)

    if text in ["who are you", "introduce yourself"]:
        intro='I am Veronica, your personal assistant.'
        speak(intro)
        veronica_notify(intro)
        return

    elif "describe yourself" in text:
        intro="I am Veronica, your personal assistant. I use python's speech recognition module to understand voice input, and google's text to speech technology to give output."
        speak(intro)
        veronica_notify(intro)

        return

    elif "toss a coin" in text:
        coin=random.randint(1,2)
        if coin==1:
            speak('It is tails')
            veronica_notify('It is tails')
        elif coin==2:
            speak('It is heads')
            veronica_notify('It is heads')
        return

    elif text in ["throw a dice", "throw a die"]:
        dice=str(random.randint(1,6))
        speak(dice)
        veronica_notify(dice)
        return

    elif text == "connection problem":
        speak('connection problem exiting')
        veronica_notify('connection problem exiting...')
        exit()

    elif text in ['stop', 'pause']:
        speak('Suspending')
        veronica_notify('Suspending')
        return 'pause'

    elif text in ["didn't get you", "terminate"]:
        if text == "terminate":
            veronica_notify('Virtual Assistant Exited')
            speak("Bye Bye")
            exit(1)
        else:
            speak(text)
            # continue

    '''
    elif text in ["stop", "go to sleep"]:
        speak('Okay sir')
        stop = StopApp()
        stop.mainloop()
        continue
    '''

    #speak('fetching results please wait')

    if 'folder' in text or 'directory' in text:#match(r'^.*(folder)|(directory) .*$', text):
        speak(nautilus.gen_folder_path(text))

    elif 'drive' in text:#search(r'drive', text):
        speak(nautilus.gen_drive_path(text))

    elif 'meaning' in text or 'define' in text:#search(r'(meaning)|(define)', text):
        speak(getMeaning(text))
        veronica_notify(getMeaning(text))

    elif 'run' in text or 'execute' in text:#search(r'(run)|(execute)', text):
        speak(nautilus.open_gnome(text))
        veronica_notify(text)

    elif 'browse' in text:#search(r'(browse)', text):
        speak(get_address(text))

    elif 'google' in text or 'search' in text:# search(r'(google)|(search)', text):
        speak(get_result(text))
        veronica_notify('There you go !')

    elif 'download audio' in text:
        youtube_mp3(text)

    elif 'download video' in text:
        youtube_mp4(text)        

    elif 'youtube' in text:#search(r'download\s(video)|(mp4)', text):
        speak('starting youtube')
        veronica_notify('starting youtube')
        url_Open(text)
        #speak(youtube_link(text[text.find('youtube results of')+len('youtube results of')+1:]))

    elif 'download lyrics' in text:#search(r'download\s(lyrics)', text):
        speak(lyrics_down(text))

    elif 'temperature' in text or 'wolfram' in text or 'wikipedia' in text:
        search(text)

    else:
        speak(get_result_google(text))
        veronica_notify('There you go !')  

    '''else:
        speak(nautilus.gen_file_path(text))'''


#if __name__ == '__main__':
#    main()

'''while True:
    if main(' '.join(sys.argv[1:])) == 'pause':
        input('Press enter to resume ')'''




