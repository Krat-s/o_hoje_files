from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    """Espera até que o elemento esteja presente (ou clicável).
    Retorna o elemento encontrado."""
    condicao = EC.element_to_be_clickable if clicavel else EC.presence_of_element_located
    return WebDriverWait(driver, timeout).until(condicao((by, value)))

def registrar_log(status, mensagem=""):
    """Registra os acessos e resultados em logs_acessos.csv"""
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
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url_target)

    def task_model(btt):
        botao = esperar(driver, By.ID, btt, timeout=10, clicavel=True)
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao
        )
        esperar(driver, By.ID, btt, timeout=5, clicavel=True)
        botao.click()
        registrar_log("SUCESSO", f"{btt} clicado com sucesso")
    
    try:
        task_model(botão_1)
        task_model(botão_2)
        task_model(botão_3)

        # esperar(driver, By.ID, "id_de_confirmacao", timeout=10, clicavel=False) #Caso queira aguardar algo após o clique (ex: confirmação)

    except Exception as e:
        erro_msg = f"Erro ao clicar no botão: {str(e)}"
        registrar_log("ERRO", erro_msg)

    finally:
        time.sleep(2)
        driver.quit()
        print("🔒 Navegador fechado.")

def iniciar_agendamentos_diarios():
    """Gera novos horários todos os dias e os agenda novamente."""
    schedule.clear("execucoes_diarias") # Limpa agendamentos anteriores
    agendas = []
    agendas += gerar_horarios(6, 12, acessos_B1)   # manhã
    agendas += gerar_horarios(12, 17, acessos_B2)  # tarde
    agendas += gerar_horarios(18, 24, acessos_B3)  # noite

    for dt in agendas:
        marcacao = dt.strftime("%H:%M")
        schedule.every().day.at(marcacao).do(task).tag("execucoes_diarias")
        print(f"🕒 Execução agendada para: {marcacao}")
    registrar_log("INÍCIO", "Agendamentos configurados com sucesso")
    registrar_log("RELATÓRIO", f"{len(agendas)} horários agendados para ({datetime.now():%Y-%m-%d})")

def daily_task_loop():
    """Controla a execução contínua do sistema (gera novos horários todo dia)."""
    iniciar_agendamentos_diarios()
    schedule.every().day.at("00:01").do(iniciar_agendamentos_diarios).tag("regerar_horarios")

    try:
        while True:
            if os.path.exists("parar.txt"):
                print("🛑 Arquivo de parada detectado. Encerrando...")
                registrar_log("ENCERRADO", "Encerrado via arquivo parar.txt")
                break
            schedule.run_pending()
            time.sleep(30)
    except KeyboardInterrupt:
        print("\n🛑 Execução interrompida manualmente (CTRL+C).")
        registrar_log("ENCERRADO", "Execução interrompida manualmente")