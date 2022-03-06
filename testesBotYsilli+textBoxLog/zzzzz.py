from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import numpy as np
import random
import keyboard
import pyautogui
import datetime

#GOOGLE CHROME
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9990")
# selenium buscará webdriver.exe en las variables de entorno del sistema cuando se ejecute
# Por lo general, coloque webdriver.exe en el directorio de python, de modo que no sea necesario especificarlo en el código.
#chrome_driver = r"C:\Program Files\LUCAS FERREIRA\Bots\botTurimBitness\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options)
#driver.get('https://testnet.bitness.pro/en/trade/BTCUSD')


sleep(2)

ultimaOrdemID = ""

def verificaOrdemAberta():
    try:
        ordemAberta = driver.find_elements(By.CLASS_NAME, 'font-regular')[0].find_elements(By.CLASS_NAME, 'orderid')[0].text
        sleep(0.1)
        return ordemAberta
    except:
        return False

ultimaOrdemHistoricoID = driver.find_elements(By.CLASS_NAME, 'font-regular')[1].find_elements(By.CLASS_NAME, 'orderid')[0]
ultimaOrdemHistoricoStatus = driver.find_elements(By.CLASS_NAME, 'font-regular')[1].find_elements(By.CLASS_NAME, 'status')[0]

ordemAtual = verificaOrdemAberta()
if ordemAtual != False:
    print(ordemAtual)
    ultimaOrdemID = ordemAtual
else:
    print('Não existem ordens abertas')

    print(ultimaOrdemHistoricoID.text, ultimaOrdemHistoricoStatus.text)


""" tt = document.getElementsByClassName("font-regular");
ultimoHistorico = tt[1].rows[0];
histOrdemId = ultimoHistorico.getElementsByClassName("orderid")[0];
winLoss = ultimoHistorico.getElementsByClassName("status")[0];
console.log(histOrdemId.textContent);
if(histOrdemId.textContent == "414060071"){
    if(winLoss.textContent == "lose"){
        console.log("perdi");
    }else{
        console.log("ganhei");
    }
} """