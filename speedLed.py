import time
import os
import re
import subprocess
import json

from rgbmatrix5x5 import RGBMatrix5x5
from datetime import datetime

def calcColour(iValue):
	r=0
	g=0
	if iValue < 25:
		r=0
		g=255
	elif iValue >75:
		r=255
		g=0
	else:
		r=int((iValue - 25)*5.1)
		g=255-r
	return (r, g, 0)
	
oColor = {
	"ok" : (26, 128, 156),
	"mh" : (255, 94, 5),
	"ko" : (194, 24, 7)
}

#Preconfiguracion del componente RGBMatrix5x5
rgbmatrix5x5 = RGBMatrix5x5()
rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.4)
bitTobyte=1048576
while True:
	response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr --format=json', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
	json_object = json.loads(response)
	#print(json_object)
	#print("\n\n")
	ping =json_object['ping']
	download = ((json_object['download']['bytes']/bitTobyte)/(json_object['download']['elapsed']/1000))*(json_object['download']['bandwidth']/bitTobyte)
	upload = ((json_object['upload']['bytes']/bitTobyte)/(json_object['upload']['elapsed']/1000))*(json_object['upload']['bandwidth']/bitTobyte)
	colUpload  = oColor['ok'] if upload > 120 else oColor['mh'] if upload > 100 else oColor['ko']
	colDownload= oColor['ok'] if download > 120 else oColor['mh'] if download > 100 else oColor['ko']
	print(json_object['timestamp'],", Upload: ",str(round(upload, 2)) ,", Download: ",str(round(download, 2)))
	a=0
	while a <= 10:
	#	rgbmatrix5x5.set_multiple_pixels(aToLed, oColor[current_timeAMPM])
		rgbmatrix5x5.set_multiple_pixels([0,5,10,15,20], colUpload)
		rgbmatrix5x5.set_multiple_pixels([1,6,11,16,21], colUpload)
		rgbmatrix5x5.set_multiple_pixels([3,8,13,18,23], colDownload)
		rgbmatrix5x5.set_multiple_pixels([4,9,14,19,24], colDownload)
		rgbmatrix5x5.show()
		time.sleep(1)
		rgbmatrix5x5.set_all(0, 0, 0)
		rgbmatrix5x5.show()
		time.sleep(1)
		a += 1
	time.sleep(600)

	

