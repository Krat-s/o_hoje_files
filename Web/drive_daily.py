import os
import sys

raiz_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_path)

import pyautogui as pg
import keyboard as kb
import Global.utils as utl
import Global.settings as cfg


pg.PAUSE = 0.5
pg.FAILSAFE = True

utl.open_software(cfg.opera)
pg.hotkey('ctrl', 't')

