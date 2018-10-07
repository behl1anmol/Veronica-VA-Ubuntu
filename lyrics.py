import requests, bs4, google,webbrowser
from settings import LYRICS_DIR
from os import chdir
from nautilus import open_file

#def find(s, ch):
#    return [i for i, ltr in enumerate(s) if ltr == ch]


def lyrics_down(text):
    text = text.split()
    text = ' '.join(text[text.index('lyrics') + 1:])
    print(text)
    addr = google.lucky(text + 'lyrics.wikia.com')#"http://lyrics.wikia.com/wiki/Twenty_One_Pilots:Ride"
    res = requests.get(addr)
    try:
        res.raise_for_status()
    except:
        return 'Downloading Error'

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    s = soup.select('.lyricbox')
    n = soup.select('h1')
    col = n[0].get_text().find(':')
    name = n[0].get_text()[:col] + ' ' + n[0].get_text()[col+1:]
    print(name)

    chdir(LYRICS_DIR)
    lyrics = open(name, 'w')

    for i in s[0].get_text('\n').split('\n'):
        #if i == '':
        lyrics.write('\n')
        lyrics.write(i)

    lyrics.close()

    return open_file(LYRICS_DIR + name)

#lyrics_down('download lyrics heathens')
