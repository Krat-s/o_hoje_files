import pyautogui as pg
import time
import keyboard as kb
import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(raiz_projeto)

import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as sy_de

pg.PAUSE = 0.3 
pg.FAILSAFE = True

# __UTILS
def take_tool(tool):
    pg.click(cfg.center_x, 10)
    kb.press(str(tool))

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

# Weeding
def open_pages_done_folder():
    pg.press('esc')
    take_tool("v")
    pg.hotkey('ctrl', '0')
    pg.hotkey('ctrl', 'o')
    time.sleep(0.2)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.2)
    kb.write(cfg.CAMINHO_EDD + "\\" + sy_de.EDD + "\\" + 'Páginas prontas')
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(0.2)
    
def cg_close():
    take_tool("v")
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'g')
    time.sleep(0.2)
    pg.hotkey('ctrl', 's')
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(0.2)
    pg.hotkey('ctrl', 'c')
    pg.hotkey('ctrl', 'f4')
    time.sleep(cfg.TIMETOCLOSE)

def close_page():
    pg.press('esc', presses=3)
    time.sleep(0.2)
    pg.hotkey('ctrl', 's')
    time.sleep(2)
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'f4')
    time.sleep(cfg.TIMETOCLOSE)
    
def move_page(left, right):
    pg.hotkey('ctrl', 'shift', 'alt', 'm')
    time.sleep(0.2)
    kb.write(str(left))
    time.sleep(0.2)
    pg.press('tab')
    time.sleep(0.2)
    kb.write(str(right))
    pg.press('enter')
    time.sleep(0.2)
    pg.press('down')
    time.sleep(0.2)
    pg.press('up')

def process_page(page_number, is_even):
    time.sleep(0.3)
    open_pages_done_folder()
    time.sleep(0.2)
    pg.write(str(page_number))
    time.sleep(0.2)
    utl.chose_suggestion()
    # utl.error_check() make a try exept here, make sure tha way be function normaly in another machine
    time.sleep(cfg.TIMETOOPEN)
    cg_close()
    time.sleep(cfg.TIMETOCLOSE + 4)
    pg.hotkey('ctrl', '0')
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'v')
    time.sleep(7)
    if is_even: 
        move_page(10, 20) 
    else: 
        move_page(290, 20)

# billhead

if __name__ == "__main__":
    print("oi")
    # pg.hotkey('win', 'e')

    # pg.hotkey('win', 's')
    # pg.hotkey('win', '4')
    time.sleep(3)
    # close_and_open_quark()