import pyautogui as pg
import locale
import os
import sys
from datetime import datetime, timedelta

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from App.modulos_quark.data_formatador import formatar_data
from Web.modulos_web import random_number as rn
import Global.tesseract_utils as pyt
import Global.data_edition_sync as sy_de

# ------------------------------------------------------------------------- Caminhos de rede
CAMINHO_EDD = r'\\192.168.1.249\redacao\diagramacao\edicao'
CAMINHO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip'
CAMINHO_WEB = r'\\192.168.1.249\redacao\web'
CAMINHO_FOTOS = r'\\192.168.1.249\fotos'
CAMINHO_MODELO_EDD = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
CAMINHO_MODELO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip\00 - Modelo'
CAMINHO_MODELO_WEB = r'\\192.168.1.249\redacao\web\00 - Modelo'

# ------------------------------------------------------------------------- Tempos de espera
TIMETOOPEN = 4
TIMETOCLOSE = 6
TIMEEXPPDF = 7

# ------------------------------------------------------------------------- Dados de edição
quantidade_repeticoes = int(1)
edicao_inicial = 8001
total_edicoes = quantidade_repeticoes * 6

# ------------------------------------------------------------------------- wedding
edicao_0 = sy_de.obter_edicao_por_data(datetime.now() + timedelta(days=1))
data_0 = formatar_data(datetime.now() + timedelta(days=1), tipo="dia_semana")
EDD = f"{edicao_0.replace('.', '')} - {data_0}"

# ------------------------------------------------------------------------- Web_botting
acessos_B1 = rn.gerar_numero(0, 3)
acessos_B2 = int(acessos_B1 / 2 + 1)
acessos_B3 = int(acessos_B2 / 2)
acessos_H1 = 1
acessos_H2 = 2
acessos_H3 = 1
jackpot = acessos_B1 + acessos_B2 + acessos_B3 * 4 #24 numero máximo de acessos (linha completamente irrelevante)

url_target = "https://ohoje.com"
botão_1 = "placement_1013993_0" #principal
botão_2 = "placement_1013994_0_i" #lateral
botão_3 = "placement_1026570_0_i" #banner rodapé

# ------------------------------------------------------------------------- Barra de tarefas
quark = 1
opera = 2 # Navegador padrão
vscode = 3
explorer = 4

# ------------------------------------------------------------------------- Configurações gerais
screen_width, screen_height = pg.size()
center_x = screen_width / 2
center_y = screen_height / 2
locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")


# ------------------------------------------------------------------------- Pytesseract and regions
already_open_r = (489, 280, 98, 103)
already_open_full_r = (489, 281, 389, 156) 
quark_icon_c_r = (499, 309, 79, 101)
quark_loading = (493, 304, 123, 111)
file_not_fond = (465, 232, 477, 210)
file_not_fond_close = (500, 260, 363, 142)
button_cancel_qk = 829, 419
button_ok_qk = 829, 385

def stats():
    print(".....")
    print("⚙️  Settings loaded ✔️")
    print(f".. Tamanho da tela: {pg.size()}")
    print(f".. Centro da tela: ({center_x}, {center_y})")
    print(f".. Edição inicial: {edicao_inicial}")
    print(f".. Quantidade de repetições: {quantidade_repeticoes}")
    print(f".. Criando modelo de {total_edicoes} edições")
    print(".....")

# ------------------------------------------------------------------------- Posições de clique (em porcentagem da tela)
# arrumar uma forma de fazer isso de forma dinamica. Opções: 1 calcular sempre que rodar o script, 2 criar um arquivo de configuração para cada resolução de tela de acordo com o dispositivo
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

# ------------------------------------------------------------------------- Ativar isso se quiser usar posições absolutas(essas funcionam na maquina do comercial)
# x_data = 49.48
# y_data = 23.06
# x_edicao_17 = 44.17
# y_edicao_17 = 12.41
# x_edicao_capa = 13.91
# y_edicao_capa = 41.30

x_data = 850
y_data = 259
x_edicao_17 = 560
y_edicao_17 = 121
x_edicao_capa = 346
y_edicao_capa = 448

if __name__ == "__main__":
    # stats()
    print(acessos_B1)