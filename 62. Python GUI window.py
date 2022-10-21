# Python gui window 

from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels and images 
# windows = serves as containerto hold or contain these widgets 

window = Tk() # instantiate an instance of a window



window.geometry("1000x1000")
window.title("Bro code first GUI program")

icon = PhotoImage(file="C:\\Users\\Timor\\OneDrive\\Python\\Course\\Rammstein_logo.png")
window.iconphoto(False, icon)
window.config(background="Sky blue")

window.mainloop() #place window on computer screen 