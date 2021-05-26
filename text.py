from tkinter import *
import time


tk=Tk()
canvas=Canvas(tk,width=900, height=900)
canvas.pack()
canvas.create_text(150,100, text='i run,')
canvas.create_text(130, 120,text='i run,')
canvas.create_text(190,200,text='i dont run!!')
time.sleep(10)