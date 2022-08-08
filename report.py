from modulos import *


class Reports(): # creates a pdf report on the webbrowser
    def print_client(self):
        webbrowser.open("client.pdf")

    def gen_rep(self):
        self.c = canvas.Canvas("client.pdf")
        self.coderep = self.code_entry.get()
        self.namerep = self.name_entry.get()
        self.phonerep = self.phone_entry.get()
        self.cityrep = self.city_entry.get()

        self.c.setFont("Helvetica-Bold", 20)
        self.c.drawString(200, 770, "FICHA DO CLIENTE") # position

        self.c.setFont("Helvetica", 10)
        self.c.drawString(50, 700, "Código: ")
        self.c.drawString(50, 650, "Nome: ")
        self.c.drawString(50, 600, "Telefone: ")
        self.c.drawString(50, 550, "Cidade: ")

        self.c.setFont("Helvetica", 10)
        self.c.drawString(100, 700, self.coderep)
        self.c.drawString(100, 650, self.namerep)
        self.c.drawString(100, 600, self.phonerep)
        self.c.drawString(100, 550, self.cityrep)

        self.c.rect(20, 400, 550, 420, fill=False, stroke=True)

        self.c.showPage()
        self.c.save()
        self.print_client()
