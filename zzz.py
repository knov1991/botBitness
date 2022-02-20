from tkinter import *

def impDados():
    try:
        global valorBase, stopWin, stopLoss, velas, martingale, multiplicador, interfacePermissao
        valorBase = float(campoValorInicial.get())
        stopWin = int(campoStopWin.get())
        stopLoss = int(campoStopLoss.get())
        velas = int(campoVelas.get())
        if(velas < 1):
            return
        #Se o checkBox Martingale estiver habilitado - pega os valores de martingale e multiplicador
        if(checkGale.get() == 1):
            #Martingale minimo = 1
            if(int(campoMartingale.get()) >= 1):
                martingale = int(campoMartingale.get())
            else:
                return
            #Multiplicador minimo = 2
            if(float(campoMultiplicador.get()) >= 2):
                multiplicador = float(campoMultiplicador.get())
            else:
                return
        #Se o checkBox Martingale não estiver habilitado - desabilita o martingale settando martingale/multiplicador = 0         
        else:
            martingale = 0
            multiplicador = 0

        #interface da permissao para o bot iniciar
        interfacePermissao = True
        btnIniciar.config(state="disabled")
        campoValorInicial.config(state="disabled")
        campoStopWin.config(state="disabled")
        campoStopLoss.config(state="disabled")
        campoVelas.config(state="disabled")
        boxGale.config(state="disabled")
        campoMartingale.config(state="disabled")
        campoMultiplicador.config(state="disabled")
        #Info - Variaveis de Uso
        Label(app,text='Valor-Inicial: '+str(valorBase),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=220,width=160,height=20)
        Label(app,text='Stop-Win: '+str(stopWin),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=240,width=160,height=20)
        Label(app,text='Stop-Loss: '+str(stopLoss),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=260,width=160,height=20)
        if(checkGale.get() == 1):
            Label(app,text='Multiplicador: '+str(multiplicador),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=280,width=160,height=20)
        #Info - Entradas/Apostas
        Label(app,text='Entrada:  $'+str(valorBase),background=corFundo,foreground=corInfo,anchor=W).place(x=190,y=220,width=160,height=20)
        if(checkGale.get() == 1):
            for i in range(martingale):
                Label(app,text='Gale -  '+str(i+1)+':'  +' $'+str(round(valorBase*(multiplicador**(i+1)), 2)),background=corFundo,foreground=corInfo,anchor=W).place(x=190,y=220+((i+1)*20),width=160,height=20)
        #Alerta Iniciar Bot
        if(martingale > 3):
            Label(app,text='O Bot sera iniciado em 10 segundos!',background=corFundo,foreground=corAlerta,anchor=W).place(x=50,y=240+((i+1)*20),width=200,height=20)
        else:
            Label(app,text='O Bot sera iniciado em 10 segundos!',background=corFundo,foreground=corAlerta,anchor=W).place(x=50,y=320,width=200,height=20)

        print(valorBase, stopWin, stopLoss, velas, martingale, multiplicador)
        app.after(10000, lambda: app.destroy())
    except:
        print('error')



#Funções de checkBox
def print_selection():
    if (checkGale.get() == 1):
        campoMartingale.config(state="normal")
        campoMultiplicador.config(state="normal")
    else:
        campoMartingale.config(state="disabled")
        campoMultiplicador.config(state="disabled")
        

#cores
corFundo = '#dde'
corTexto = '#c0c'
corAlerta = '#f00'
corInfo = '#070'
#interface
app=Tk()
app.title('TURIM FERRARI')
app.geometry('800x600')
app.resizable(False,False)
app.configure(background=corFundo)
#campo de texto para variaveis
#ValorInicial
Label(app,text='Valor-Inicial',background=corFundo,foreground=corTexto,anchor=W).place(x=10,y=15,width=80,height=20)
campoValorInicial=Entry(app)
campoValorInicial.place(x=20,y=35,width=50,height=20)
#campoValorInicial.insert(END, 1)
#StopWin
Label(app,text='Stop-Win',background=corFundo,foreground=corTexto,anchor=W).place(x=90,y=15,width=80,height=20)
campoStopWin=Entry(app)
campoStopWin.place(x=90,y=35,width=50,height=20)
#StopLoss
Label(app,text='Stop-Loss',background=corFundo,foreground=corTexto,anchor=W).place(x=160,y=15,width=80,height=20)
campoStopLoss=Entry(app)
campoStopLoss.place(x=160,y=35,width=50,height=20)
#Velas
Label(app,text='Velas',background=corFundo,foreground=corTexto,anchor=W).place(x=230,y=15,width=80,height=20)
campoVelas=Entry(app)
campoVelas.place(x=230,y=35,width=50,height=20)

#Informação Gale
checkGale = IntVar()
boxGale = Checkbutton(app, text='Martingale',variable=checkGale, onvalue=1, offvalue=0, command=print_selection)
boxGale.place(x=300,y=35,width=100,height=20)

Label(app,text='Qtd.Gale',background=corFundo,foreground=corTexto,anchor=W).place(x=420,y=15,width=80,height=20)
campoMartingale=Entry(app)
campoMartingale.place(x=420,y=35,width=50,height=20)
campoMartingale.config(state="disabled")

Label(app,text='Mult.Gale',background=corFundo,foreground=corTexto,anchor=W).place(x=480,y=15,width=80,height=20)
campoMultiplicador=Entry(app)
campoMultiplicador.place(x=480,y=35,width=50,height=20)
campoMultiplicador.config(state="disabled")


#Alerta - Uso
Label(app,text='No Valor-Inicial usar ponto . e não virgula ,',background=corFundo,foreground=corAlerta,anchor=W).place(x=30,y=60,width=240,height=20)
Label(app,text='stopWin ou stopLoss = 0 desabilita stop',background=corFundo,foreground=corAlerta,anchor=W).place(x=30,y=80,width=240,height=20)
Label(app,text='Mult.Gale 0 ou 2+ // 0 = mão fixa',background=corFundo,foreground=corAlerta,anchor=W).place(x=30,y=100,width=240,height=20)
#Campo Informativo
Label(app,text='Verificar Configuração ao Iniciar',background=corFundo,foreground=corInfo,anchor=W).place(x=60,y=190,width=200,height=20)

#botao para iniciar o BOT
btnIniciar = Button(app,text='INICIAR BOT',command=lambda: [impDados()])
#btnIniciar.pack(ipadx=30,ipady=10,expand=True)
btnIniciar.place(x=50,y=120,width=200,height=60)
#IniciarInterface
app.mainloop()