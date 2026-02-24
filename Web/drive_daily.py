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

import pyautogui as pg
import keyboard as kb
import Global.utils as utl
import Global.settings as cfg
import Global.data_edition_sync as sy_de
import Global.data_formatador as fd


pg.PAUSE = 0.5
pg.FAILSAFE = True

URL_DRIVE = 'https://drive.google.com/drive/home?hl=pt-br'

ontem = datetime.now() - timedelta(days=1)

def open_Brownser():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL_DRIVE)

    try:
        # time.sleep(3)
        # botao = driver.find_element(By.ID, btt)
        # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao)
        # time.sleep(1)
        # botao.click()
        if
        
            Faça login
            
        print("✅ Botão clicado com sucesso!")
        # open_Brownser()
    except Exception as e:
        print(f"⚠️ Erro ao clicar no botão: {e}")

    finally:
        time.sleep(5)  # Tempo para visualizar o resultado
        driver.quit()



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
    open_Brownser()