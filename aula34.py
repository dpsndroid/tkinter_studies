from modulos import *
from validentry import Validators
from framegrad import *
from report import *
from funcionality import *
import pycep_correios



window1 = tix.Tk()

class Aplication(Funcs, Reports, Validators): # it can use function Funcs in Aplication
    def __init__(self):
        self.window1 = window1  # Mentioning the window inside the class
        self.validate_entries()
        self.screen() # call the function screen in the class 
        self.screen_frames() # call the function to insert a frame in the window
        self.widgets_frame1()
        self.list_frame2()
        self.mount_tables() # call the database and mount the table if it not exists
        self.select_list() # update the list in the database
        self.menus()
        window1.mainloop() # insert an infinite loop to show the window

    def cepCorreios(self):
        try:
            self.city_entry.delete(0, END)
            self.addr_entry.delete(0, END)
            self.neig_entry.delete(0, END)
            zipcode = self.cep_entry.get()
            data_cep = pycep_correios.get_address_from_cep(zipcode)
            print(data_cep)
            self.city_entry.insert(END, data_cep["cidade"])
            self.addr_entry.insert(END, data_cep["logradouro"])
            self.neig_entry.insert(END, data_cep["bairro"])
        except:
            messagebox.showerror("Erro", "Cep não encontrado")

            
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
# abas
        self.abas = ttk.Notebook(self.frame1)
        
        self.aba1 = Frame(self.abas)
        self.aba1.configure(background="lightgrey")
        self.abas.add(self.aba1, text = "Aba 1")

        self.aba2 = GradientFrame(self.abas, "grey", "white")
        self.aba2.configure(background="lightgrey")
        self.abas.add(self.aba2, text = "Aba 2")

        self.abas.place(relx=0.01, rely=0, relwidth=0.99, relheight=0.98)
#----------------------------------------------------------------------------------
# canvas
        self.canvas_bt = Canvas(self.aba1, bd=2, bg="darkgrey", highlightbackground= "grey", highlightthickness=3)
        self.canvas_bt.place(relx=0.02, rely=0.13, relwidth=0.96, relheight=0.22)
#-----------------------------------------------------------------------------------
# button limpar
        self.bt_clean = Button(self.aba1, text="Limpar", bd=2, bg="lightgrey", fg="darkgreen", activebackground="darkgrey", activeforeground="white", font= ("verdana", 10, "bold"), command=self.clean_screen)
        self.bt_clean.place(relx=0.35, rely=0.17, relwidth=0.1, relheight=0.15)
# button buscar
        self.bt_search = Button(self.aba1, text="Buscar", bd=2, bg="lightgrey", fg="darkgreen", activebackground="darkgrey", activeforeground="white", font= ("verdana", 10, "bold"), command=self.window2)
        self.bt_search.place(relx=0.47, rely=0.17, relwidth=0.1, relheight=0.15)
# message balloon
        self.bl_search = tix.Balloon(self.aba1)
        txt_bl_search = "Busca cliente cadastrado"
        self.bl_search.bind_widget(self.bt_search, balloonmsg = txt_bl_search)
# button novo
        self.bt_new = Button(self.aba1, text="Novo", bd=2, bg="lightgrey", fg="darkgreen", activebackground="darkgrey", activeforeground="white", font= ("verdana", 10, "bold"), command= self.add_client)
        self.bt_new.place(relx=0.59, rely=0.17, relwidth=0.1, relheight=0.15)  
# button mudar
        self.bt_change = Button(self.aba1, text="Mudar", bd=2, bg="lightgrey", fg="darkgreen", activebackground="darkgrey", activeforeground="white", font= ("verdana", 10, "bold"), command= self.change_client)
        self.bt_change.place(relx=0.71, rely=0.17, relwidth=0.1, relheight=0.15)  
# button apagar
        self.bt_erase = Button(self.aba1, text="Apagar", bd=2, bg="lightgrey", fg="darkgreen", activebackground="darkgrey", activeforeground="white", font= ("verdana", 10, "bold"), command= self.del_client)
        self.bt_erase.place(relx=0.83, rely=0.17, relwidth=0.1, relheight=0.15)
#---------------------------------------------------------------------------------
        self.lb_code = Label(self.aba1, text="Código", background="darkgrey", fg="darkgreen", font= ("verdana", 10, "bold"))
        
        self.lb_code.place(relx=0.05, rely=0.18)

        self.code_entry = Entry(self.aba1, bg="lightgreen", fg="darkgreen", font= ("verdana", 10, "bold"), validate="key", validatecommand= self.vcmd2)
        
        self.code_entry.place(relx=0.17, rely=0.18, relwidth=0.09)
#---------------------------------------------------------------------------------
        self.lb_name = Label(self.aba1, text="Nome", background="lightgrey", fg="darkgreen", font= ("verdana", 11, "bold"))
        
        self.lb_name.place(relx=0.01, rely=0.39)

        self.name_entry = Entry(self.aba1, fg="darkgreen", font= ("verdana", 11, "bold"))
        
        self.name_entry.place(relx=0.12, rely=0.39, relwidth=0.47, relheight=0.12)
#---------------------------------------------------------------------------------
# button cep
        self.bt_cep = Button(self.aba1, text="Cep:", bd=2, bg="lightgrey", fg="darkgreen", activebackground="darkgrey", activeforeground="white", font= ("verdana", 10, "bold"), command=self.cepCorreios)
        
        self.bt_cep.place(relx=0.67, rely=0.39)

        self.cep_entry = Entry(self.aba1, fg="darkgreen", font= ("verdana", 11, "bold"))
        
        self.cep_entry.place(relx=0.77, rely=0.39, relwidth=0.20, relheight=0.12)
#----------------------------------------------------------------------------------
        self.lb_phone = Label(self.aba1, text="Telefone", background="lightgrey", fg="darkgreen", font= ("verdana", 11, "bold"))
        
        self.lb_phone.place(relx=0.01, rely=0.59)

        self.phone_entry = Entry(self.aba1, fg="darkgreen", font= ("verdana", 11, "bold"))
        
        self.phone_entry.place(relx=0.16, rely=0.59, relwidth=0.20, relheight=0.12)
#---------------------------------------------------------------------------------
        self.lb_city = Label(self.aba1, text="Cidade", background="lightgrey", fg="darkgreen", font= ("verdana", 11, "bold"))
        
        self.lb_city.place(relx=0.40, rely=0.59)

        self.city_entry = Entry(self.aba1, fg="darkgreen", font= ("verdana", 11, "bold"))
        
        self.city_entry.place(relx=0.53, rely=0.59, relwidth=0.40, relheight=0.12)
#----------------------------------------------------------------------------------
        self.lb_addr = Label(self.aba1, text="End:", background="lightgrey", fg="darkgreen", font= ("verdana", 11, "bold"))
        
        self.lb_addr.place(relx=0.01, rely=0.80)

        self.addr_entry = Entry(self.aba1, fg="darkgreen", font= ("verdana", 11, "bold"))
        
        self.addr_entry.place(relx=0.09, rely=0.80, relwidth=0.48, relheight=0.12)
#---------------------------------------------------------------------------------
        self.lb_neig = Label(self.aba1, text="Bairro", background="lightgrey", fg="darkgreen", font= ("verdana", 11, "bold"))
        
        self.lb_neig.place(relx=0.53, rely=0.80)

        self.neig_entry = Entry(self.aba1, fg="darkgreen", font= ("verdana", 11, "bold"))
        
        self.neig_entry.place(relx=0.64, rely=0.80, relwidth=0.35, relheight=0.12)
#----------------------------------------------------------------------------------
# Menu popup
        self.tipvar = StringVar()
        self.tipv = ("Solteiro (a)", "Casado (b)", "Divorciado (c)", "Viúvo (d)")
        self.tipvar.set("Solteiro (a)")
        self.popupmenu = OptionMenu(self.aba2, self.tipvar, *self.tipv)
        self.popupmenu.place(relx=0.04, rely=0.15, relwidth=0.2, relheight=0.17)
        self.estate = self.tipvar.get()
        print(self.estate)

        self.bt_calendar = Button(self.aba2, width= 10, text= "Data", command= self.calendarnew)
        self.bt_calendar.place(relx=0.37, rely=0.15)
        self.entry_date = Entry(self.aba2, width= 10)
        self.entry_date.place(relx=0.37, rely=0.35, relheight=0.17)

    def list_frame2(self):
# Table to show the results
        self.ListCli = ttk.Treeview(self.frame2, height=3, columns=("col1", "col2", "col3", "col4"))  
        self.ListCli.heading("#0", text="")
        self.ListCli.heading("#1", text="Código")
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
        self.ListCli.bind("<Double-1>", self.double_click)

    def menus(self):
        menubar = Menu(self.window1)
        self.window1.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu3 = Menu(menubar)

        def quit():
            self.window1.destroy()

        menubar.add_cascade(label= "Opções", menu= filemenu)
        filemenu.add_command(label = "Limpa tela", command=self.clean_screen)
        filemenu.add_command(label = "Sair", command= quit)

        menubar.add_cascade(label = "Sobre", menu= filemenu2)
        filemenu2.add_command(label = "Versão 1.0")

        menubar.add_cascade(label= "Ficha do Cliente", menu=filemenu3)
        filemenu3.add_command(label= "Gerar PDF", command= self.gen_rep)

    def window2(self):
        self.root2 = Toplevel()
        self.root2.title("Janela 2")
        self.root2.configure(background="lightblue")
        self.root2.geometry("400x200")
        self.root2.resizable(False, False)
        self.root2.transient(self.window1) # the opening path
        self.root2.focus_force() # places the object in front
        self.root2.grab_set() # don't allow to type in other window, only this

    def validate_entries(self):
        self.vcmd2 = (self.window1.register(self.validate_entry2), "%P")

Aplication()