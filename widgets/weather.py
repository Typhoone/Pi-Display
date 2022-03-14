
import json
from operator import concat
from pprint import pprint
from PIL import Image
from widgets.common import *

weather_module_width=650

def draw_current(canvas, draw, x, y, data, unitSymbol="°ᶜ"):
    currentTemp = concat(str(round(data['current']['temp'])), unitSymbol)
    print("Current Temp", currentTemp)
    currentTempX = x+weather_module_width
    bigFont= ImageFont.truetype(DEFAULT_FONT_PATH, 90)
    xy = get_text_right_tuple(currentTempX, y+50, currentTemp, bigFont)
    draw.text(xy, currentTemp, font=bigFont)

    iconName = data['current']['weather'][0]['icon']
    iconFileName =  './assets/weather/' + iconName + '@4x.png'
    icon = Image.open(iconFileName)
    canvas.paste(icon, (x, y), icon)
    print(iconFileName)

    feelsLike = 'Feels like: ' + str(round(data['current']['feels_like'])) + unitSymbol
    xy = get_text_center_tuple(x+weather_module_width//2, y+50, feelsLike)
    draw.text(xy, feelsLike, font=DEFAULT_FONT)

    todaysLow = round(data['daily'][0]['temp']['min'])
    todaysHigh = round(data['daily'][0]['temp']['max'])
    highLow = str(todaysLow) + unitSymbol + " ▽ |" + str(todaysHigh) +  unitSymbol+" ▲"
    xy = get_text_center_tuple(x+weather_module_width//2, y+100, highLow)
    draw.text(xy, highLow, font=DEFAULT_FONT)

def get_weather_mock(lat, long, apikey):
    f = open('weatherdata.json')
    return json.load(f)

def print_weather(canvas, draw,x, y, lat, long, apikey):
    data = get_weather_mock(lat, long, apikey)
    # pprint(data['current'])
    draw_current(canvas, draw, x, y, data)
    return 0