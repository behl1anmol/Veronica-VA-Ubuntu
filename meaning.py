

import requests, bs4


def getMeaning(query):
    if '*' in query:
        return 'Sorry big guy, this one you have to find out yourself.'
    text = []
    res = requests.get('https://www.google.co.in/search?q=' + query)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    try:
        text.append(soup.find('span', {'style': "font-weight:bold"}).text)
        soup = bs4.BeautifulSoup(soup.prettify(), 'lxml')
        s = soup.select('.g ol li')
        for index, output in enumerate(s):
            text.append(str(index+1) + '. ' + ' '.join(output.text.split()))

        if len(text) == 1:
            return "No results found for meaning of " + text[0]
        else:
            if len(text) == 2:
                return "Meaning of " + text[0] + " is " + text[1][3:]
            else:
                return "Meaning of " + text[0] + " is " + text[1] + " and " + text[2]
    except:
        soup = bs4.BeautifulSoup(soup.prettify(), 'lxml')
        s = soup.select('._sPg')
        return ' '.join(s[0].text.split('\n'))
#print(getMeaning('meaning of capital'))
