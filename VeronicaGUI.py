#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from AudioIO import listen, speak
from MainEngine import main, update_log
from settings import LOGO_PATH, LOG_DIR
from _thread import start_new_thread


def getTextInput():
    print(user_command.get())
    main(user_command.get())


def getVoInput():
    box.set('')
    user_command.delete(0, END)
    speak('listening')
    text = listen().lower()
    print(text)
    user_command.insert(0, text)
    start_new_thread(main, (text,))


def open_log():
    main('open file microphone_log')


def yes_log():
    update_log(user_command.get() + ' $EXPECTED$')


def no_log():
    update_log(user_command.get() + ' $UNEXPECTED$')


def open_req():
    main('open file requirements')


root = Tk()
frame = Frame(root, height=100, width=100)
root.title('V.E.R.O.N.I.C.A')

# Menubar
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Logs", command=open_log)
filemenu.add_command(label="Requirements", command=open_req)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Extras", menu=filemenu)
menubar.add_cascade(label='extras')

mb = Menubutton()
root.config(menu=menubar)

# Label - Logo
photo = PhotoImage(file=LOGO_PATH)
Label(root, image=photo).grid(row=0, columnspan=2)

#Label(root,image=photo).grid(row=4,columnspan=3)

# ComboBox - Select Command
value = StringVar()
box = ttk.Combobox(root, textvariable=value, state='readonly')
box['values'] = ('google ', 'play audio ', 'play video ', 'download audio ', 'download video ',
                 'download lyrics ', 'open file ', 'open folder ', 'open drive ', 'execute ', 'browse ')
box.set("Select Command")
box.grid(row=1, column=0)


# Entry - User Request
user_command = Entry(root, bd=1)
user_command.grid(row=1, column=1)

# Button - Search
btn_search = Button(root, text="Search", width=18, command=getTextInput,
                    bg="#4169e1", fg="white").grid(row=2, column=1)

# Button - Microphone
btn_voInput = Button(root, text="Microphone", width=19, command=getVoInput,
                     bg="#DF0101", fg="white").grid(row=2, column=0)

'''
# Button - Yes
photo_yes = PhotoImage(file=LOG_DIR+'images/yes.png')
yes_img = photo_yes.subsample(40, 40)
btn_voInput = Button(root, text="Expected O/P", command=yes_log,
                     bg="green", fg="white", image=yes_img).grid(row=3, column=0)

# Button - No
photo_no = PhotoImage(file=LOG_DIR+'images/no.png')
no_img = photo_no.subsample(40, 40)
btn_voInput = Button(root, text="Unexpected O/P", command=no_log,
                     bg="#DF0101", fg="white", image=no_img).grid(row=3, column=1)
'''

root.mainloop()


