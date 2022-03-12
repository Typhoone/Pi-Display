from tkinter import font

from widgets.common import draw_centered_text



def print_hello_world(draw, x, y, text="Hello World"):
    draw.text((x,y), text)


def print_hello_world_centered(draw, x, y, text="Hello World"):
    draw_centered_text(draw, x, y, text)
