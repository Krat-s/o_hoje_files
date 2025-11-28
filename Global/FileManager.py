import os
import sys
import time
import pyautogui as pg
import keyboard as kb
from dataclasses import dataclass

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as desync


def take_file(arquivo):
    kb.press_and_release('ctrl+f')
    time.sleep(0.5)
    kb.write(str(arquivo))
    time.sleep(2)
    pg.click(cfg.center_x, cfg.center_y)
    pg.press('down')
    time.sleep(0.3)
    pg.press('down')
    time.sleep(0.3)
    kb.press_and_release('enter')

def copy_files(caminho, pasta_nome, de=None):
    if de:
        utl.go_to(de)
    time.sleep(2)
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'a')
    time.sleep(1)
    pg.hotkey('ctrl', 'c')
    # utl.safe_copy()
    # if not utl.safe_copy():
    #     raise Exception("Falha ao copiar arquivos — p\\192.168.1.249\redacao\arte\00 Pagflipasta vazia ou nada selecionado.")
    utl.go_to(f"{caminho}\\{pasta_nome}")
    pg.hotkey('ctrl', 'v')
    time.sleep(2)

def go_to(específico=None):
    pg.hotkey(*atalho_endereço())
    time.sleep(0.4)
    if específico:
        kb.write(específico) 
    pg.press('enter')
    time.sleep(0.4)

def make_folder(nome, em=None):
    if em:
        go_to(em)
    time.sleep(0.4)
    max_windows()
    time.sleep(0.4)
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'shift', 'n')
    time.sleep(0.4)
    kb.write(nome)
    pg.press('enter')
    time.sleep(1.5)

def open_folder(endereco):
    os.startfile(endereco)
    max_windows()
    pg.click(cfg.center_x, cfg.center_y)

def safe_copy():
    # Antes de copiar, limpa a área de transferência
    pyperclip.copy("")

    pg.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pg.hotkey('ctrl', 'c')
    time.sleep(0.2)

    conteudo = pyperclip.paste()

    # Checar se o conteúdo provavelmente NÃO é lista de arquivos
    if "\\" not in conteudo and "/" not in conteudo:
        raise Exception("Nenhum arquivo selecionado — Ctrl+C copiou apenas o nome da pasta.")

    return True
