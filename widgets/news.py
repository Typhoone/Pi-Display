# Configurable to show local and international news, need to figure out how to do that, perhaps with a datasource middleware
# pip install feedparser
from operator import concat
from datetime import datetime
from pprint import pprint
import feedparser
import textwrap
from pytz import timezone

from widgets.common import *

def getTime(publishedTime):
    publishedTime = publishedTime.replace("GMT", "+0000")
    try:
        date = datetime.strptime(publishedTime, "%a, %d %b %Y %H:%M:%S %z")
    except:
        date = datetime.strptime(publishedTime, "%a, %d %b %Y %H:%M:%S %Z")
        print("God damn timezones causing me troubles: ", publishedTime)
    tz = timezone('Pacific/Auckland')
    date = date.astimezone(tz)
    return date

def drawItem(draw, x, y, entry, width, lineLim = 38, numOfLines=4):
    # pprint(item.nzTime.strftime("%a %H:%M %z"))
    # print("------")
    feedInfo = " ".join([entry.feedTitle, entry.localTime.strftime("%H:%M")])
    title = textwrap.shorten(entry.summary, lineLim*numOfLines, placeholder="...")
    title = textwrap.fill(title, lineLim)
    draw.multiline_text((x,y), title, font=DEFAULT_FONT, align="left")
   
    numOfLines = title.count('\n')
    ypos=y + (numOfLines+1.1)*DEFAULT_FONT_SIZE+15
    xy = get_text_right_tuple(x+width-50, ypos, feedInfo)
    draw.text(xy, feedInfo, font=DEFAULT_FONT)

    return numOfLines+1

def getLatest(feeds, num = 3):
    items = []
    for feed in feeds:
        NewsFeed = feedparser.parse(feed)
        for entry in NewsFeed.entries:

            entry.feedTitle = NewsFeed.feed.title.split()[0]
            # TODO: guse this to get favicon
            entry.RSSlink = NewsFeed.feed.link
            entry.localTime=getTime(entry.published)
            items.append(entry)
    items.sort(key=lambda x: x.localTime, reverse=True)

    return items[0:num]


def print_feeds(draw, x, y, width, feeds, title):
    itemsToPrint = getLatest(feeds)
    xpos = x
    ypos = y

    xy = get_title_text_center_tuple(x+width//2, ypos, title)
    draw.text(xy, title, font=DEFAULT_TITLE_FONT)

    ypos = ypos + DEFAULT_TITLE_FONT_SIZE + 10

    for item in itemsToPrint:
        print(ypos)
        totalLines = drawItem(draw, xpos, ypos,item, width)
        ypos = ypos + 230
            



