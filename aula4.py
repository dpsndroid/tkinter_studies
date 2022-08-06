from tkinter import * # * importa tudo


window1 = Tk()

class Aplication():
    def __init__(self):
        self.window1 = window1  # Mentioning the window inside the class
        self.screen() # call the function screen in the class 
        self.screen_frames() # call the function to insert a frame in the window
        self.widgets_frame1()
        window1.mainloop() # insert an infinite loop to show the window
    
    def screen(self):
        self.window1.title("CADASTRO DE CLIENTES") # insert a title in the window
        self.window1.configure(background="black") # choose the background. Better with hexadecimal
        self.window1.geometry('600x500') # defines the size of the window
        self.window1.resizable(True, True) # False: you can't change the size of the window
        self.window1.maxsize(width=900, height=700) # maximum size to stretch, even with the fullscreen mode
        self.window1.minsize(width=600, height=500) # minimum size to stretch

    def screen_frames(self):
        self.frame1 = Frame(self.window1, bd= 4, bg="lightgrey", highlightbackground="grey", highlightthickness=3) # create a frame in the window
        # bd is border, bg is background of the frame, highlight is the color of the frame's border, thickness is the size of the border
        
        self.frame1.place(relx= 0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        # rel x,y is the relative position on the screen. You can stretch the window and the elements will follow with the proportion defined
        
        self.frame2 = Frame(self.window1, bd= 4, bg="white", highlightbackground="grey", highlightthickness=3)
        self.frame2.place(relx= 0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
#---------------------------------------------------------------------------------
        self.bt_clean = Button(self.frame1, text="Limpar")
        self.bt_clean.place(relx=0.23, rely=0.15, relwidth=0.1, relheight=0.15)

        self.bt_search = Button(self.frame1, text="Buscar")
        self.bt_search.place(relx=0.35, rely=0.15, relwidth=0.1, relheight=0.15)

        self.bt_new = Button(self.frame1, text="Novo")
        self.bt_new.place(relx=0.58, rely=0.15, relwidth=0.1, relheight=0.15)  

        self.bt_change = Button(self.frame1, text="Mudar")
        self.bt_change.place(relx=0.70, rely=0.15, relwidth=0.1, relheight=0.15)  

        self.bt_erase = Button(self.frame1, text="Apagar")
        self.bt_erase.place(relx=0.82, rely=0.15, relwidth=0.1, relheight=0.15)
#---------------------------------------------------------------------------------
        self.lb_code = Label(self.frame1, text="Código", background="lightgrey")
        self.lb_code.place(relx=0.05, rely=0.05)

        self.code_entry = Entry(self.frame1)
        self.code_entry.place(relx=0.05, rely=0.16, relwidth=0.09)
#---------------------------------------------------------------------------------
        self.lb_name = Label(self.frame1, text="Nome", background="lightgrey")
        self.lb_name.place(relx=0.05, rely=0.40)

        self.name_entry = Entry(self.frame1)
        self.name_entry.place(relx=0.05, rely=0.53, relwidth=0.88)
#---------------------------------------------------------------------------------
        self.lb_phone = Label(self.frame1, text="Celular", background="lightgrey")
        self.lb_phone.place(relx=0.05, rely=0.69)

        self.phone_entry = Entry(self.frame1)
        self.phone_entry.place(relx=0.05, rely=0.80, relwidth=0.40)
#---------------------------------------------------------------------------------
        self.lb_city = Label(self.frame1, text="Cidade", background="lightgrey")
        self.lb_city.place(relx=0.53, rely=0.69)

        self.city_entry = Entry(self.frame1)
        self.city_entry.place(relx=0.53, rely=0.80, relwidth=0.40)
#---------------------------------------------------------------------------------        

Aplication()