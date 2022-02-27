from time import sleep
from PIL import Image, ImageDraw


import argparse

minX=30
minY=10
maxX=1345
maxY=1840
boarderFrameWidth=10
canvasWidth=maxX-minX
canvasHeight = maxY - minY

BLACK=0
WHITE=255


def main():

    print('Initializing buffer...')
    canvas = Image.new('1', (canvasWidth, canvasHeight), WHITE)
    draw = ImageDraw.Draw(canvas)

    

    print("Saving Image...")
    canvas.save("display.png")
    
    print('Done!')

if __name__ == '__main__':
    main()
