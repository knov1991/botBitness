import tkinter as tk
from tkinter import scrolledtext
from tkinter import *
from time import sleep
import threading

resultado = 0
dead = False
stop = threading.Event()
iniciado = False

def iniciarBot():
    global log, iniciado
    if stop.is_set():
        window.destroy()
    if not iniciado:
        iniciado = True
        log.start()
        print('começa bot')

def congelar():
    global resultado, dead
    btnTest.config(state='disabled')
    while not stop.is_set():
        sleep(0.5)   
        entry0.config(state='normal')
        entry0.insert('insert', str(resultado)+'\n')
        entry0.config(state='disabled')
        entry0.see(tk.END)
        resultado += 1

def btn_clicked():
    global resultado
    print("Button Clicked")
    stop.set()
    btnTest.config(state='normal')


window = Tk()
window.title('Bot Turim')
window.iconbitmap('iconeTurim.ico')
window.geometry("800x600")
window.configure(bg = "#3a7ff6")

canvas = Canvas(
    window,
    bg = "#3a7ff6",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
btnIniciar = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

btnIniciar.place(
    x = 106, y = 335,
    width = 150,
    height = 60)


btnTest = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = iniciarBot,
    relief = "flat")

btnTest.place(
    x = 150, y = 435,
    width = 150,
    height = 60)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    581.0, 285.0,
    image = entry0_img)

""" entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0,
    font=("Times New Roman",15)) """

entry0 = scrolledtext.ScrolledText(window,wrap=tk.WORD,width=50,height=20,font=("Times New Roman",15),state="normal")

entry0.place(
    x = 406, y = 10,
    width = 350,
    height = 548)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    181.0, 215.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 106, y = 185,
    width = 150,
    height = 58)

window.resizable(False, False)
#window.overrideredirect(True)


log = threading.Thread(target=congelar, daemon=True)
window.mainloop()