from tkinter import *
from jinja2 import Undefined
import pyautogui
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime, date
import csv
import os.path

##############################
#######   VARIÁVEIS    #######
##############################
#Coordenadas  Botões/campoAposta/limparTela
btnRED = (1800, 360)
btnGREEN = (1700, 360)
btnAPOSTA = (1750, 690)
campoValorAposta = (1822, 466)
clickLimparTela = (1755, 255)
#Vela//Indicador Volume opacidade 100%
velaAtual = (733, 822)
velaAnterior = (683, 822)
corVelaVermelha = (254, 71, 97)
corVelaVerde = (63, 207, 180)
#Quadrado para analise de tencendia
coordQuadradoTendencia = (683, 753)
corQuadradoVermelho = (255, 0, 0)
corQuadradoAmarelo = (255, 229, 0)
tendencia = Undefined
#Win / Loss / contador de gale / contador de velas para trocar tendencia
contadorVelasTendencia = 0
contadorTrocaTendencia = 0
galeAtual = 0
win = 0
loss = 0
#Configurações de Aposta -- Ajuste Pessoal para funcionamento do Bot
travaTrocaTendencia = 10
valorGale = [1.03,3.09,7.27,16.76,38.02,82.19,172.85,360.89,733]
maxGale = 9 #quantidade de gales + entrada inicial // ex: 8 gales + entrada inicial = 9
contadorGales = []
for i in range(maxGale):
	contadorGales.append(0)


##############################
#####   GOOGLE CHROME    #####
##############################
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9990")
driver = webdriver.Chrome(options=options)


##############################
########   FUNÇÕES    ########
##############################
#Pegar dia/mes/ano
def verificaData():
    hoje = date.today()
    dia = hoje.day
    mes = hoje.month
    ano = hoje.year
    return [dia,mes,ano]

def main():
	while True:
		#TRAVAR O BOT APOS DATA LIMITE
		dataHoje = verificaData()
    	#Se Mês for diferente de Março ou Ano diferente de 2022 // Fecha o Bot
		if(dataHoje[1] != 3 or dataHoje[2] != 2022):
			exit()

		#Inicia Analise/Aposta do Bot
		if verificarTempo() == 59:
			if type(tendencia) == bool:
				verificarWinLoss()
				resultadoBancoDados()
			#primeira analise de tendencia // analisa tendencia quanto quantidade de velas passar da trava
			if tendencia == Undefined or contadorVelasTendencia >= travaTrocaTendencia:
				analisarTendencia()
			apostar()
		sleep(0.3)


def analisarTendencia():
	global tendencia, contadorVelasTendencia, contadorTrocaTendencia
	print("Buscando a tendencia.....")
	for i in range(coordQuadradoTendencia[0], 0, -50):
		if pyautogui.pixelMatchesColor(i, coordQuadradoTendencia[1], (corQuadradoVermelho), tolerance=10): #Tendencia Baixa // quadrado vermelho
			if tendencia == True:
				contadorTrocaTendencia += 1
			tendencia = False
			contadorVelasTendencia = 0
			print("Tendencia de BAIXA!")
			break
		if pyautogui.pixelMatchesColor(i, coordQuadradoTendencia[1], (corQuadradoAmarelo), tolerance=10): #Tendencia Alta // quadrado amarelo
			if tendencia == False:
				contadorTrocaTendencia += 1
			tendencia = True
			contadorVelasTendencia = 0
			print("Tendencia de ALTA!")
			break


def balance():
	wallet = driver.find_element(By.CSS_SELECTOR, ".group-wallet .wallet").text
	digito = '0123456789.'
	valor = ""
	for i in wallet:
		for a in digito:
			if i == a:
				valor += i
	return float(valor)


def verificarWinLoss():
	global win, loss, galeAtual
	for i in range(velaAnterior[1], 772, -1):
		if pyautogui.pixelMatchesColor(velaAnterior[0], i, (corVelaVermelha), tolerance=10): #Vela Vermelha
			if tendencia == False:
				print('win tendencia baixa / vela anterior vermelha')
				win += 1
				galeAtual = 0
				break
			else:
				print('loss tendencia alta / vela anterior verde')
				loss += 1
				galeAtual += 1
				break
		if pyautogui.pixelMatchesColor(velaAnterior[0], i, (corVelaVerde), tolerance=10): #Vela Verde
			if tendencia == True:
				print('win tendencia alta / vela anterior verde')
				win += 1
				galeAtual = 0
				break
			else:
				print('loss tendencia alta / vela anterior vermelha')
				loss += 1
				galeAtual += 1
				break

def resultadoBancoDados():
	global win, loss, contadorGales
	nAposta = win + loss
	porcentagem = (win/nAposta)*100

	carteira = balance()

	now = datetime.now()
	horaAtual = now.strftime("%H:%M:%S")

	print("Vitorias = ", win)
	print("Derrotas = ", loss)
	print("Total de apostas = ", nAposta)
	print("Porcentagem de vitoria = ", porcentagem, "%")
	print("total de gales:", contadorGales[0], contadorGales[1], contadorGales[2], contadorGales[3], contadorGales[4], contadorGales[5], contadorGales[6], contadorGales[7], contadorGales[8])


	arquivoExiste = os.path.exists('Info.csv')
	if arquivoExiste == True:
		with open('Info.csv', 'a', newline='\n') as csvfile:
				fieldnames = ['Vitorias', 'Derrotas', 'Numero de apostas','Porcentagem de vitoria','Carteira','0 Gale','1 Gale', '2 Gale', '3 Gale', '4 Gale', '5 Gale', '6 Gale', '7 Gale', '8 Gale', 'Horário']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writerow({'Vitorias': win, 'Derrotas': loss,'Numero de apostas': nAposta,'Porcentagem de vitoria': porcentagem,'Carteira': str(carteira),'0 Gale': contadorGales[0],'1 Gale': contadorGales[1], '2 Gale': contadorGales[2], 
									'3 Gale': contadorGales[3], '4 Gale': contadorGales[4], '5 Gale':contadorGales[5], '6 Gale': contadorGales[6], '7 Gale': contadorGales[7], '8 Gale': contadorGales[8],'Horário': horaAtual})
	else:
		with open('Info.csv', 'w', newline='\n') as csvfile:
				fieldnames = ['Vitorias', 'Derrotas', 'Numero de apostas','Porcentagem de vitoria','Carteira','0 Gale','1 Gale', '2 Gale', '3 Gale', '4 Gale', '5 Gale', '6 Gale', '7 Gale', '8 Gale','Horário']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()
				writer.writerow({'Vitorias': win, 'Derrotas': loss,'Numero de apostas': nAposta,'Porcentagem de vitoria': porcentagem,'Carteira': str(carteira),'0 Gale': contadorGales[0],'1 Gale': contadorGales[1], '2 Gale': contadorGales[2], 
									'3 Gale': contadorGales[3], '4 Gale': contadorGales[4], '5 Gale':contadorGales[5], '6 Gale': contadorGales[6], '7 Gale': contadorGales[7], '8 Gale': contadorGales[8],'Horário': horaAtual})


def clicar(coordenada):
	pyautogui.moveTo(coordenada)
	sleep(0.1)
	pyautogui.click()
	sleep(0.1)


def alterarValorAposta():
	pyautogui.moveTo(campoValorAposta)
	sleep(0.1)
	pyautogui.click()
	pyautogui.click()
	sleep(0.1)
	keyboard.write(str(valorGale[galeAtual]))
	sleep(0.1)


def apostar():
	global contadorVelasTendencia, contadorGales
	if tendencia == False: #click vermelho
		clicar(btnRED)
		alterarValorAposta()
		clicar(btnAPOSTA)
	if tendencia == True: #click verde
		clicar(btnGREEN)
		alterarValorAposta()
		clicar(btnAPOSTA)
	#apos apostar adicionar informação no banco de dados // aumentar contador de gales
	sleep(15)
	contadorGales[galeAtual] += 1
	contadorVelasTendencia += 2
	sleep(60)
	clicar(clickLimparTela)
	sleep(2)


def verificarTempo():
	try:
		segundos = driver.find_elements(By.CLASS_NAME, 'border')[1].text
		return int(segundos)
	except:
		return 0



##############################
######   INICIAR BOT    ######
##############################
sleep(3)
main()