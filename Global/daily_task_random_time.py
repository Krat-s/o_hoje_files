from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from threading import Thread
from datetime import datetime, timedelta
import time
import schedule
import random

import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Global.settings import url_target, botão_1, botão_2, botão_3, acessos_B1, acessos_B2, acessos_B3

def gerar_horarios(inicio_h, fim_h, n_acessos):
    """Gera horários aleatórios em um intervalo"""
    hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start = hoje + timedelta(hours=inicio_h)
    end   = hoje + timedelta(hours=fim_h)
    total_s = int((end - start).total_seconds())

    horarios = sorted(
        start + timedelta(seconds=random.randint(0, total_s))
        for _ in range(n_acessos)
    )
    return horarios

def task():
    """Abre o navegador e clica em um botão específico"""    
    print(f"🌐 Acessando {url_target}")
    # Configurações do Chrome (opcional: modo headless)
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Descomente se quiser rodar sem abrir janela

    # Inicializa o driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url_target)

    try:
        time.sleep(3)
        botao = driver.find_element(By.ID, botão_1)
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao) #Scroll
        time.sleep(1)  # Dá tempo para o scroll e animações
        botao.click()
        print("✅ Botão 1 com sucesso!")    

    except Exception as e:
        print(f"⚠️ Erro ao clicar no botão: {e}")

    finally:
        time.sleep(5)  # Tempo para visualizar o resultado
        driver.quit()
        print("🔒 Navegador fechado.")

# Cria e inicia as threads
threads = []
check = 0

# for _ in range(NUM_NAVEGADORES):
#     t = Thread(target=task)
#     t.start()
#     threads.append(t)

# # Aguarda todas as threads terminarem
# for t in threads:
#     t.join()

print("🏁 Automação finalizada!")
print(f'Número de acessos --> {check}')

# 1. Gere todos os horários do dia
agendas = []
agendas += gerar_horarios(6,  12, acessos_B1)   # manhã
agendas += gerar_horarios(12, 17, acessos_B2)  # tarde
agendas += gerar_horarios(18, 24, acessos_B3)  # noite

# 2. Agende cada execução
for dt in agendas:
    marcacao = dt.strftime("%H:%M")
    # schedule.every().day.at(marcacao).do(abrir_navegador_e_clickar)
    print(f"Agendado para: {marcacao}")

# # 3. Loop principal
# # while True:
# #     # schedule.run_pending()
# #     # time.sleep(30)
# #     print(agendas)
# # print(agendas)

if __name__ == "__main__":
    for dt in agendas:
        marcacao = dt.strftime("%H:%M")
        # schedule.every().day.at(marcacao).do(abrir_navegador_e_clickar)
        print(f": {marcacao}")