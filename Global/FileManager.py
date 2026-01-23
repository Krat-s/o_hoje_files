import os
import sys
import time
import pyautogui as pg
import keyboard as kb
from pywinauto import Desktop
from typing import Iterable
import pyperclip

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

import Global.settings as cfg
import Global.utils as utl
from Global.Logs.logs import log

pg.PAUSE = 0.5
pg.FAILSAFE = True

def take_file(arquivo):
    time.sleep(0.5)
    kb.press_and_release('ctrl+f')
    time.sleep(0.5)
    kb.write(str(arquivo))
    time.sleep(2)
    pg.click(cfg.center_x, cfg.center_y)
    time.sleep(0.5)
    pg.press('down')
    time.sleep(0.3)
    pg.press('down')
    time.sleep(0.3)
    kb.press_and_release('enter')

def copy_files(caminho, pasta_nome, de=None):
    if de:
        go_to(de)
    time.sleep(2)
    pyperclip.copy("")
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'a')
    time.sleep(1)
    pg.hotkey('ctrl', 'c')
    go_to(f"{caminho}\\{pasta_nome}")
    pg.hotkey('ctrl', 'v')
    time.sleep(4)

def go_to(específico=None):
    pg.hotkey(*utl.atalho_endereço())
    time.sleep(0.5)
    if específico:
        kb.write(específico) 
    pg.press('enter')
    time.sleep(0.8)

def make_folder(nome, em=None):
    if em:
        go_to(em)
    time.sleep(0.4)
    utl.max_windows()
    time.sleep(0.4)
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'shift', 'n')
    time.sleep(0.4)
    kb.write(nome)
    pg.press('enter')
    time.sleep(1.5)

def open_folder(endereco):
    os.startfile(endereco)
    utl.max_windows()
    pg.click(cfg.center_x, cfg.center_y)

def explorer_is_open() -> bool:
    """
    Verifica se há alguma janela do Explorador de Arquivos aberta.
    """
    janelas = Desktop(backend="uia").windows()
    for janela in janelas:
        if janela.class_name() == "CabinetWClass":
            return True
    return False

def get_explorer_texts(janela) -> list[str]:
    textos = []

    try:
        # título da janela
        titulo = janela.window_text()
        if titulo:
            textos.append(titulo.lower())

        # todos os textos visíveis relevantes
        for ctrl in janela.descendants():
            try:
                if ctrl.friendly_class_name() in ("Edit", "Text"):
                    val = ctrl.window_text()
                    if val:
                        textos.append(val.lower())
            except Exception:
                continue

    except Exception:
        pass

    return textos

def folder_is_open(folder_names: Iterable[str]) -> bool:
    desktop = Desktop(backend="uia")
    nomes = [n.lower() for n in folder_names]

    for janela in desktop.windows(class_name="CabinetWClass"):
        textos = get_explorer_texts(janela)

        for texto in textos:
            for nome in nomes:
                if nome in texto:
                    return True

    return False

def open_main_folder():
    if folder_is_open(["00 - Teste"]):
        print("teste")
        open_folder(cfg.CAMINHO_MODELO_EDD)
        go_to(cfg.CAMINHO_PAGFLIP)
        pass
    elif folder_is_open(["4 Adianto de novas edições"]):
        print("4 adianto")
        open_folder(cfg.CAMINHO_MODELO_EDD_0)
        go_to(cfg.CAMINHO_PAGFLIP)
    elif folder_is_open(["fotos"]):
        open_folder(cfg.CAMINHO_FOTOS)
        print("fotos")
        go_to(cfg.CAMINHO_PAGFLIP)
    elif folder_is_open(["web"]):
        print("web")
        open_folder(cfg.CAMINHO_WEB)
        go_to(cfg.CAMINHO_PAGFLIP)
    elif folder_is_open(["00 Pagflip"]):
        open_folder(cfg.CAMINHO_PAGFLIP)
    else:
        open_folder(cfg.CAMINHO_PAGFLIP)

def auto_folders(pasta_nome, modelo_path):
    try:
        open_main_folder()
        time.sleep(1)
        make_folder(pasta_nome)
        time.sleep(1)
        make_folder(pasta_nome, cfg.CAMINHO_WEB)
        time.sleep(1)
        make_folder(pasta_nome, cfg.CAMINHO_FOTOS)
        time.sleep(1)
        make_folder(pasta_nome, cfg.CAMINHO_MODELO_EDD)
        time.sleep(1)
        copy_files(cfg.CAMINHO_WEB, pasta_nome, cfg.CAMINHO_MODELO_WEB)
        time.sleep(1)
        copy_files(cfg.CAMINHO_MODELO_EDD, pasta_nome, modelo_path)
        time.sleep(1)
        pg.hotkey('alt', 'up')
        log("FileManager", "sucesso", f"Pasta {pasta_nome} criada")
        log("All_in_one", "sucesso", f"Pasta {pasta_nome} criada")
        
    except Exception as e:
        log("FileManager", "ERRO", f"Erro ao criar pasta: {str(e)}")
        log("All_in_one", "ERRO", f"Erro ao criar pasta: {str(e)}")