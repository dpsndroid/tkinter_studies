from tkinter import *
from tkinter.font import BOLD


window1 = Tk()
window1.geometry("800x600")
window1.resizable(True, True)
window1.title("Exercícios da Aula 42")
window1.configure(background="#483A58")
window1.attributes("-alpha", 0.97)  # acrescenta alpha a janela

# Frame -------------------------------------------

frame1 = Frame(window1)
frame1.place(relx=0, rely=0, relwidth=1, relheight=0.40)

frame2 = Frame(window1, background="#CB462A")
frame2.place(relx=0, rely=0.40, relwidth=1, relheight=0.40)

# Botões ------------------------------------------

botao1 = Button(frame1, text="Novo", bg="#cb462a", fg="#ffffff", font=("verdana", 13, "bold"))
botao1.place(relx=0.05, rely=0.10, relwidth=0.15, relheight=0.20)

botao2 = Button(frame1, text="Alterar", bg="#cb462a", fg="#ffffff", font=("verdana", 13, "bold"))
botao2.place(relx=0.25, rely=0.10, relwidth=0.15, relheight=0.20)

botao3 = Button(frame1, text="Apagar", bg="#cb462a", fg="#ffffff", font=("verdana", 13, "bold"))
botao3.place(relx=0.45, rely=0.10, relwidth=0.15, relheight=0.20)

botao4 = Button(frame1, text="Buscar", bg="#cb462a", fg="#ffffff", font=("verdana", 13, "bold"))
botao4.place(relx=0.65, rely=0.10, relwidth=0.15, relheight=0.20)

# Labels -------------------------------------

label1 = Label(frame1, text="código:", font=("verdana", 12, "bold"))
label1.place(relx=0.05, rely=0.35, relwidth=0.15, relheight=0.15)

label2 = Label(frame1, text="nome:", font=("verdana", 12, "bold"))
label2.place(relx=0.05, rely=0.50, relwidth=0.15, relheight=0.15)

label3 = Label(frame1, text="telefone:", font=("verdana", 12, "bold"))
label3.place(relx=0.05, rely=0.65, relwidth=0.15, relheight=0.15)

# Entries --------------------------

Entry1 = Entry(frame1, font=("verdana", 12, "bold"))
Entry1.place(relx=0.23, rely=0.37, relwidth=0.30, relheight=0.10)

Entry2 = Entry(frame1, font=("verdana", 12, "bold"))
Entry2.place(relx=0.23, rely=0.52, relwidth=0.30, relheight=0.10)

Entry3 = Entry(frame1, font=("verdana", 12, "bold"))
Entry3.place(relx=0.23, rely=0.67, relwidth=0.30, relheight=0.10)




window1.mainloop()