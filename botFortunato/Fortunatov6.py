from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import numpy as np
import random
import keyboard
import pyautogui
import datetime
import tkinter as tk
from tkinter import *
import csv
from datetime import datetime

#GOOGLE CHROME
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9990")
# selenium buscará webdriver.exe en las variables de entorno del sistema cuando se ejecute
# Por lo general, coloque webdriver.exe en el directorio de python, de modo que no sea necesario especificarlo en el código.
chrome_driver = r"C:\Users\BRABO\Desktop\FOTUNATO V6\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)


#Configuracion
xCua = 808 #x cuadrado
yCua = 309 #y cuadrado

xBV = 1700 #x botao verde
yBV = 360 #y botao verde

xBR = 1800 #x botao rojo
yBR = 360 #y botao rojo

xAmount = 1822 #x amount
yAmount = 466 #y amount

xBA = 1750 #x botao de aposta
yBA = 690 #y botao de aposta

xSkip = 1764 #x skip
ySkip = 756 #y skip

xVol = 688
yVol = 822


#Variables
estados = 0
balAnterior = 0.0
corDeCompra = False #Color compra
cPasada = False #Compra pasada
gala = [1.03,3.09,7.27,16.76,38.02,82.19,172.85,360.89,733]
#gala = [3.09,9.27,27.81,83.43,250.29,766.32]
perdidas = 0
dicto = "1234567890."
vitoria = 0
derrota = 0
nAposta = 0
percentagem = 0
cor = 2
createdCsvFile = False
contadorDeAposta = 0
#Gales
contadorGale = []
maxGales = 5
for i in range(maxGales):
	contadorGale.append(0)


def main():
	while True:
		if estados == 0:
			print("Analizando o estado do mercado....")
			analizar()
			print("Analizamento foi concluido....")

		if estados == 1:
			print("Iniciando Função Compra....")
			compra()
			printarInformacao()
	'''
	global frame
	global start

	window = tk.Tk()
	window.geometry("718x800")

	# Add image file
	bgImage = PhotoImage(file = "background.png")
	startButton = PhotoImage(file = "start.png")
  
	# Show image using label
	bg = Label( window, image = bgImage)
	bg.place(x = 0, y = 0)

	# Create Frame
	frame = Frame(window)
	frame.pack(pady = 0 )
	  
	  #500x555
	# Add buttons
	start = Button(window, command = robot, image = startButton, highlightthickness = 0, borderwidth = 0, bd = 0)
	start.place(x= 580,y= 55)
	##button2 = Button( frame, text = "Start")
	#button2.pack(pady = 20)



	window.mainloop()'''


def robot():
	global start
	print("robot started")
	while True:
		if estados == 0:
			print("Analizando o estado do mercado....")
			analizar()
			print("Analizamento foi concluido....")

		if estados == 1:
			print("Iniciando Função Compra....")
			compra()
			
			printarInformacao()



def printarInformacao():
	global vitoria
	global derrota
	global percentagem
	global contadorGale
	global nAposta
	global createdCsvFile
	global balAnterior

	nAposta = vitoria + derrota
	percentagem = (vitoria/nAposta)*100

	now = datetime.now()

	current_time = now.strftime("%H:%M:%S")

	

	print("Vitorias = ", vitoria)
	print("Derrotas = ", derrota)
	print("Total numero de apostas = ", nAposta)
	print("Percentagem de vitorias = ", percentagem, "%")
	print("total de gales:", aGale, bGale, cGale, dGale, eGale, fGale, gGale, hGale, iGale)

	if createdCsvFile == False:
		with open('Info.csv', 'w', newline='\n') as csvfile:
				fieldnames = ['Vitorias', 'Derrotas', 'numero de apostas','percentagem de vitorias','balanca','0 Gales','1 Gale', '2 Gale', '3 Gale', '4 Gale', '5 Gale', '6 Gale', '7 Gale', '8 Gale', 'Time']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writeheader()
				writer.writerow({'Vitorias': vitoria, 'Derrotas': derrota,'numero de apostas': nAposta,'percentagem de vitorias': percentagem,'balanca': balAnterior,'0 Gales': aGale,'1 Gale': bGale, '2 Gale': cGale, 
									'3 Gale': dGale, '4 Gale': eGale, '5 Gale':fGale, '6 Gale': gGale, '7 Gale': hGale, '8 Gale': iGale,'Time': current_time})
	else:
		with open('Info.csv', 'a', newline='\n') as csvfile:
				fieldnames = ['Vitorias', 'Derrotas', 'numero de apostas','percentagem de vitorias','balanca','0 Gales','1 Gale', '2 Gale', '3 Gale', '4 Gale', '5 Gale', '6 Gale', '7 Gale', '8 Gale','Time']
				writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
				writer.writerow({'Vitorias': vitoria, 'Derrotas': derrota,'numero de apostas': nAposta,'percentagem de vitorias': percentagem,'balanca': balAnterior,'0 Gales': aGale,'1 Gale': bGale, '2 Gale': cGale, 
									'3 Gale': dGale, '4 Gale': eGale, '5 Gale':fGale, '6 Gale': gGale, '7 Gale': hGale, '8 Gale': iGale,'Time': current_time})
	

	createdCsvFile = True

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
	global cor

	tiempo()
	time.sleep(2)

	mudartendencia = False #iniciando variable mudartendencia

	cor = sinal #lendo o estado do ultimo quadrado

	'''
	if cor != 2: 
		if cor == 0: #Roja
			corDeCompra = False
									
		if cor == 1: #Verde
			corDeCompra = True
	'''
	tiempo()	
	time.sleep(8)

	pyautogui.click(xSkip, ySkip, duration=0.6)# skip

	#Determianr vitoria
	ganhar = determinadorDeVitoria()
	print(ganhar)



	if ganhar == cor:
		print("Ganhou! =) ")
		derrota = 0
		vitoria += 1
		contarGale()
		perdidas = 0
		if contadorDeAposta == 7: #contado de aposta para mudanca de tendencia
			mudartendencia = True
			print("Mudar a tedencia")
			contadorDeAposta = 0
	else:
		print("Perdeu :( ")
		derrota += 1
		if contadorDeAposta == 7: #contado de aposta para mudanca de tendencia com renato
			mudartendencia = True
			print("Mudar a tedencia")
			contadorDeAposta = 0

		if perdidas == 8: #quantidade de gales a se fazer
			perdidas = 0
		else:
			perdidas += 1

		if derrota == 4: #quantidade de gales perdidos para dormir
			tendenciaAtual = cuadrado()
			if tendenciaAtual != cor:
				print("hora de dormir por 5 minutos!")
				time.sleep(300)
				cor = cuadrado()

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
	contadorDeAposta += 1
	aposta()

def determinadorDeVitoria():
	ganhar = 2
	print("Buscando a cor.....")
	time.sleep(3)
	
	if pyautogui.pixelMatchesColor(xVol, yVol, (255, 235, 59)): #verde
		ganhar = 1 
		print("verde volume encontrado")
			
	if pyautogui.pixelMatchesColor(xVol, yVol, (254, 71, 97)): #vermelho
		ganhar = 0
		print("vermelho volume encontrado")

	return ganhar

def cuadrado():
	global cor

	color = cor
	for i in range(xCua, 0, -15):
		print("Buscando a tendencia.....")
		if pyautogui.pixelMatchesColor(i, yCua, (255, 0, 0)):  #vermelho
			color = 0 
			print("Tendencia achada cor vermelha")
			break
		if pyautogui.pixelMatchesColor(i, yCua, (255, 235, 59)):  #verde
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
		pyautogui.click(xBV, yBV, duration=0.6)   #clica no botao de aposta verde     corDeCompra = true
	else:
		pyautogui.click(xBR, yBR, duration=0.6)	  #clica no botao de aposta Vermelho   corDeCompra = false

	pyautogui.click(xAmount, yAmount, duration=0.6)   
	pyautogui.click(xAmount, yAmount)

	keyboard.write(str(gala[perdidas]))

	pyautogui.click(xBA, yBA, duration=0.6) #clica do botao de aposta

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