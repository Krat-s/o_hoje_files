import time
import pyautogui as pg

pg.FAILSAFE = True

def manter_pc_ligado():
    while True:
        pg.moveRel(50, 0)  # Move o mouse 2 pixels para a direita
        time.sleep(5)  # Espera 30 segundos
        pg.moveRel(-50, 0)  # Move o mouse 2 pixels para a esquerda
        time.sleep(2)  # Espera mais 30 segundos

manter_pc_ligado()
False