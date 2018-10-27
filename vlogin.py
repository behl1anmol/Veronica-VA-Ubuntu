from tkinter import *
from tkinter import ttk
from encode_faces import test,train,name

root = Tk()
root.wm_attributes('-fullscreen','true')
root.geometry('1920x1080')
root.title('V.E.R.O.N.I.C.A')


LOGO_PATH  = '/home/anmol/VA/Documents/veronica/login.png'

font=('',11,'bold')


# Label - Logo
photo = PhotoImage(file=LOGO_PATH)
Label(root, image=photo).grid(row=0,column=0, columnspan=2,padx=(750,0),pady=(300,50))


# ComboBox - Select Command
box = ttk.Label(root,font=font, text='ENTER USERNAME')
box.grid(row=1, column=0,padx=(750,0))


# Entry - User Request
user_command = Entry(root, bd=1,textvariable=name)
user_command.grid(row=1, column=1,padx=(42,0))


print(name)
# Button - Search
btn_train = Button(root, text="TRAIN", width=18, command=train,
                    bg="#4169e1", fg="white").grid(row=2, column=0,padx=(750,0),pady=(10,0))

# Button - Microphone
btn_login = Button(root, text="LOGIN", width=19, command=test,
                     bg="#DF0101", fg="white").grid(row=2, column=1,padx=(42,0),pady=(10,0))



root.mainloop()                     