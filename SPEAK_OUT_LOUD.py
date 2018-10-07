

import pyperclip
from AudioIO import speak

#f = open(pyperclip.paste(), 'r')
#text = f.readlines()
#print(''.join(text))
#speak(''.join(text))
speak(pyperclip.paste())
'''
for i in text:
    print(i)
    speak(i)
'''
