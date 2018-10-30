from os import chdir
from saavn import open_saavn
from time import sleep
from _thread import start_new_thread
from subprocess import getoutput
from settings import DRIVE_DIR, HOME_DIR, DRIVES, IGNORE_DIRS
from AudioIO import speak

def mounted():
    global mounted_drives
    mounted_drives = [DRIVE_DIR+dir+"/" for dir in DRIVES] + [HOME_DIR+'Downloads/',
                                                          HOME_DIR+'Documents/',
                                                          HOME_DIR+'Videos/',
                                                          HOME_DIR+'Desktop/',
                                                          HOME_DIR+'projects/',
                                                          HOME_DIR+'projects/gitlab']
    # Creating command for IGNORE_DIRS
    global except_dirs
    except_dirs = ''
    if len(IGNORE_DIRS) == 0:
        except_dirs = HOME_DIR
    else:
        for i, dir in enumerate(IGNORE_DIRS):
            if i == 0:
                except_dirs += ' -path ' + dir
            else:
                except_dirs += ' -o -path ' + dir
    #print(except_dirs)


def open_drive(path):
    getoutput('nautilus ' + path)
    return "there you go"


def open_folder(path):
    chdir('/')
    getoutput('nautilus ' "'" + path + "'")
    return "there you go"


def open_file(path):
    chdir('/')
    start_new_thread(getoutput, ('gnome-open ' + "'"+path+"'",))
    sleep(1)
    return "there you go"


def gen_drive_path(text):
    mounted()
    try:
        for drive in DRIVES:
            if drive.lower() in text:
                return open_drive(DRIVE_DIR + drive)
        else:
            raise FileExistsError()

    except FileExistsError:
        if "root" in text:
            return open_drive('/')
            # if word in DRIVES:
            #    return "This drive is not mounted."
        else:
            return "There is no such drive mounted."


def gen_folder_path(text):
    mounted()
    text = text.split()
    if 'folder' in text:
        text = ' '.join(text[text.index('folder') + 1:])
    elif 'directory' in text:
        text = ' '.join(text[text.index('directory') + 1:])
    else:
        return "say again with specific command"
    print(text)
    opt = []
    for index, drive in enumerate(mounted_drives):
        cmd = "find " + drive + " \(" + except_dirs + " \) -prune -o -type d -iname " + '\'*' + text + '*\''
        #print(cmd)
        r = getoutput(cmd)
        if text in r.lower():
            for i in r.split('\n'):
                if text in i.lower():
                    opt.append(i)
                    break
    #print(opt)
    if len(opt) == 1:
        return open_folder(opt[0])
    try:
        if len(opt) != 0:
            speak('multiple results found')
            for i, dir in enumerate(opt):
                print(i + 1, dir)
            return open_folder(opt[int(input("Enter folder no. to open => ")) - 1])
        else:
            return "No match found"
    except Exception as ex:
        print(ex)


def gen_file_path(text):
    extension = ['']
    mounted()
    text = text.split()
    if 'play' in text:
        if 'audio' in text:
            extension = ['.mp3']
            text = ' '.join(text[text.index('audio') + 1:])
        elif 'video' in text:
            extension = ['.mp4', '.avi', '.mkv']
            text = ' '.join(text[text.index('video') + 1:])

    elif 'file' in text:
        text = ' '.join(text[text.index('file') + 1:])

    elif 'image' in text:
        extension = ['.jpg', '.png', '.jpeg', '.gif', '.bmp']
        text = ' '.join(text[text.index('image') + 1:])

    else:
        return "say again with specific command"
    print(text)
    opt = []
    for index, drive in enumerate(mounted_drives):
        for ext in extension:
            cmd = "find " + drive + " \(" + except_dirs + " \) -prune -o -type f -iname " + '\'*'+text+'*'+ext+'\''
            r = getoutput(cmd)
            #print(r)
            if text in r.lower():
                for i in r.split('\n'):
                    if text in i.lower():
                        opt.append(i)
    print(opt)
    if len(opt) == 1:
        return open_file(opt[0])
    try:
        if len(opt) != 0:
            speak('multiple results found')
            for i, vid in enumerate(opt):
                print(i+1, vid[vid.rfind('/')+1:])
            return open_file(opt[int(input("Enter file no. to play => "))-1])
        else:
            return "No match found"
    except Exception as ex:
        print(ex)


def open_gnome(text):
    thread = start_new_thread
    process = getoutput
    try:
        if 'system monitor' in text:
            thread(process, ('gnome-system-monitor',))
        elif 'vlc' in text:
            thread(process, ('vlc',))
        if 'nautilus' in text:
            thread(process, ('nautilus',))      
        elif 'terminal' in text:
            thread(process, ('gnome-terminal',))
        elif 'python' in text or 'shell' in text:
            thread(process, ('python3',))
        elif 'pycharm' in text:
            thread(process, ('./"../Documents/pycharm-2016.1.4/bin/pycharm.sh"',))
        elif 'lock' in text:
            thread(process, ('gnome-screensaver-command -l',))
        elif 'reboot' in text:
            thread(process, ('reboot',))
        elif 'saavn' in text:
            open_saavn()
            #thread(process,('./"/home/anmol/Desktop/INNOTECH2K18/saavn/Saavn-linux-x64/Saavn"',))    
        elif 'shutdown' in text:
            thread(process, ('poweroff',))
        else:
            return text + " is not a valid command"
        #time.sleep(3)
    except:
        return "oops something went wrong."
    return "there you go"

#mounted()
#gen_drive_path('open green drive')
#bangongen_folder_path('open folder music')
#open_gnome('system monitor')
#gen_file_path('play audio ullu ka pattha')
