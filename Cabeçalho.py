import os
import time
import locale
from datetime import datetime, timedelta
import pyautogui as pg
import keyboard as kb
from Modulos.data_formatador import formatar_data
from Modulos.edicao_formatador import gerar_edicoes
from pywinauto import Desktop

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True
time.sleep(0.5)

locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")

screen_width, screen_height = pg.size()
center_x = screen_width / 2
center_y = screen_height / 2

edicao_inicial = 6600
quantidade_por_semana = 5
quantidade_repeticoes = 2
data_inicial = datetime(2025, 7, 21) #Precisa ser uma segunda-feira

# ---------------------------- CONSTANTES ----------------------------
CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
EDD_PADRAO = "0000 - TESTE"
TEMPO_ABERTURA = 4
TEMPO_FECHAMENTO = 3

# ---------------------------- POSIÇÕES DE CLIQUE ----------------------------
# --MARKETING 1
x_data = 49.48
y_data = 23.06
x_edicao_17 = 44.17
y_edicao_17 = 12.41
x_edicao_capa = 13.91
y_edicao_capa = 41.30

# --COMERCIAL 3
# x_data = 68.45
# y_data = 33.20
# x_edicao_17 = 41.14
# y_edicao_17 = 15.40
# x_edicao_capa = 18.74
# y_edicao_capa = 58.07

# --LIXO?
# x_data = int(screen_width * 0.6428)
# y_data = int(screen_height * 0.3255)
# x_edicao_17 = int(screen_width * 0.4173)
# y_edicao_17 = int(screen_height * 0.1536)
# x_edicao_capa = int(screen_width * 0.1962) 
# y_edicao_capa = int(screen_height * 0.5690)

# ---------------------------- FUNÇÕES UTILITÁRIAS ----------------------------
def ajustar_data(data):
    return data + timedelta(days=1) if data.weekday() == 6 else data

def click(x_percent, y_percent):
    screen_width, screen_height = pg.size()
    x = int((x_percent / 100) * screen_width)
    y = int((y_percent / 100) * screen_height)
    pg.click(x, y)

def abrir_software(numero):
    pg.hotkey('win', 's')
    pg.hotkey('win', str(numero))
    pg.press('enter')
    time.sleep(0.5)

def maximizar_janela():
    kb.press_and_release('alt+space')
    time.sleep(0.2)
    kb.press_and_release('x')

def pasta_esta_aberta(nome_pasta):
    janelas = Desktop(backend="uia").windows()
    for janela in janelas:
        if janela.class_name() == "CabinetWClass":
            titulo = janela.window_text()
            if nome_pasta.lower() in titulo.lower():
                return True
    return False

# ---------------------------- EXPLORADOR DE ARQUIVOS ----------------------------
def criar_pasta(nome):
    time.sleep(0.5)
    maximizar_janela()
    time.sleep(0.5)
    pg.click(center_x, center_y)
    pg.hotkey('ctrl', 'shift', 'n')
    time.sleep(0.5)
    kb.write(nome)
    pg.press('enter')

def copiar_modelo_para_pasta(ed, data_formatada):
    nome_pasta = f"{ed.replace('.', '')} - {data_formatada}"
    pg.click(center_x, center_y)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    time.sleep(0.3)
    pg.hotkey('ctrl', 'l')
    kb.write(f"{CAMINHO_ADIANTO}\\{nome_pasta}")
    pg.press('enter')
    pg.hotkey('ctrl', 'v')

def abrir_pasta(endereco):
    os.startfile(endereco)
    maximizar_janela()
    pg.click(center_x, center_y)

def fechar_explorer():
    pg.click(center_x, center_y)
    pg.hotkey('alt', 'f4')

def voltar_pasta():
    pg.click(center_x, center_y)
    pg.hotkey('alt', 'up')

# ---------------------------- FUNÇÕES UTILITÁRIAS (QUARK)----------------------------
def selecionar_ferramenta(tecla):
    time.sleep(0.2)
    pg.click(center_x, 10)
    time.sleep(0.2)
    pg.press("v")
    kb.press(tecla)

def preencher_data(data_formatada):
    selecionar_ferramenta("v")
    click(x_data, y_data)
    selecionar_ferramenta("t")
    pg.press('t', presses=2)
    time.sleep(0.4)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.4)
    kb.write(data_formatada)

def aplicar_autodata(numero, edicao_formatada, dia_semana, data_formatada):
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'o')
    nome_pasta = f"{edicao_formatada.replace('.', '')} - {dia_semana}"
    kb.write(f"{CAMINHO_ADIANTO}\\{nome_pasta}")
    pg.press('enter')
    pg.write(str(numero))
    time.sleep(0.3)
    pg.press('down')
    time.sleep(0.3)
    pg.press('enter')
    time.sleep(TEMPO_ABERTURA)
    preencher_data(data_formatada)
    time.sleep(0.4)
    pg.press('esc')
    pg.hotkey('ctrl', 's')

def fechar_pagina():
    pg.hotkey('ctrl', 'f4')
    time.sleep(TEMPO_FECHAMENTO)

# ---------------------------- AUTODATA ----------------------------
def autodata_paginas(edicao_formatada, dia_semana, data_formatada):
    for i in range(20, 1, -1):
        if i in [17, 18, 19]:
            continue
        else:
            aplicar_autodata(i, edicao_formatada, dia_semana, data_formatada)
            fechar_pagina()
           
def autodata_edicao_1(edicao_formatada, data_formatada, dia_semana):
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'o')
    pg.write('1')
    pg.press('down')
    pg.press('enter')
    time.sleep(TEMPO_ABERTURA + 3)
    selecionar_ferramenta("v")
    click(x_edicao_capa, y_edicao_capa)
    selecionar_ferramenta("t")
    pg.press('t', presses=4)
    pg.press('backspace', presses=5)
    kb.write(f"nº {edicao_formatada} ")
    pg.press('right', presses=2)
    pg.press('backspace')
    kb.write(f"|  {data_formatada}")
    pg.press('esc', presses=2)
    pg.hotkey('ctrl', 's')
    time.sleep(0.2)
    fechar_pagina()

def autodata_edicao_17(edicao_formatada, data_formatada, dia_semana):
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', '0')
    pg.hotkey('ctrl', 'o')
    time.sleep(0.3)
    kb.write(CAMINHO_ADIANTO + '\\' + f"{edicao_formatada.replace('.', '')} - {dia_semana}")
    pg.press('enter')
    time.sleep(0.5)
    kb.write('17')
    pg.press('down')
    pg.press('enter')
    time.sleep(TEMPO_ABERTURA)
    pg.press('esc', presses=3)
    preencher_data(data_formatada)
    time.sleep(0.3)
    pg.press('esc', presses=3)
    selecionar_ferramenta("v")
    pg.hotkey('ctrl', '0')
    click(x_edicao_17, y_edicao_17)
    selecionar_ferramenta("t")
    pg.press('t', presses=4)
    pg.hotkey('ctrl', 'a')
    kb.write(f"Ano 21 - nº {edicao_formatada}")
    time.sleep(0.2)
    pg.hotkey('ctrl', 's')
    time.sleep(0.2)
    pg.press('esc', presses=3)
    fechar_pagina()

# ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------
def main():
    print("📦 Edições geradas:")
    edicao = edicao_inicial
    data = data_inicial

    for _ in range(quantidade_repeticoes):
        edicoes = gerar_edicoes(edicao, quantidade_por_semana)

        for ed in edicoes:
            data_formatada = formatar_data(data)
            # dia_semana = formatar_data(data, tipo='dia_semana')
            info = {
            "edicao_formatada": ed,
            "data_formatada": formatar_data(data),
            "dia_semana": formatar_data(data, tipo='dia_semana')
            }
            modelo_path = {
            0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
            5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
            }.get(data.weekday(), r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição')

            #--------------------------------------------------------------------------Criando pasta da edicão e copiando modelo

            if pasta_esta_aberta("4 Adianto de novas edições"):
                abrir_pasta(CAMINHO_ADIANTO)
            else:
                abrir_pasta(CAMINHO_ADIANTO)
            criar_pasta(f"{ed.replace('.', '')} - {formatar_data(data, tipo='dia_semana')}")
            time.sleep(0.4)
            pg.hotkey('ctrl', 'l')
            kb.write(modelo_path)
            pg.press('enter')
            copiar_modelo_para_pasta(ed, formatar_data(data, tipo='dia_semana'))
            voltar_pasta()
            time.sleep(0.3)

            # -------------------------------------------------------------------------Aplicando autodata
            abrir_software(1)
            selecionar_ferramenta("v")
            autodata_edicao_17(**info) #prepara o local no quark
            autodata_paginas(**info)
            autodata_edicao_1(**info)
            abrir_software(4)
                                 
            print(f"📦 {ed} - {data_formatada}")
            data += timedelta(days=1)
            data = ajustar_data(data)
        edicao += quantidade_por_semana + 2

if __name__ == "__main__":
    main()