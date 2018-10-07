

from AudioIO import speak
from os import chdir
#from pytube import YouTube
from pprint import pprint
from settings import MP4_DIR
import requests
from os import chdir, system
from bs4 import BeautifulSoup
from google import lucky
from settings import MP4_DIR
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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


def down_link(src):
    soup = BeautifulSoup(src, 'lxml')
    name = soup.find('div', {'class': 'row title'}).get('title')
    print(name)
    s = soup.findAll('a', {'class': 'link link-download subname ga_track_events', 'data-type': 'MP4'})
    for i in s[0:1]:
        quality = i.get('data-quality')
        link = i.get('href')
        print(name, quality, link)
        return vid_download(link, name)


def get_page(url):
    # url = 'https://www.google.com'
    # driver = webdriver.Firefox()
    chromedriver = "/home/imnobody0396/Documents/chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    try:
        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.CLASS_NAME, "info-box")))
    except:
        driver.refresh()
    src = driver.page_source
    driver.close()
    return down_link(src)


def vid_download(link, name):
    chdir(MP4_DIR)
    vid = open(name + '.mp4', 'wb')
    res = requests.get(link, stream=True)
    dl = 0
    total_length = int(res.headers.get('content-length'))
    printProgressBar(dl, total_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for chunk in res.iter_content(chunk_size=100000):
        if chunk:
            vid.write(chunk)
            dl += 100000
            sleep(0.1)
            printProgressBar(dl, total_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
            vid.flush() 
    vid.close()
    return "Download Finished"


def youtube_link(text):
    base_url = "https://www.youtube.com"
    res = requests.get(base_url + "/results?search_query=" + text.replace(' ', '+'), verify=False)
    try:
        res.raise_for_status()
    except Exception as ex:
        print(ex.args)
    soup = BeautifulSoup(res.text, 'lxml')
    links = soup.findAll('h3', {'class':'yt-lockup-title'})#.find('a').get('href')
    speak('here are the results')
    for i,link in enumerate(links):
        print(i+1, link.find('a').get('title'))
    dl_link = base_url + links[int(input('Enter Video No. to download => '))-1].find('a').get('href')
    #print(dl_link)
    return get_page("http://en.savefrom.net/#url=" + dl_link)#lucky('site:www.youtube.com "' + text + '"'))


# driver = webdriver.Firefox()
# driver.get('http://www.google.com')
# driver.close()

'''




def vid_download(link):
    try:
        chdir(MP4_DIR)
    except:
        return 'Download path is not mounted.'
    try:
        yt = YouTube(link)
    except:
        print("Cipher Error")
        return ("Cipher Error")

    pprint(yt.get_videos())
    quality = ['720p', '480p', '360p']
    for i in quality:
        try:
            video = yt.get('mp4', i)
            AudioIO.speak('Downloading in ' + i + " " + yt.filename)
            video.download('.')
            AudioIO.speak('Download Complete')
            break
        except:
            continue
    else:
        return 'Not found in good quality'


def youtube_link(text):
    #res = requests.get('https://www.google.com/search?q=' + text)
    #res.raise_for_status()
    #soup = bs4.BeautifulSoup(res.text, 'lxml')
    #link = soup.select_one('cite').getText()
    #print(text,link, lucky(text))
    try:
        return vid_download(lucky(text))
    except Exception as ex:
        AudioIO.speak("Age Restricted Video")

#youtube_link(input() + ' youtube')
#vid_download('https://www.youtube.com/watch?v=Ib8XaRKCAfo')
'''
