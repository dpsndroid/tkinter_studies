# Using binding. It means the interaction of python with the peripherals

from tkinter import *
from tkinter import ttk
from tkinter import font
window1 = Tk()

window1.geometry("500x200")
window1.title("BIND PROCESSES")
window1.resizable(False, False)
l = ttk.Label(window1, text="STARTING..." , font= ("Arial", 16))
l.place(relx=0.06, rely= 0.4)

# Lambda is a function inside a function

l.bind("<Enter>", lambda e: l.configure(text= "THE MOUSE IS INSIDE")) 
l.bind("<Leave>", lambda e: l.configure(text= "THE MOUSE LEFT THE SPACE"))
l.bind("<1>", lambda e: l.configure(text= "THE LEFT MOUSE BUTTON WAS CLICKED"))
l.bind("<Double-1>", lambda e: l.configure(text= "DOUBLE CLICK WAS MADE"))
l.bind("<B3-Motion>", lambda e: l.configure(text= "DRAGGING WITH RIGHT BUTTON TO %d,%d" % (e.x, e.y)))


window1.mainloop()

 