from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Timor\\OneDrive\\Python\\Course",
                                          title = "Open file",
                                          filetypes = (("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,'rt')
    print(file.read())
    file.close()


window = Tk()

button = Button(window,
                text="Open a file",
                command = openFile)

button.pack()

window.mainloop()