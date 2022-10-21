from tkinter import *

# an area widget that holds text and or an image within a window

window = Tk()

photo = PhotoImage(file="C:\\Users\\Timor\\OneDrive\\Python\\Course\\Rammstein_logo.png")



label = Label(window,
              text = "Hello world",
              font=('Arial',40,'bold'),
              fg=('Green'),
              bg = 'Yellow',
              relief = SUNKEN,
              bd = 10,
              padx = 20,
              pady = 20,
              image = photo,
              compound = 'bottom') #extra ruimte tussen text en border


label.pack()            

#label.place(x=100,y=100)

window.mainloop()