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


def print_task(adon_link, adon_name_folder, gif=None):
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
    # wait_d(driver, By.CSS_SELECTOR, adon_link)
    print(  f"✅ Anúncio encontrado")
    time.sleep(0.5)

    def button_print(adon_link):
        print(f"🖨️ Imprimindo anúncio: {adon_name_folder}")
        ad = wait_d(driver, By.CSS_SELECTOR, adon_link)

        time.sleep(3)
        driver.execute_script(
            """
            document.body.style.zoom='65%';
            const element = arguments[0];
            const yOffset = -150;
            const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
            window.scrollTo({top: y});
            """, ad
        )
        # print(driver.execute_script("""
        # const r = arguments[0].getBoundingClientRect();
        # return {
        #     top: r.top,
        #     bottom: r.bottom,
        #     pageY: window.pageYOffset
        # };
        # """, ad))
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
        button_print(adon_link)

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
def auto_print_by_link_all_ads(gif=None):
    '''verifica quais anúncios estão configurados e executa a função de print para cada um deles'''
    if cfg.ad_1_pi != None:
        print_task(cfg.ad_1_link, cfg.ad_1_folder, gif)

    if cfg.ad_2_pi != None:
        print_task(cfg.ad_2_link, cfg.ad_2_folder, gif)

    if cfg.ad_3_pi != None:
        print_task(cfg.ad_3_link, cfg.ad_3_folder, gif)

    if cfg.ad_4_pi != None:
        print_task(cfg.ad_4_link, cfg.ad_4_folder, gif)

    if cfg.ad_alt_pi != None:
        print('Printando anúncio alternativo...')
        time.sleep(60* 6)
        print_task(cfg.ad_alt_link, cfg.ad_alt_folder, gif)
        time.sleep(60)
        print_task(cfg.ad_alt_link, f'{cfg.ad_alt_folder}_retry', gif)



if __name__ == "__main__":
    print('Print ad rodando...')
  
    # auto_print_by_link_all_ads()
    print_task(cfg.ad_4_link, cfg.ad_4_folder)
    print('Print ad finalizado.')