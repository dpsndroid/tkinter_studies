from tkinter import *


window1 = Tk()
window1.geometry("800x600")
window1.resizable(True, True)
window1.title("Exercícios da Aula 40")
window1.configure(background="#483A58")

frame1 = Frame(window1)
label1 = Label(frame1, text="Primeiro")
frame1.place(relx=0, rely=0, relwidth=1, relheight=0.20)

frame2 = Frame(window1, background="#CB462A")
label2 = Label(window1, text="Segundo")
frame2.place(relx=0, rely=0.20, relwidth=1, relheight=0.20)

window1.mainloop()