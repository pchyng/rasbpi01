import sys
import time
import ST7789

from datetime import datetime

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


print("""
Test de imagenes en pantalla LCD 1.3"

""")
MESSAGE = datetime.now().strftime("%H:%M:%S")
#MESSAGE = "PCHYNG Test"
	
display_type = "square"
disp = ST7789.ST7789(
	port=0,
	cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
	dc=9,
	backlight=19,               # 18 for back BG slot, 19 for front BG slot.
	spi_speed_hz=80 * 1000 * 1000,
	offset_left=0 if display_type == "square" else 40,
	offset_top=53 if display_type == "rect" else 0
)

# Initialize display.
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height


img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)

size_x, size_y = draw.textsize(MESSAGE, font)

text_x = disp.width
text_y = (disp.height - size_y) // 2

t_start = time.time()

while True:
    x = (time.time() - t_start) * 100
    x %= (size_x + disp.width)
    draw.rectangle((0, 0, disp.width, disp.height), (0, 0, 0))
    draw.text((int(text_x - x), text_y), MESSAGE, font=font, fill=(255, 255, 255))
    disp.display(img)
