import os
import sys
import time
import pyautogui as pg
import keyboard as kb
from dataclasses import dataclass

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

import App.modulos_quark.utils_quark as utlq

from App.modulos_quark.utils_quark import close_page
import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as desync
from typing import Protocol

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True

# ---------------------------- FUNÇÕES UTILITÁRIAS (QUARK) ----------------------------
class EdicaoQuarkLike(Protocol):
    edicao_formatada: str
    data_formatada: str
    dia_semana: str

def auto_date(info: EdicaoQuarkLike):
    utlq.take_tool("v")
    pg.click(cfg.x_data, cfg.y_data)
    utlq.take_tool("t")
    utl.press_repeat('t', 2)
    time.sleep(0.4)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.4)
    kb.write(info.data_formatada)

def auto_pages(numero, info: EdicaoQuarkLike):
    utl.press_repeat('esc', 3)
    pg.hotkey('ctrl', 'o')
    nome_pasta = f"{info.edicao_formatada.replace('.', '')} - {info.dia_semana}"
    kb.write(f"{cfg.CAMINHO_MODELO_EDD}\\{nome_pasta}")
    pg.press('enter')
    pg.write(str(numero))
    utl.chose_suggestion(1, cfg.TIMETOOPEN)
    auto_date(info)

def aply_1(info: EdicaoQuarkLike):
    utl.press_repeat('esc', 3)
    pg.hotkey('ctrl', 'o')
    pg.write('1')
    utl.chose_suggestion(1, 3)
    utlq.take_tool("v")
    pg.click(cfg.x_edicao_capa, cfg.y_edicao_capa)
    utlq.take_tool("t")
    utl.press_repeat('t', 4)
    utl.press_repeat('backspace', 5)
    kb.write(f"nº {info.edicao_formatada} ")
    utl.press_repeat('right', 2)
    pg.press('backspace')
    kb.write(f"|  {info.data_formatada}")
    utlq.close_page()

def aply_17(info: EdicaoQuarkLike):
    time.sleep(0.3)
    utl.press_repeat('esc', 3)
    pg.hotkey('ctrl', '0')
    time.sleep(0.3)
    utlq.take_tool("v")
    time.sleep(0.3)
    pg.hotkey('ctrl', 'o')
    time.sleep(0.3)
    kb.write(cfg.CAMINHO_MODELO_EDD + '\\' + f"{info.edicao_formatada.replace('.', '')} - {info.dia_semana}")
    time.sleep(0.3)
    pg.press('enter')
    time.sleep(0.5)
    kb.write('17')
    utl.chose_suggestion(1, 1)
    utl.press_repeat('esc', 3)
    auto_date(info)
    time.sleep(0.4)
    utl.press_repeat('esc', 3)
    utlq.take_tool("v")
    pg.hotkey('ctrl', '0')
    pg.click(cfg.x_edicao_17, cfg.y_edicao_17)
    utlq.take_tool("t")
    utl.press_repeat('t', 4)
    pg.hotkey('ctrl', 'a')
    kb.write(f"Ano 21 - nº {info.edicao_formatada}")
    utlq.close_page()

def auto_date_all_non_especial_pages(info: EdicaoQuarkLike):
    for i in range(20, 1, -1):
        if i in [17, 18, 19]:
            continue
        auto_pages(i, info)
        utlq.close_page()