from tkinter import *
from tkinter import ttk
import tkinter as tk
from AudioIO import listen, speak
from MainEngine import main, update_log
from settings import LOGO_PATH, LOG_DIR
from _thread import start_new_thread

# LOGO_PATH  = '/home/anmol/VA/Documents/veronica/logo.gif'
# open_log='hello'
# open_req='hi'

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




class windowclass(Frame):
	#gui application#
	def __init__(self,master):
		#frame initialize#
		ttk.Frame.__init__(self,master)

		self.grid()
		self.create_widgets()

	def command(self):
		print('Button is pressed!')
		self.newWindow = tk.Toplevel(self.master)
		self.app = windowclass1(self.newWindow)

	
	def create_widgets(self):

		# #Menubar
		# menubar = Menu(root)
		# self.filemenu = Menu(menubar,tearoff=0)
		# self.filemenu.add_command(label="Logs", command=open_log)
		# self.filemenu.add_command(label="Requirements", command=open_req)

		# self.filemenu.add_separator()

		# self.filemenu.add_command(label="Exit", command=root.quit)
		# self.menubar.add_cascade(label="Extras", menu=filemenu)
		# self.menubar.add_cascade(label='extras')

		# self.mb = Menubutton()
		# root.config(menu=menubar)

		#Label - Logo
		photo = PhotoImage(file=LOGO_PATH)
		self.lbl1=Label(root, image=photo).grid(row=0, columnspan=2)

		#self.lbl2=Label(root,image=photo).grid(row=4,columnspan=3)

		# ComboBox - Select Command
		value = StringVar()
		self.box = ttk.Combobox(root, textvariable=value, state='readonly')
		self.box['values'] = ('google ', 'play audio ', 'play video ', 'download audio ', 'download video ',
		                 'download lyrics ', 'open file ', 'open folder ', 'open drive ', 'execute ', 'browse ')
		self.box.set("Select Command")
		self.box.grid(row=1, column=0)


		#Entry - User Request
		self.user_command = Entry(root, bd=1)
		self.user_command.grid(row=1, column=1)

		# Button - Search
		self.btn_search = Button(root, text="Search", width=18, command=getTextInput,
		                    bg="#4169e1", fg="white").grid(row=2, column=1)

		# Button - Microphone
		self.btn_voInput = Button(root, text="Microphone", width=19, command=getVoInput,
		                     bg="#DF0101", fg="white").grid(row=2, column=0)


		# Button - Yes
		photo_yes = PhotoImage(file=LOG_DIR+'images/yes.png')
		yes_img = photo_yes.subsample(40, 40)
		self.btn_voInput = Button(root, text="Expected O/P", command=yes_log,
		                     bg="green", fg="white", image=yes_img).grid(row=3, column=0)

		# Button - No
		photo_no = PhotoImage(file=LOG_DIR+'images/no.png')
		no_img = photo_no.subsample(40, 40)
		self.btn_voInput = Button(root, text="Unexpected O/P", command=no_log,
		                     bg="#DF0101", fg="white", image=no_img).grid(row=3, column=1)

		# Button - gmail
		self.btn_gmail = Button(root, text="Gmail", width=19, command=self.command,
		                     bg="#DF0101", fg="white").grid(row=4, column=0)




class windowclass1():

        def __init__(self , master):
                self.master = master
                self.frame = tk.Frame(master)
                master.title("Gmail")
                self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25 , command = self.close_window)
                self.quitButton.pack()
                self.frame.pack()


        def close_window(self):
                self.master.destroy()


root = Tk()

root.title("V.E.R.O.N.I.C.A")

#root.geometry("350x50")

cls1= windowclass(root)

root.mainloop()