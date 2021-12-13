# Create GUI with Built-In Package

import tkinter

main_window = tkinter.Tk()

def event_pressMe():
    label2 = tkinter.Label(main_window, text="Thanks for Pressing Me ^__^")
    label2.pack()

label = tkinter.Label(main_window, text="Hello I am GUI \n In Python!!!")
button = tkinter.Button(main_window, text="Press Me", command= event_pressMe) # command for create function

# how to print 
label.pack()
button.pack()

main_window.mainloop() # looping