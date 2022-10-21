from tkinter import *

def doSomething(event):
    print("you pressed " + event.keysym)

window = Tk()

window.bind("<Return>",doSomething)
# window.bind("<Up>",doSomething)
# window.bind("<Key>",doSomething)


window.mainloop()
