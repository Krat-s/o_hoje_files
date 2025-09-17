import os
import sys
import time
import pyautogui as pg
import keyboard as kb
from datetime import datetime, timedelta
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)
from Quark_automações.Modulos_quark.data_formatador import formatar_data
from Quark_automações.Modulos_quark.edicao_formatador import gerar_edicoes

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