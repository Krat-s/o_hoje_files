import time
from datetime import datetime

from pyautogui import screenshot 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

import config.settings.settings as cfg
from config.storage.Logs.logs import log
from config.utils import max_windows
import config.file_manager as fm
from Web.modules.web_diver import wait_d


screen_date = f'{datetime.now().strftime("%Y - %m - %d")}'


def print_task(adon, adon_name_folder, gif=None):
    """Abre o navegador, clica no botão e registra o resultado."""
    print(f"🌐 Acessando {cfg.url_target}")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")

    try:
        driver = webdriver.Chrome(options=chrome_options)
        max_windows()

    except Exception as e:
        erro_msg = f"Falha ao iniciar ChromeDriver: {str(e)}"
        log("All_in_one", "ERRO", erro_msg)
        log("print_ad", "ERRO", erro_msg)
        return
    driver.get(cfg.url_target)

    wait_d(driver, By.TAG_NAME, "body",)
    wait_d(driver, By.LINK_TEXT, adon)
    print(  f"✅ Anúncio encontrado: {adon}")
    time.sleep(0.5)

    def button_print(adon):
        print('1')
        ad = wait_d(driver, By.LINK_TEXT, adon)
        print('2')

        driver.execute_script(
            """
            document.body.style.zoom='125%';
            const element = arguments[0];
            const yOffset = -10;
            const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
            window.scrollTo({top: y});
            """, ad
        )

        time.sleep(2)
        fm.make_folder_print(adon_name_folder)
        
        if gif is not None:
            fm.make_folder(f'frames - {adon_name_folder}', in_local=f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}")
            time.sleep(1)
            screenshot(f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\{screen_date} - frame 1.png")
            time.sleep(3.5)
            screenshot(f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\{screen_date} - frame 2.png")
            time.sleep(3.5)
            screenshot(f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\{screen_date} - frame 3.png")

        else:
            screenshot(f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\{screen_date}.png")
            frames_folder = f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\frames"
            os.makedirs(frames_folder, exist_ok=True)
            time.sleep(1.5)
            screenshot(f"{frames_folder}\\{screen_date} - frame 1.png")
            time.sleep(1.5)
            screenshot(f"{frames_folder}\\{screen_date} - frame 2.png")
            time.sleep(1.5)
            screenshot(f"{frames_folder}\\{screen_date} - frame 3.png")           
    
    try:
        button_print(adon)

    except Exception as e:
        erro_msg = f"Falha ao salvar imagem: {str(e)}"
        log("All_in_one", "ERRO", erro_msg)
        log("print_ad", "ERRO", erro_msg)

    finally:
        time.sleep(2)
        driver.quit()
        log("All_in_one", "RELATÓRIO", "Drive fechado após execução da tarefa")
        log("print_ad", "RELATÓRIO", "Drive fechado após execução da tarefa")
        

# ------n8n trigger
def run_print_ad(ad=None, folder=None):
    print_task(ad, folder)


# ------------------manual trigger 
def auto_print_all_ads(gif=None):
    '''verifica quais anúncios estão configurados e executa a função de print para cada um deles'''
    if cfg.ad_1_pi != None:
        print_task(cfg.ad_1, cfg.ad_1_folder, gif)

    if cfg.ad_2_pi != None:
        print_task(cfg.ad_2, cfg.ad_2_folder, gif)

    if cfg.ad_3_pi != None:
        print('Printando anúncio 3...')
        print_task(cfg.ad_3, cfg.ad_3_folder, gif)

    if cfg.ad_4_pi != None:
        print_task(cfg.ad_4, cfg.ad_4_folder, gif)

    if cfg.ad_alt_pi != None:
        print('Printando anúncio alternativo...')
        time.sleep(60* 6)
        print_task(cfg.ad_alt, cfg.ad_alt_folder, gif)
        time.sleep(60)
        print_task(cfg.ad_alt_ad, f'{cfg.ad_alt_folder}_retry', gif)



if __name__ == "__main__":
    print('Print ad rodando...')
    auto_print_all_ads()
    print('Print ad finalizado.')