from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title="This is an info message box",message="You are a person")
    # messagebox.showwarning(title="This is an info message box", message="You are a person")
    # messagebox.showerror(title="This is an info message box", message="You are a person")

    # if messagebox.askokcancel(title='ask ok cancel',message='Do you want do do the thing?') == True:
    #     print("You did a thing")
    # else:
    #     print("You canceld a thing")

    # if messagebox.askretrycancel(title='ask ok cancel',message='Do you want do do the thing?') == True:
    #     print("You did a thing")
    # else:
    #     print("You canceld a thing")

    # if messagebox.askyesno(title='ask ok cancel',message='Do you want do do the thing?') == True:
    #     print("You did a thing")
    # else:
    #     print("You canceld a thing")

    # if messagebox.askquestion(title='ask ok cancel', message='Do you want do do the thing?') == 'yes':
    #     print("You did a thing")
    # else:
    #     print("You canceld a thing")

    print(messagebox.askyesnocancel(title='yes no cancel',message='Do you like to code',icon='warning'))


window = Tk()

button = Button(window, command=click, text='click me')

button.pack()

window.mainloop()
