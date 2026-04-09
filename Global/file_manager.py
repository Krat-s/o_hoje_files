import os
import sys
import time
import pyautogui as pg
import keyboard as kb
from pywinauto import Desktop
from typing import Iterable

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

import Global.settings.settings as cfg
import Global.utils as utl
from Global.Logs.logs import log
import Global.waits_checks as wc

pg.PAUSE = 0.8
pg.FAILSAFE = True



def open_folder(endereco):
    time.sleep(0.2)
    os.startfile(endereco)
    wc.wait_explorer_open()
    utl.max_windows()
    time.sleep(0.5)


def go_to(específico=None):
    pg.hotkey(*utl.atalho_endereço())
    time.sleep(0.2)
    if específico:
        kb.write(específico) 
    pg.press('enter')
    time.sleep(1)


def make_folder(name_folder, in_local=None):
    if in_local:
        go_to(in_local)
    utl.max_windows()
    time.sleep(1)
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'shift', 'n')
    time.sleep(1)
    kb.write(name_folder)
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.press('s')
    time.sleep(0.5)
    pg.press('esc', presses=3)
    pg.press('f5')
    time.sleep(2.5)


def make_folder_(name_folder):
    caminho_completo = os.path.join(cfg.CAMINHO_PRINTS, name_folder)
    os.makedirs(caminho_completo, exist_ok=True)
    return caminho_completo


def take_file(arquivo):
    wc.wait_explorer_open(0.5, 15)
    kb.press_and_release('ctrl+f')
    time.sleep(0.5)
    kb.write(str(arquivo))
    wc.wait_image(r"C:\Users\terravista.JORNALOHOJE\Documents\GitHub\o_hoje_files\Backup\Prints\(11, 5, 27, 24) selecionado em17h28.png", timeout=15)
    pg.click(cfg.center_x, cfg.center_y)
    pg.press('down')
    pg.press('down')
    kb.press_and_release('enter')
    time.sleep(0.5)


def copy_files(caminho, folder_name, _from=None):
    if _from:
        go_to(_from)
    time.sleep(0.5)
    utl.max_windows()
    pg.click(cfg.center_x, cfg.center_y + 100)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    time.sleep(0.5)
    go_to(f"{caminho}\\{folder_name}")
    wc.wait_folder_open(folder_name, timeout=20)
    pg.hotkey('ctrl', 'v')
    pg.hotkey('alt', 's')
    time.sleep(4)


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
    try:
        if folder_is_open(["00 - modelo"]):
            open_folder(cfg.CAMINHO_MODELO_EDD)
            go_to(cfg.CAMINHO_PAGFLIP)
        elif folder_is_open(["4 Adianto de novas edições"]):
            open_folder(cfg.CAMINHO_MODELO_EDD_0)
            go_to(cfg.CAMINHO_PAGFLIP)
        elif folder_is_open(["fotos"]):
            open_folder(cfg.CAMINHO_FOTOS)
            go_to(cfg.CAMINHO_PAGFLIP)
        elif folder_is_open(["web"]):
            open_folder(cfg.CAMINHO_WEB)
            go_to(cfg.CAMINHO_PAGFLIP)
        elif folder_is_open(["00 Pagflip"]):
            open_folder(cfg.CAMINHO_PAGFLIP)
        else:
            open_folder(cfg.CAMINHO_PAGFLIP)

        log("All_in_one", "SUCESSO", f"FileManager: Open_main_folder")
        
    except Exception as e:
        log("All_in_one", "ERRO", f"FileManager-auto_folders: {str(e)}")


def auto_folders(pasta_nome, modelo_path):
    try:
        open_main_folder()

        make_folder(pasta_nome)

        make_folder(pasta_nome, cfg.CAMINHO_FOTOS)
        
        make_folder(pasta_nome, cfg.CAMINHO_WEB)
        copy_files(cfg.CAMINHO_WEB, pasta_nome, cfg.CAMINHO_MODELO_WEB)

        make_folder(pasta_nome, cfg.CAMINHO_MODELO_EDD)
        copy_files(cfg.CAMINHO_MODELO_EDD, pasta_nome, modelo_path)
        time.sleep(0.5)
        pg.hotkey('alt', 'up')
        time.sleep(0.5)
        open_main_folder()
        
        log("FileManager", "SUCESSO", f"Pasta {pasta_nome} criada")
        log("All_in_one", "SUCESSO", f"FileManager-auto_folders: pasta {pasta_nome} criada")
        time.sleep(1)
        
        
    except Exception as e:
        log("FileManager", "ERRO", f"Erro ao criar pasta: {str(e)}")
        log("All_in_one", "ERRO", f"FileManager-auto_folders: erro ao criar pasta: {pasta_nome}: {str(e)}")