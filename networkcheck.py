import socket

def connected():
	try:
		socket.create_connection(("www.google.com",80))
		return True
	except 	OSError:
		pass
	return False

if connected()==True:
	print("connected")
else:
	print("not connected")	