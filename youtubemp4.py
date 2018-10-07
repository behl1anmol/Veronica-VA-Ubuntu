import youtube_dl as ydl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download(['https://www.youtube.com/watch?v=0VwgpYJ4q38'])
