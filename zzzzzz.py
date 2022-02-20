from datetime import date

def verificaData():
    hoje = date.today()
    dia = hoje.day
    mes = hoje.month
    ano = hoje.year
    return [dia,mes,ano]

dataHoje = verificaData()
    #Bot para de funcionar se passar do mês 2 ou do ano 2022
if(dataHoje[0] != 19):
    print('passou do dia')