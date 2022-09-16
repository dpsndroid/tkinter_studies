from tkinter import *
from tkinter import ttk



window1 = Tk()

class janela():
    def __init__(self):
        self.window1 = window1
        self.window1.geometry("800x700")
        self.window1.resizable(False, False)
        self.window1.title("Exercícios da Aula 44")
        self.window1.configure(background="#483A58")
        self.window1.attributes("-alpha", 0.95)  # acrescenta alpha a janela

        self.frame_superior()
        self.frame_inferior()

        self.window1.mainloop()

    def frame_superior(self):

# Frame -------------------------------------------

        frame1 = Frame(window1)
        frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.39)
        
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

        

    def frame_inferior(self):

        frame2 = Frame(window1, background="#CB462A")
        frame2.place(relx=0.01, rely=0.41, relwidth=0.98, relheight=0.58)

# Treeview --------------------------------

        lista = ttk.Treeview(frame2, height=5, column=("col0", "col1", "col2"))
        lista.heading("#0", text="Código")
        lista.heading("#1", text="Nome")
        lista.heading("#2", text="Telefone")

        lista.column("#0", width=100)
        lista.column("#1", width=400)
        lista.column("#2", width=150)

        lista.place(relx=0.02, rely=0.03, relwidth=0.96, relheight=0.94)

        barra = ttk.Scrollbar(frame2, orient="vertical")
        barra.place(relx=0.95, rely=0.04, relwidth=0.03, relheight=0.92)



janela()