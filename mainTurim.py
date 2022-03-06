#pip install tk
from tkinter import *
#pip install pypiwin32
import win32api, win32con
#dependencias instaladas pelo nome
import pyautogui
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
#dependencia para separar ponto/virgula da carteira 
import re
#Conexão banco de dados MySQL
#import conexao
#Telegram BOT
#import telegramTurimFerrari
#dependencia q já vem no python
from time import sleep
from datetime import date


##########################################
####### INICIAR VARIAVEIS GLOBAIS ########
##########################################
#calculo de entrada de aposta
valorBase = 1
multiplicador = 0
martingale = 0
galeAtual = 0
soros = 0
sorosAtual = 0
#carteira
carteiraInicial = 0
carteiraAntesAposta = 0
#win/loss/falha(retorna aposta)/ultimo loss
win = 0
loss = 0
falha = 0
ultimoLoss = 2 #0 = vermelho // 1 = verde // 2 = nada apenas para iniciar variavel
#Analise de Velas
velas = 0
verde = 0
vermelho = 0
#valores ganhos e perdidos
profit = 0
#stopLoss e stopWin
stopLoss = 0
stopWin = 0
totalWinLoss = 0
#permissoes de acesso
interfacePermissao = False


##########################################
#### INTERFACE PARA AJUSTE DO USUARIO ####
##########################################
def impDados():
    try:
        global valorBase, stopWin, stopLoss, velas, martingale, multiplicador, interfacePermissao, soros
        valorBase = float(campoValorInicial.get())
        stopWin = int(campoStopWin.get())
        stopLoss = int(campoStopLoss.get())
        velas = int(campoVelas.get())
        if(velas < 1):
            return
        
        #MARTINGALE
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

        #SOROS
        #Se o checkBox Soros estiver habilitado - pega a quantidade de entradas no soros
        if(checkSoros.get() == 1):
            #Soros minimo = 1
            if(int(campoSoros.get()) >= 1):
                soros = int(campoSoros.get())
            else:
                return

        

        #interface da permissao para o bot iniciar
        interfacePermissao = True
        btnIniciar.config(state="disabled")
        campoValorInicial.config(state="disabled")
        campoStopWin.config(state="disabled")
        campoStopLoss.config(state="disabled")
        campoVelas.config(state="disabled")
        boxGale.config(state="disabled")
        campoMartingale.config(state="disabled")
        campoSoros.config(state="disabled")
        campoMultiplicador.config(state="disabled")
        #Info - Variaveis de Uso
        Label(app,text='Valor-Inicial: '+str(valorBase),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=220,width=160,height=20)
        Label(app,text='Stop-Win: '+str(stopWin),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=240,width=160,height=20)
        Label(app,text='Stop-Loss: '+str(stopLoss),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=260,width=160,height=20)       
        #Info - Entradas/Apostas
        Label(app,text='Entrada:  $'+str(valorBase),background=corFundo,foreground=corInfo,anchor=W).place(x=190,y=220,width=160,height=20)
        #Martingale
        if(checkGale.get() == 1):
            Label(app,text='Multiplicador: '+str(multiplicador),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=280,width=160,height=20)
            for i in range(martingale):
                Label(app,text='Gale -  '+str(i+1)+':'  +' $'+str(round(valorBase*(multiplicador**(i+1)), 2)),background=corFundo,foreground=corInfo,anchor=W).place(x=190,y=220+((i+1)*20),width=160,height=20)
        #Soros
        if(checkSoros.get() == 1):
            Label(app,text='Mãos Soros: '+str(soros),background=corFundo,foreground=corInfo,anchor=W).place(x=30,y=280,width=160,height=20)
            if(valorBase >= 2):
                for i in range(soros):
                    Label(app,text='Soros -  '+str(i+1)+':'  +' $'+str(round(valorBase**(i+2), 2)),background=corFundo,foreground=corInfo,anchor=W).place(x=190,y=220+((i+1)*20),width=160,height=20)
            elif(valorBase < 2):
                for i in range(soros):
                    Label(app,text='Soros -  '+str(i+1)+':'  +' $'+str(round((valorBase*2)**(i+1), 2)),background=corFundo,foreground=corInfo,anchor=W).place(x=190,y=220+((i+1)*20),width=160,height=20)
        
        """ elif(sorosAtual > 0 and valorBase >= 2):
            keyboard.write(str(round(valorBase**(sorosAtual+1), 2)))
        elif(sorosAtual > 0 and valorBase < 2):
            keyboard.write(str(round((valorBase*2)**sorosAtual, 2))) """
        #Alerta Iniciar Bot

        if(martingale > 3 or soros > 3):
            Label(app,text='O Bot sera iniciado em 10 segundos!',background=corFundo,foreground=corAlerta,anchor=W).place(x=50,y=240+((i+1)*20),width=200,height=20)
        else:
            Label(app,text='O Bot sera iniciado em 10 segundos!',background=corFundo,foreground=corAlerta,anchor=W).place(x=50,y=320,width=200,height=20)

        app.after(10000, lambda: app.destroy())
    except:
        print('error')



#Funções de checkBox
def ativadorMartingale():
    if (checkGale.get() == 1):
        campoMartingale.config(state="normal")
        campoMultiplicador.config(state="normal")
        #Ativar Martingale desativa Soros
        checkSoros.set(0)
        campoSoros.config(state="disabled")
    else:
        campoMartingale.config(state="disabled")
        campoMultiplicador.config(state="disabled")

def ativadorSoros():
    if (checkSoros.get() == 1):
        campoSoros.config(state="normal")
        #Ativar Soros desativa Martingale
        checkGale.set(0)
        campoMartingale.config(state="disabled")
        campoMultiplicador.config(state="disabled")
    else:
        campoSoros.config(state="disabled")
        

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
boxGale = Checkbutton(app, text='Martingale',variable=checkGale, onvalue=1, offvalue=0, command=ativadorMartingale)
boxGale.place(x=300,y=35,width=100,height=20)

Label(app,text='Qtd.Gale',background=corFundo,foreground=corTexto,anchor=W).place(x=420,y=15,width=80,height=20)
campoMartingale=Entry(app)
campoMartingale.place(x=420,y=35,width=50,height=20)
campoMartingale.config(state="disabled")

Label(app,text='Mult.Gale',background=corFundo,foreground=corTexto,anchor=W).place(x=480,y=15,width=80,height=20)
campoMultiplicador=Entry(app)
campoMultiplicador.place(x=480,y=35,width=50,height=20)
campoMultiplicador.config(state="disabled")

#Informação Soros
checkSoros = IntVar()
boxSoros = Checkbutton(app, text='Soros',variable=checkSoros, onvalue=1, offvalue=0, command=ativadorSoros)
boxSoros.place(x=300,y=90,width=100,height=20)

Label(app,text='Qtd.Soros',background=corFundo,foreground=corTexto,anchor=W).place(x=420,y=70,width=80,height=20)
campoSoros=Entry(app)
campoSoros.place(x=420,y=90,width=50,height=20)
campoSoros.config(state="disabled")

#Alerta - Uso
Label(app,text='Nos valores com virgula 2,5 usar ponto 2.5',background=corFundo,foreground=corAlerta,anchor=W).place(x=30,y=60,width=240,height=20)
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

#exit usado para encerrar o bot // apenas para testar interface
#exit()



#iniciar o bot se a interface der permissão // sem permissão o bot fecha
if(interfacePermissao == True):
    pass
else:
    exit()
    


##########################################
######## INICIAR NAVEGADOR CHROME ########
##########################################
#PATH = "D:\Developer\Meus Projetos\Python\bitness\chromedriver.exe"
#driver = webdriver.Chrome(executable_path=r"D:\Developer\Meus Projetos\Python\bitness\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument("log-level=3")
#options.add_experimental_option("debuggerAddress", "127.0.0.1:9990")
chrome_driver = r".\chromedriver.exe"
driver = webdriver.Chrome(options=options)

#Conta Real
#driver.get("https://bitness.pro/en/trade/BTCUSD")
#Conta Teste
driver.get("https://testnet.bitness.pro/en/trade/BTCUSD")
driver.maximize_window()


sleep(60)



##########################################
######## FUNÇÕES DO BOT - EXECUTAR #######
##########################################
#usado para limitar a data de funcionamento do BOT
def verificaData():
    hoje = date.today()
    dia = hoje.day
    mes = hoje.month
    ano = hoje.year
    return [dia,mes,ano]

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def alteraValor():
    global valorBase, martingale, multiplicador, galeAtual
    click(1780,510) #valor da aposta 2 clicks
    click(1780,510)
    sleep(0.1)
    #Martingale
    if(galeAtual > 0):
        keyboard.write(str(round(valorBase*(multiplicador**galeAtual), 2)))
    #Soros
    elif(sorosAtual > 0 and valorBase >= 2):
        keyboard.write(str(round(valorBase**(sorosAtual+1), 2)))
    elif(sorosAtual > 0 and valorBase < 2):
        keyboard.write(str(round((valorBase*2)**sorosAtual, 2)))
    else:
        keyboard.write(str(valorBase))

def ordemVenda():
    try:
        ordem = driver.find_elements(By.CLASS_NAME, 'btn-order btn-red')[0]
        sleep(1)
        ordem.click()
    except:
        print('ERRO ORDEM-VENDA')

def wallet():
    try:
        wallet = driver.find_element(By.CLASS_NAME, 'wallet')
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
                #if r == 23 and g == 77 and b == 82:
                if r >= 19 and r <= 27 and g >= 73 and g <= 81 and b >= 78 and b <= 86:
                    verde += 1
                    return
                #vermelho
                #if r == 89 and g == 30 and b == 53:
                if r >= 85 and r <= 93 and g >= 26 and g <= 34 and b >= 49 and b <= 57:
                    vermelho += 1
                    return
    except:
        print('ERRO VERIFICAR VELAS')

def verificaTempo():
    try:
        segundos = driver.find_elements(By.CLASS_NAME, 'border')[1]
        segundos = int(segundos.get_attribute('innerHTML'))
        return segundos
    except:
        return 0

def verificaStopWinLoss():
    global win,stopWin,loss,stopLoss
    try:
        #verifica se atingiu stopWin ou stopLoss
        if(stopWin > 0 and win-loss >= stopWin):
            print('StopWin atingido, Bot encerrado!')
            print('Win: '+str(win), ' Loss: '+str(loss))
            input()
            exit()
        elif(stopLoss > 0 and win-loss <= -stopLoss):
            print('StopLoss atingido, Bot encerrado!')
            print('Win: '+str(win), ' Loss: '+str(loss))
            input()
            exit()
        else:
            pass
    except:
        pass


##########################################
######### VALIDAR ACESSO AO BOT ##########
##########################################
# Login e pega idUsuario
""" print('##################################################')
print('Iniciando Turim Bot')
print('Requisitando Acesso...')
idUsuario = conexao.verificaLogin('rafael@rafael.com','123123')
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
# inicia o valor da carteira
carteiraInicial = carteiraAntesAposta = wallet()
print('Carteira: $' +str(round(carteiraInicial,2)))
print('Entrada: $' +str(valorBase))
print('stopWin: ' +str(stopWin))
print('stopLoss: ' +str(stopLoss))
print('##################################################')
sleep(2)



##########################################
############# INICIAR O BOT ##############
##########################################
# inicia bot
while True:

    #TRAVAR O BOT APOS DATA LIMITE
    dataHoje = verificaData()
    #Se passar do Mês 3 ou do Ano 2022
    if(dataHoje[1] > 3 or dataHoje[2] > 2022):
        exit()
    #Se passar do Dia 7 do Mês 3
    elif(dataHoje[0] > 7 and dataHoje[1] == 3):
        exit()

    #verifica tempo
    segundos = verificaTempo()

    # Tempo de Apostar   
    if(segundos == 58):
        print('Analisando Velas...')
        verde=vermelho=0
        for i in range(velas):
            verificaVela(665-(i*50),860)
            sleep(0.2)

        #verificaVela(665,860) #vela1 = 665 860  #AWS Amazon EC2 666 860
        #sleep(0.2)
        #verificaVela(615,860) #vela2 = 615 860  #AWS Amazon EC2 615 860
        #sleep(0.2)
        #verificaVela(565,860) #vela3 = 565 860  #AWS Amazon EC2 565 860
        #sleep(0.2)
        print('Verdes:', verde, ' Vermelhas:', vermelho)
        # Rodada de Apostar
        if(verde == velas):
            print(str(velas)+' Velas Verdes - Iniciando Entrada')
            if(ultimoLoss == 1): #verde
                print('Ultimo Loss '+str(velas)+' Verdes, Entrada Cancelada...')
                sleep(5)
            else:
                print('Entrada Autorizada!')
                carteiraAntesAposta = wallet()
                alteraValor()
                sleep(0.3)
                click(1800,420) #altera para comprar vermelho(oposto das 3 velas)
                sleep(0.3)
                click(1780,730)
                sleep(130) #espera resultado
                #clicar 2x em intervalo de tempo pra limpar a tela
                click(1780,800)
                sleep(10)
                click(1780,800)
                sleep(1)
                #WIN
                if(wallet() > carteiraAntesAposta):
                    win += 1
                    ultimoLoss = 2 #nada
                    #Martingale
                    if(martingale > 0 and galeAtual > 0):
                        galeAtual = 0
                    #Soros
                    if(soros > 0 and sorosAtual < soros):
                        sorosAtual += 1
                    elif(soros > 0 and sorosAtual == soros):
                        sorosAtual = 0
                        print('SUCESSO NA SEQUENCIA DE '+str(soros)+' MÕAS DE SOROS! - VOLTANDO PARA ENTRADA INICIAL!')
                #LOSS
                elif(wallet() < carteiraAntesAposta):
                    loss += 1
                    ultimoLoss = 1
                    #Martingale
                    if(galeAtual < martingale):
                        galeAtual += 1
                    elif(martingale > 0 and galeAtual == martingale):
                        galeAtual = 0
                        print('ESTOUROU MARTINGALE - RESETANDO PARA ENTRADA INICIAL!')
                    #Soros
                    if(soros > 0 and sorosAtual != 0):
                        sorosAtual = 0
                #FALHA
                else:
                    falha += 1
                    ultimoLoss = 2 #nada
                sleep(0.1)
                profit = wallet() - carteiraAntesAposta
                sleep(0.2)
                #print('Enviando informação para o Banco de Dados...')
                #conexao.adicionaAposta(str(idUsuario),str(profit),'0',str(wallet()),str(win),str(loss),str(falha))
                print('*****Resultado*****')
                resultado = 'Turim Ferrari\nCarteira: $'+str(wallet())+'  Win: '+str(win)+'  Loss: '+str(loss)+'  Falha: '+str(falha)
                print(resultado)
                #telegramTurimFerrari.envia_mensagem(resultado)
        if(vermelho == velas):
            print(str(velas)+' Velas Vermelhas - Iniciando Entrada')
            if(ultimoLoss == 0): #vermelho
                print('Ultimo Loss '+str(velas)+' Vermelhas, Entrada Cancelada...')
                sleep(5)
            else:
                print('Entrada Autorizada!')
                carteiraAntesAposta = wallet()
                alteraValor()
                sleep(0.3)
                click(1700,420) #altera para comprar verde(oposto das 3 velas)
                sleep(0.3)
                click(1780,730)
                sleep(130) #espera resultado
                #clicar 2x em intervalo de tempo pra limpar a tela
                click(1780,800)
                sleep(10)
                click(1780,800)
                sleep(1)
                #WIN
                if(wallet() > carteiraAntesAposta):
                    win += 1
                    ultimoLoss = 2 #nada
                    #Martingale
                    if(martingale > 0 and galeAtual > 0):
                        galeAtual = 0
                    #Soros
                    if(soros > 0 and sorosAtual < soros):
                        sorosAtual += 1
                    elif(soros > 0 and sorosAtual == soros):
                        sorosAtual = 0
                        print('SUCESSO NA SEQUENCIA DE '+str(soros)+' MÕAS DE SOROS! - VOLTANDO PARA ENTRADA INICIAL!')
                #LOSS
                elif(wallet() < carteiraAntesAposta):
                    loss += 1
                    ultimoLoss = 0 #vermelho
                    #Martingale
                    if(galeAtual < martingale):
                        galeAtual += 1
                    elif(martingale > 0 and galeAtual == martingale):
                        galeAtual = 0
                        print('ESTOUROU MARTINGALE - RESETANDO PARA ENTRADA INICIAL')
                    #Soros
                    if(soros > 0 and sorosAtual != 0):
                        sorosAtual = 0
                #FALHA
                else:
                    falha += 1
                    ultimoLoss = 2 #nada
                sleep(0.1)
                profit = wallet() - carteiraAntesAposta
                sleep(0.2)
                #print('Enviando informação para o Banco de Dados...')
                #conexao.adicionaAposta(str(idUsuario),str(profit),'0',str(wallet()),str(win),str(loss),str(falha))
                print('*****Resultado*****')
                resultado = 'Turim Ferrari\nCarteira: $'+str(wallet())+'  Win: '+str(win)+'  Loss: '+str(loss)+'  Falha: '+str(falha)
                print(resultado)
                #telegramTurimFerrari.envia_mensagem(resultado)
        # Fim Tempo de Apostar
        print('##################################################')
        #verifica se atinjiu stopWin ou stopLoss
        verificaStopWinLoss()
        sleep(0.5)