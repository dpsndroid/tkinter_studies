from tkinter import * # * importa tudo

window1 = Tk()

class Aplication():
    def __init__(self):
        self.window1 = window1  # Mentioning the window inside the class
        self.screen() # call the function screen in the class 
        window1.mainloop()
    
    def screen(self):
        self.window1.title("CADASTRO DE CLIENTES") # insert a title in the window
        self.window1.configure(background="green") # choose the background. Better with hexadecimal
        self.window1.geometry('600x500') # defines the size of the window
        self.window1.resizable(True, True) # False: you can't change the size of the window
        self.window1.maxsize(width=900, height=700) # maximum size to stretch, even with the fullscreen mode
        self.window1.minsize(width=600, height=500) # minimum size to stretch

Aplication()