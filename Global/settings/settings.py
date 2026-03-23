
import pyautogui as pg
import locale

import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(raiz_projeto)

from Global.module import gen_randon_numbers as rn
import Global.data_edition_sync as sy_de
from Global.settings.settings_edition_request import edicao_inicial, total_edicoes, quantidade_repeticoes

# ------------------------------------------------------------------------- Caminhos de rede
CAMINHO_FOTOS = r'\\192.168.1.249\fotos'
CAMINHO_WEB = r'\\192.168.1.249\redacao\web'
CAMINHO_MODELO_WEB = r'\\192.168.1.249\redacao\web\00 - Modelo'
CAMINHO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip'
CAMINHO_MODELO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip\00 - Modelo'
CAMINHO_EDD = r'\\192.168.1.249\redacao\diagramacao\edicao'
CAMINHO_MODELO_EDD = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições\00 - modelo'
CAMINHO_MODELO_EDD_0 = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
CAMINHO_PRINTS = r'\\192.168.1.249\comercial\PRINTS'


# ------------------------------------------------------------------------- Tempos de espera
TIMETOOPEN = 4
TIMETOCLOSE = 6
TIMEEXPPDF = 7

# ------------------------------------------------------------------------- Web_botting
acessos_B1 = rn.generate_number(0, 3)
acessos_B2 = int(acessos_B1 / 2 + 1)
acessos_B3 = int(acessos_B2 / 2)
acessos_H1 = 1
acessos_H2 = 2
acessos_H3 = 1

url_target = "https://ohoje.com"
botão_1 = str("ads-728 mx-auto") #principal
botão_2 = "p-3 pb-0" #lateral
botão_3 = "placement_1026570_0_i" #banner rodapé


adon_1 = "img.ads-728.mx-auto" #addon Halfpage
adon_1_pi = 39095
adon_1_client = "GOV"
adon_1_name = f'Width ({adon_1_client}) - {adon_1_pi}'

adon_2 = "section.block-ads img.ads-728.mx-auto[alt='Publicidade']" #addon Width
adon_2_pi = 39141
adon_2_client = "GOV"
adon_2_name = f'Halfpage ({adon_2_client}) - {adon_2_pi}'

adon_3 = "aa" #addon banner principal
adon_3_pi = 00000
adon_3_client = "SECOM"
adon_3_full_name = f'Main {adon_3_client} - {adon_3_pi}'


# ------------------------------------------------------------------------- Barra de tarefas
quark = 1
opera = 2 # any browser
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

x_data = 850
y_data = 259
x_edicao_17 = 560
y_edicao_17 = 121
x_edicao_capa = 346
y_edicao_capa = 448

def stats():
    print(".....")
    print("⚙️  Settings loaded ✔️")
    print(f".. Tamanho da tela: {pg.size()}")
    print(f".. Centro da tela: ({center_x}, {center_y})")
    print(f".. Edição inicial: {edicao_inicial}")
    print(f".. Quantidade de repetições: {quantidade_repeticoes}")
    print(f".. Criando modelo de {total_edicoes} edições")
    print(".....")


if __name__ == "__main__":
    stats()
    print(sy_de.EDD)