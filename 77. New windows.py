from tkinter import *

def create_window():
    #new_window = Toplevel() #new window closes if you close main window
    new_window = Tk() #new window doesnt close if you close main window

    old_window.destroy()

old_window = Tk()

button = Button(old_window,
                text = "Create new window",
                command = create_window)

button.pack()

old_window.mainloop()