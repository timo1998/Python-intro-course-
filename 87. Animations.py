from tkinter import *
import time



WIDTH = 500
HEIGHT = 500
xVelocity = 1
yVelocity = 1

window = Tk()

canvas = Canvas(window,width = WIDTH, height = HEIGHT)
canvas.pack()

photo_image = PhotoImage(file='speaker (1).png')


myImage = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()



while True:
    coordinates = canvas.coords(myImage)
    print(coordinates)
    if (coordinates[0]) >= WIDTH-image_width or (coordinates[0]) <0:
        xVelocity = xVelocity*-1
    if (coordinates[1]) >= HEIGHT - image_height or (coordinates[1]) < 0:
        yVelocity = yVelocity * -1
    canvas.move(myImage,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()