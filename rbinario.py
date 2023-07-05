#Reloj binario
import time
from rgbmatrix5x5 import RGBMatrix5x5
from datetime import datetime

print("""
	Reloj binario v-0.0.1
	falta saber pintar por arrays :S
	rgbmatrix5x5.set_multiple_pixels([1, 3],  (26, 128, 156))
	00 05 10 15 20
	01 06 11 16 21
	02 07 12 17 22
	03 08 13 18 23
	04 09 14 19 24
	
	am = 3,4
	pm = 0,1
	
	para calcular la columna sumamos 5 al led de oLeds por cada espacio a la derecha
	

""")
oLeds = {
	"0" : [],
	"1" : [4],
	"2" : [3],
	"3" : [3,4],
	"4" : [2],
	"5" : [2,4],
	"6" : [2,3],
	"7" : [2,3,4],
	"8" : [1],
	"9" : [1,4],
	
}
oColor = {
	"AM" : (26, 128, 156),
	"PM" : (188, 26, 154)
}
def numToBinled(sNumber,sRow):
	lRet = []
	for x in oLeds[sNumber]:
		lRet.append( x + ( sRow * 5 ) )
	return lRet
	
#Preconfiguracion del componente RGBMatrix5x5
rgbmatrix5x5 = RGBMatrix5x5()
rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.4)

oldH1=''
oldH2=''
oldM1=''
oldM2=''
oldDT=''

while True:
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	current_timeS = now.strftime("%S")
	current_timeM = now.strftime("%M")
	current_timeH = now.strftime("%H")
	current_timeAMPM = now.strftime("%p")
	
	if oldH1 != current_timeH[0]:
		rgbmatrix5x5.set_multiple_pixels([5,6,7,8,9], (0, 0, 0))
		oldH1 = current_timeH[0]
	if oldH2 != current_timeH[1]:
		rgbmatrix5x5.set_multiple_pixels([10,11,12,13,14], (0, 0, 0))
		oldH2 = current_timeH[1]
	if oldM1 != current_timeM[0]:
		rgbmatrix5x5.set_multiple_pixels([15,16,17,18,19], (0, 0, 0))
		oldM1 = current_timeM[0]
	#if oldM2 != current_timeM[2]:
	rgbmatrix5x5.set_multiple_pixels([20,21,22,23,24], (0, 0, 0))

	#rgbmatrix5x5.clear()
	rgbmatrix5x5.show()
	time.sleep(1)
	
	col1 = numToBinled(current_timeH[0],1)
	col2 = numToBinled(current_timeH[1],2)
	col3 = numToBinled(current_timeM[0],3)
	col4 = numToBinled(current_timeM[1],4)
	
	aToLed = []
	aToLed.extend(col1)
	aToLed.extend(col2)
	aToLed.extend(col3)
	aToLed.extend(col4)
	
	rgbmatrix5x5.set_multiple_pixels(aToLed, oColor[current_timeAMPM])
	print(current_time)
	rgbmatrix5x5.show()
	time.sleep(1)
	
