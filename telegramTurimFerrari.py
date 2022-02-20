import requests
import json

#http usando token do BOT para descobrir o ID do grupo -- https://api.telegram.org/bot1942976509:AAEkZ8h0O4LVX1lHHkZbvaL0dz3PUeX_9Dg/getUpdates
#Enviar mensagem iniciado com barra /opa - no grupo em que o bot esta para conseguir o idGrupo
token = '1942976509:AAEkZ8h0O4LVX1lHHkZbvaL0dz3PUeX_9Dg'
#idGrupo = '-1001433809691' #TurimBot
idGrupo = '-1001528584550' #TurimFerrari
stickerWin = 'CAACAgEAAxkBAAECpxRhAbNmQxm3DQaTS4-rSJuNfMgp3AACEgIAAgcE6UfTL460p7V2jSAE'

# enviar mensagens utilizando o bot para um chat específico
def envia_mensagem(mensagem):
    global token, idGrupo
    try:
        msg = mensagem
        data = {"chat_id": idGrupo, "text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        req = requests.post(url, data)
        print(url)
    except Exception as e:
        print("Erro no sendMessage:", e)

def stopWin():
    global token, idGrupo
    try:
        files = {"photo": open('Win.png', 'rb')}
        url = ("https://api.telegram.org/bot"+token+"/sendPhoto?chat_id="+idGrupo)
        requests.post(url, files = files)
    except Exception as e:
        print("Erro no sendMessage:", e)

def sendSticker():
    global token, idGrupo, stickerWin
    try:
        
        url = ("https://api.telegram.org/bot"+token+"/sendSticker?chat_id="+idGrupo+"&sticker="+stickerWin)
        requests.post(url,)
    except Exception as e:
        print("Erro no sendMessage:", e)