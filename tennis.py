import tkinter
import time
import random
from tkinter import messagebox

canvasWidth = 850
canvasHeight = 500
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
canvas.pack()
bat = canvas.create_rectangle(0, 0, 40, 10, fill="dark turquoise")
ball = canvas.create_oval(0, 0, 10, 10, fill="deep pink")
windowOpen = True

leftPressed = 0
rightPressed = 0
batSpeed = 6
ballMoveX = 4
ballMoveY = -4
setBatTop = canvasHeight - 40
setBatBottom = canvasHeight - 30
gameSpeedDelay = 0.1

score = 0
def move_ball():
global ballMoveX, ballMoveY, score
ballMoveY= -ballMoveY
def  score()
    def main_loop():






        def move_ball():


def on_key_press(event):
        global leftPressed, rightPressed
        if event.keysym == "Left":
            leftPressed = 1
        elif event.keysym == "Right":
            rightPressed = 1


def on_key_release(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0


def move_bat():
    batMove = batSpeed * rightPressed - batSpeed * leftPressed
    (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
    if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
        canvas.move(bat, batMove, 0)


def move_ball():
    global ballMoveX, ballMoveY
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballMoveX > 0 and ballRight > canvasWidth:
        ballMoveX = -ballMoveX
    if ballMoveX < 0 and ballLeft < 0:
        ballMoveX = -ballMoveX
    if ballMoveY < 0 and ballTop < 0:
        ballMoveY = -ballMoveY
    if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
        (batLeft, batTop, batRight, BatBottom) = canvas.coords(bat)
        if ballRight > batLeft and ballLeft < batRight:
            ballMoveY = -ballMoveY
    canvas.move(ball, ballMoveX, ballMoveY)


def check_game_over():
    (ballLeft, BallTop, ballRight, BallBottom) = canvas.coords(ball)
    print(BallTop)
    print(canvasHeight)
    if BallTop > canvasHeight:
        playAgain = tkinter.messagebox.askyesno(message="Do you want playAgin?")
        if playAgain == True:
            reset()
        else:
            close()


def close():
    global windowOpen
    windowOpen = False
    window.destroy()


def reset():
    global leftPressed, rightPressed
    global ballMoveX, ballMoveY
    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY = -4
    ballStartX = random.randint(20, canvasWidth - 10)
    canvas.coords(bat, 10, setBatTop, 50, setBatBottom)
    canvas.coords(ball, ballStartX, setBatTop - 10, ballStartX + 10, setBatTop)


window.protocol("WM_DELETE_WINDOW", close)
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)

reset()
main_loop():

