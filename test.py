from time import sleep
from pprint import pprint
import argparse
import configparser
import schedule

from layout import drawLayout, testCanvas 


def main():

    config = configparser.ConfigParser()
    config.read('config.ini')
    print("Config Loaded:", config.sections())
    pprint(config['weather'])

    print('Initializing buffer...')
    canvas = testCanvas()
    print("Initialised")
    
    schedule.every(10).seconds.do(updateDisplay, canvas=canvas, config=config)
    print("Update Display Scheduled")
    updateDisplay(canvas, config)

    try:
        while True:
            schedule.run_pending()
            sleep(1)
    except KeyboardInterrupt:
        print('interrupted!')
    
    print('Done!')

def updateDisplay(canvas, config):
    print("Updating Display...")
    drawLayout(canvas, config)
    print("Saving Image...")
    canvas.save("display.png")
    print("Update Complete")

if __name__ == '__main__':
    main()
