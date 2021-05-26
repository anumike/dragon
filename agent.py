from  tkinter import *
import random
import time

class Game:
    def _int_(self):
        self.tk =Tk()
        self.tk.title("agent-cane run for exit")
        self.tk.resizable(0,.0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk,wight=500,height=500,/hightlightthickness=0)
        self.canvas.pack()
        self.tk.update()wight=500
        self.canvas_height = 500
        self.canvas_wight=500
        self.bg = PhotoImage(file="background.gif")
        w = self.bg.width()
        h = self.bg.height()
        for