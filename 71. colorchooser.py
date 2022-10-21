from tkinter import *
from tkinter import colorchooser, Tk


def click():
    # color = colorchooser.askcolor()
    # colorhex = color[1]
    # window.config(bg=colorhex)
    window.config(bg=colorchooser.askcolor()[1])

window: Tk = Tk()

window.geometry("420x420")

button = Button(text='click me',command=click)

button.pack()

window.mainloop()
