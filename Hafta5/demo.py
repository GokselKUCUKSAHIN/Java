#edited for Python3, raspberry pi 3B, sh1106

from oled.device import sh1106
from oled.render import canvas
from PIL import ImageFont

font = ImageFont.load_default()
device = sh1106(port=1, address=0x3C)

with canvas(device) as draw:
    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = 2
    shape_width = 20
    top = padding
    bottom = device.height - padding - 1
    # Draw a rectangle of the same size of screen
    draw.rectangle((0, 0, device.width-1, device.height-1), outline=255, fill=0)
    # Move left to right keeping track of the current x position for drawing shapes.
    x = padding
    # Draw an ellipse.
    draw.ellipse((x, top, x+shape_width, bottom), outline=255, fill=0)
    x += shape_width + padding
    # Draw a rectangle.
    draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
    x += shape_width + padding
    # Draw a triangle.
    draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
    x += shape_width+padding
    # Draw an X.
    draw.line((x, bottom, x+shape_width, top), fill=255)
    draw.line((x, top, x+shape_width, bottom), fill=255)
    x += shape_width+padding

    # Load default font.
    font = ImageFont.load_default()

    # Alternatively load a TTF font.
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php
    # font = ImageFont.truetype('Minecraftia.ttf', 8)

    # Write two lines of text.
    draw.text((x, top),    'Hello',  font=font, fill=255)
    draw.text((x, top+20), 'World!', font=font, fill=255)
