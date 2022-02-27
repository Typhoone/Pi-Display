
from time import sleep
import argparse

from IT8951.display import AutoEPDDisplay



def main():

    print('Initializing EPD...')

    # here, spi_hz controls the rate of data transfer to the device, so a higher
    # value means faster display refreshes. the documentation for the IT8951 device
    # says the max is 24 MHz (24000000), but my device seems to still work as high as
    # 80 MHz (80000000)
    # display = AutoEPDDisplay(vcom=-1.55, rotate="CCW", spi_hz=24000000)
    # print('VCOM set to', display.epd.get_vcom())

    

    print('Done!')

if __name__ == '__main__':
    main()
