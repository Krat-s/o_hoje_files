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

from Global.settings.settings import url_target, adon_1, adon_2, adon_3

from Global.Logs.logs import log

def wait_d(driver, by, value, timeout=10, clicavel=True):
    """Espera até que o elemento esteja presente (ou clicável).
    Retorna o elemento encontrado."""
    condicao = EC.element_to_be_clickable if clicavel else EC.presence_of_element_located
    return WebDriverWait(driver, timeout).until(condicao((by, value)))


def print_task():
    """Abre o navegador, clica no botão e registra o resultado."""
    print(f"🌐 Acessando {url_target}")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")

    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        erro_msg = f"Falha ao iniciar ChromeDriver: {str(e)}"
        log("All_in_one", "ERRO", erro_msg)
        log("boost_ad", "ERRO", erro_msg)
        return
    driver.get(url_target)
    

    def button_view_(btt, n_view):
        for i in range(n_view):
            botao = wait_d(driver, By.ID, btt, timeout=15, clicavel=True)
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao
            )
            time.sleep(0.5)
            wait_d(driver, By.ID, btt, timeout=10, clicavel=True)
            time.sleep(0.5)
        log("All_in_one", "SUCESSO", f"{btt} visualizado {n_view * 3} vezes")
        log("boost_ad", "SUCESSO", f"{btt} visualizado {n_view * 3} vezes")
        

    def button_print(adon):
        try: 
            botao = wait_d(driver, By.ID, adon, timeout=15, clicavel=True)
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao
            )
            wait_d(driver, By.ID, adon, timeout=10, clicavel=True)
            time.sleep(0.5)
            botao.click()
            time.sleep(0.5)
            log("All_in_one", "SUCESSO", f"{adon} printado")
            log("boost_ad", "SUCESSO", f"{adon} printado")
            # cheackar se o clique resultou em algo esperado (ex: nova janela, mudança de elemento, etc) e logar o resultado
            
        except Exception as e:
                erro_msg = f"Falha ao clicar no botão: {str(e)}"
                log("All_in_one", "ERRO", erro_msg)
                log("boost_ad", "ERRO", erro_msg)
        

    try:
        for _ in range (4):
            button_view_(adon_1)
            button_view_(adon_2)
            button_view_(adon_3)
        button_print(adon_1)
        button_print(adon_2)
        button_print(adon_3)

        # wait_d(driver, By.ID, "id_de_confirmacao", timeout=10, clicavel=False) #Caso queira aguardar algo após o clique (ex: confirmação)

    except Exception as e:
        erro_msg = f"Falha ao clicar no botão: {str(e)}"
        log("All_in_one", "ERRO", erro_msg)
        log("boost_ad", "ERRO", erro_msg)

    finally:
        time.sleep(2)
        driver.quit()
        log("All_in_one", "RELATÓRIO", "Drive fechado após execução da tarefa")
        log("boost_ad", "RELATÓRIO", "Drive fechado após execução da tarefa")