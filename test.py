from time import sleep
from pprint import pprint
import argparse
import configparser

from layout import drawLayout, testCanvas


def main():

    config = configparser.ConfigParser()
    config.read('config.ini')
    print("Config Loaded:", config.sections())
    pprint(config['weather'])

    print('Initializing buffer...')
    canvas = testCanvas()
    
    drawLayout(canvas, config)

    print("Saving Image...")
    canvas.save("display.png")
    
    print('Done!')

    

if __name__ == '__main__':
    main()
