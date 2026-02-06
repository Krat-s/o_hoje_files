import time
import os
import sys

import pyautogui as pg
import keyboard as kb
import tkinter as tk
from tkinter import messagebox

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(raiz_projeto)

import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as sy_de
import App.modulos_quark.utils_quark as utlq
from Global.FileManager import take_file
from Global.Logs.logs import log
from Global.waits_until import wait_explorer_open, wait_folder_open
from Global.FileManager import auto_folders
import Global.FileManager as fm




def open_main_folder():
    if fm.folder_is_open(["00 - Teste"]):
        print("teste")
        fm.open_folder(cfg.CAMINHO_MODELO_EDD)
        fm.go_to(cfg.CAMINHO_PAGFLIP)
        pass
    elif fm.folder_is_open(["4 Adianto de novas edições"]):
        print("4 adianto")
        fm.open_folder(cfg.CAMINHO_MODELO_EDD_0)
        fm.go_to(cfg.CAMINHO_PAGFLIP)
    elif fm.folder_is_open(["fotos"]):
        fm.open_folder(cfg.CAMINHO_FOTOS)
        print("fotos")
        fm.go_to(cfg.CAMINHO_PAGFLIP)
    elif fm.folder_is_open(["web"]):
        print("web")
        fm.open_folder(cfg.CAMINHO_WEB)
        fm.go_to(cfg.CAMINHO_PAGFLIP)
    elif fm.folder_is_open(["00 Pagflip"]):
        fm.open_folder(cfg.CAMINHO_PAGFLIP)
    else:
        fm.open_folder(cfg.CAMINHO_PAGFLIP)


wait_explorer_open()
# wait_folder_open('00 Pagflip', 10)