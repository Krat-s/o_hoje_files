from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from threading import Thread
import time

'''pretend to be a automation for bot clicking in site, manual adjust'''

URL_JORNAL = "https://ohoje.com"
BOTAO_ID_1 = "placement_1013993_0" #Principal
BOTAO_ID_2 = "placement_1013994_0_i" #Lateral
BOTAO_ID_3 = "placement_1026570_0_i" #Banner/Rodapé
QTD_CB1 = 7
QTD_CB2 = int(QTD_CB1 / 2)
QTD_CB3 = int(QTD_CB2 / 2 + 1)


# Função que cada navegador executa
def open_browser_and_click(btt):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL_JORNAL)

    try:
        time.sleep(3)
        botao = driver.find_element(By.ID, btt)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao)
        time.sleep(1)
        botao.click()
        print("✅ Botão clicado com sucesso!")
    
    except Exception as e:
        print(f"⚠️ Erro ao clicar no botão: {e}")

    finally:
        time.sleep(5)
        driver.quit()


def clickar_button_1():
    '''Creates and starts Main threads'''
    threads = []
    for _ in range(QTD_CB1):
        t = Thread(target=open_browser_and_click(BOTAO_ID_1))
        t.start()
        threads.append(t)

    # Aguarda todas as threads terminarem
    for t in threads:
        t.join()
    print("🏁 Botão 1 clickado")


def clickar_button_2():
    threads = []
    for _ in range(QTD_CB2):
        t = Thread(target=open_browser_and_click(BOTAO_ID_2))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
    print("🏁 Botão 2 clickado")


def clickar_button_3():
    threads = []
    for _ in range(QTD_CB3):
        t = Thread(target=open_browser_and_click(BOTAO_ID_3))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("🏁 Botão 3 clickado")



if __name__ == "__main__":
    clickar_button_3()
    clickar_button_2()
    clickar_button_1()