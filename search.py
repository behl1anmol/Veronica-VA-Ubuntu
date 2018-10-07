import webbrowser, google


def open_link(address):
    webbrowser.open(address)
    return "there you go"


def get_result(text):
    text = text.split()
    try:
        text = ' '.join(text[text.index('google') + 1:])
    except ValueError:
        text = ' '.join(text[text.index('search') + 1:])
    #print(google.lucky(text))
    return open_link('https://www.google.com/search?q='+text.replace(' ', '+'))

#get_result('google India')
