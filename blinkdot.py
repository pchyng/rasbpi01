import time
from rgbmatrix5x5 import RGBMatrix5x5

print("""
Test de librerías RGBMatrix5x5
""")
#Funciones dentro de la librería
'''
	set_clear_on_exit(self, value=true)
	set_gamma(self, gamma_table)
	clear(self)
	set_brightness(self, brightness)
	set_all(self, r, g, b, brightness=1.0)
	set_pixel(self, x, y, r, g, b, brightness=1.0)
	set_multiple_pixels(self, indexes, from_colour, to_colour=None)
	show(self)
	
	
'''
rgbmatrix5x5 = RGBMatrix5x5()
rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.4)

#RGB  26, 188, 156 

colores = [
    (0xff, 0x00, 0x00),
    (0x00, 0xff, 0x00),
    (0x00, 0x00, 0xff)
]
xIndex = 0
r, g, b = colores.pop(0)

while True:
		#print(list(range(1, 25, 2)))
		#colores.append((r, g, b))
		#rgbmatrix5x5.set_all('26', '128', '156')
		#print((r, g, b))
		#rgbmatrix5x5.set_multiple_pixels([1, 3],  (26, 128, 156))
		rgbmatrix5x5.clear()
		rgbmatrix5x5.set_pixel(xIndex,0,'26', '128', '156')
		rgbmatrix5x5.show()
		time.sleep(0.5)
		rgbmatrix5x5.clear()
		rgbmatrix5x5.set_pixel(xIndex,1,'26', '128', '156')
		rgbmatrix5x5.show()
		time.sleep(0.5)
		rgbmatrix5x5.clear()
		rgbmatrix5x5.set_pixel(xIndex,2,'26', '128', '156')
		rgbmatrix5x5.show()
		time.sleep(0.5)
		rgbmatrix5x5.clear()
		rgbmatrix5x5.set_pixel(xIndex,3,'26', '128', '156')
		rgbmatrix5x5.show()
		time.sleep(0.5)
		rgbmatrix5x5.clear()
		rgbmatrix5x5.set_pixel(xIndex,4,'26', '128', '156')
		rgbmatrix5x5.show()
		time.sleep(0.5)
		xIndex = 0 if xIndex == 4 else xIndex+1
