from modulos import *

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

    def variables(self):
        self.code = self.code_entry.get()
        self.name = self.name_entry.get()
        self.phone = self.phone_entry.get()
        self.city = self.city_entry.get()

    def add_client(self): # to receive the entries
        self.variables()
        if self.name_entry.get() == "":
            msg = "Para cadastrar um novo cliente é necessário \n"
            msg += "que seja digitado pelo menos um nome"
            messagebox.showinfo("Cadastro de clientes - Aviso!!!", msg)
        else:
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

    def double_click(self, event): # event is to inform that an event will occur
        self.clean_screen()
        self.ListCli.selection()
        for n in self.ListCli.selection():
            col1, col2, col3, col4 = self.ListCli.item(n, "values")
            self.code_entry.insert(END, col1)
            self.name_entry.insert(END, col2)
            self.phone_entry.insert(END, col3)
            self.city_entry.insert(END, col4)

    def del_client(self):
        self.variables()
        self.connect_db()
        self.cursor.execute(""" DELETE FROM clients WHERE cod = ? """, (self.code))
        self.conn.commit()
        self.disconnect_db()
        self.clean_screen()
        self.select_list()

    def change_client(self):
        self.variables()
        self.connect_db()
        self.cursor.execute(""" UPDATE clients SET nome_cliente = ?, telefone = ?, cidade = ? WHERE cod = ? """, (self.name, self.phone, self.city, self.code))
        self.conn.commit()
        self.disconnect_db()
        self.select_list()
        self.clean_screen()

    def search_client(self):
        self.connect_db()
        self.ListCli.delete(*self.ListCli.get_children())
        self.name_entry.insert(END, "%")
        name = self.name_entry.get()
        self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clients WHERE nome_cliente LIKE "%s" ORDER BY nome_cliente ASC """ % name)
        search_name_cli = self.cursor.fetchall()
        for i in search_name_cli:
            self.ListCli.insert("", END, values=i)
        self.clean_screen()
        self.disconnect_db()

    def calendarnew(self):
        self.calendar1 = Calendar(self.aba2, fg="grey75", bg= "blue", font= ("Times", 9, "bold"), locale="pt_br")
        self.calendar1.place(relx=0.55, rely=0.03)
        self.date_start = Button(self.aba2, text="Inserir data", command= self.print_call)
        self.date_start.place(relx=0.37, rely=0.55, relheight=0.17)
    
    def print_call(self):
        date_begin = self.calendar1.get_date()
        self.calendar1.destroy()
        self.entry_date.delete(0, END)
        self.entry_date.insert(END, date_begin)
        self.date_start.destroy()