import os
import csv
import inspect  # Importe o módulo inspect
from datetime import datetime

def log(report_name_file, status, message=""):
    '''Registra o status das operaçõesm na pasta logs, cria o arquivo .csv, caso não exista'''
    
    # --- NOVIDADE ---
    # f_back pega o frame de quem chamou a função log()
    # .f_code.co_name extrai o nome dessa função
    frame_chamador = inspect.currentframe().f_back
    try:
        name_func = frame_chamador.f_code.co_name
        # Pega apenas o nome do arquivo (ex: main.py) em vez do caminho C:/.../main.py
        name_arc = os.path.basename(frame_chamador.f_code.co_filename)
    except AttributeError:
        name_func = "unknown"
        name_arc = "unknown"

    pasta_logs = os.path.join(os.path.dirname(__file__), "..", 'Logs')
    os.makedirs(pasta_logs, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_logs, f"{report_name_file}.csv")

    cabecalho = ["data", "hora", "status", "origem", "função", "message"]

    data_agora = datetime.now()
    linha = [data_agora.strftime("%Y-%m-%d"),
             data_agora.strftime("%H:%M:%S"),
             status,
             name_arc,
             name_func,
             message,
             ]

    file_exists = os.path.exists(caminho_arquivo)

    with open(caminho_arquivo, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(cabecalho)
        writer.writerow(linha)
