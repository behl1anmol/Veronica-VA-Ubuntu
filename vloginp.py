from tkinter import *
from tkinter import ttk

root = Tk()
frame = Frame(root)
root.geometry('360x500')
root.title('V.E.R.O.N.I.C.A')


LOGO_PATH  = '/home/anmol/VA/Documents/veronica/login.png'

font=('',11,'bold')


# Label - Logo
photo = PhotoImage(file=LOGO_PATH)
Label(root, image=photo).grid(row=0, columnspan=2,padx=50,pady=100)


# ComboBox - Select Command
box = ttk.Label(root,font=font, text='ENTER USERNAME')
box.grid(row=1, column=0)


# Entry - User Request
user_command = Entry(root, bd=1)
user_command.grid(row=1, column=1)


# ComboBox - Select Command
box = ttk.Label(root,font=font, text='ENTER PASSWORD')
box.grid(row=2, column=0)


# Entry - User Request
user_command = Entry(root, bd=1)
user_command.grid(row=2, column=1)

# Button - Search
btn_train = Button(root, text="FORGOT PASSWORD", width=18, command='',
                    bg="#4169e1", fg="white").grid(row=3, column=1,padx=0,pady=0)

# Button - Microphone
btn_login = Button(root, text="LOGIN", width=19, command='',
                     bg="#DF0101", fg="white").grid(row=3, column=0)

root.mainloop()