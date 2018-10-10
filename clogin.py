from tkinter import *
from tkinter import ttk
import os
from os import chdir

root = Tk()
frame = Frame(root)
root.geometry('360x500')
root.title('V.E.R.O.N.I.C.A')


LOGO_PATH  = '/home/anmol/VA/Documents/veronica/login.png'
FILE_PATH  = '/home/anmol/Desktop/test/'

font=('',11,'bold')

def fgui():
    chdir(FILE_PATH)
    os.system('python3 vlogin.py')


def pgui():
    chdir(FILE_PATH)
    os.system('python3 vloginp.py')



# Label - Logo
photo = PhotoImage(file=LOGO_PATH)
Label(root, image=photo).grid(row=0, columnspan=2,padx=50,pady=100)



# Button - Search
btn_train = Button(root, text="FACE DATA", width=18, command=fgui,
                    bg="#4169e1", fg="white").grid(row=3, column=1,padx=0,pady=0)

# Button - Microphone
btn_login = Button(root, text="PASSCODE", width=19, command=pgui,
                     bg="#DF0101", fg="white").grid(row=3, column=0)

root.mainloop()