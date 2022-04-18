from datetime import datetime
import json
from pprint import pprint
import sys
import textwrap
import requests
from widgets.common import *
from os.path import exists
from os import remove
from glob import glob

DAYFILE = "./day-in-history-cache-"

def get_day(API_KEY, APP_NAME):
    print("Getting day in History from API")

    today = datetime.now()
    date = today.strftime('%m/%d')

    
    url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/selected/' + date
    headers = {
        'Authorization': 'Bearer ' + API_KEY,
        'User-Agent': APP_NAME
        }

    res = requests.get(url, headers=headers)
    if (res.status_code==200):
        jsonRes=res.json()
        # pprint(jsonRes)
        return jsonRes
    else:
        print("Error getting day: ", res.status_code)
        sys.exit("Failed to get This Day in History")

def clean_old_files():
    fileList = glob(DAYFILE + "*.json")
    for filePath in fileList:
        try:
            print("Removing old file: ", filePath)
            remove(filePath)
        except:
            print("Error while deleting file : ", filePath)

def get_day_cache(API_KEY, APP_NAME):
    today = datetime.date(datetime.now())
    filename = DAYFILE + str(today) + ".json"
    print(filename)
    if (exists(filename)):
        print("Pulling Day in History from cache file")
        f = open(filename)
        return json.load(f)
    else:
        clean_old_files()
        QOD = get_day(API_KEY, APP_NAME)
        f = open(filename, "x")
        json.dump(QOD, f)
        return QOD

def get_day_mock(API_KEY, APP_NAME):
    f = open('day_mock.json')
    return json.load(f)

def process_day(API_KEY, APP_NAME):
    dayJSON = get_day_cache(API_KEY, APP_NAME)
    thisDay = dayJSON['selected'][0]
    dayText = thisDay["text"]
    dayExtract = thisDay["pages"][0]['extract']
    dayTitle = thisDay["pages"][0]['normalizedtitle']
    dayYear = thisDay["year"]

    subText = "~~ " + dayTitle + " " + str(dayYear) + " ~~"

    lineLim = 70
    dayText = textwrap.shorten(dayText, lineLim*4, placeholder="...")
    dayText = textwrap.fill(dayText, lineLim)

    return[dayText, subText]


def print_day(draw,x, y,  canvasWidth, API_KEY, APP_NAME):
    dayOb=process_day(API_KEY, APP_NAME)
    print(dayOb)

    xy = get_text_center_tuple(x +canvasWidth//2, y, dayOb[0])
    draw.multiline_text(xy, dayOb[0], font=DEFAULT_FONT, align="center")

    xy = get_text_center_tuple(x +canvasWidth//2, y+DEFAULT_FONT_SIZE*4, dayOb[1])
    draw.multiline_text(xy, dayOb[1], font=DEFAULT_FONT, align="center")
    


