from tkinter import *
from tkinter import messagebox

window1 = Tk()

def display():
    messagebox.showinfo("Info", "Só para você saber")
    messagebox.showwarning("Perigo, melhor ter cuidado")
    messagebox.showerror("Erro", "Algo deu errado")

    okcancel = messagebox.askokcancel("O que você acha?", "Devemos ir em frente?")
    print(okcancel)

    yesno = messagebox.askyesno("O que você acha?", "Por favor, decida")
    print(yesno)

    retrycancel = messagebox.askretrycancel("O que você acha?", "Qual a sua resposta?")
    print(retrycancel)

    answer = messagebox.askquestion("O que você acha?", "Decida-se!!!")

b1 = Button(window1, text= "Exibir diálogos", command= display)
b1.pack()


window1.mainloop()