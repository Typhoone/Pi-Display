from datetime import datetime
import json
from operator import concat
from pprint import pprint
import sys
import textwrap
import requests
from widgets.common import *
from os.path import exists
from os import remove
from glob import glob

QODFILE = "./QOD-cache-"


def get_qod():
    print("Getting QOD from API")
    res = requests.get("https://quotes.rest/qod?language=en")
    if (res.status_code==200):
        jsonRes=res.json()
        print(jsonRes)
        return jsonRes
    else:
        print("Error getting QOD: ", res.status_code==200)
        sys.exit("QOD can not load for some reason")

def clean_old_files():
    fileList = glob(QODFILE + "*.json")
    for filePath in fileList:
        try:
            print("Removing old file: ", filePath)
            remove(filePath)
        except:
            print("Error while deleting file : ", filePath)

def get_qod_cache():
    today = datetime.date(datetime.now())
    filename = QODFILE + str(today) + ".json"
    print(filename)
    if (exists(filename)):
        print("Pulling QOD from cache file")
        f = open(filename)
        return json.load(f)
    else:
        clean_old_files()
        QOD = get_qod()
        f = open(filename, "x")
        json.dump(QOD, f)
        return QOD

def get_qod_mock():
    print('Pullinng QOD from Mock')
    f = open('QOD_mock.json')
    return json.load(f)

def process_QOD():
    qodJSON = get_qod_cache()
    quote = qodJSON["contents"]["quotes"][0]
    qod = quote["quote"]
    qodAuthor = quote["author"]
    date = datetime.strptime(quote['date'], '%Y-%m-%d').strftime('%d/%m/%y')
    authourText = "~~ " + qodAuthor + " ~~"

    lineLim = 70
    qod = textwrap.shorten(qod, lineLim*3, placeholder="...")
    qod = textwrap.fill(qod, lineLim)

    return[qod, authourText]


def print_QOD(draw,x, y,  canvasWidth):
    qodOb=process_QOD()
    print(qodOb)

    xy = get_text_center_tuple(x +canvasWidth//2, y, qodOb[0])
    draw.multiline_text(xy, qodOb[0], font=DEFAULT_FONT, align="center")

    xy = get_text_center_tuple(x +canvasWidth//2, y+DEFAULT_FONT_SIZE*4, qodOb[1])
    draw.multiline_text(xy, qodOb[1], font=DEFAULT_FONT, align="center")


    


