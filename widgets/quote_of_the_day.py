from datetime import datetime
import json
from operator import concat
from pprint import pprint
import textwrap
import requests
from widgets.common import *


def get_qod():
    print("Getting QOD")
    res = requests.get("https://quotes.rest/qod?language=en")
    if (res.status_code==200):
        jsonRes=res.json()
        print(jsonRes)
        return jsonRes
    else:
        print("Error getting QOD: ", res.status_code==200)
        return {"quote": "Error Retirving QOD", "length": 19, "author": res.status_code} 

def get_qod_mock():
    f = open('QOD_mock.json')
    return json.load(f)

def process_QOD():
    qodJSON = get_qod_mock()
    quote = qodJSON["contents"]["quotes"][0]
    qod = quote["quote"]
    qodAuthor = quote["author"]
    date = datetime.strptime(quote['date'], '%Y-%m-%d').strftime('%d/%m/%y')
    authourText = "~~ " + qodAuthor + " " + date + " ~~"

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
    


