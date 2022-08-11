from tkinter import * 
from estiloWidgets.entryPlaceHolder import *  # criado por Rafael Serafin
from estiloWidgets.gradienteFrame import *

window1 = Tk()

gradiente = GradientFrame(window1, "yellow", "red")
gradiente.pack()

holder = EntPlaceHold(window1, "Digite seu nome")
holder.place(x=10, y=10)

window1.mainloop()