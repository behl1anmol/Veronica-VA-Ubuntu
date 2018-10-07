from __future__ import unicode_literals
import youtube_dl 
from settings import MP4_DIR, veronica_notify
import urllib.request
import urllib.parse
from os import chdir, system
import AudioIO
import re



# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
# 	ydl.download(['https://www.youtube.com/watch?v=0VwgpYJ4q38'])
#url=input("enter video name to download:---  ")

def youtube_mp4(usr):
	try:
		chdir(MP4_DIR)
		query_string=urllib.parse.urlencode({"search_query" : usr})
		html_content=urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
		search_results=re.findall(r'href=\"\/watch\?v=(.{11})',html_content.read().decode())
		url_result="http://www.youtube.com/watch?v=" + search_results[0] 
		print("result of search",url_result)
		#webbrowser.open_new_tab("http://www.youtube.com/watch?v=" + search_results[0])
		ydl_opts={}
		AudioIO.speak(usr + 'starting')
		veronica_notify(usr + ' starting')
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    ydl.download([url_result])
		AudioIO.speak(usr + 'completed')    
		veronica_notify(usr + ' completed')    
	except:
		AudioIO.speak('Could not download video try again later')
		veronica_notify('Could not download video try again later')		    

#youtube_mp4(url)
