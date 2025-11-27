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

from settings import url_target, botão_1, botão_2, botão_3, acessos_B1, acessos_B2, acessos_B3, acessos_H1, acessos_H2, acessos_H3

def esperar(driver, by, value, timeout=10, clicavel=True):
    """Espera até que o elemento esteja presente (ou clicável).
    Retorna o elemento encontrado."""
    condicao = EC.element_to_be_clickable if clicavel else EC.presence_of_element_located
    return WebDriverWait(driver, timeout).until(condicao((by, value)))

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

    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        registrar_log("ERRO", f"Falha ao iniciar ChromeDriver: {e}")
        return
    driver.get(url_target)
    
    def task_view(btt, n_view):
        for i in range(n_view):
            botao = esperar(driver, By.ID, btt, timeout=15, clicavel=True)
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao
            )
            time.sleep(0.5)
            esperar(driver, By.ID, btt, timeout=10, clicavel=True)
            time.sleep(0.5)
        registrar_log("SUCESSO", f"{btt} visualizado {n_view * 3} vezes")
        
    def task_click(btt, n_clk):
        for i in range(n_clk):
            botao = esperar(driver, By.ID, btt, timeout=15, clicavel=True)
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", botao
            )
            esperar(driver, By.ID, btt, timeout=10, clicavel=True)
            time.sleep(0.5)
            botao.click()
            time.sleep(0.5)
        registrar_log("SUCESSO", f"{btt} clicado {n_clk} vezes")

    try:
        for _ in range (3):
            task_view(botão_1, acessos_B1)
            task_view(botão_2, acessos_B2)
            task_view(botão_3, acessos_B3)
        task_click(botão_1, acessos_B1)
        task_click(botão_2, acessos_B2)
        task_click(botão_3, acessos_B3)

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
    agendas += gerar_horarios(6, 16, acessos_H1)   # manhã
    agendas += gerar_horarios(16, 22, acessos_H2)  # tarde
    agendas += gerar_horarios(22, 24, acessos_H3)  # noite

    for dt in agendas:
        marcacao = dt.strftime("%H:%M")
        schedule.every().day.at(marcacao).do(task).tag("execucoes_diarias")
        print(f"🕒 Execução agendada para: {marcacao}")
    print(f"✅ {len(agendas)} horários configurados para {datetime.now():%Y-%m-%d}")
    registrar_log("INÍCIO", "Agendamentos configurados com sucesso")
    registrar_log("RELATÓRIO", f"{len(agendas)} horários agendados para ({datetime.now():%Y-%m-%d})")

def daily_task_loop():
    """Controla a execução contínua do sistema (gera novos horários todo dia)."""
    print("🚀 Loop de tarefas iniciado. Pressione CTRL+C ou crie 'parar.txt' para encerrar.")
    iniciar_agendamentos_diarios()
    schedule.every().day.at("00:01").do(iniciar_agendamentos_diarios).tag("regerar_horarios")

    try:
        while True:
            caminho_parar = os.path.join(os.path.dirname(__file__), "parar.txt")
            if os.path.exists(caminho_parar):
                print("🛑 Arquivo de parada detectado. Encerrando...")
                registrar_log("ENCERRADO", "Encerrado via arquivo parar.txt")
                break
            schedule.run_pending()
            time.sleep(30)
    except KeyboardInterrupt:
        print("\n🛑 Execução interrompida manualmente (CTRL+C).")
        registrar_log("ENCERRADO", "Execução interrompida manualmente")

    
# if __name__ == "__main__":
#     iniciar_agendamentos_diarios()
