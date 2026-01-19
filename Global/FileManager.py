import os
import sys
import time
import pyautogui as pg
import keyboard as kb
from dataclasses import dataclass
from pywinauto import Desktop
from typing import Iterable
import pyperclip

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as desync
from Global.Logs.logs import log

pg.PAUSE = 0.5
pg.FAILSAFE = True

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
        go_to(de)
    time.sleep(2)
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'a')
    time.sleep(1)
    pg.hotkey('ctrl', 'c')
    # utl.safe_copy()
    # if not utl.safe_copy():
    #     raise Exception("Falha ao copiar arquivos — p\\192.168.1.249\redacao\arte\00 Pagflipasta vazia ou nada selecionado.")
    go_to(f"{caminho}\\{pasta_nome}")
    pg.hotkey('ctrl', 'v')
    time.sleep(3)

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

# Verificações do explores
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
    """
    Verifica se alguma janela do Explorer contém
    uma pasta com o nome informado (Win10 / Win11).
    """
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

def auto_folder(pasta_nome, modelo_path):
        open_main_folder()
        make_folder(pasta_nome, cfg.CAMINHO_MODELO_EDD)
        time.sleep(1)
        copy_files(cfg.CAMINHO_MODELO_EDD, pasta_nome, modelo_path)
        pg.hotkey('alt', "up")

def auto_folders(pasta_nome, modelo_path):
    try:
        open_main_folder()
        make_folder(pasta_nome)
        make_folder(pasta_nome, cfg.CAMINHO_WEB)
        make_folder(pasta_nome, cfg.CAMINHO_FOTOS)
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


def teste(pasta_nome):
    open_main_folder()
    make_folder(pasta_nome, cfg.CAMINHO_MODELO_EDD)
    time.sleep(1)
    copy_files(cfg.CAMINHO_MODELO_EDD, pasta_nome, r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira')
    pg.hotkey('alt', 'up')


if __name__ == "__main__":
    teste("ptest")  #Testar com o safe copy