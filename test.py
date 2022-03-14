from time import sleep
from PIL import Image, ImageDraw

import argparse


# widgets
from widgets.hello_world import *
from widgets.quote_of_the_day import print_QOD
from widgets.news import print_feeds
from widgets.weather import print_weather
from widgets.header import print_header

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

    print('Initializing buffer...')
    canvas = Image.new('1', (canvasWidth, canvasHeight), WHITE)
    draw = ImageDraw.Draw(canvas)


    # print_hello_world_centered(draw, canvasWidth//2, canvasHeight//2, "I keep asking myself these three questions.. What do you have? What do")

    print_header(draw, minX, minY, canvasWidth)

    draw.line([minX+40, 880, maxX-40, 880])
    print_QOD(draw, minX, 900, canvasWidth)

    draw.line([minX+40, 1080, maxX-40, 1080])
    nzFeeds=["https://www.rnz.co.nz/rss/national.xml", "https://www.stuff.co.nz/rss"]
    print_feeds(draw, minX+10, 1100, canvasWidth//2, nzFeeds, "New Zealand")
    draw.line([canvasWidth//2, 1150, canvasWidth//2, maxY-50])
    worldFeeds=["https://www.rnz.co.nz/rss/world.xml", "http://feeds.bbci.co.uk/news/rss.xml", "https://rss.nytimes.com/services/xml/rss/nyt/World.xml", "https://moxie.foxnews.com/feedburner/latest.xml"]
    print_feeds(draw, minX+10+canvasWidth//2, 1100, canvasWidth//2, worldFeeds, "World")

    print_weather(canvas, draw, minX + canvasWidth//2 - 325, minY+70, -41.2866, 174.7756, "foobar")


    draw.rectangle([minX,minY,maxX,maxY],outline=BLACK)
    print("Saving Image...")
    canvas.save("display.png")
    
    print('Done!')

    

if __name__ == '__main__':
    main()
