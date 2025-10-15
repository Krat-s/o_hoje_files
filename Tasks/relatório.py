import pyautogui as pg
import time
import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Tasks.Modulos import index_numeros as ni

time.sleep(1)
pg.PAUSE = 0.3 
pg.FAILSAFE = True

edicao_inicial = 36500
quantidade_de_numeros = 5

def openSofware(numero):
    """Atalho para abrir navegador no Gmail"""
    pg.hotkey('win', 's')
    pg.hotkey('win', str(numero))  # Verificar se é o navegador correto
    time.sleep(0.5)

def vigencia(dia):
    openSofware(5)
    for i in range (25):
        pg.write(str(dia))
        pg.press("tab")

def pedidos():
    ni.gerar_n(36400)

if __name__ == "__main__":
    print(ni.gerar_n(37000))




