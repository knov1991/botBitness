#pip install pymysql
import pymysql
import time


def conexaoBanco():
    HOST='turimdb.cqvpghqsplex.us-east-2.rds.amazonaws.com'
    DB='bitness'
    USER='admin'
    PASSWORD='turim972468'

    """ HOST='localhost'
    DB='bitness'
    USER='root'
    PASSWORD='root' """
    try:
        con = pymysql.connect(host=HOST, database=DB, user=USER, password=PASSWORD)
        #conc = con.cursor()
    except:
        return -1
    return con

def verificaLogin(email,password):
    try:
        con = conexaoBanco()
        cursor = con.cursor()
        sql = "select * from usuarios where email = '"+email+"' and password = '"+password+"';"
        cursor.execute(sql)
        res = cursor.fetchone()
        #usuario existe
        if(res):
            """ #procedure verifica se usuario ainda tem dias de acesso(dia de hoje < data do usuario)
            verD = "call verificaData("+str(res[0])+",@vrdata)"
            cursor.execute(verD)
            verData = cursor.fetchone()
            if(verData[0] == 1): """
            idUsuario = res[0] # idUsuario
            if(res[3] == 0): #verifica se usuario esta bloqueado // 0 = não bloqueado - 1 = bloqueado
                #print('Bem Vindo')
                return int(idUsuario)
            else:
                #print('Acesso Negado')
                return -1
        else:
            #print('Acesso Negado')
            return -1
    except:
        return -1

def adicionaAposta(idUsuario,profit,martingale,carteira,win,loss,falha):
    try:
        con = conexaoBanco()
        cursor = con.cursor()
        sql = "insert into apostas(idUsuario, profit, martingale, carteira, win, loss, falha) value('"+idUsuario+"','"+profit+"','"+martingale+"','"+carteira+"','"+win+"','"+loss+"','"+falha+"');"
        cursor.execute(sql)
        con.commit()
    except:
        print('ERRO ENVIAR INFORMAÇÃO PARA O BANCO DE DADOS')
