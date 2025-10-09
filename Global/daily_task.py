from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from threading import Thread

import random
from datetime import datetime, timedelta
import time

# Configurações
URL_JORNAL = "https://ohoje.com"
BOTAO_ID_1 = "placement_1013993_0"
BOTAO_ID_2 = "placement_1013994_0_i"
BOTAO_ID_3 = "placement_1026570_0_i"
NUM_NAVEGADORES = 8   

# Função que cada navegador executa
def gerar_horarios(inicio_h, fim_h, n_acessos):
    hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start = hoje + timedelta(hours=inicio_h)
    end   = hoje + timedelta(hours=fim_h)
    total_s = int((end - start).total_seconds())

    horarios = sorted(
        start + timedelta(seconds=random.randint(0, total_s))
        for _ in range(n_acessos)
    )
    print(horarios)
    return horarios

def abrir_navegador_e_clickar():
    # # Configurações do Chrome (opcional: modo headless)
    # chrome_options = Options()
    # # chrome_options.add_argument("--headless")  # Descomente se quiser rodar sem abrir janela

    # # Inicializa o driver
    # driver = webdriver.Chrome(options=chrome_options)
    # driver.get(URL_JORNAL)

    # try:
    #     # Espera a página carregar
    #     time.sleep(3)

    #     # Localiza o botão
    #     botao = driver.find_element(By.ID, BOTAO_ID_3)

    #     # Faz scroll até o botão
    #     driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao)
    #     time.sleep(1)  # Dá tempo para o scroll e animações

    #     # Clica no botão
    #     # botao.click()
    #     print("✅ Botão 1 com sucesso!")

    

    # except Exception as e:
    #     print(f"⚠️ Erro ao clicar no botão: {e}")

    # finally:
    #     time.sleep(5)  # Tempo para visualizar o resultado
    #     driver.quit()
    print("Simulando clique no botão...")

# Cria e inicia as threads
threads = []
check = 0

for _ in range(NUM_NAVEGADORES):
    t = Thread(target=abrir_navegador_e_clickar)
    t.start()
    threads.append(t)
    check += 1

# Aguarda todas as threads terminarem
for t in threads:
    t.join()

print("🏁 Automação finalizada!")
print(f'Número de acessos --> {check}')
