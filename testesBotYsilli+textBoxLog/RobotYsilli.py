from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import numpy as np
import random
import keyboard
import pyautogui
import datetime

#GOOGLE CHROME
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9990")
# selenium buscará webdriver.exe en las variables de entorno del sistema cuando se ejecute
# Por lo general, coloque webdriver.exe en el directorio de python, de modo que no sea necesario especificarlo en el código.
#chrome_driver = r"C:\Users\ygor_\OneDrive\Área de Trabalho\bitness\robot\chromedriver.exe"
#chrome_driver = r"C:\Program Files\LUCAS FERREIRA\Bots\botTurimBitness\output\chromedriver.exe"
driver = webdriver.Chrome(options=options)


#Configuracion
xCua = 1000 #x cuadrado
yCua = 778 #y cuadrado

xBV = 1673 #x botao verde
yBV = 367 #y botao verde

xBR = 1815 #x botao rojo
yBR = 367 #y botao rojo

xAmount = 1819 #x amount
yAmount = 467 #y amount

xBA = 1751 #x botao de aposta
yBA = 617 #y botao de aposta

xSkip = 1761 #x skip
ySkip = 681 #y skip

vela1x = 685 #coordenada x da vela anterior
vela1y = 420 #coordenada y da vela anterior


#Variables
estados = 0
balAnterior = 0.0
corDeCompra = False #Color compra
cPasada = False #Compra pasada
gala = [1.03,3.09,7.27,16.76,38.02,82.19,172.85,360.89,733]
perdidas = 0
dicto = "1234567890."
vitoria = 0
derrota = 0
nAposta = 0
percentagem = 0
aGale = 0
bGale = 0
cGale = 0
dGale = 0
eGale = 0
fGale = 0
gGale = 0
hGale = 0
iGale = 0

def main():
	while True:
		if estados == 0:
			print("Analizando o estado do mercado....")
			analizar()
			print("Analizamento foi concluido....")

		if estados == 1:
			print("Iniciando Função Compra....")
			compra()
			nAposta = vitoria + derrota
			percentagem = (vitoria/nAposta)*100
			printarInformacao()


def printarInformacao():
	global vitoria
	global derrota
	global percentagem
	global aGale 
	global bGale 
	global cGale 
	global dGale 
	global eGale 
	global fGale
	global gGale
	global hGale
	global iGale


	print("Vitorias = ", vitoria)
	print("Derrotas = ", derrota)
	print("Percentagem de vitorias = ", percentagem, "%")
	print("total de gales:", aGale, bGale, cGale, dGale, eGale, fGale, gGale, hGale, iGale)

				
def contarGale():
	global perdidas
	global aGale 
	global bGale 
	global cGale 
	global dGale 
	global eGale 
	global fGale
	global gGale
	global hGale
	global iGale
	global mudartendencia

	if mudartendencia == True:
		if(perdidas == 0):
			aGale += 1
		if(perdidas == 1):
			bGale += 1
		if(perdidas == 2):
			cGale += 1
		if(perdidas == 3):
			dGale += 1
		if(perdidas == 4):
			eGale += 1
		if(perdidas == 5):
			fGale += 1
		if(perdidas == 6):
			gGale += 1
		if(perdidas == 7):
			hGale += 1
		if(perdidas == 8):
			iGale += 1
	
	



def analizar():
	global estados
	global corDeCompra
	global gala
	global perdidas
	global sinal

	tiempo()
	time.sleep(1)

	sinal = cuadrado()

	if sinal != 2:
		if sinal == 0: #Roja
			print("Quadrado VERMELHO encontrado")
			corDeCompra = False    #false e vermelho
			aposta()			   #Chama a Função aposta
			estados = 1
		if sinal == 1: #Verde
			print("Quadrado VERDE encontardo")
			corDeCompra = True     #true e verde
			aposta()
			estados = 1
	else:
		print("Quadrado nao foi encontrado")

def compra():
	global estados
	global corDeCompra
	global cPasada
	global balAnterior
	global perdidas
	global mudartendencia
	global sinal
	global derrota
	global vitoria
	global ganhar

	tiempo()
	time.sleep(2)

	mudartendencia = True #iniciando variable mudartendencia

	cor = sinal #lendo o estado do ultimo quadrado

	'''
	if cor != 2: 
		if cor == 0: #Roja
			corDeCompra = False
									
		if cor == 1: #Verde
			corDeCompra = True
	'''
	tiempo()	
	time.sleep(7)

	pyautogui.click(xSkip, ySkip, duration=0.2)# skip

	#Determianr vitoria
	ganhar = determinadorDeVitoria()
	print(ganhar)


	if ganhar == cor:
		print("Ganhou! =) ")
		vitoria += 1
		contarGale()
		perdidas = 0
		mudartendencia = True
		print("Mudar a tedencia")
	else:
		print("Perdeu :( ")
		derrota += 1
		mudartendencia = False
		print("Nao mudar a tedencia")
		if perdidas == 8:
			perdidas = 0
		else:
			perdidas += 1


	'''	
	if balance() != balAnterior:
		print("Ganhou! =) ")
		vitoria += 1
		contarGale()
		perdidas = 0
		mudartendencia = True
		print("Mudar a tedencia")

	else:
		print("Perdeu :( ")
		derrota += 1
		mudartendencia = False
		print("Nao mudar a tedencia")
		if perdidas == 8:
			perdidas = 0
		else:
			perdidas += 1 '''
	
	if mudartendencia == True:		
		cor = cuadrado()
		print(".......mudando a tendencia")
	
	

	#Se quadrado for de cor vermelha ou verde variable corDeCompra e mudado de acordo
	if cor != 2:
		if cor == 0: #Roja
			corDeCompra = False
									
		if cor == 1: #Verde
			corDeCompra = True

	sinal = cor
	aposta()

def determinadorDeVitoria():
	ganhar = 2
	print("Buscando a cor.....")
	if pyautogui.pixelMatchesColor(685, 420, (255, 228, 14)): #verde
		ganhar = 1 
			
	if pyautogui.pixelMatchesColor(685, 420, (255, 7, 0)): #vermelho
		ganhar = 0

	return ganhar

def cuadrado():
	color = 2
	for i in range(xCua, 0, -15):
		print("Buscando a tendencia.....")
		if pyautogui.pixelMatchesColor(i, yCua, (255, 7, 0)): 
			color = 0 
			print("Tendencia achada cor vermelha")
			break
		if pyautogui.pixelMatchesColor(i, yCua, (255, 228, 14)):
			color = 1
			print("Tendencia achada cor verde")
			break

	return color

def aposta():
	global corDeCompra
	global balAnterior
	global gala
	global perdidas

	if corDeCompra:
		pyautogui.click(xBV, yBV, duration=0.2)   #clica no botao de aposta verde     corDeCompra = true
	else:
		pyautogui.click(xBR, yBR, duration=0.2)	  #clica no botao de aposta Vermelho   corDeCompra = false

	pyautogui.click(xAmount, yAmount, duration=0.2)   
	pyautogui.click(xAmount, yAmount)

	keyboard.write(str(gala[perdidas]))

	pyautogui.click(xBA, yBA, duration=0.2) #clica do botao de aposta

	time.sleep(3)
	balAnterior = balance()

def tiempo():
	cont = driver.find_element_by_css_selector("div[class='orderform flexbox']")
	subCont = cont.find_element_by_css_selector("div[class='content']")
	timeD = subCont.find_element_by_css_selector("div[class='timedown']")
	tiempos = timeD.find_elements_by_css_selector("div[class='item']")

	contador = 0
	segun = ""

	for t in tiempos:
		if contador == 1:
			segun = t.find_element_by_css_selector("div[class='border']").text
			break

		contador += 1

	segun = int(segun)

	#REGRESIVA
	for i in range(segun):
		print(segun)
		time.sleep(1)
		segun -= 1
		if (segun == 1):
			time.sleep(2)
			break

def balance():
	content = driver.find_element_by_css_selector("div[class='group-wallet']")
	trade = content.find_element_by_css_selector("[class='wallet']").text
	cadena = ""
	for i in trade:
		for a in dicto:
			if i == a:
				cadena += i

	return float(cadena)


main()