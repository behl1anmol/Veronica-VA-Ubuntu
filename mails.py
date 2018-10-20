from flask import Flask
from flask_mail import Mail, Message
from AudioIO import listen, speak
from settings import veronica_notify
#import os

app = Flask(__name__)

def s_mail(mail_S,mail_R,mail_Sub,mail_M):

  print('inside func')

  # mail_ID=input("V.E.R.O.N.I.C.A: Enter Mail Id:")
  # mail_P=input("V.E.R.O.N.I.C.A: Enter Password:")
  # mail_M=input("V.E.R.O.N.I.C.A:Enter Your Mail:")
  # mail_R=input("V.E.R.O.N.I.C.A:Enter Recipents Email:")
  mail_settings = {
      "MAIL_SERVER": 'smtp.gmail.com',
      "MAIL_PORT": 465,
      "MAIL_USE_TLS": False,
      "MAIL_USE_SSL": True,
      "MAIL_USERNAME": mail_S,
      "MAIL_PASSWORD": 'veronica1311'
  }

  app.config.update(mail_settings)
  mail = Mail(app)
  print('settings done')

  #if __name__ == '__main__':
  with app.app_context():
      msg = Message(subject=mail_Sub,
                    sender=app.config.get("MAIL_USERNAME"),
                    recipients=[mail_R], # replace with your email for testing
                    body=mail_M)
      say('sending mail')
      veronica_notify('Sending Mail')
      mail.send(msg)
      speak("Mail Send")
      veronica_notify("Mail Send")

#s_mail()