import webbrowser,google

def open_link_google(address):
    webbrowser.open(address)
    return "there you go"


def get_result_google(text):
    return open_link_google('https://www.google.com/search?q='+text.replace(' ', '+'))    