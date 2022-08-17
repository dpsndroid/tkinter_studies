from cProfile import label
from tkinter import *


window1 = Tk()
window1.geometry("1000x600")
window1.resizable(False, False)
window1.title("Exercícios da Aula 38")
window1.configure(background="darkblue")

frame1 = Frame(window1)
frame1.pack(side=TOP, ipadx=400, ipady=125, padx=10, pady=10) # pode usar left, right, top e botton.
# ipadx e ipady alteram o tamanho da label, padx e pady afasta da borda
label1 = Label(frame1, text="Label 1")
label1.pack()

frame2 = Frame(window1)
frame2.pack(side=BOTTOM, ipadx=400, ipady=125, padx=10, pady=10)
label2 = Label(frame2, text="Label 2")
label2.pack()

frame3 = Frame(frame1)
frame3.pack(side=LEFT, ipadx=200, ipady=62, padx=10, pady=10)
label3 = Label(frame3, text="Label 3")
label3.pack()

frame4 = Frame(frame1)
frame4.pack(side=RIGHT, ipadx=200, ipady=62, padx=10, pady=10)
label4 = Label(frame4, text="Label 4")
label4.pack()

window1.mainloop()