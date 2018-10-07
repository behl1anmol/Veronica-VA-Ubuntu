import notify2
import subprocess

def veronica_notify(text):     #Desktop Notification
    notify2.init('Veronica')
    #subprocess.call(['/usr/bin/canberra-gtk-play', '--id', 'message-new-instant'])
    n = notify2.Notification('V.E.R.O.N.I.C.A', text, icon=LOGO_PATH)
    n.show()