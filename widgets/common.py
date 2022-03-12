
from PIL import ImageFont

DEFAULT_FONT_PATH="/usr/share/fonts/TTF/DejaVuSans.ttf"
DEFAULT_FONT_SIZE = 30
DEFAULT_FONT = ImageFont.truetype(DEFAULT_FONT_PATH, DEFAULT_FONT_SIZE)

def draw_centered_text(draw, x, y, text, font=DEFAULT_FONT, fontsize=DEFAULT_FONT_SIZE):
    xy = get_text_center_tuple(x, y, text, font, fontsize)
    draw.text(xy, text, font=font)
    draw_border(draw, draw_x-10, draw_y-10, text_width+20, fontsize+20)

def get_text_center_tuple(x, y, text, font=DEFAULT_FONT, fontsize=DEFAULT_FONT_SIZE):
    text_width = 0
    lines = text.split("\n")
    for line in lines:
        line = line.replace("\n", "")
        tmp_width, tmp_hieght = font.getsize(line)
        if tmp_width > text_width:
            text_width = tmp_width
    
    text_width
    print(text_width)
    print(text)

    draw_x = x - text_width//2
    # draw_y = y + fontsize//2
    draw_y = y

    return (draw_x, draw_y)
    

def draw_border(draw, x, y, width, height, thickness = 5):
    xy=[(x,y),(x+width, y+height)]
    draw.rectangle(xy, width=thickness)


