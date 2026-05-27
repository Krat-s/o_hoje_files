import os
import sys
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

raiz_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_path)

from Web.modules.web_diver import wait_d

import pyautogui as pg
import keyboard as kb
import config.utils as utl
import config.settings.settings as cfg
import config.core.data_edition_sync as sy_de
import config.core.data_formatter as fd

pg.PAUSE = 0.8
pg.FAILSAFE = True

URL_DRIVE = 'https://drive.google.com/drive/home?hl=pt-br'
ontem = datetime.now() - timedelta(days=1)


def auto_drive():

    chrome_options = Options()

    CHROME_ARGS = [
        # r'--user-data-dir=C:\Users\terravista.JORNALOHOJE\AppData\Local\Google\Chrome\User Data',
        # '--profile-directory=Default',
        r'--user-data-dir=C:\chrome_automation',
        '--start-maximized',
        '--disable-blink-features=AutomationControlled',
        '--disable-extensions',
    ]

    for arg in CHROME_ARGS:
        chrome_options.add_argument(arg)

    chrome_options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )

    chrome_options.add_experimental_option(
        "useAutomationExtension",
        False
    )
  
    driver = webdriver.Chrome(options=chrome_options)
  
    time.sleep(5)

    driver.get(URL_DRIVE)



def process_daily():
    pg.click(cfg.center_x, cfg.center_y)
    print('tt')



def att_model(editoria):
    pg.press('/')
    kb.write(editoria)
    pg.press('enter')
    time.sleep(1)
    kb.write(f'{fd.formatar_data(ontem, tipo="dia_semana")}')
    process_daily()



def open_drive():
    utl.open_software(cfg.opera)
    time.sleep(1)
    pg.hotkey('ctrl', 't')
    # driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    kb.write('https://drive.google.com/drive/u/0/home')
    pg.press('enter')
    time.sleep(1)
    pg.press('/')
    kb.write('Redação')
    pg.press('enter')
    pg.click(cfg.center_x, cfg.center_y)
    


def main_drive_bot():
    open_drive()
    att_model(str('7 - Mundo'))
    att_model(str('5 - Esportes'))
    att_model(str('4 - Negócios e Concursos'))
    att_model(str('2 - Política'))
    att_model(str('1 - Cidades - Economia'))



if __name__ == "__main__":
    # open_drive()
    # att_model(str('0 - esportes'))
    # print(str(fd.formatar_data(datetime.now(), tipo='dia')))
    auto_drive()
    # main_drive_bot()