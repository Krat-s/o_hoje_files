import time
from datetime import datetime

# import pyautogui as pg 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

import Global.settings.settings as cfg
from Global.Logs.logs import log
from Global.utils import max_windows
import Global.file_manager as fm
from Web.modules.web_diver import wait_d


screen_date = f'{datetime.now().strftime("%Y - %m - %d")}'

#


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

    wait_d(driver, By.TAG_NAME, "body", timeout=15)
    wait_d(driver, By.CSS_SELECTOR, adon, timeout=15, clicavel=False)

    driver.execute_script("document.body.style.zoom='75%'")
    time.sleep(1)


    def button_print(adon):
        try: 
            ad = wait_d(driver, By.CSS_SELECTOR, adon, timeout=15, clicavel=True)
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", ad
            )
            
            fm.make_folder_(adon_name_folder)
            if gif is not None:
                time.sleep(1)
            #     pg.screenshot(f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\{screen_date} - frame1.png")
            #     time.sleep(3.5)
            #     pg.screenshot(f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\{screen_date} - frame2.png")
            #     time.sleep(3.5)
            #     pg.screenshot(f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\{screen_date} - frame3.png")
            # else:
            #     pg.screenshot(f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\{screen_date}.png")

            log("All_in_one", "SUCESSO", f"{adon} printado")
            log("print_ad", "SUCESSO", f"{adon} printado")
            
        except Exception as e:
                erro_msg = f"Falha ao salvar imagem: {str(e)}"
                log("All_in_one", "ERRO", erro_msg)
                log("print_ad", "ERRO", erro_msg)
    
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
def autoprint(NUM, gif=None):
    if NUM == 1:
        print_task(cfg.ad_1, cfg.ad_1_folder, gif)
    elif NUM == 2:
        print_task(cfg.ad_2, cfg.ad_2_folder, gif)
    elif NUM == 3:
        print_task(cfg.ad_3, cfg.ad_3_folder, gif)

def auto_print_all_ads(gif=None):
    '''verifica quais anúncios estão configurados e executa a função de print para cada um deles'''
    if cfg.ad_1_pi != None:
        autoprint(1, gif)

    if cfg.ad_2_pi != None:
        autoprint(2, gif)

    if cfg.ad_3_pi != None:
        autoprint(3, gif)


if __name__ == "__main__":
    print('Print ad rodando...')
    # auto_print_all_ads(gif=True)
    print('Print ad finalizado.')
    import pyautogui as ase
    ase.moveTo(11, 11)