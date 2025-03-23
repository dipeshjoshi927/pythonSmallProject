from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window,height=HEIGHT,width=WIDTH)
canvas.pack()

space_image = PhotoImage(file='space.png')
background = canvas.create_image(0,0,image=space_image,anchor=NW)

photo_image = PhotoImage(file='ufo.png')
image = canvas.create_image(0,0,image=photo_image,anchor=NW)


image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity

    canvas.move(image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()