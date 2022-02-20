import time

def tempo():
    try:
        return time.gmtime().tm_hour
    except:
        return -1

tempo = tempo()
if(tempo > 0 and tempo < 12):
    print(tempo)
    print('manhã')
if(tempo > 12):
    print(tempo)
    print('tarde')