import pyautogui as pg
import time
import os
import sys

import tkinter as tk
from tkinter import messagebox
import keyboard as kb

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

pg.PAUSE = 0.5
pg.FAILSAFE = True



#detectar onde ocorreu a mudança, qual dia da semana do modelo foi alterado, ou fazer menu de escolha para decidir se eu mudo só em modelos de edições específicas
#Pegar parte da página que mudou o modelo sem cabeçalho 
#loop - abrir pasta por pasta a página em que mudou no adianto de edições
#tirar tudo, fora as datas
#colar modelo da pasta no lugar
#salvar
#abrir proxima pasta
#repetir
#detectar quando não houver mais edições e parar







if __name__ == "__main__":
    print("suasyayhusfbal")