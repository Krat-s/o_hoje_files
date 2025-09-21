import ctypes
import pyautogui as pg
import time
from pywinauto import Desktop

def abrir_software(numero):
    pg.hotkey('win', 's')
    pg.hotkey('win', str(numero))
    pg.press('enter')
    time.sleep(0.5)


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