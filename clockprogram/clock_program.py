from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")      # %I = Hour ,%M = minute ,%S = seconds ,%p = AM or PM
    time_label.config(text = time_string)

    day_string = strftime("%A")                 # %A = day of the week
    day_label.config(text = day_string)

    date_string = strftime("%B %d, %Y")                 # %B = Month ,%d = date of the month ,%Y = Year
    date_label.config(text = date_string)

    window.after(1000,update)

window = Tk()

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="Black")
time_label.pack()

day_label = Label(window,font=("Ink Free",20))
day_label.pack()

date_label = Label(window,font=("Ink Free",20))
date_label.pack()

update()

window.mainloop()