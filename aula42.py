from tkinter import *
from tkinter.font import BOLD


window1 = Tk()
window1.geometry("800x600")
window1.resizable(True, True)
window1.title("Exercícios da Aula 42")
window1.configure(background="#483A58")
window1.attributes("-alpha", 0.97)  # acrescenta alpha a janela

frame1 = Frame(window1)
label1 = Label(frame1, text="Primeiro")
frame1.place(relx=0, rely=0, relwidth=1, relheight=0.20)

botao1 = Button(frame1, text="Novo", bg="#cb462a", fg="#ffffff", font=("verdana", 13, "bold"))
botao1.place(relx=0.05, rely=0.10, relwidth=0.15, relheight=0.40)

botao2 = Button(frame1, text="Alterar", bg="#cb462a", fg="#ffffff", font=("verdana", 13, "bold"))
botao2.place(relx=0.25, rely=0.10, relwidth=0.15, relheight=0.40)

botao3 = Button(frame1, text="Apagar", bg="#cb462a", fg="#ffffff", font=("verdana", 13, "bold"))
botao3.place(relx=0.45, rely=0.10, relwidth=0.15, relheight=0.40)

botao4 = Button(frame1, text="Buscar", bg="#cb462a", fg="#ffffff", font=("verdana", 13, "bold"))
botao4.place(relx=0.65, rely=0.10, relwidth=0.15, relheight=0.40)

frame2 = Frame(window1, background="#CB462A")
label2 = Label(window1, text="Segundo")
frame2.place(relx=0, rely=0.20, relwidth=1, relheight=0.20)

window1.mainloop()