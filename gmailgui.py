import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
from tkinter import *
from tkinter import ttk
import math
from mails import s_mail



class Application(Frame):
	#gui application#
	def __init__(self,master):
		#frame initialize#
		ttk.Frame.__init__(self,master)

		self.grid()
		self.create_widgets()

	def create_widgets(self):
		
		font=('',15,'bold')

		# row 0
        #create first button
		self.btnConnect = Button(self,  font=font, text = "Send Mail", bg='red', fg='white', command=self.send_mail).grid(row=0, column=0, sticky=W)

		#row 1
		#column 0
		#padx=50
		#pady=100
		#to label
		self.recipient=Label(self,font=font,text = 'TO: ').grid(row=1,column=0,pady=10,padx=10,sticky=E)	

		#combobox for to
		#column 1
		self.cbToEmail=ttk.Combobox(self,font=font,width=40,textvariable=varTo)
		self.cbToEmail['values']=('anmol.1721cs1039@kiet.edu','behl1anmol@gmail.com')
		self.cbToEmail.grid(row=1,column=1,pady=10,padx=10)

		# #row 2
		# #column 0
		# #sender
		
		# self.sender=Label(self,font=font,text='FROM: ').grid(row=2,column=0,pady=10,padx=10,sticky=E)

		# #combobox for from
		# #column 1
		# self.cbFromEmail=ttk.Combobox(self,font=font,width=40,textvariable=varFrom)
		# self.cbFromEmail['values']=('','')
		# self.cbFromEmail.grid(row=2,column=1,pady=10,padx=10)

		#row 3
		#column 0
		#subject

		self.subject=Label(self,font=font,text='SUBJECT: ').grid(row=3,column=0,pady=10,padx=10,sticky=E)

		#combobox for subject
		#column 1
		self.cbSubject=ttk.Combobox(self,font=font,width=40,textvariable=varSubject)
		self.cbSubject.grid(row=3,column=1,pady=10,padx=10)

		#row 4
		#columnapn 2
		#text
		self.text=Text(self,font=('',12),width=90,height=25)
		self.text.grid(row=4,column=0,columnspan=2,padx=5,pady=5,sticky='nsew')

		self.scrollb=Scrollbar(self,command=self.text.yview)
		self.scrollb.grid(row=4,rowspan=8,columnspan=2,pady=10,sticky='nse')
		self.text['yscrollcommand']=self.scrollb.set

	def send_mail(self):
		#from_address=varFrom.get()
		to_address=varTo.get()
		subject_text=varSubject.get()
		text_letter=self.text.get('1.0',END)
		s_mail('veronica.va.ubuntu@gmail.com',to_address,subject_text,text_letter)

root1=Tk()

	
root1.title('GMAIL')
root1.geometry('840x625')
root1.attributes('-topmost',True)
varTo=StringVar(root1,value='to_address@gmail.com')
#varFrom=StringVar(root1,value='from_address@gmail.com')
varText_Letter=StringVar()
varSubject=StringVar(root1,value='enter subject')
varEmail_List=StringVar(root1,value='address_email.txt')
app=Application(root1)

root1.mainloop()

#gmail_open()