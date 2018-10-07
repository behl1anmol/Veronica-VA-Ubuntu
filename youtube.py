from __future__ import unicode_literals
import urllib.request
import urllib.parse
import re
import webbrowser


def url_Open(usr):
    query_string=urllib.parse.urlencode({"search_query" : usr})
    html_content=urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results=re.findall(r'href=\"\/watch\?v=(.{11})',html_content.read().decode())
    url_result="http://www.youtube.com/watch?v=" + search_results[0] 
    webbrowser.open_new_tab("http://www.youtube.com/watch?v=" + search_results[0])
    


