import os
import sys
import time
import keyboard as kb
import pyautogui as pg
# from datetime import datetime, timedelta
from edicao_formatador import gerar_edicoes

# from Quark_automações.Modulos_quark.data_formatador import formatar_data

import sys
import os

# Caminho até a subpasta onde está o módulo
subpasta_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Quartk_automações', 'Modulos_quark'))
sys.path.append(subpasta_path)


# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.4
pg.FAILSAFE = True
time.sleep(1)

largura, altura = pg.size()
centro_x = largura / 2
centro_y = altura / 2


# ---------------------------- VARIÁVEIS ----------------------------
quantidade_por_semana = 5
quantidade_repeticoes = 2
edicao_inicial = 6881 #Precisa ser uma edição de segunda-feira
data_inicial = datetime(2025, 9, 15) #Precisa ser uma segunda-feira

# ---------------------------- VARIÁVEIS ----------------------------


for _ in range(quantidade_repeticoes):
    ed = gerar_edicoes(edicao_inicial, quantidade_por_semana)
    print (f"📦 Edições: {ed}")