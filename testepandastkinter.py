
from argparse import FileType
from ast import Lambda
from fileinput import filename
from re import T
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

janela = tk.Tk()
janela.geometry("600x600")

# Frame for Tree view
frame1 = tk.LabelFrame(janela, text="Excel Data")
frame1.place(height=300, width=600)

tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)
scrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
scrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
scrollx.pack(side="bottom", fill="x")
scrolly.pack(side="right", fill="y")

# Frame for open file dialog
frame2 = tk.LabelFrame(janela, text="Open File Dialog")
frame2.place(height=150, width=600, rely=0.65, relx=0)

button1 = tk.Button(frame2, text="Browse a file", command=lambda: file_dialog())
button1.place(rely=0.65, relx=0.50)

button2 = tk.Button(frame2, text="Open the file", command=lambda : load_excel_data())
button2.place(rely=0.65, relx=0.30)

labelfile = ttk.Label(frame2, text="No file selected")
labelfile.place(rely=0, relx=0)

def file_dialog():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a file",             filetype=(("Excel files", "*.xlsx"),("All files", "*.*")))
    labelfile["text"] = filename
    return None


def load_excel_data():
    file_path = labelfile["text"]
    try:
        excel_filename = r"{}".format(file_path)
        df = pd.read_excel(filename)
    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", "No such file as (file_path)")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["column"]:
        tv1.heading(column, text=column)
    
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values=row)
    return None
    
def clear_data():
    tv1.deletea(*tv1.get_children())

janela.mainloop()

