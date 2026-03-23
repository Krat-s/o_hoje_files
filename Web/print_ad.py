import os
import sys

import pyautogui as pg
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

import Global.settings.settings as cfg
from Global.Logs.logs import log

pasta_destino_ = f"{cfg.CAMINHO_PRINTS}\\Auto-prints" 


def wait_d(driver, by, value, timeout=10, clicavel=True):
    """Espera até que o elemento esteja presente (ou clicável).
    Retorna o elemento encontrado."""
    condicao = EC.element_to_be_clickable if clicavel else EC.presence_of_element_located
    return WebDriverWait(driver, timeout).until(condicao((by, value)))


def print_task():
    """Abre o navegador, clica no botão e registra o resultado."""
    print(f"🌐 Acessando {cfg.url_target}")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--Zoom-level=0.75")


    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        erro_msg = f"Falha ao iniciar ChromeDriver: {str(e)}"
        log("All_in_one", "ERRO", erro_msg)
        log("print_ad", "ERRO", erro_msg)
        return
    driver.get(cfg.url_target)
    

    def button_print(adon):
        try: 
            botao = wait_d(driver, By.CSS_SELECTOR, adon, timeout=15, clicavel=True)
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao
            )

            time.sleep(0.5)
            log("All_in_one", "SUCESSO", f"{adon} printado")
            log("print_ad", "SUCESSO", f"{adon} printado")
            
        except Exception as e:
                erro_msg = f"Falha ao salvar imagem: {str(e)}"
                log("All_in_one", "ERRO", erro_msg)
                log("print_ad", "ERRO", erro_msg)
    

    try:
        button_print(cfg.adon_2)
        # button_print(cfg.adon_2)
        # button_print(cfg.adon_3)

    except Exception as e:
        erro_msg = f"Falha ao salvar imagem: {str(e)}"
        log("All_in_one", "ERRO", erro_msg)
        log("print_ad", "ERRO", erro_msg)

    finally:
        time.sleep(2)
        driver.quit()
        log("All_in_one", "RELATÓRIO", "Drive fechado após execução da tarefa")
        log("print_ad", "RELATÓRIO", "Drive fechado após execução da tarefa")



if __name__ == "__main__":
    print_task()






# def auto_print(name_ad, adon):
    
#     os.makedirs(f'{pasta_destino_}\\{name_ad}', exist_ok=True)
#     pg.screenshot(f"{adon}_print.png")
#     # caminho_arquivo = os.path.join(pasta_destino_, f"{adon_1}.png")
#     # file_exists = os.path.exists(caminho_arquivo)

#     # if file_exists:
#     #     log("print_ad", "AVISO", f"O arquivo {adon_1}.png já existe. Ele será substituído.")

#     # print_task()
#     # os.startfile(pasta_destino_)