from tkinter import *
import win32api, win32con
import pyautogui
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from time import sleep
from datetime import date

##############################
#######   VARIÁVEIS    #######
##############################
#Coordenadas
btnRED = (1800, 360)
btnGREEN = (1700, 360)
btnAPOSTA = (1750, 690)
quadradoAnalise = (808, 309)
campoValorAposta = (1822, 466)
clickLimparTela = (1764, 756)
#Configurações de Aposta
botIniciado = False
entradaGale = [1.03,3.09,7.27,16.76,38.02,82.19,172.85,360.89,733]
contadorGales = []
maxGale = 8
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
		if botIniciado == False:
			print('analisar primeira entrada')
		else:
			print('apostar')
		sleep(5)


def balance():
	content = driver.find_element(By.CSS_SELECTOR, "div[class='group-wallet']")
	trade = content.find_element(By.CSS_SELECTOR, "[class='wallet']").text
	digito = '0123456789.'
	valor = ""
	for i in trade:
		for a in digito:
			if i == a:
				valor += i
	return float(valor)



print(contadorGales)