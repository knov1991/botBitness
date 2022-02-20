import pyautogui
import keyboard
import time


#vela1 = 665 845   666 855 
#vela2 = 615 845   616 855
#vela3 = 565 845   566 855
######
vela1x = 665
vela1y = 845
vela2x = 615
vela2y = 845
vela3x = 565
vela3y = 845

varx=590
vary=665
vermelho=0
verde=0
falha=0

def verificaVela(velaX,velaY):
    global verde,vermelho
    try:
        sc = pyautogui.screenshot(region=(velaX,velaY,1,5))
        width,height = sc.size
        for x in range(0,width,1):
            for y in range(0,height,1):
                r,g,b = sc.getpixel((x,y))
                #verde
                if r >= 21 and r <= 25 and g >= 75 and g <= 79 and b >= 80 and b <= 84:
                    verde += 1
                    return
                #vermelho
                if r >= 87 and r <= 91 and g >= 28 and g <= 32 and b >= 51 and b <= 55:
                    vermelho += 1
                    return
    except:
        print('ERRO VERIFICAR VELAS')

while True:
    verde=vermelho=falha=0
    verificaVela(665,845) #vela1 = 665 845 #1920x1080
    verificaVela(615,845) #vela2 = 615 845 #1920x1080
    verificaVela(565,845) #vela3 = 565 845 #1920x1080
    verificaVela(515,845) #vela4 = 615 845 #1920x1080
    verificaVela(465,845) #vela5 = 615 845 #1920x1080
    print('verde:',verde,'vermelho:',vermelho)
    time.sleep(2)