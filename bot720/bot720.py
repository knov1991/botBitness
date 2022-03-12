from tkinter import *
from jinja2 import Undefined
import pyautogui
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import date

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
galeAtual = 0
win = 0
loss = 0
#Configurações de Aposta -- Ajuste Pessoal para funcionamento do Bot
travaTrocaTendencia = 14
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
def main():
	while True:
		if verificarTempo() == 59:
			#primeira analise de tendencia // analisa tendencia quanto quantidade de velas passar da trava
			if tendencia == Undefined or contadorVelasTendencia >= travaTrocaTendencia:
				analisarTendencia()
			apostar()
		sleep(0.3)


def analisarTendencia():
	global tendencia, tendencia, contadorVelasTendencia
	for i in range(coordQuadradoTendencia[0], 0, -50):
		print("Buscando a tendencia.....")
		if pyautogui.pixelMatchesColor(i, coordQuadradoTendencia[1], (corQuadradoVermelho), tolerance=10): #Tendencia Baixa // quadrado vermelho
			tendencia = False
			contadorVelasTendencia = 0
			print("Tendencia de BAIXA!")
			break
		if pyautogui.pixelMatchesColor(i, coordQuadradoTendencia[1], (corQuadradoAmarelo), tolerance=10): #Tendencia Alta // quadrado amarelo
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
	global win, loss, tendencia, galeAtual
	for i in range((velaAnterior[0]), 772, -1):
		if pyautogui.pixelMatchesColor(i, velaAnterior[1], (corVelaVermelha), tolerance=10): #Vela Vermelha
			if tendencia == False:
				win += 1
				galeAtual = 0
				break
			else:
				loss += 1
				galeAtual += 1
				break
		if pyautogui.pixelMatchesColor(i, velaAnterior[1], (corVelaVerde), tolerance=10): #Vela Verde
			if tendencia == True:
				win += 1
				galeAtual = 0
				break
			else:
				loss += 1
				galeAtual += 1
				break


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
	global tendencia, contadorVelasTendencia
	if tendencia == False: #click vermelho
		clicar(btnRED)
		alterarValorAposta()
		clicar(btnAPOSTA)
	if tendencia == True: #click verde
		clicar(btnGREEN)
		alterarValorAposta()
		clicar(btnAPOSTA)
	#adicionar vela atual + vela de analise para contador de velas usado na trava de tendencix
	contadorVelasTendencia += 2
	sleep(70)
	clicar(clickLimparTela)
	sleep(2)


def verificarTempo():
	try:
		segundos = driver.find_elements(By.CLASS_NAME, 'border')[1].text
		return int(segundos)
	except:
		return 0

sleep(3)
main()