
from time import sleep
import argparse
from PIL import Image, ImageDraw

from IT8951 import constants
from IT8951.display import AutoEPDDisplay

# widgets
from widgets.hello_world import *
from widgets.quote_of_the_day import print_QOD
from widgets.news import print_feeds

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

    print_QOD(draw, minX, 1000, canvasWidth)

    nzFeeds=["https://www.rnz.co.nz/rss/national.xml", "https://www.stuff.co.nz/rss"]
    print_feeds(draw, minX+10, 1100, canvasWidth//2, nzFeeds, "New Zealand")
    worldFeeds=["https://www.rnz.co.nz/rss/world.xml", "http://feeds.bbci.co.uk/news/rss.xml", "https://rss.nytimes.com/services/xml/rss/nyt/World.xml", "https://moxie.foxnews.com/feedburner/latest.xml"]
    print_feeds(draw, minX+canvasWidth//2, 1100, canvasWidth//2, worldFeeds, "World")

    display.draw_full(constants.DisplayModes.GC16)

    print('Done!')

    sleep(60)
    display.clear()

if __name__ == '__main__':
    main()
