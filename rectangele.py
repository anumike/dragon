from tkinter import colorchooser
import random
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()



def random_rectengle(wight, height, fill_color):
    x1 = random.randrange(wight)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(wight))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
c=colorchooser.askcolor()
random_rectengle(400,400, c[1])