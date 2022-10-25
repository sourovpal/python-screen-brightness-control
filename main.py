from itertools import count
import screen_brightness_control as sbc
from tkinter import *
from tkinter.ttk import *
 
# creates a Tk() object
master = Tk()
 
# sets the geometry of main
# root window
master.geometry("200x200")
 
 
# function to open a new window
# on a button click
counter = 0;
def openNewWindow():
    global counter
    sbc.set_brightness(counter)
    if counter < 100:
        counter = counter + 5
        print("++", counter)

def conterminus():
    global counter
    sbc.set_brightness(counter)
    if counter > 0:
        counter = counter - 5
        print("--", counter)

 
# a button widget which will open a
# new window on button click
btn = Button(master,
             text ="++",
             command = openNewWindow)
btn.pack(pady = 10)

btn2 = Button(master,
             text ="--",
             command = conterminus)
btn2.pack(pady = 10)
 
# mainloop, runs infinitely
mainloop()

