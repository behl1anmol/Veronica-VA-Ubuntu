from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from google import lucky
from mp3download import download_song

chromedriver = "/home/anmol/VA/chromedriver"
base_url = url = "http://musicpleer.audio"


def get_down_link(url, name):
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    link = soup.select("#download-btn")[0].get("href")
    download_song(link, name)
    print(link)


def get_search_results(url):
    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    data = soup.select("#searchResults > ul > li > a")
    song_data = {"name": [], "artist": [], "size": [], "link": []}
    for song in data:
        song_data["link"].append(base_url + song.get("href"))
        song_data["name"].append(song.select("h3")[0].getText())
        song_data["artist"].append(song.select("p")[0].getText())
        song_data["size"].append(song.select("span")[0].getText())

    driver.close()

    for i in range(len(data)):
        print("%d | %s | %s | %s"%(i+1,
                             song_data["name"][i],
                             song_data["artist"][i],
                             song_data["size"][i]))
    index = int(input("Enter a number : "))
    get_down_link(song_data["link"][index],
                  song_data["name"][index])
    return data



get_search_results(lucky(input("Enter song name : ") + " site:musicpleer.audio"))
