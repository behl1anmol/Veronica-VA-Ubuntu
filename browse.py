import webbrowser, google
#import requests, bs4


def open_link(address):
    webbrowser.open(address)
    return "there you go"


def get_address(text):
    text = text.split()
    try:
        text = ' '.join(text[text.index('browse') + 1:])
    except ValueError:
        text = ' '.join(text[text.index('open') + 1:])

    '''
    res = requests.get('https://www.google.com/search?q=' + text)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    link = soup.select_one('cite').getText()
    print(link)
    '''
    return open_link(google.lucky(text))

#get_address('browse fb')



