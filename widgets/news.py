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

def drawItem(draw, x, y, item):
    lineLim = 40
    # pprint(item.nzTime.strftime("%a %H:%M %z"))
    # print("------")
    feedInfo = concat(item.feedTitle, item.nzTime.strftime("%a %H:%M"))
    title = textwrap.shorten(item.summary, lineLim*4, placeholder="...")
    title = textwrap.fill(title, lineLim)
    draw.multiline_text((x,y), title, font=DEFAULT_FONT, align="left")
    print(title)
    print("------")
    desc = textwrap.shorten(item.description, lineLim*2, placeholder="...")

    return 4

def getLatest(feeds, num = 5):
    items = []
    for feed in feeds:
        NewsFeed = feedparser.parse(feed)
        for entry in NewsFeed.entries:

            entry.feedTitle = ' '.join(NewsFeed.feed.title.split()[:2])
            # TODO: guse this to get favicon
            entry.RSSlink = NewsFeed.feed.link
            entry.nzTime=getTime(entry.published)
            items.append(entry)
    items.sort(key=lambda x: x.nzTime, reverse=True)

    return items[0:num]


def print_feeds(draw, x, y, width, feeds, title):
    itemsToPrint = getLatest(feeds)
    xpos = x + 5
    ypos = y

    xy = get_title_text_center_tuple(x+width//2, ypos, title)
    draw.text(xy, title, font=DEFAULT_TITLE_FONT, align="center")

    ypos = ypos + DEFAULT_TITLE_FONT_SIZE

    for item in itemsToPrint:
        # print(item.feedTitle, item.title, item.published)
        totalLines = drawItem(draw, xpos, ypos,item)
        ypos = ypos + (totalLines * DEFAULT_TITLE_FONT_SIZE)
            



