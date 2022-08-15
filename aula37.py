from tkinter import *


window1 = Tk()
window1.geometry("800x200")
window1.resizable(False, False)
window1.title("Exercícios da Aula 37")
window1.configure(background="darkblue")
frame1 = Frame(window1)
frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.50)

window1.mainloop()