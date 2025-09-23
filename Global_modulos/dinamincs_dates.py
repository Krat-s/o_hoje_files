import os
import sys
import time
import pyautogui as pg
import keyboard as kb
from datetime import datetime, timedelta
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)
import Global_modulos.settings as cg
from Quark_automações.Modulos_quark.data_formatador import formatar_data
from Quark_automações.Modulos_quark.edicao_formatador import gerar_edicoes

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.4
pg.FAILSAFE = True
time.sleep(1)

# ---------------------------- VARIÁVEIS ----------------------------
quantidade_por_semana = 5
quantidade_repeticoes = 2
edicao_inicial = 6881 #Precisa ser uma edição de segunda-feira
data_inicial = datetime(2025, 9, 15) #Precisa ser uma segunda-feira

# ---------------------------- VARIÁVEIS ----------------------------
def ajustar_data(data):
    return data + timedelta(days=1) if data.weekday() == 6 else data

edicao = edicao_inicial
data = data_inicial
    
for _ in range(cg.quantidade_repeticoes):
    edicoes = gerar_edicoes(edicao, cg.quantidade_por_semana)

    for ed in edicoes:
        dia_semana = formatar_data(data, tipo='dia_semana')
        pasta_nome = f"{ed.replace('.', '')} - {dia_semana}"
        info = {
        "edicao_formatada": ed,
        "data_formatada": formatar_data(data),
        "dia_semana": formatar_data(data, tipo='dia_semana')
        }

        # ---------------CRIANDO PASTAS, COPIANDO MODELOS E APLICANDO CABEÇALHO--------
                                        
        print(f"📦 Criando pasta: {pasta_nome}")
        data += timedelta(days=1)
        data = ajustar_data(data)
    edicao += cg.quantidade_por_semana + 2