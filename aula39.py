from cProfile import label
from tkinter import *


window1 = Tk()
window1.geometry("800x600")
window1.resizable(False, False)
window1.title("Exercícios da Aula 39")
window1.configure(background="#483A58")

####################################    FRAME 1    ##################################################
frame1 = Frame(window1)
label1 = Label(frame1, text="Label 1")
frame1.grid(column=0, row=1, columnspan=1, ipadx=100, ipady=100, padx=1, pady=1)

####################################    FRAME 2    ##################################################
frame2 = Frame(window1)
label2 = Label(frame2, text="Label 2")
frame2.grid(column=1, row=2, columnspan=1, ipadx=100, ipady=100, padx=1, pady=1)


window1.mainloop()