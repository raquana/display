from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from time import strftime
from datetime import datetime
import time
import random

def getAvRGB(a, x, y):
    tot = a + x + y
    mult = 255 / float(tot)
    return int(a * mult)


def makeImage():
    lines = [line.rstrip('\n') for line in open("hc.dsp")]

    #text = (("Saturday 7th February, 2015",(135,26,227)),)
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    text = ((strftime("%H:%M  %a, %d-%b-%Y") + " HC: " + lines[0],(getAvRGB(r,g,b),getAvRGB(g,b,r),getAvRGB(b,r,g))),)
#    text = ((strftime("%H:%M               "),(getAvRGB(r,g,b),getAvRGB(g,b,r),getAvRGB(b,r,g))),)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 16)
    all_text = ""
    for text_color_pair in text:
        t = text_color_pair[0]
        all_text = all_text + t

#    print(all_text)
    width, ignore = font.getsize(all_text)
#    print(width)

    im = Image.new("RGB", (width + 30, 16), "black")
    draw = ImageDraw.Draw(im)

    x = 0;
    for text_color_pair in text:
        t = text_color_pair[0]
        c = text_color_pair[1]
#        print("t=" + t + " " + str(c) + " " + str(x))
        draw.text((x, 0), t, c, font=font)
        x = x + font.getsize(t)[0]

    im.save("test.ppm")

currentMinute = datetime.now().minute
makeImage()
while True:
    if currentMinute != datetime.now().minute:
        currentMinute = datetime.now().minute
        makeImage()
    time.sleep(2)
