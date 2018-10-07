

import requests, bs4, AudioIO
from os import chdir, system
from settings import MP3_DIR, veronica_notify
from time import sleep

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    system('clear')
    print('\n\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()
        

def download_song(link, name):
    chdir(MP3_DIR)
    print('Downloading ' + name + '...')
    AudioIO.speak('Downloading ' + name + '...')
    res = requests.get(link, stream=True)
    try:
        res.raise_for_status()
    except:
        AudioIO.speak('Downloading Error')
        return False
    song = open(name, 'wb')
    dl = 0
    total_length = int(res.headers.get('content-length'))
    printProgressBar(dl, total_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for chunk in res.iter_content(100000):
        song.write(chunk)
        dl += 100000
        sleep(0.1)
        printProgressBar(dl, total_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
        song.flush()
    song.close()
    veronica_notify("Downloaded\n" + name)
    #AudioIO.speak('Download finished')
    return True


def download_link(addr):
    res = requests.get(addr)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    s = soup.select('a')
    link = []
    for i in s:
        try:
            if "Download In" in i.get_text('strong'):# and "Quality" in i.get_text('strong'):
                link.append(i.get('href'))
        except:
            pass
    try:
        name = link[-1][len(link[-1]) - link[-1][::-1].find('/'):]
    except IndexError:
        return False
    return download_song(link[-1], name)


def page_link(name):
    name += ' mp3mad'
    res = requests.get('https://google.com/search?q=' + name)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    opt = soup.select('.r a')
    for link in opt[:3]:
        try:
            addr = link.get('href')
            addr = addr[7:addr.index('&')]
            print('trying -> ' + addr)
            if download_link(addr):
                return 'Download finished'
        except IndexError:
            pass
    else:
        return "No Link found"



#page_link(input())

