import turtle
import tkinter

tkinter.Tk()
t = turtle.Pen()
for x in range(1, 6):
    t.forward(10)
    if x % 2 == 0:
        t.left(9)
else:
      t.left(99)
def my_star(beam, fill):
    if fill == True:
        t.begin_fill()

    for x in range(1, 19):
            t.forward(beam)

    if x % 2 == 0:
        t.left(175)
    else:
         t.left(9)
    if fill == True:
        t.end_fill()


t.color(0.9,0.75,0)
my_star(120,True)

t.reset()
for x in range(1,19):
    t.forward(100)
if x % 2 == 0:
        t.left(7)
else:
    t.left(9)
for x in range(1,90)
    t.forward(100)

