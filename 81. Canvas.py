from tkinter import *

window = Tk()

canvas = Canvas(window,
                height = 500,
                width = 500)

# canvas.create_line(0,0,500,500,fill = "blue",width = 5)
# canvas.create_line(0,500,500,0,fill = "red",width = 5)
# canvas.create_rectangle(50,50,250,250, fill = "yellow",width = 5)
# canvas.create_polygon(250,0,500,500,0,500, fill = "purple",outline="orange",width=5)
# canvas.create_arc(0,0,500,500,fill="gold",style=ARC,start=0,extent=180)

canvas.create_arc(0,0,500,500,fill="Red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="White",start=180,extent=180,width=10)
canvas.create_oval(190,190,310,310,fill="White",width = 10)

canvas.pack()

window.mainloop()