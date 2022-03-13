from time import sleep
from PIL import Image, ImageDraw

import argparse


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

    print('Initializing buffer...')
    canvas = Image.new('1', (canvasWidth, canvasHeight), WHITE)
    draw = ImageDraw.Draw(canvas)

    draw.rectangle([minX,minY,maxX,maxY],outline=BLACK)

    # print_hello_world_centered(draw, canvasWidth//2, canvasHeight//2, "I keep asking myself these three questions.. What do you have? What do")

    print_QOD(draw, minX, 1000, canvasWidth)

    nzFeeds=["https://www.rnz.co.nz/rss/national.xml"]
    print_feeds(draw, minX+10, 1100, canvasWidth//2, nzFeeds, "New Zealand")
    worldFeeds=["https://www.rnz.co.nz/rss/world.xml", "http://feeds.bbci.co.uk/news/rss.xml", "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"]
    print_feeds(draw, minX+canvasWidth//2, 1100, canvasWidth//2, worldFeeds, "World")


    print("Saving Image...")
    canvas.save("display.png")
    
    print('Done!')

if __name__ == '__main__':
    main()
