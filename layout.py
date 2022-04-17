from PIL import Image, ImageDraw

# widgets
from widgets.hello_world import *
from widgets.quote_of_the_day import print_QOD
from widgets.news import print_feeds
from widgets.weather import print_weather
from widgets.header import print_header
from widgets.this_day_in_history import print_day

minX=30
minY=10
maxX=1375
maxY=1850
boarderFrameWidth=10
canvasWidth=maxX-minX
canvasHeight = maxY - minY

BLACK=0
WHITE=255

def drawLayout(canvas, config):
    draw = ImageDraw.Draw(canvas)
    print_header(draw, minX, minY, canvasWidth)

    print_weather(canvas, draw, minX + canvasWidth//2 - 325, minY+70, config['weather']['lat'], config['weather']['lon'], config['weather']['apikey'])
    lineOffset = 340
    draw.line([minX + canvasWidth//2 - lineOffset, minY+100, minX + canvasWidth//2 - lineOffset, 650])
    draw.line([minX + canvasWidth//2 + lineOffset, minY+100, minX + canvasWidth//2 + lineOffset, 650])

    draw.line([minX+40, 680, maxX-40, 680])
    print_day(draw, minX, 700, canvasWidth, config['dayInHistory']['token'], config['dayInHistory']['appName'])

    draw.line([minX+40, 880, maxX-40, 880])
    print_QOD(draw, minX, 900, canvasWidth)

    draw.line([minX+40, 1080, maxX-40, 1080])
    print_feeds(draw, minX+10, 1100, canvasWidth//2, config['news']['localFeeds'].split(), config['news']['localFeedsName'])
    draw.line([canvasWidth//2, 1150, canvasWidth//2, maxY-50])
    print_feeds(draw, minX+10+canvasWidth//2, 1100, canvasWidth//2, config['news']['worldFeeds'].split(), "World")

    draw.rectangle([minX,minY,maxX,maxY],outline=BLACK)

def testCanvas():
    return Image.new('1', (canvasWidth+50, canvasHeight+50), WHITE)
