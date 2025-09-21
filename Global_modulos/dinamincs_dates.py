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

# ---------------------------- VARIÁVEIS ----------------------------
quantidade_por_semana = 5
quantidade_repeticoes = 2
edicao_inicial = 6881 #Precisa ser uma edição de segunda-feira
data_inicial = datetime(2025, 9, 15) #Precisa ser uma segunda-feira

# ---------------------------- VARIÁVEIS ----------------------------
def formatar_numero(num):
    """Formata número com ponto como separador de milhar: 6794 → 6.794"""
    return f"{num:,}".replace(",", ".")

def formatar_edicao(inicio, fim):
    """
    Formata dois números de edição com separador de milhar,
    e suprime prefixo comum no segundo número quando apropriado.
    """
    inicio_str = str(inicio)
    fim_str = str(fim)

    # Encontra prefixo comum
    i = 0
    while i < len(inicio_str) and i < len(fim_str) and inicio_str[i] == fim_str[i]:
        i += 1

    if i == 0:
        return f"{formatar_numero(inicio)}-{formatar_numero(fim)}"

    sufixo_fim = fim_str[i:]
    return f"{formatar_numero(inicio)}-{sufixo_fim}"

def gerar_edicoes(inicial, quantidade_por_semana):
    """
    Gera uma lista de edições formatadas com ponto,
    e edição de fim de semana usando formatação inteligente.
    """
    edicoes = []

    for _ in range(quantidade_por_semana):
        edicoes.append(formatar_numero(inicial))
        inicial += 1

    edicao_fds = formatar_edicao(inicial, inicial + 1)
    edicoes.append(edicao_fds)

    return edicoes

# 🧪 Teste didático
if __name__ == "__main__":
    print("📦 Edições geradas:")
    for _ in range(quantidade_repeticoes):
        edicoes = gerar_edicoes(edicao_inicial, quantidade_por_semana)
        for edicao in edicoes:
            print(f"teste: {edicao}")

        edicao_inicial += quantidade_por_semana + 2