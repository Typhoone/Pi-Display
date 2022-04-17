from time import sleep
from pprint import pprint
import argparse
import configparser
import schedule

from layout import drawLayout

from IT8951 import constants
from IT8951.display import AutoEPDDisplay

def main():

    print('Initializing Config...')

    config = configparser.ConfigParser()
    config.read('config.ini')
    print("Config Loaded:", config.sections())

    print('Initializing EPD...')

    # here, spi_hz controls the rate of data transfer to the device, so a higher
    # value means faster display refreshes. the documentation for the IT8951 device
    # says the max is 24 MHz (24000000), but my device seems to still work as high as
    # 80 MHz (80000000)
    display = AutoEPDDisplay(vcom=-1.55, rotate="CCW", spi_hz=24000000)
    print('VCOM set to', display.epd.get_vcom())

    print('Initializing buffer...')
    canvas = display.frame_buf
    print("Initialised")
    
    schedule.every(5).minutes.do(updateDisplay, canvas=canvas, config=config, display=display)
    print("Update Display Scheduled")
    updateDisplay(canvas, config, display)

    try:
        while True:
            schedule.run_pending()
            sleep(30)
    except KeyboardInterrupt:
        print('interrupted!')

    sleep(5)
    display.clear()
    print('Done!')

def updateDisplay(canvas, config, display):
    print("Updating Display...")
    drawLayout(canvas, config)
    print("Displaying Image...")
    display.draw_partial(constants.DisplayModes.GC16)
    print("Update Complete")

if __name__ == '__main__':
    main()
