import tkinter

window = tkinter.Tk()
button = tkinter.Button(window, text="don't press this button.", width=40)
button.pack(padx=10, pady=10)
clickCount = 0


def onClick(event):
    global clickCount
    clickCount += 1
    if clickCount == 1:
        button.config(text="seriously?Don't.Press.This.Button!")
    elif clickCount == 2:
        button.config(text="hah! button will disappear")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)

window.mainloop()
