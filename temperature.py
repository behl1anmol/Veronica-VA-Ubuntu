### Author - Raghav Maheshwari ###

import requests, bs4


def getTemperature(query):
    if 'temperature' not in query:
        return 'try saying temperature again'
    res = requests.get('https://www.google.co.in/search?q=' + query)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    s = soup.select('.wob_t')
    text = "tempearature is " + s[0].text + " and " + " wind speed is " + s[2].text
    return text

#print(getTemperature("temperature"))