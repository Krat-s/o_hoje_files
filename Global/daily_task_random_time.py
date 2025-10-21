from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread
from datetime import datetime, timedelta
import time
import schedule
import random
import csv
import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Global.settings import url_target, botão_1, botão_2, botão_3, acessos_B1, acessos_B2, acessos_B3

def esperar(driver, by, value, timeout=10, clicavel=True):
    """
    Espera até que o elemento esteja presente (ou clicável).
    Retorna o elemento encontrado.
    """
    condicao = EC.element_to_be_clickable if clicavel else EC.presence_of_element_located
    return WebDriverWait(driver, timeout).until(condicao((by, value)))

def registrar_log(status, mensagem=""):
    """
    Registra os acessos e resultados em logs_acessos.csv.
    Cria o arquivo se ele não existir.
    """
    caminho_arquivo = os.path.join(os.path.dirname(__file__), "logs_acessos.csv")
    cabecalho = ["data", "hora", "status", "mensagem"]

    data_agora = datetime.now()
    linha = [data_agora.strftime("%Y-%m-%d"), data_agora.strftime("%H:%M:%S"), status, mensagem]

    arquivo_existe = os.path.exists(caminho_arquivo)

    with open(caminho_arquivo, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not arquivo_existe:
            writer.writerow(cabecalho)
        writer.writerow(linha)

def gerar_horarios(inicio_h, fim_h, n_acessos):
    """Gera horários aleatórios dentro de um intervalo de horas."""
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
    """Abre o navegador, clica no botão e registra o resultado."""
    print(f"🌐 Acessando {url_target}")

    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Rode sem abrir janela se quiser
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url_target)

    try:
        # Espera o botão 1 ficar clicável
        botao = esperar(driver, By.ID, botão_1, timeout=10, clicavel=True)

        # Faz scroll suave até o botão
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao
        )

        # Espera o botão estar visível após o scroll
        esperar(driver, By.ID, botão_1, timeout=5, clicavel=True)

        botao.click()
        registrar_log("SUCESSO", "Botão 1 clicado com sucesso")

        # Caso queira aguardar algo após o clique (ex: confirmação)
        esperar(driver, By.ID, "id_de_confirmacao", timeout=10, clicavel=False)

    except Exception as e:
        erro_msg = f"Erro ao clicar no botão: {str(e)}"
        registrar_log("ERRO", erro_msg)

    finally:
        # Pequena pausa opcional só para ver o resultado
        time.sleep(2)
        driver.quit()
        print("🔒 Navegador fechado.")


# 1. Gerar horários do dia
def agendamento():
    agendas = []
    agendas += gerar_horarios(6, 12, acessos_B1)   # manhã
    agendas += gerar_horarios(12, 17, acessos_B2)  # tarde
    agendas += gerar_horarios(18, 24, acessos_B3)  # noite

    # 2. Mostrar horários e agendar
    for dt in agendas:
        marcacao = dt.strftime("%H:%M")
        schedule.every().day.at(marcacao).do(task)
        print(f"🕒 Execução agendada para: {marcacao}")

    registrar_log("INÍCIO", "Agendamentos configurados com sucesso")

    # 3. Loop principal
    while True:
        schedule.run_pending()
        time.sleep(30)  # Checa a cada 30 segundos

if __name__ == "__main__":
    print("📅 Iniciando agendamento de execuções automáticas...\n")
    print("\n✅ Todas as execuções foram agendadas com sucesso.")
    agendamento()