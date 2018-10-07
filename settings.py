import notify2
#from wolframalpha import Client
from os import listdir


def veronica_notify(text):     #Desktop Notification
    notify2.init('Veronica')
    n = notify2.Notification('V.E.R.O.N.I.C.A', text, icon=LOGO_PATH)
    n.show()

#app_id = "KHHH6P-HTUJE286QJ"
#client = Client(app_id)

LOGO_PATH  = '/home/anmol/VA/Documents/veronica/logo.gif'
HOME_DIR   = '/home/anmol/VA/home/'
DRIVE_DIR  = '/home/anmol/VA/media/'
LOG_DIR    = '/home/anmol/VA/Documents/VLOG/'
LYRICS_DIR = '/home/anmol/VA/media/Green/Videos/Lyrics/'
MP3_DIR    = '/home/anmol/VA/media/Green/Music/'
MP4_DIR    = '/home/anmol/VA/media/Green/Videos/'
IGNORE_DIRS= ['/home/anmol/VA/media/Green/Matlab', '/media/Blue/.Tempp']

DRIVES = [dir for dir in listdir(DRIVE_DIR)]
