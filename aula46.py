from tkinter import *
from tkinter import ttk
import awesometkinter as atk


window1 = Tk()

class janela():
    def __init__(self):
        self.window1 = window1
        self.window1.geometry("800x700")
        self.window1.resizable(False, False)
        self.window1.title("Exercícios da Aula 44")
        self.window1.configure(background="gray20")
        self.window1.attributes("-alpha", 0.95)  # acrescenta alpha a janela

        self.frame_superior()
        self.frame_inferior()

        self.window1.mainloop()

    def frame_superior(self):

# Frame -------------------------------------------

        frame1 = atk.Frame3d(window1)
        frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.39)
        
# Botões ------------------------------------------

        botao1 = atk.Button3d(frame1, text="Novo")
        botao1.place(relx=0.05, rely=0.10, relwidth=0.15, relheight=0.20)
        atk.tooltip(botao1, "Insere novas informações à Treeview")

        botao2 = atk.Button3d(frame1, text="Alterar")
        botao2.place(relx=0.25, rely=0.10, relwidth=0.15, relheight=0.20)
        atk.tooltip(botao2, "Atera as informações da Treeview")

        botao3 = atk.Button3d(frame1, text="Apagar")
        botao3.place(relx=0.45, rely=0.10, relwidth=0.15, relheight=0.20)
        atk.tooltip(botao3, "Apaga as informações da Treeview")

        botao4 = atk.Button3d(frame1, text="Buscar")
        botao4.place(relx=0.65, rely=0.10, relwidth=0.15, relheight=0.20)
        atk.tooltip(botao4, "Busca informações na Treeview")

# Labels -------------------------------------

        label1 = Label(frame1, text="código:", background="gray20", font=("verdana", 12, "bold"))
        label1.place(relx=0.05, rely=0.35, relwidth=0.15, relheight=0.15)

        label2 = Label(frame1, text="nome:", background="gray20", font=("verdana", 12, "bold"))
        label2.place(relx=0.05, rely=0.50, relwidth=0.15, relheight=0.15)

        label3 = Label(frame1, text="telefone:", background="gray20",
        font=("verdana", 12, "bold"))
        label3.place(relx=0.05, rely=0.65, relwidth=0.15, relheight=0.15)

# Entries --------------------------

        Entry1 = Entry(frame1, font=("verdana", 12, "bold"))
        Entry1.place(relx=0.23, rely=0.37, relwidth=0.30, relheight=0.10)

        Entry2 = Entry(frame1, font=("verdana", 12, "bold"))
        Entry2.place(relx=0.23, rely=0.52, relwidth=0.30, relheight=0.10)

        Entry3 = Entry(frame1, font=("verdana", 12, "bold"))
        Entry3.place(relx=0.23, rely=0.67, relwidth=0.30, relheight=0.10)

        barra = atk.RadialProgressbar3d(frame1, fg="cyan", bg=atk.DEFAULT_COLOR, size=120)
        barra.place(relx=0.82, rely=0.07)
        barra.start()

        

    def frame_inferior(self):

        frame2 = atk.Frame3d(window1)
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