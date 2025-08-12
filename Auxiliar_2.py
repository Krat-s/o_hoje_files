import os
import pygetwindow as gw
import pyautogui as pg
from pywinauto import Desktop
import time

CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'

def abrir_pasta(endereco):
    os.startfile(endereco) 

# abrir_pasta(CAMINHO_ADIANTO)

# for i in range (5):
#     abrir_pasta(CAMINHO_ADIANTO)



def pasta_esta_aberta(nome_pasta):
    janelas = Desktop(backend="uia").windows()
    for janela in janelas:
        if janela.class_name() == "CabinetWClass":
            titulo = janela.window_text()
            if nome_pasta.lower() in titulo.lower():
                return True
    return False

if pasta_esta_aberta("4 Adianto de novas edições"):
    continue
else:
    abrir_pasta(CAMINHO_ADIANTO)

