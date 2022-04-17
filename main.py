
from time import sleep
import argparse
from PIL import Image, ImageDraw
import configparser

from IT8951 import constants
from IT8951.display import AutoEPDDisplay

# widgets
from widgets.hello_world import *
from widgets.quote_of_the_day import print_QOD
from widgets.news import print_feeds
from widgets.weather import print_weather
from widgets.header import print_header
from widgets.this_day_in_history import print_day

minX=30
minY=10
maxX=1345
maxY=1840
boarderFrameWidth=10
canvasWidth=maxX-minX
canvasHeight = maxY - minY

BLACK=0
WHITE=255

def main():

    print('Initializing Config...')

    config = configparser.ConfigParser()
    config.read('config.ini')
    print("Config Loaded:", config.sections())

    print('Initializing EPD...')

    # here, spi_hz controls the rate of data transfer to the device, so a higher
    # value means faster display refreshes. the documentation for the IT8951 device
    # says the max is 24 MHz (24000000), but my device seems to still work as high as
    # 80 MHz (80000000)
    display = AutoEPDDisplay(vcom=-1.55, rotate="CCW", spi_hz=24000000)
    print('VCOM set to', display.epd.get_vcom())

    print('Initializing buffer...')
    canvas = display.frame_buf
    draw = ImageDraw.Draw(canvas)

    print_header(draw, minX, minY, canvasWidth)

    print_weather(canvas, draw, minX + canvasWidth//2 - 325, minY+70, config['weather']['lat'], config['weather']['lon'], config['weather']['apikey'])
    lineOffset = 340
    draw.line([minX + canvasWidth//2 - lineOffset, minY+100, minX + canvasWidth//2 - lineOffset, 650])
    draw.line([minX + canvasWidth//2 + lineOffset, minY+100, minX + canvasWidth//2 + lineOffset, 650])

    draw.line([minX+40, 680, maxX-40, 680])
    print_day(draw, minX, 700, canvasWidth, config['dayInHistory']['token'], config['dayInHistory']['appName'])

    draw.line([minX+40, 880, maxX-40, 880])
    print_QOD(draw, minX, 1000, canvasWidth)

    draw.line([minX+40, 1080, maxX-40, 1080])
    print_feeds(draw, minX+10, 1100, canvasWidth//2, config['news']['localFeeds'].split(), config['news']['localFeedsName'])
    draw.line([canvasWidth//2, 1150, canvasWidth//2, maxY-50])
    print_feeds(draw, minX+10+canvasWidth//2, 1100, canvasWidth//2, config['news']['worldFeeds'].split(), "World")

    display.draw_full(constants.DisplayModes.GC16)

    print('Done!')

    sleep(60)
    display.clear()

if __name__ == '__main__':
    main()
