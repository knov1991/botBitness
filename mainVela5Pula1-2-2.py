
#pip install tk
from tkinter import *
#pip install pypiwin32
import win32api, win32con
#dependencias instaladas pelo nome
import pyautogui
import keyboard
from time import sleep
from selenium import webdriver
# dependencia para separar ponto/virgula da carteira 
import re
# importar arquivos do projeto
#import conexao

##########################################
####### INICIAR VARIAVEIS GLOBAIS ########
##########################################

#calculo de entrada de aposta
valorBase = 1
multiplicador = 2.05
martingale = 0
# Verificador de Aposta/Resultado
pular = 0
apostou = False #Primeira entrada inicia com aposta False
#carteira
carteiraInicial = 0
CarteiraAtual = 0
carteiraAntesAposta = 0
#win/loss/falha(retorna aposta)/ultimo loss
win = 0
loss = 0
falha = 0
#stopWin e stopLoss
stopWin = 0
stopLoss = 0
#cor da vela
verde = 0
vermelho = 0
#valores ganhos e perdidos
profit = 0





##########################################
#### INTERFACE PARA AJUSTE DO USUARIO ####
##########################################
def impDados():
    try:
        global stopWin, stopLoss, valorBase, multiplicador
        stopWin=int(campoStopWin.get())
        stopLoss=int(campoStopLoss.get())
        valorBase=float(campoValorInicial.get())
        multiplicador=float(campoMultiplicador.get())
        btnIniciar.config(state="disabled")
        campoValorInicial.config(state="disabled")
        campoStopWin.config(state="disabled")
        campoStopLoss.config(state="disabled")
        sleep(0.1)
        print('valorInicial:',valorBase)
        print('stopWin:',stopWin)
        print('stopLoss:',stopLoss)
        #Info - Variaveis de Uso
        Label(app,text='Valor-Inicial: '+str(valorBase),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=220,width=160,height=20)
        Label(app,text='Stop-Win: '+str(stopWin),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=240,width=160,height=20)
        Label(app,text='Stop-Loss: '+str(stopLoss),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=260,width=160,height=20)
        Label(app,text='Multiplicador: 2.05',background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=280,width=160,height=20)
        #Info - Entradas/Apostas
        Label(app,text='Entrada:  $'+str(valorBase),background=corFundo,foreground=corInfo,anchor=W).place(x=190,y=220,width=160,height=20)
        Label(app,text='Gale -  1:  '+'$'+str(round(valorBase*(multiplicador**1), 2)),background=corFundo,foreground=corInfo,anchor=W).place(x=190,y=240,width=160,height=20)
        Label(app,text='Gale -  2:  '+'$'+str(round(valorBase*(multiplicador**2), 2)),background=corFundo,foreground=corInfo,anchor=W).place(x=190,y=260,width=160,height=20)
        Label(app,text='Gale -  3:  '+'$'+str(round(valorBase*(multiplicador**3), 2)),background=corFundo,foreground=corInfo,anchor=W).place(x=190,y=280,width=160,height=20)
        Label(app,text='Gale -  4:  '+'$'+str(round(valorBase*(multiplicador**4), 2)),background=corFundo,foreground=corInfo,anchor=W).place(x=190,y=300,width=160,height=20)
        #Alerta Iniciar Bot
        Label(app,text='O Bot sera iniciado em 10 segundos!',background=corFundo,foreground=corAlerta,anchor=W).place(x=50,y=320,width=200,height=20)
    except:
        print('error')

#cores
corFundo = '#dde'
corTexto = '#c0c'
corAlerta = '#f00'
corInfo = '#070'
#interface
app=Tk()
app.title('TURIM FERRARI')
app.geometry('300x340')
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
#Multiplicador
Label(app,text='Mult.Gale',background=corFundo,foreground=corTexto,anchor=W).place(x=230,y=15,width=80,height=20)
campoMultiplicador=Entry(app)
campoMultiplicador.place(x=230,y=35,width=50,height=20)
#Alerta - Uso
Label(app,text='No Valor-Inicial usar ponto . e não virgula ,',background=corFundo,foreground=corAlerta,anchor=W).place(x=30,y=80,width=240,height=20)
#Campo Informativo
Label(app,text='Verificar Configuração ao Iniciar',background=corFundo,foreground=corInfo,anchor=W).place(x=60,y=190,width=200,height=20)

#botao para iniciar o BOT
btnIniciar = Button(app,text='INICIAR BOT',command=lambda: [impDados()])
#btnIniciar.pack(ipadx=30,ipady=10,expand=True)
btnIniciar.place(x=50,y=120,width=200,height=60)
#IniciarInterface
app.mainloop()

#exit usado para encerrar o bot // apenas para testar interface
#exit()

##########################################
######## INICIAR NAVEGADOR CHROME ########
##########################################

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument("log-level=3")
driver = webdriver.Chrome(chrome_options=options)

#Conta Real
#driver.get("https://bitness.pro/en/trade/BTCUSD")
#Conta Teste
driver.get("https://testnet.bitness.pro/en/trade/BTCUSD")

sleep(60)



##########################################
######## FUNÇÕES DO BOT - EXECUTAR #######
##########################################

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def calculaMartingale():
    try:
        global valorBase,martingale,multiplicador
        return round(valorBase*(multiplicador**martingale), 2)
    except:
        print('ERRO CALCULO MARTINGALE')

def alteraValor(valorCalculado):
    click(1780,510)
    click(1780,510)
    sleep(0.1)
    keyboard.write(str(valorCalculado))

def wallet():
    try:
        wallet = driver.find_element_by_class_name('wallet')
        wallet = wallet.get_attribute('innerHTML')
        wallet = re.sub(r"[,]", '', wallet)
        wallet = round(float(wallet), 2)
        return wallet
    except:
        print('ERRO CARTEIRA')

def verificaVela(velaX,velaY):
    global verde,vermelho
    try:
        sc = pyautogui.screenshot(region=(velaX,velaY,1,5))
        width,height = sc.size
        for x in range(0,width,1):
            for y in range(0,height,1):
                r,g,b = sc.getpixel((x,y))
                #verde
                if r >= 19 and r <= 27 and g >= 73 and g <= 81 and b >= 78 and b <= 86:
                    verde += 1
                    return
                #vermelho
                if r >= 85 and r <= 93 and g >= 26 and g <= 34 and b >= 49 and b <= 57:
                    vermelho += 1
                    return
    except:
        print('ERRO VERIFICAR VELAS')

# Verifica Tempo
def verificaTempo():
    try:
        segundos = driver.find_elements_by_class_name('border')[1]
        segundos = int(segundos.get_attribute('innerHTML'))
        return segundos
    except:
        return 0

# Resultado
def resultado():
    try:
        global win,loss,falha,martingale,profit,carteiraAtual,carteiraAntesAposta,idUsuario,apostou,pular
        if(apostou == True):
            sleep(0.1)
            click(1780,450)
            sleep(0.1)
            carteiraAtual = wallet()
            sleep(0.1)
            profit = carteiraAtual - carteiraAntesAposta
            if(carteiraAtual > carteiraAntesAposta):
                win = 1
                loss = 0
                falha = 0
                print('*****Resultado*****')
                print('profit:',round(profit,2),'win:',win,'loss:',loss,'falha:',falha,'martingale:',martingale)
                print('Enviando informação para o Banco de Dados...')
                #conexao.adicionaAposta(str(idUsuario),str(round(profit,2)),str(martingale),str(round(carteiraAtual,2)),str(win),str(loss),str(falha))
                print('##################################################')
                martingale = 0
            elif(carteiraAtual < carteiraAntesAposta):
                win = 0
                loss = 1
                falha = 0
                print('*****Resultado*****')
                print('profit:',round(profit,2),'win:',win,'loss:',loss,'falha:',falha,'martingale:',martingale)
                print('Enviando informação para o Banco de Dados...')
                #conexao.adicionaAposta(str(idUsuario),str(round(profit,2)),str(martingale),str(round(carteiraAtual,2)),str(win),str(loss),str(falha))
                print('##################################################')
                martingale += 1
                # Se atingir Martingale 4 reseta para 0
                if(martingale >= 4):
                    martingale = 0
            elif(carteiraAtual == carteiraAntesAposta):
                win = 0
                loss = 0
                falha = 1
                print('*****Resultado*****')
                print('profit:',round(profit,2),'win:',win,'loss:',loss,'falha:',falha,'martingale:',martingale)
                print('Enviando informação para o Banco de Dados...')
                #conexao.adicionaAposta(str(idUsuario),str(round(profit,2)),str(martingale),str(round(carteiraAtual,2)),str(win),str(loss),str(falha))
                print('##################################################')
            else:
                win = 0
                loss = 0
                falha = 99
                print('*****Resultado*****')
                print('profit:',round(profit,2),'win:',win,'loss:',loss,'falha:',falha,'martingale:',martingale)
                print('Enviando informação para o Banco de Dados...')
                #conexao.adicionaAposta(str(idUsuario),str(round(profit,2)),str(martingale),str(round(carteiraAtual,2)),str(win),str(loss),str(falha))
                print('##################################################')
        sleep(0.05)
        apostou = False
        pular = 0
        sleep(0.05)
    except:
        print('ERRO RESULTADO')



##########################################
######### VALIDAR ACESSO AO BOT ##########
##########################################

# Login e pega idUsuario
""" print('##################################################')
print('Iniciando Turim Bot')
print('Requisitando Acesso...')
idUsuario = conexao.verificaLogin('vela5@vela5.com','123123')
sleep(1)
if(idUsuario < 0):
    sleep(1)
    print('Acesso Negado!')
    driver.quit()
    exit()
sleep(1)
print('Acesso Autorizado!') """




##########################################
######## VALORES INICIAIS DO BOT #########
##########################################
carteiraInicial = carteiraAtual = carteiraAntesAposta = wallet()
print('Carteira Inicial: $' +str(round(carteiraInicial,2)))
print('Valor de Aposta Inicial: $' +str(valorBase))
print('Multiplicador', multiplicador)
print('##################################################')





##########################################
############# INICIAR O BOT ##############
##########################################
while True:
    segundos = verificaTempo()

    # Fecha imagem de Win
    if(segundos == 30 or 31):
        click(1780,450)
        sleep(5)

    # Resultado
    if(segundos == 51 and apostou == True):
        click(1780,450)
        sleep(0.3)
        if(pular == 2):
            resultado()
            sleep(0.2)
            carteiraAntesAposta = wallet()
            print('52s pular==2 e martingale =',martingale)
            # Segundo Reset de Martingale 4 por segurança
            if(martingale == 1):
                print('Entrada Autorizada, Martingale 1')
                alteraValor(calculaMartingale())
                sleep(0.3)
                click(1780,730) #Enviar Ordem de Aposta
                sleep(0.1)
                pular = 1
                apostou = True
                sleep(3)
            if(martingale == 4):
                martingale = 0
        else:
            pular += 1
            print('52s pular: ',pular)
            sleep(3)
    # Fim Resultado

    # Tempo de Apostar
    if(segundos == 58 or segundos == 57):
        click(1780,450)
        sleep(0.3)
        if(apostou == False):
            # Entrada Martingale 0
            if(martingale == 0):
                print('Analisando Velas Anteriores...')
                verde = vermelho = 0
                sleep(0.05)
                verificaVela(665,860) #vela1 = 665 860 #1920x1080
                verificaVela(615,860) #vela2 = 615 860 #1920x1080
                verificaVela(565,860) #vela3 = 565 860 #1920x1080
                verificaVela(515,860) #vela4 = 615 860 #1920x1080
                verificaVela(465,860) #vela5 = 615 860 #1920x1080
                print('Verdes:', verde, ' Vermelhas:', vermelho)
                if(verde == 5):
                    carteiraAntesAposta = wallet()
                    sleep(0.05)
                    print('Entrada Autorizada, 5 Velas Verdes')
                    alteraValor(calculaMartingale())
                    sleep(0.1)
                    click(1780,730) #Enviar Ordem de Aposta
                    sleep(0.2)
                    pular = 0
                    apostou = True
                    sleep(3)
                else:
                    print('Entrada Cancelada, Esperando 5 Velas Verdes')
                    print('##################################################')
                    sleep(3)
            # Fim Entrada Martingale 0
            if(martingale == 2):
                print('Entrada Autorizada, Martingale 2')
                alteraValor(calculaMartingale())
                sleep(0.3)
                click(1780,730) #Enviar Ordem de Aposta
                sleep(0.1)
                pular = 0
                apostou = True
                sleep(3)

            if(martingale == 3):
                print('Entrada Autorizada, Martingale 3')
                alteraValor(calculaMartingale())
                sleep(0.3)
                click(1780,730) #Enviar Ordem de Aposta
                sleep(0.1)
                pular = 0
                apostou = True
                sleep(3)

    # Fim Tempo de Apostar
    sleep(0.6)