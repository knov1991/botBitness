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

def trocarAbaOrdem(trocarAba):
    btnAba = driver.find_elements(By.CSS_SELECTOR, "a[href='#tab-"+trocarAba+"']")[0]
    driver.execute_script("arguments[0].click();", btnAba)
    sleep(1)

""" sleep(1)
btnOpenOrder = driver.find_elements(By.CSS_SELECTOR, "a[href='#tab-open']")[0]
driver.execute_script("arguments[0].click();", btnOpenOrder)

sleep(1)
btnHistoryOrder = driver.find_elements(By.CSS_SELECTOR, "a[href='#tab-history']")[0]
driver.execute_script("arguments[0].click();", btnHistoryOrder) """

trocarAbaOrdem('open')
trocarAbaOrdem('history')