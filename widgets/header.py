import subprocess
from datetime import datetime

from widgets.common import *

WhiteText=(255,255,255,0)

def draw_wifi(draw, x, y, width):
    # https://www.iconsdb.com/black-icons/black-wifi-icons.html
    wifiStrength = subprocess.run(['awk', 'NR==3 {print $3}', '/proc/net/wireless'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    if not wifiStrength:
        wifiStrength = "??"
    else:
        wifiStrength = wifiStrength.replace(".","")
    print("Wifi Stength: ", wifiStrength)

def printUpdateTime(draw, x, y, width):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)
    xy = get_text_center_tuple(x, y, current_time)
    draw.text(xy, current_time, fill=255, font=DEFAULT_FONT)


def print_header(draw, x, y, width):
    draw.rectangle([x,y,x+width, y+50], fill=0)
    # draw_wifi(draw, x, y, width)
    printUpdateTime(draw, x+(width/2), y+10, width)
    
