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
NUM_NAVEGADORES = 4   

# Função que cada navegador executa
def abrir_navegador_e_clickar():
    # Configurações do Chrome (opcional: modo headless)
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Descomente se quiser rodar sem abrir janela

    # Inicializa o driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL_JORNAL)

    try:
        # Espera a página carregar
        time.sleep(3)

        # Localiza o botão
        botao = driver.find_element(By.ID, BOTAO_ID_3)

        # Faz scroll até o botão
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao)
        time.sleep(1)  # Dá tempo para o scroll e animações

        # Clica no botão
        # botao.click()
        print("✅ Botão 1 com sucesso!")

    

    except Exception as e:
        print(f"⚠️ Erro ao clicar no botão: {e}")

    finally:
        time.sleep(5)  # Tempo para visualizar o resultado
        driver.quit()

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







        #2 repetir o mesmo processo com os outros botões
#         fazer em outros navegadors  
# tentar descobrir link do relatório
