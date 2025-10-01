import pyautogui as pg
import os
import sys
import keyboard
from datetime import datetime, timedelta
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

import Global.utils as ut
import time
# ------------------------------------------------------------------------- Caminhos de rede
CAMINHO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip'
CAMINHO_MODELO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip\Modelo'
CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
CAMINHO_MODELO_WEB = r'\\192.168.1.249\redacao\web\Modelo páginas casadas'
CAMINHO_WEB = r'\\192.168.1.249\redacao\web'
CAMINHO_FOTOS = r'\\192.168.1.249\fotos'
CAMINHO_EDD = r'\\192.168.1.249\redacao\diagramacao\edicao'

screen_width, screen_height = pg.size()
center_x = screen_width / 2
center_y = screen_height / 2

# ------------------------------------------------------------------------- Dados para Casamento
pg.FAILSAFE = True
print(f"...")
print(f"...     Failsafe on")
print(f"...     Settings loading sucess")
print(f"...")

# ------------------------------------------------------------------------- Dados de edição
quantidade_repeticoes = 2
edicao_inicial = 6895

# ------------------------------------------------------------------------- Posições de clique (em porcentagem da tela)
# if pg.size() == (1366, 768):
#     x_data = 49.48
#     y_data = 23.06
#     x_edicao_17 = 44.17
#     y_edicao_17 = 12.41
#     x_edicao_capa = 13.91
#     y_edicao_capa = 41.30
# elif pg.size() == (1920, 1080):
#     x_data = 68.45
#     y_data = 33.20
#     x_edicao_17 = 41.14
#     y_edicao_17 = 15.40
#     x_edicao_capa = 18.74
#     y_edicao_capa = 58.07

# ------------------------------------------------------------------------- Tempos de espera
TEMPO_ABERTURA = 4
TEMPO_FECHAMENTO = 3
TIMETOCLOSE = 6


# x_data = 49.48
# y_data = 23.06
# x_edicao_17 = 44.17
# y_edicao_17 = 12.41
# x_edicao_capa = 13.91
# y_edicao_capa = 41.30

# ------------------------------------------------------------------------- Ativar isso se quiser usar posições absolutas(essas funcionam na maquina do comercial)
x_data = 850
y_data = 259
x_edicao_17 = 560
y_edicao_17 = 121
x_edicao_capa = 346
y_edicao_capa = 448

if __name__ == "__main__":
    print(f"Tamanho da tela: {pg.size()}")
    print(f"Centro da tela: ({center_x}, {center_y})")
    print(f"Edição inicial: {edicao_inicial}")