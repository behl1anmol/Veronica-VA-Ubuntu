

import requests, bs4
from os import chdir, makedirs
from subprocess import getoutput

url = "http://wallpaperswide.com"


def getCategories(soup):
    category_links = []
    categories = soup.findAll("li", {"style": "padding-left:0px;"})
    for ind, i in enumerate(categories):
        print(str(ind + 1) + ". " + i.getText() + " -> " + i.find('a').get('href'))
        category_links.append(tuple([i.getText(), url + i.find('a').get('href')]))
    return category_links


def getWallpapers(soup):
    walls = soup.select('#hudtitle')
    for i in walls:
        link = i.find('a').get('href')
        title = i.find('a').get('title')
        print(url + link + " -> " + title)
        down_link(getSoup(url + link), title)


def down_link(soup, title):
    link = soup.find('a', {'title': "HD 16:9 1600 x 900 wallpaper"})
    wall_link = url + link.get('href')
    #print(wall_link)
    down_wall(wall_link, title)


def down_wall(link, title):
    #print(link + " -> " + title)
    getoutput("wget " + link)
    print('Downloaded ' + title)


# url = "http://wallpaperswide.com/altitude_2-wallpapers.html"
# url = "http://wallpaperswide.com/motors-desktop-wallpapers"
# url = "http://wallpaperswide.com/"
def getSoup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    return soup


categories = getCategories(getSoup(url))
cat_num = int(input("Enter category index number :- "))
pages = int(input("1 page consist of 10 wallpapers\nEnter no. of pages :- "))

chdir('/media/imnobody0396/Green/Wallpapers/')
try:
    makedirs(categories[cat_num - 1][0].split(" ")[0])
except FileExistsError:
    pass
chdir(categories[cat_num - 1][0].split(" ")[0])
# print(categories[cat_num-1][0].split(" ")[0], categories[cat_num-1][1])
for i in range(1, pages + 1):
    if i == 1:
        link = categories[cat_num - 1][1]
    else:
        link = categories[cat_num - 1][1] + "/page/" + str(i)
    print(link)
    getWallpapers(getSoup(link))
# down_link(soup)
# down_wall(input(), "1.jpg")
#gsettings set org.gnome.desktop.background picture-uri file:///path/to/your/image.png

