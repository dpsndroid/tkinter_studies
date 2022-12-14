from tkinter import * # * importa tudo
from tkinter import ttk
import sqlite3

window1 = Tk()

class Funcs():
    def clean_screen(self):
        self.code_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.city_entry.delete(0, END)

    def connect_db(self):
        self.conn = sqlite3.connect("clients.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")

    def disconnect_db(self):
        self.conn.close(); print("Banco de dados desconectado com sucesso")

    def mount_tables(self):
        self.connect_db()
        # this print is to show in terminal the beginning when connecting
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(40)
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.disconnect_db

    def add_client(self): # to receive the entries
        self.code = self.code_entry.get()
        self.name = self.name_entry.get()
        self.phone = self.phone_entry.get()
        self.city = self.city_entry.get()
        self.connect_db() # to call the sql

        self.cursor.execute(""" INSERT INTO clients (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.name, self.phone, self.city))
        self.conn.commit()
        self.disconnect_db()
        self.select_list()
        self.clean_screen()
    
    def select_list(self):
        self.ListCli.delete(*self.ListCli.get_children())
        self.connect_db()
        list1 = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clients ORDER BY nome_cliente ASC; """)
        for i in list1:
            self.ListCli.insert("", END, values=i)
        self.disconnect_db()


class Aplication(Funcs): # it can use function Funcs in Aplication
    def __init__(self):
        self.window1 = window1  # Mentioning the window inside the class
        self.screen() # call the function screen in the class 
        self.screen_frames() # call the function to insert a frame in the window
        self.widgets_frame1()
        self.list_frame2()
        self.mount_tables() # call the database and mount the table if it not exists
        self.select_list() # update the list in the database
        window1.mainloop() # insert an infinite loop to show the window
            
    def screen(self):
        self.window1.title("CADASTRO DE CLIENTES") # insert a title in the window
        self.window1.configure(background="darkgreen") # choose the background. Better with hexadecimal
        self.window1.geometry('600x500') # defines the size of the window
        self.window1.resizable(True, True) # False: you can't change the size of the window
        self.window1.maxsize(width=900, height=700) # maximum size to stretch, even in the fullscreen mode
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
# button limpar
        self.bt_clean = Button(self.frame1, text="Limpar", bd=2, bg="lightgreen", fg="darkgreen", font= ("verdana", 10, "bold"), command= self.clean_screen)

        self.bt_clean.place(relx=0.23, rely=0.15, relwidth=0.1, relheight=0.15)
# button buscar
        self.bt_search = Button(self.frame1, text="Buscar", bd=2, bg="lightgreen", fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.bt_search.place(relx=0.35, rely=0.15, relwidth=0.1, relheight=0.15)
# button novo
        self.bt_new = Button(self.frame1, text="Novo", bd=2, bg="lightgreen", fg="darkgreen", font= ("verdana", 10, "bold"), command= self.add_client)
        
        self.bt_new.place(relx=0.58, rely=0.15, relwidth=0.1, relheight=0.15)  
# button mudar
        self.bt_change = Button(self.frame1, text="Mudar", bd=2, bg="lightgreen", fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.bt_change.place(relx=0.70, rely=0.15, relwidth=0.1, relheight=0.15)  
# button apagar
        self.bt_erase = Button(self.frame1, text="Apagar", bd=2, bg="lightgreen", fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.bt_erase.place(relx=0.82, rely=0.15, relwidth=0.1, relheight=0.15)
#---------------------------------------------------------------------------------
        self.lb_code = Label(self.frame1, text="C??digo", background="lightgrey", fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.lb_code.place(relx=0.05, rely=0.05)

        self.code_entry = Entry(self.frame1, bg="lightgreen", fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.code_entry.place(relx=0.05, rely=0.17, relwidth=0.09)
#---------------------------------------------------------------------------------
        self.lb_name = Label(self.frame1, text="Nome", background="lightgrey", fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.lb_name.place(relx=0.05, rely=0.39)

        self.name_entry = Entry(self.frame1, fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.name_entry.place(relx=0.05, rely=0.52, relwidth=0.88)
#---------------------------------------------------------------------------------
        self.lb_phone = Label(self.frame1, text="Telefone", background="lightgrey", fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.lb_phone.place(relx=0.05, rely=0.69)

        self.phone_entry = Entry(self.frame1, fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.phone_entry.place(relx=0.05, rely=0.80, relwidth=0.40)
#---------------------------------------------------------------------------------
        self.lb_city = Label(self.frame1, text="Cidade", background="lightgrey", fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.lb_city.place(relx=0.53, rely=0.69)

        self.city_entry = Entry(self.frame1, fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.city_entry.place(relx=0.53, rely=0.80, relwidth=0.40)

    def list_frame2(self):
# Table to show the results
        self.ListCli = ttk.Treeview(self.frame2, height=3, columns=("col1", "col2", "col3", "col4"))  
        self.ListCli.heading("#0", text="")
        self.ListCli.heading("#1", text="C??digo")
        self.ListCli.heading("#2", text="Nome")
        self.ListCli.heading("#3", text="Telefone")
        self.ListCli.heading("#4", text="Cidade")

        self.ListCli.column("#0", width=1)
        self.ListCli.column("#1", width=50) # The proportion of the list is 500
        self.ListCli.column("#2", width=200)
        self.ListCli.column("#3", width=125)
        self.ListCli.column("#4", width=125)
        self.ListCli.place(relx= 0.01, rely= 0.02, relwidth=0.95, relheight=0.96)

        self.scrollist = Scrollbar(self.frame2, orient="vertical")
        self.ListCli.configure(yscroll=self.scrollist.set)  # listCli constains the scrollbar
        self.scrollist.place(relx=0.96, rely=0.02, relwidth=0.04, relheight=0.05)


Aplication()