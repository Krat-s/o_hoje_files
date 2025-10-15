from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from threading import Thread
import time

# Configurações
URL_JORNAL = "https://ohoje.com"
BOTAO_ID_1 = "placement_1013993_0"
BOTAO_ID_2 = "placement_1013994_0_i"
BOTAO_ID_3 = "placement_1026570_0_i"
NUM_NAVEGADORES = 2   

# Função que cada navegador executa
def abrir_navegador_e_clickar():
    chrome_options = Options()

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL_JORNAL)

    try:
        time.sleep(3)
        botao = driver.find_element(By.ID, BOTAO_ID_1)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao)
        time.sleep(1)
        botao.click()
        print("✅ Botão clicado com sucesso!")
    
    except Exception as e:
        print(f"⚠️ Erro ao clicar no botão: {e}")

    finally:
        time.sleep(5)  # Tempo para visualizar o resultado
        driver.quit()

# Cria e inicia as threads
threads = []
for _ in range(NUM_NAVEGADORES):
    t = Thread(target=abrir_navegador_e_clickar)
    t.start()
    threads.append(t)

# Aguarda todas as threads terminarem
for t in threads:
    t.join()

print("🏁 Automação finalizada!")

