
from datetime import datetime
import json
from operator import concat
from pprint import pprint
from PIL import Image
from widgets.common import *
import requests

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
    canvas.paste(icon, (x-30, y), icon)
    print(iconFileName)

    feelsLike = 'Feels like: ' + str(round(data['current']['feels_like'])) + unitSymbol
    xy = get_text_center_tuple(x+weather_module_width//2, y+50, feelsLike)
    draw.text(xy, feelsLike, font=DEFAULT_FONT)

    todaysLow = round(data['daily'][0]['temp']['min'])
    todaysHigh = round(data['daily'][0]['temp']['max'])
    highLow = str(todaysLow) + unitSymbol + " ▽ |" + str(todaysHigh) +  unitSymbol+" ▲"
    xy = get_text_center_tuple(x+weather_module_width//2, y+100, highLow)
    draw.text(xy, highLow, font=DEFAULT_FONT)

def draw_forecast(canvas, draw, x, y, data, unitSymbol="°ᶜ"):
    dailyArr=data['daily']
    forecastWidth = 650
    forecastSep = forecastWidth//7
    # Skip first day as that is today
    for idx, day in enumerate(dailyArr[1:8]):
        dayName = datetime.utcfromtimestamp(day['dt']).strftime('%a')
        dayLow = round(day['temp']['min'])
        dayHigh = round(day['temp']['max'])
        # Day
        print(dayName, str(dayLow), str(dayHigh), idx)
        xy = get_text_center_tuple(x+((idx+0.5)*forecastSep), y, dayName)
        draw.text(xy, dayName, font=DEFAULT_FONT)

        # Separator
        if idx > 0 and idx < 7:
            draw.line([x+(idx*forecastSep), y, x+(idx*forecastSep), y+130])
        dayHighLowStr = str(dayLow) + "|" + str(dayHigh)

        # symbol
        iconName = day['weather'][0]['icon']
        iconFileName =  './assets/weather/' + iconName + '@2x.png'
        icon = Image.open(iconFileName)
        canvas.paste(icon, (x+((idx)*forecastSep), y+10), icon)

        # High Low
        xy = get_text_center_tuple(x+((idx+0.5)*forecastSep), y+90, dayHighLowStr)
        draw.text(xy, dayHighLowStr, font=DEFAULT_FONT)


def get_weather_mock(lat, long, apikey):
    f = open('weatherdata.json')
    return json.load(f)

def get_weather(lat, lon, apikey):
    reqURL="https://api.openweathermap.org/data/2.5/onecall?lat="+ str(lat) +"&lon=" + str(lon) + "&units=metric&appid=" + str(apikey)
    print(reqURL)
    res = requests.get(reqURL)
    if (res.status_code==200):
        jsonRes=res.json()
        return jsonRes
    else:
        print("Error getting Weather data: ", res.status_code)
        return get_weather_mock(lat, lon, apikey)

def print_weather(canvas, draw,x, y, lat, lon, apikey):
    print("Weather begin")
    data = get_weather(lat, lon, apikey)
    # pprint(data['current'])
    draw_current(canvas, draw, x, y, data)
    draw_forecast(canvas, draw, x, y+160, data)
    print("Weather End")
    return 0