import ctypes
import pyautogui as pg
import keyboard as kb
import time
from pywinauto import Desktop
from datetime import datetime, timedelta
import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

import Global.settings as cfg

# ---------------------------- Funções passivas ----------------------------
def verificar_windows() -> str:
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
    windows = verificar_windows()
    return ('ctrl', 'l') if "Windows 11" in windows else ('ctrl', 'l')

# ---------------------------- Funções gerais ----------------------------
def ajustar_data(data):
    return data + timedelta(days=1) if data.weekday() == 6 else data

def abrir_software(numero):
    pg.hotkey('win', 's')
    pg.hotkey('win', str(numero))
    pg.press('enter')
    time.sleep(0.5)

def explorer_esta_aberto() -> bool:
    """
    Verifica se há alguma janela do Explorador de Arquivos aberta.
    """
    janelas = Desktop(backend="uia").windows()
    for janela in janelas:
        if janela.class_name() == "CabinetWClass":
            return True
    return False

def janela_esta_aberta(nome_pasta: str) -> bool:
    """
    Verifica se uma janela do Explorador de Arquivos com nome específico está aberta.
    """
    janelas = Desktop(backend="uia").windows()
    for janela in janelas:
        if janela.class_name() == "CabinetWClass":
            if nome_pasta.lower() in janela.window_text().lower():
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

def ir_para(específico=None):
    pg.hotkey(*atalho_endereço())
    time.sleep(0.2)
    if específico:
        kb.write(específico) 
    pg.press('enter')
    time.sleep(0.2)

def criar_pasta(nome, em=None):
    if em:
        ir_para(em)
    time.sleep(0.4)
    max_windows()
    time.sleep(0.4)
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'shift', 'n')
    time.sleep(0.4)
    kb.write(nome)
    pg.press('enter')
    time.sleep(0.4)

def abrir_pasta(endereco):
    os.startfile(endereco)
    max_windows()
    pg.click(cfg.center_x, cfg.center_y)

# ---------------------------- Funções quark ----------------------------
def cancel_qk():
    time.sleep(0.2)
    pg.moveTo(cfg.button_cancel_qk, duration=0.5)
    time.sleep(0.2)
    pg.click()
    time.sleep(0.2)

def ok_qk():
    time.sleep(0.2)
    pg.press('esc')
    time.sleep(0.2)

def error_check():
    if cfg.status == "open":
        print("Tratamento concluído para arquivo aberto.")
    if cfg.status == "not_found":
        print("Tratamento concluído para arquivo não encontrado.")
    else:
        print("Tudo certo, seguindo...")

# ---------------------------- functions explorer (server journal) ----------------------------
def open_web():
    os.startfile(cfg.CAMINHO_WEB + "\\" + cfg.EDD)
    time.sleep(0.3)
    max_windows()

def chose_suggestion(QTD=1, TEMPO=2):
    time.sleep(0.2)
    pg.press('down', presses=QTD)
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(int(TEMPO))
