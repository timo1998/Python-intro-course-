from tkinter import *

count = 0

def click():
    global count
    count += 1
    print("You clicked the button")


window = Tk()

photo = PhotoImage(file = "C:\\Users\\Timor\\OneDrive\\Python\\Course\\speaker (1).png")

button = Button(window,
                text = "click me!",
                command = click,
                font = ("Comic Sans",30),
                fg = "Orange",
                bg = "black",
                activeforeground = "Orange",
                activebackground = "black",
                state = ACTIVE,
                image = photo,
                compound = 'bottom'
                )

button.pack()

window.mainloop()
