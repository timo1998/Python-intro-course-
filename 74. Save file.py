from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir = "C:\\Users\\Timor\\OneDrive\\Python\\Course",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file",".html"),
                                        ("all files",".*")
                                    ])
    if file is None:
        return

    #filetext = str(text.get(1.0,END))
    filetext = input("Enter some text i guess: ") #Tekst ingeven in de prompt
    file.write(filetext)
    file.close()


window = Tk()

button = Button(window,
                text = "save",
                command = saveFile)

text = Text(window)
text.pack()

button.pack()

window.mainloop()