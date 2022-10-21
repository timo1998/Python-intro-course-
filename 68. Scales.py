from tkinter import *

def submit():
    print("The temperature is ", scale.get()," degrees c")

window = Tk()

scale = Scale(window,
              from_=200,
              to=0,
              length = 600,
              orient= VERTICAL,
              font = ('Consolas',20),
              tickinterval = 10, #This adds numeric indicators for value 
              showvalue = 0,
              resolution = 5,
              troughcolor = "blue",
              fg = 'Red',
              bg = 'White')

#scale.set(50)
scale.set(((scale['from']-scale['to'])/2)+scale['to'])

scale.pack()


button = Button(window,
                text="Submit",
                command = submit)

button.pack()

window.mainloop()