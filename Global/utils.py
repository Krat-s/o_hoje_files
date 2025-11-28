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
import Global.utils_tesseract as tutl

# ---------------------------- Funções passivas ----------------------------
def check_windows() -> str:
    """
    Detecta corretamente se é Windows 10 ou 11 usando a API nativa.
    """
    class OSVERSIONINFOEXW(ctypes.Structure):
        _fields_ = [
            ("dwOSVersionInfoSize", ctypes.c_ulong),
            ("dwMajorVersion", ctypes.c_ulong),
            ("dwMinorVersion", ctypes.c_ulong),
            ("dwBuildNumber", ctypes.c_ulong),
            ("dwPlatformId", ctypes.c_ulong),
            ("szCSDVersion", ctypes.c_wchar * 128),
            ("wServicePackMajor", ctypes.c_ushort),
            ("wServicePackMinor", ctypes.c_ushort),
            ("wSuiteMask", ctypes.c_ushort),
            ("wProductType", ctypes.c_byte),
            ("wReserved", ctypes.c_byte),
        ]

    ver_info = OSVERSIONINFOEXW()
    ver_info.dwOSVersionInfoSize = ctypes.sizeof(OSVERSIONINFOEXW)

    ret = ctypes.windll.Ntdll.RtlGetVersion(ctypes.byref(ver_info))
    if ret != 0:
        return "Não foi possível detectar o Windows"

    major = ver_info.dwMajorVersion
    build = ver_info.dwBuildNumber

    if major == 10 and build >= 22000:
        return "Windows 11"
    elif major == 10:
        return "Windows 10"
    else:
        return f"Windows {major}"

def atalho_endereço():
    ''''Retorna o atalho correto para a barra de endereço do Explorador de Arquivos'''
    windows = check_windows()
    return ('ctrl', 'l') if "Windows 11" in windows else ('ctrl', 'l')

def adjust_date(data):
    return data + timedelta(days=1) if data.weekday() == 6 else data

def explorer_is_open() -> bool:
    """
    Verifica se há alguma janela do Explorador de Arquivos aberta.
    """
    janelas = Desktop(backend="uia").windows()
    for janela in janelas:
        if janela.class_name() == "CabinetWClass":
            return True
    return False

def folder_is_open(nomes: str) -> bool:
    """
    Verifica se uma janela do Explorador de Arquivos com nome específico está aberta.
    """
    janelas = Desktop(backend="uia").windows()
    for janela in janelas:
        if janela.class_name() == "CabinetWClass":
            titulo = janela.window_text().lower()
            for nome in nomes:
                if nome.lower() in titulo:
                    return True
    return False

def max_windows():
    kb.press_and_release('alt+space')
    time.sleep(0.2)
    kb.press_and_release('x')

def open_software(numero):
    pg.hotkey('win', 's')
    pg.hotkey('win', str(numero))
    pg.press('enter')
    time.sleep(0.5)

def error_check():
    if tutl.status == "open":
        print("Tratamento concluído para arquivo aberto.")
    if tutl.status == "not_found":
        print("Tratamento concluído para arquivo não encontrado.")
    else:
        print("Tudo certo, seguindo...")

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

def close_page():
    pg.press('esc', presses=3)
    time.sleep(0.2)
    pg.hotkey('ctrl', 's')
    time.sleep(0.2)
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'f4')
    time.sleep(cfg.TIMETOCLOSE)

def close_and_open_quark():
    pg.hotkey('alt', 'f4')
    pg.hotkey('win', 's')
    pg.hotkey('win', '1')
    time.sleep(4)

def press_repeat(key, n):
    for _ in range(n):
        pg.press(key)