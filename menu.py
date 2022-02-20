#pip install tk
from tkinter import *
from time import sleep

#iniciando variaveis
stopWin = 0
stopLoss = 0

def impDados():
    global stopWin, stopLoss
    stopWin=float(campoStopWin.get())
    stopLoss=float(campoStopLoss.get())

#cores
corFundo = '#dde'
corTexto = '#c0c'
#interface
app=Tk()
app.title('Turim')
app.geometry('500x300')
app.resizable(False,False)
app.configure(background=corFundo)
#campo de texto para variaveis
#stopWin
Label(app,text='StopWin',background=corFundo,foreground=corTexto,anchor=W).place(x=20,y=15,width=50,height=20)
campoStopWin=Entry(app)
campoStopWin.place(x=20,y=40,width=50,height=20)
#stopLoss
Label(app,text='StopLoss',background=corFundo,foreground=corTexto,anchor=W).place(x=120,y=15,width=50,height=20)
campoStopLoss=Entry(app)
campoStopLoss.place(x=120,y=40,width=50,height=20)
#botao para iniciar o BOT
#Button(app,text='imprimir',command=impDados).place(x=100,y=100,width=100,height=20)
btnIniciar = Button(app,text='Iniciar',command=lambda: [impDados()])
btnIniciar.pack(ipadx=5,ipady=5,expand=True)
#IniciarInterface
app.mainloop()



""" while True:
    print('iniciando bot')
    sleep(1)
    print(stopWin)
    print(stopLoss) """