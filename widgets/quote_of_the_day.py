from operator import concat
import textwrap
import requests
from widgets.common import *

def get_qod():
    print("Getting QOD")
    res = requests.get("https://quotes.rest/qod?language=en")
    if (res.status_code==200):
        jsonRes=res.json()
        print(jsonRes)
        return jsonRes["contents"]["quotes"][0]
    else:
        print("Error getting QOD: ", res.status_code==200)
        return {"quote": "Error Retirving QOD", "length": 19, "author": res.status_code} 

def get_qod_mock():
    return {"quote": "I keep asking myself these three questions.. What do you have? What do you want? What will you give up?", "length": 105, "author": "Jack Ma"}

def process_QOD():
    qodJSON = get_qod_mock()
    qod = qodJSON["quote"]
    qodAuthor = concat("Author: ", qodJSON["author"])


    lineLim = 70
    qod = textwrap.shorten(qod, lineLim*3, placeholder="...")
    qod = textwrap.fill(qod, lineLim)

    return[qod, qodAuthor]


def print_QOD(draw,x, y,  canvasWidth):
    qodOb=process_QOD()
    print(qodOb)

    xy = get_text_center_tuple(x +canvasWidth//2, y, qodOb[0])

    draw.multiline_text(xy, qodOb[0], font=DEFAULT_FONT, align="center")
    


