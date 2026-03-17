import pyautogui as pg
import keyboard as kb
import time
from datetime import timedelta
import os
import sys
import time

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

import Global.settings.settings as cfg
import Global.data_edition_sync as sy_de
from Global.settings.win_manager import check_windows



def press_repeat(key, n):
    for _ in range(n):
        pg.press(key)


def atalho_endereço():
    ''''Retorna o atalho correto para a barra de endereço do Explorador de Arquivos'''
    windows = check_windows()
    return ('ctrl', 'l') if "Windows 11" in windows else ('ctrl', 'l')


def max_windows():
    kb.press_and_release('alt+space')
    time.sleep(0.2)
    kb.press_and_release('x')


def open_software(numero):
    time.sleep(0.5)
    kb.press_and_release('win+s')
    time.sleep(0.5)
    kb.press_and_release(f"win+{str(numero)}")
    time.sleep(0.5)



# ---------------------------- functions explorer (server journal) ----------------------------
def open_web_day_0():
    os.startfile(cfg.CAMINHO_WEB + "\\" + sy_de.EDD)
    time.sleep(0.3)
    max_windows()


def chose_suggestion(QTD=1, TEMPO=2):
    time.sleep(0.2)
    pg.press('down', presses=QTD)
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(int(TEMPO))


if __name__ == "__main__":
    # print("oi")
    # pg.hotkey('win', 'e')

    # pg.hotkey('win', 's')
    # pg.hotkey('win', '4')
    # time.sleep(3)
    # open_software(cfg.quark)
    # # close_and_open_quark()
    # # def error_check():
    # #     if tutl.status == "open":
    # #         print("Tratamento concluído para arquivo aberto.")
    # #     if tutl.status == "not_found":
    # #         print("Tratamento concluído para arquivo não encontrado.")
    # #     else:
    # #         print("Tudo certo, seguindo...")
    print_fullscreen()