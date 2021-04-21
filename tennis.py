import tkinter
import time
from tkinter import messagebox

canvasWidth = 750
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
setBatTop = canvasWidth - 40
setBatBottom = canvasHeight - 30



def main_loop():
    while windowOpen == True:
        move_bat()
        # move_ball()
        window.update()
        print("-----")
        time.sleep(1)
        if windowOpen == True:
            check_game_over()


def on_key_press(event):
    global leftPressed, rightPressed
    if event.keysym == "left":
        leftPressed = 1
    elif event.keysym == "right":
        rightPressed = 1


def on_key_release(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "right":
        rightPressed = 0


def move_bat():
    batMove = batSpeed * rightPressed - batSpeed * leftPressed
    (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
    if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
        canvas.move(bat, batMove, 0)


def move_ball():
    global ballMoveX, ballMoveY
    (balleLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballMoveX > 0 and ballRight > canvasWidth:
        ballMoveX = -ballMoveX
    if ballMoveX > 0 and balleLeft < 0:
        ballMoveX = -ballMoveX
    if ballMoveY < 0 and ballTop < 0:
        ballMoveY = -ballMoveY
    if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
        (batLeft, batTop, batRight, BatBottom) = canvas.coords(bat)
        if ballRight > batLeft and balleLeft < batRight:
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
    canvas.coords(bat, 10, setBatTop, 50, setBatBottom)
    canvas.coords(ball, 20, setBatTop - 10, 30, setBatTop)


window.protocol("WM_DELETE_WINDOW", close)
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)
reset()
main_loop()
