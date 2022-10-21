from tkinter import *
def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()

text = Text(window,
            bg = "yellow",
            font = ("Ink Free",25),
            height = 8,
            width = 20,
            padx = 20,
            pady = 20,
            fg = "Purple")
text.pack()

button = Button(window,command=submit,text="submit")
button.pack()


window.mainloop()
