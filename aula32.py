from textwrap import fill
from tkinter import *
from tkinter import ttk
from turtle import color, width

window1 = Tk()

v = ttk.Scrollbar(window1, orient=VERTICAL)
h = ttk.Scrollbar(window1, orient=HORIZONTAL)

canvas = Canvas(window1, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)  # starts at 0, ends at 1000

h["command"] = canvas.xview
v["command"] = canvas.yview

ttk.Sizegrip(window1).grid(column=1, row=1, sticky=(S,E)) # sizegrip is used to reduce and increase the screen

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
window1.grid_columnconfigure(0, weight=1)
window1.grid_rowconfigure(0, weight=1)

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx = canvas.canvasx(event.x)
    lasty = canvas.canvasy(event.y) # defines the movement of the mouse

def set_color(newcolor):
    global color
    color = newcolor
    canvas.dtag("all", "paletteSelected")
    canvas.itemconfigure("palette", outline="white")
    canvas.addtag("paletteSelected", "withtag", "palette%s" % color)
    canvas.itemconfigure("paletteSelected", outline="#999999")

def addLine(event):
    global lastx, lasty
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags="currentLine")
    lastx, lasty = x, y 

def done_stroke(event):
    canvas.itemconfigure("currentLine", width=1)
    
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", done_stroke)

id = canvas.create_rectangle((10,10,30,30), fill="red", tags=("palette", "palettered"))
canvas.tag_bind(id, "<Button-1>", lambda x: set_color("red"))

id = canvas.create_rectangle((10,35,30,55), fill="blue", tags=("palette", "paletteblue"))
canvas.tag_bind(id, "<Button-1>", lambda x: set_color("blue"))

id = canvas.create_rectangle((10,60,30,80), fill="black", tags=("palette", "paletteblack"))
canvas.tag_bind(id, "<Button-1>", lambda x: set_color("black"))

set_color("black")
canvas.itemconfigure("palette", width=5)



window1.mainloop()