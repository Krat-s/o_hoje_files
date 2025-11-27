
import os
import csv
from datetime import datetime, timedelta

def log(script, status, mensagem=""):
    """Registra os acessos e resultados em logs_acessos.csv"""
    
    # Caminho da pasta Logs
    pasta_logs = os.path.join(os.path.dirname(__file__), "..", 'Logs')
    os.makedirs(pasta_logs, exist_ok=True)

    # Caminho do arquivo CSV
    caminho_arquivo = os.path.join(pasta_logs, f"{script}.csv")

    cabecalho = ["data", "hora", "status", "mensagem"]

    data_agora = datetime.now()
    linha = [data_agora.strftime(" %Y-%m-%d"),
             data_agora.strftime(" %H:%M:%S"),
              status,
              mensagem]

    arquivo_existe = os.path.exists(caminho_arquivo)

    with open(caminho_arquivo, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not arquivo_existe:
            writer.writerow(cabecalho)
        writer.writerow(linha)