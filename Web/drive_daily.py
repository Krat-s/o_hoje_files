import os
import sys
import time

raiz_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_path)

import pyautogui as pg
import keyboard as kb
import Global.utils as utl
import Global.settings as cfg
import Global.data_edition_sync as sy_de


pg.PAUSE = 0.5
pg.FAILSAFE = True


def process_daily():
    pg.click(cfg.center_x, cfg.center_y)
    print('tt')


def att_model(editoria):
    pg.press('/')
    kb.write(editoria)
    pg.press('enter')
    time.sleep(1)
    kb.write(str(sy_de.data_0))
    process_daily()


def open_drive():
    utl.open_software(cfg.opera)
    time.sleep(1)
    pg.hotkey('ctrl', 't')
    kb.write('https://drive.google.com/drive/u/0/home')
    pg.press('enter')
    time.sleep(1)
    pg.press('/')
    kb.write('Redação')
    pg.press('enter')
    pg.click(cfg.center_x, cfg.center_y)
    att_model(str('editoria'))




if __name__ == "__main__":
    open_drive()
    att_model(str('0 - esportes'))