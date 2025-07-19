from Modulos.data_formatador import formatar_data
import pyautogui as pg
import locale
from datetime import datetime, timedelta
import keyboard as kb
import time
import os

# ---------------------------- Configurações gerais
pg.PAUSE = 0.5
pg.FAILSAFE = True
locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")
screen_width, screen_height = pg.size()
center_x, center_y = screen_width / 2, screen_height / 2

# ---------------------------- Constantes
EDICAO_INICIAL = 6794
DATA_INICIAL = datetime(2025, 7, 21)
CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
CAMINHO_WEB = r'\\192.168.1.249\redacao\web'
EDD_PADRAO = "0000 - TESTE"
TEMPO_ABERTURA = 4
TEMPO_FECHAMENTO = 3
QTD_SEMANAL = 5
REPETICOES = 2

# ---------------------------- Posições de clique
x_data = int(screen_width * 0.6428)
y_data = int(screen_height * 0.3255)
x_edicao_17 = int(screen_width * 0.4173)
y_edicao_17 = int(screen_height * 0.1536)
x_edicao_capa = int(screen_width * 0.1740)
y_edicao_capa = int(screen_height * 0.4648)

# ---------------------------- Funções utilitárias
def gerar_edicoes(inicial, quantidade):
    edicoes = [str(inicial + i) for i in range(quantidade)]
    edicoes.append(f"{inicial + quantidade:,}-{inicial + quantidade + 1:,}".replace(",", "."))
    return edicoes

def ajustar_data(data):
    return data + timedelta(days=1) if data.weekday() == 6 else data

def criar_pasta(nome):
    time.sleep(0.5)
    maximizar_janela()
    time.sleep(0.5)
    pg.click(center_x, center_y)
    pg.hotkey('ctrl', 'shift', 'n')
    time.sleep(0.5)
    kb.write(nome)
    pg.press('enter')

def copiar_modelo_para_pasta(edicao, data_formatada):
    pg.click(center_x, center_y)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    time.sleep(0.3)
    pg.hotkey('alt', 'd')
    nome_pasta = f"{edicao.replace('.', '')} - {formatar_data(data_formatada, tipo='dia_semana')}"
    kb.write(f"{CAMINHO_ADIANTO}\\{nome_pasta}")
    pg.press('enter')
    pg.hotkey('ctrl', 'v')

def maximizar_janela():
    kb.press_and_release('alt+space')
    time.sleep(0.2)
    kb.press_and_release('x')

def selecionar_ferramenta(tecla):
    pg.click(center_x, 10)
    kb.press(tecla)

def abrir_quark():
    pg.hotkey('win', 's')
    time.sleep(0.2)
    pg.hotkey('win', '1')
    time.sleep(0.2)

def abrir_software(indice):
    pg.hotkey('win', 's')
    time.sleep(0.2)
    pg.hotkey('win', str(indice))
    time.sleep(0.2)

def preencher_data():
    selecionar_ferramenta("v")
    pg.click(x_data, y_data)
    selecionar_ferramenta("t")
    pg.press('t', presses=2)
    time.sleep(0.3)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.3)
    kb.write(data_formatada)

def aplicar_autodata(numero):
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'o')
    nome_arquivo = f"{edicao.replace('.', '')} - {formatar_data(data_da_edicao, tipo='dia_semana')}"
    kb.write(f"{CAMINHO_ADIANTO}\\{nome_arquivo}")
    pg.press('enter')
    pg.write(str(numero))
    time.sleep(0.3)
    pg.press('down')
    time.sleep(0.3)
    pg.press('enter')
    time.sleep(TEMPO_ABERTURA)
    preencher_data()
    time.sleep(0.4)
    pg.press('esc')
    pg.hotkey('ctrl', 's')

def fechar_pagina():
    pg.hotkey('ctrl', 'f4')
    time.sleep(TEMPO_FECHAMENTO)

def autodata_paginas():
    for i in range(20, 1, -1):
        if i == 17:
            continue
        aplicar_autodata(i)
        fechar_pagina()

def autodata_edicao_17():
    aplicar_autodata(17)
    selecionar_ferramenta("v")
    pg.hotkey('ctrl', '0')
    pg.click(x_edicao_17, y_edicao_17)
    pg.hotkey('ctrl', 'a')
    kb.write(f"Ano 21 - nº {edicao_formatada}")
    time.sleep(0.2)
    pg.hotkey('ctrl', 's')
    time.sleep(0.2)
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'f4')
    time.sleep(TEMPO_FECHAMENTO)

def autodata_edicao_1():
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'o')
    kb.write(f"{CAMINHO_ADIANTO}\\{EDD_PADRAO}")
    pg.press('enter')
    pg.write('1')
    time.sleep(0.2)
    pg.press('down')
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(TEMPO_ABERTURA + 3)
    selecionar_ferramenta("v")
    pg.click(x_edicao_capa, y_edicao_capa)
    selecionar_ferramenta("t")
    pg.press('t', presses=4)
    time.sleep(0.3)
    pg.press('Backspace', presses=5)
    kb.write(f"nº {edicao_formatada}")
    time.sleep(0.4)
    pg.press('right')
    time.sleep(0.4)
    pg.press('del')
    time.sleep(0.4)
    kb.write(f" | {data_formatada} ")

def cabeçalho():
    autodata_paginas()
    autodata_edicao_1()
    autodata_edicao_17()

def abrir_pasta():
    os.startfile(CAMINHO_ADIANTO)
    maximizar_janela()
    pg.click(center_x, center_y)

def fechar_explorer():
    pg.click(center_x, center_y)
    pg.hotkey('alt', 'f4')
    time.sleep(0.5)

def voltar_pasta():
    pg.click(center_x, center_y)
    pg.hotkey('alt', 'up')
    time.sleep(0.5)

# ---------------------------- Execução principal
data_da_edicao = DATA_INICIAL - timedelta(days=1)

# abrir_pasta()

for _ in range(REPETICOES):
    edicoes_geradas = gerar_edicoes(EDICAO_INICIAL, QTD_SEMANAL)

    for edicao in edicoes_geradas:
        EDD = edicao
        data_da_edicao += timedelta(days=1)
        data_da_edicao = ajustar_data(data_da_edicao)
        data_formatada = formatar_data(data_da_edicao)
        edicao_formatada = (
            f"{int(edicao):,}".replace(",", ".")
            if data_da_edicao.weekday() != 5 else edicao
        )

        # nome_pasta = f"{edicao.replace('.', '')} - {formatar_data(data_da_edicao, tipo='dia_semana')}"
        # criar_pasta(nome_pasta)

        # modelo_path = {
        #     0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
        #     5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
        # }.get(data_da_edicao.weekday(), r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição')

        # time.sleep(0.3)
        # pg.hotkey('alt', 'd')
        # kb.write(modelo_path)
        # pg.press('enter')
        # copiar_modelo_para_pasta(edicao, data_da_edicao)
        # voltar_pasta()
        # time.sleep(0.3)

        # time.sleep(0.5)
        # abrir_quark()
        # time.sleep(0.5)
        # pg.press('esc', presses=3)
        # time.sleep(0.5)
        # autodata_edicao_17()
        # abrir_software(4)  # Explorer
        # pg.hotkey('alt', 'up')
        # pg.click(center_x, center_y)

        # Se quiser aplicar cabeçalho apenas nos dias úteis:
        # if data_da_edicao.weekday() < 5:
        #     cabeçalho()

        print(edicao_formatada)
        # print(edicao_formatada.replace(".", ""))

    EDICAO_INICIAL += QTD_SEMANAL + 2