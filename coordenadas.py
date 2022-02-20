import keyboard
import pyautogui

while keyboard.is_pressed('c')==False:
    #função para verificar RGB e posição
    pyautogui.displayMousePosition()