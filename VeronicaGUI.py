#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
import sys
import os
from os import chdir
from AudioIO import listen, speak
from MainEngine import main, update_log
from settings import LOGO_PATH, LOG_DIR
from _thread import start_new_thread
import pyglet
from wolfwiki import search
import webbrowser
from settings import veronica_notify
from taggingwords import content

vs=''

  
LOGO1_PATH  = '/home/anmol/VA/Documents/veronica/login.png'

root = Tk()
frame = Frame(root, height=100, width=100)
root.wm_attributes('-fullscreen','true')
root.title('Veronica')
font=('',14,'italic')

#textbox
text=Text(font=('',12),width=40,height=25)
text.grid(row=0,column=3,rowspan=6,columnspan=2,sticky='nsew',padx=(42,0),pady=(200,50))
###################################FUNCTIONS FOR TKINTER GUI#######################################

def login():
    chdir('/home/anmol/projects/gitlab/Veronica--VA--Ubuntu')
    os.system('python3 vlogin.py')

def getTextInput():
    vs=content(user_command.get())
    print(vs)
    text.insert(END,"\n")
    text.insert(END,"SIR: ")
    text.insert(END,vs)
    text.insert(END,"\n")
    # reply=main(user_command.get())
    text.insert(END,"Veronica:")
    reply=main(vs)
    text.insert(END,reply)
    vs=''
    reply=''



def getVoInput():
    #box.set('')
    user_command.delete(0, END)
    speak('listening')
    text1 = listen().lower()
    print(text1)
    text.insert(END,text1)
    text.insert(END,"\n")
    user_command.insert(0, text1)
    start_new_thread(main, (text1,))


def open_log():
    main('open file microphone_log')


def yes_log():
    update_log(user_command.get() + ' $EXPECTED$')


def no_log():
    update_log(user_command.get() + ' $UNEXPECTED$')


def open_req():
    main('open file requirements')

def callgui():
    chdir('/home/anmol/projects/gitlab/Veronica--VA--Ubuntu')
    os.system('python3 gmailgui.py')

def callguigame():
    chdir('/home/anmol/projects/gitlab/Veronica--VA--Ubuntu')
    os.system('python3 snake.py')

def yt():
    webbrowser.open_new_tab("http://www.youtube.com")
    veronica_notify("There You GO!!")
    text.insert(END,"Veronica:There You Go!!\n")
    speak("There You Go!!")


def fb():
    webbrowser.open_new_tab("http://www.facebook.com")
    veronica_notify("There You GO!!")
    text.insert(END,"Veronica:There You Go!!\n")
    speak("There You Go!!")

def insta():
    webbrowser.open_new_tab("http://www.instagram.com")
    veronica_notify("Veronica:There You GO!!")
    text.insert(END,"There You Go!!\n")
    speak("There You Go!!")



####################################DEFINING TKINTER GUI##########################################



# root = Tk()
# frame = Frame(root, height=100, width=100)
# root.title('Veronica')
# font=('',14,'italic')

# Menubar
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Logs", command=open_log)
filemenu.add_command(label="Requirements", command=open_req)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Extras", menu=filemenu)
menubar.add_cascade(label="Logout", menu=filemenu)


mb = Menubutton()
root.config(menu=menubar)

# # # Label - Logo
# photo = PhotoImage(file=LOGO1_PATH)
# Label(root, image=photo).grid(row=0,rowspan=6, columnspan=2)


#good morning label
Label(root,font=font,text = '   Sweet Dreams   ',borderwidth=2,relief="groove",fg='white',bg='pink').grid(row=0,column=0,columnspan=2,padx=(500,0),pady=(200,50))

#weather
Label(root,font=font,text = '    WEATHER    ',bg='blue',fg='white').grid(row=1,column=0,columnspan=2,padx=(500,0))
#weather label
temp=search('temperature')
Label(root,text = '  ' + temp + '  ',borderwidth=2,relief="groove",bg='blue',fg='white').grid(row=2,column=0,columnspan=2,padx=(500,0))

#News
Label(root,font=font,text = '    NEWS    ',bg='red',fg='white').grid(row=3,column=0,columnspan=2,padx=(500,0))
#News label
#news=search('temperature')
Label(root,text = '3 Lakh People Evacuated From Coastal Odisha',bg='red',fg='white',borderwidth=2,relief="groove").grid(row=4,column=0,columnspan=2,padx=(500,0))


#player
btn_player = Button(root, text="Songs", width=18, command='',
                    bg="#4169e1", fg="white").grid(row=8, column=3)

#Bitcoin Button
btn_bitcoin = Button(root, text="Bitcoin Status", width=18, command='',
                    bg="yellow", fg="black").grid(row=8, column=4)


# Entry - User Request
user_command = Entry(root, bd=1)
user_command.grid(row=7, column=1)
# Button - Search
btn_search = Button(root, text="Search", width=18, command=getTextInput,
                    bg="#4169e1", fg="white").grid(row=8, column=1)

# Button - Microphone
btn_voInput = Button(root, text="Microphone", width=19, command=getVoInput,
                     bg="#DF0101", fg="white").grid(row=8, column=0,padx=(600,10))

#Button-logout
btn_logout = Button(root, text="Close", width=18, command=root.destroy,
                    bg="#4169e1", fg="white").grid(row=7, column=3)

#Button-games
btn_play = Button(root, text="Play Game", width=18, command=callguigame,
                    bg="green", fg="white").grid(row=7, column=4)


# # Button - Yes
# photo_yes = PhotoImage(file=LOG_DIR+'images/yes.png')
# yes_img = photo_yes.subsample(40, 40)
# btn_voInput = Button(root, text="Expected O/P", command=yes_log,
#                      bg="green", fg="white", image=yes_img).grid(row=9, column=0)

# # Button - No
# photo_no = PhotoImage(file=LOG_DIR+'images/no.png')
# no_img = photo_no.subsample(40, 40)
# btn_voInput = Button(root, text="Unexpected O/P", command=no_log,
#                      bg="#DF0101", fg="white", image=no_img).grid(row=9, column=1)

# # Button - gmail
# games = Button(root, text="GAMES", width=19, command='',
#                      bg="green", fg="white").grid(row=9, column=3)

# Button - gmail
gmail = Button(root, text="Gmail", width=19, command=callgui,
                     bg="#DF0101", fg="white").grid(row=10, column=0,padx=(600,10))

#Button - facebook
facebook = Button(root, text="Facebook", width=18, command=fb,
                    bg="#4169e1", fg="white").grid(row=10, column=1)

# Button - youtube
youtube = Button(root, text="Youtube", width=19, command=yt,
                     bg="#DF0101", fg="white").grid(row=10, column=3)

# Button - youtube
instagram = Button(root, text="Instagram", width=19, command=insta,
                     bg="grey", fg="white").grid(row=10, column=4)

def whatcanido():
    text.insert(END,"\nVERONICA:\nThere lots of think i can help you with...\n\n1)Daily news\n2)Browse websites\n3)Download Audio\n4)Download video\nand many more...\nJust tap the microphone\nOr type the text")
    veronica_notify("There lots of think i can help you with...\n\n1)Daily news\n2)Browse websites\n3)Download Audio\n4)Download video\nand many more...\nJust tap the microphone or type the text")
    speak("There lots of think i can help you with,Just tap the microphone or type the text")

#Help
btn_vhelp = Button(root, text="Help", width=18, command=whatcanido,
                    bg="#4169e1", fg="white").grid(row=7, column=0,padx=(600,10))    
login()


try:
    animation=pyglet.image.load_animation(LOGO_PATH)
    animSprite=pyglet.sprite.Sprite(animation)

    w=animSprite.width
    h=animSprite.height


    window=pyglet.window.Window(width=w,height=h)

    r,g,b,alpha=0.5,0.5,0.8,0.5

    pyglet.gl.glClearColor(r,g,b,alpha)
    pyglet.clock.schedule_once(pyglet.app.exit(),8)
    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()
    pyglet.app.run()
except:
    window.close()
    speak("Hello sir,here is some daily info for you")
    veronica_notify("Hello sir,here is some daily info for you")
    text.insert(END,"Veronica:Hello Sir,here is some daily info for you\n")
    root.mainloop()  


