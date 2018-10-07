from __future__ import unicode_literals
import youtube_dl
from settings import MP3_DIR, veronica_notify
from os import chdir, system
import urllib.request
import AudioIO
import urllib.parse
import re

#url=input("enter video name to download")

def youtube_mp3(usr):
	chdir(MP3_DIR)
	try:		
		query_string=urllib.parse.urlencode({"search_query" : usr})
		html_content=urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
		search_results=re.findall(r'href=\"\/watch\?v=(.{11})',html_content.read().decode())
		url_result="http://www.youtube.com/watch?v=" + search_results[0] 
		print("result of search",url_result)
		#webbrowser.open_new_tab("http://www.youtube.com/watch?v=" + search_results[0])
		ydl_opts = {
		    'format': 'bestaudio/best',
		    'postprocessors': [{
		        'key': 'FFmpegExtractAudio',
		        'preferredcodec': 'mp3',
		        'preferredquality': '192',
		    }],
		}
		AudioIO.speak(usr + 'starting')
		veronica_notify(usr + ' starting')
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    ydl.download([url_result])
		AudioIO.speak(usr + 'complete')    
		veronica_notify(usr + ' complete')    
	except:
		AudioIO.speak('Could not download audio try later')
		veronica_notify('Could not download audio try later')	    

#youtube_mp3(url)
