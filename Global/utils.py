import ctypes
import pyautogui as pg
import keyboard as kb
import time
from pywinauto import Desktop
from datetime import datetime, timedelta
import os
import sys
import pyperclip
import time

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

import Global.settings as cfg
import Global.data_edition_sync as sy_de
from Global.WinManager import check_windows
import Global.utils_tesseract as tutl


# Functions
def press_repeat(key, n):
    for _ in range(n):
        pg.press(key)

def atalho_endereço():
    ''''Retorna o atalho correto para a barra de endereço do Explorador de Arquivos'''
    windows = check_windows()
    return ('ctrl', 'l') if "Windows 11" in windows else ('ctrl', 'l')

def press_repeat(key, n):
    for _ in range(n):
        pg.press(key)

def max_windows():
    kb.press_and_release('alt+space')
    time.sleep(0.2)
    kb.press_and_release('x')

def open_software(numero):
    time.sleep(0.5)
    kb.press_and_release('win+s')
    time.sleep(0.5)
    kb.press_and_release(f"win+{numero}")

    pg.hotkey('win', numero)

# ---------------------------- functions explorer (server journal) ----------------------------
def open_web():
    os.startfile(cfg.CAMINHO_WEB + "\\" + sy_de.EDD)
    time.sleep(0.3)
    max_windows()

def chose_suggestion(QTD=1, TEMPO=2):
    time.sleep(0.2)
    pg.press('down', presses=QTD)
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(int(TEMPO))

# ------expecífica o bastante para ser separada mas não atiquetável a ponto de entrar em módulo
def close_and_open_quark():
    pg.hotkey('alt', 'f4')
    time.sleep(0.5)
    open_software(str(1))
    time.sleep(4)

def adjust_date(data):
    return data + timedelta(days=1) if data.weekday() == 6 else data

if __name__ == "__main__":
    print("oi")
    pg.hotkey('win', 's')
    pg.hotkey('win', '4')

    close_and_open_quark()
    # def error_check():
    #     if tutl.status == "open":
    #         print("Tratamento concluído para arquivo aberto.")
    #     if tutl.status == "not_found":
    #         print("Tratamento concluído para arquivo não encontrado.")
    #     else:
    #         print("Tudo certo, seguindo...")