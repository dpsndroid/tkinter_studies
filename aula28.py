
from tkinter import *
from tkinter import ttk
import time

window1 = Tk()
window1.title("PROGRESS BAR")
window1.geometry("500x200")

def step():
    #progress1['value'] += 2
    #progress1.start(2)
    for x in range(100):
        progress1["value"] += 1
        window1.update_idletasks()
        time.sleep(1)

def stop():
    progress1.stop()

progress1 = ttk.Progressbar(window1, orient=HORIZONTAL, length=300, mode="determinate")
progress1.pack(pady=20)

button_bar = Button(window1, text="Progress", command=step)
button_bar.pack(pady=20)

button_bar2 = Button(window1, text="Parar", command=stop)
button_bar2.pack(pady=10)

window1.mainloop()