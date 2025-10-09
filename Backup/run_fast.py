import random
import time

# Lista de ações com "peso"
def web_scraping_simulation1():
    print(  "Simulando web scraping...")
def web_scraping_simulation1():
    print(  "Simulando web scraping 2...")


acoes = ["Verificar status", "Enviar alerta", "Reiniciar serviço"]
pesos = [0.5, 0.3, 0.2]  # Probabilidades relativas

# Número máximo de execuções
max_execucoes = 5

for _ in range(max_execucoes):
    acao = random.choices(acoes, weights=pesos, k=1)[0]
    print(f"Ação aleatória: {acao}")
    time.sleep(random.uniform(0.5, 2))