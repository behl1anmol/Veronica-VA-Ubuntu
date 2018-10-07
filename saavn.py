from subprocess import call
import os
def open_saavn():
	os.chdir("/home/anmol/Desktop/INNOTECH2K18/saavn/Saavn-linux-x64")
	call(["./Saavn"])
	return	