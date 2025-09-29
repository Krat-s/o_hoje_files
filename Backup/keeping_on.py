import time
import pyautogui as pg

pg.FAILSAFE = True

import time
import pyautogui

def manter_pc_ligado():
    while True:
        pyautogui.moveRel(50, 0)  # Move o mouse 2 pixels para a direita
        time.sleep(2)  # Espera 30 segundos
        pyautogui.moveRel(-50, 0)  # Move o mouse 2 pixels para a esquerda
        time.sleep(2)  # Espera mais 30 segundos

manter_pc_ligado()
False