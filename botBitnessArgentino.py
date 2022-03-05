from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import numpy as np
import keyboard
import pyautogui

#GOOGLE CHROME
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9990")
# selenium buscará webdriver.exe en las variables de entorno del sistema cuando se ejecute
# Por lo general, coloque webdriver.exe en el directorio de python, de modo que no sea necesario especificarlo en el código.
chrome_driver = r"C:\Users\marce\OneDrive\Área de Trabalho\bitness\ROBOTCRUZ\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)


#Configuracion
xCua = 1315 #x cuadrado
yCua = 755 #y cuadrado

xBV = 2336 #x boton verde
yBV = 360 #y boton verde

xBR = 2456 #x boton rojo
yBR = 360 #y boton rojo

xAmount = 2464 #x amount
yAmount = 469 #y amount

xBA = 2402 #x boton apuesta
yBA = 684 #y boton apuesta

xSkip = 2390 #x skip
ySkip = 652 #y skip


#Variables
estados = 0
balAnterior = 0.0
cCompra = False #Color compra
cPasada = False #Compra pasada
gala = [1.03,3.09,7.27,16.76,38.02,82.19,172.85,360.89,733]
perdidas = 0
dicto = "1234567890."
ultimoQuadrado = int


def main():
	while True:
		if estados == 0:
			busqueda()

		if estados == 1:
			compra()

		
			
def busqueda():
	global estados
	global cCompra
	global gala
	global perdidas

	tiempo()
	time.sleep(1)

	señal = cuadrado()

	if señal != 2:
		if señal == 0: #Roja
			print("Cuadrado Rojo")
			cCompra = False
			apuesta()
			estados = 1
		if señal == 1: #Verde
			print("Cuadrado Verde")
			cCompra = True
			apuesta()
			estados = 1
	else:
		print("Cuadrado no encontrado")

def compra():
	global estados
	global cCompra
	global cPasada
	global balAnterior
	global perdidas
	global ultimoQuadrado


	tiempo()
	time.sleep(2)

	cuadrado()

	tiempo()
	time.sleep(7)

	pyautogui.click(xSkip, ySkip, duration=0.6)# skip

	if balance() != balAnterior:
		print("Gano")
		perdidas = 0
		if ultimoQuadrado == 0: #Roja
			cCompra = False
		if ultimoQuadrado == 1: #Verde
			cCompra = True
	else:
		print("perdio")
		if perdidas == 8:
			perdidas = 0
		else:
			perdidas += 1

	apuesta()

def cuadrado():
	global ultimoQuadrado

	color = 2
	if pyautogui.pixelMatchesColor(xCua, yCua, (255, 0, 0)):
		color, ultimoQuadrado = 0, 0

	if pyautogui.pixelMatchesColor(xCua, yCua, (255, 235, 59)):
		color, ultimoQuadrado = 1, 1

	return color

def apuesta():
	global cCompra
	global balAnterior
	global gala
	global perdidas

	if cCompra:
		pyautogui.click(xBV, yBV, duration=0.6)# color verde
	else:
		pyautogui.click(xBR, yBR, duration=0.6)# color rojo

	pyautogui.click(xAmount, yAmount, duration=0.6)
	pyautogui.click(xAmount, yAmount)

	keyboard.write(str(gala[perdidas]))

	pyautogui.click(xBA, yBA, duration=0.6) #boton apuesta

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