import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import subprocess
import time

#text = (("Happy", (0, 255, 0)), (" Birthday", (255, 28, 28)), (" Andrew, you're the best!", (85, 85, 255)))
#text = (("Holly, in ", (255, 100, 100)), (" St Davids ", (255, 255, 0)), (" is the best . . . . . (and so is Benj)", (0, 5, 255)))
#text = (("Holly is lovely . . .       ", (255, 55, 55)), ("Robyn is scruffly . . .       ", (55, 255, 55)), ("Benjamin is great . . ." , (55, 55, 255)))
#text = (("H a p p y  H a l l o l w e e n  .  .  .", (142, 79, 8)), ("Get SWEETS from the coffin if you dare . . . ",(135,26,227)))
text = (("Saturday 7th February, 2015",(135,26,227)),)


font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 16)
all_text = ""
for text_color_pair in text:
    t = text_color_pair[0]
    all_text = all_text + t

print(all_text)
width, ignore = font.getsize(all_text)
print(width)


im = Image.new("RGB", (width + 30, 16), "black")
draw = ImageDraw.Draw(im)

x = 0;
for text_color_pair in text:
    t = text_color_pair[0]
    c = text_color_pair[1]
    print("t=" + t + " " + str(c) + " " + str(x))
    draw.text((x, 0), t, c, font=font)
    x = x + font.getsize(t)[0]

im.save("test.ppm")

#os.system("../rpi-rgb-led-matrix/led-matrix 1 test.ppm")

proc = subprocess.Popen(['../rpi-rgb-led-matrix/led-matrix','1','test.ppm'],stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
print "Process Id: " + str(proc.pid)
time.sleep(5)
print "Stopping"
