from tkinter import *

def openFile():
    print("file has been opened")

def saveFile():
    print("File has been saved")

def cut():
    print("You cut something")

def coppy():
    print("You paste something")

def paste():
    print("You coppy something")

window = Tk()

openImage = PhotoImage(file="speaker (1).png")

menubar = Menu(window)

window.config(menu=menubar)

fileMenu = Menu(menubar,
                tearoff=0, #getting rid of the tear off
                font = ("MV Boli",15))


menubar.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="Open",command = openFile,image=openImage,compound='left')
fileMenu.add_command(label="Save", command = saveFile)
fileMenu.add_separator() #adding a break line
fileMenu.add_command(label="Exit", command = quit)

editMenu = Menu(menubar,
                tearoff = 0,
                font = ("MV Boli",15))

menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command = cut)
editMenu.add_command(label="Coppy",command = coppy)
editMenu.add_command(label="Paste",command = paste)

window.mainloop()