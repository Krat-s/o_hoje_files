import os
import time
import locale
from datetime import datetime, timedelta
import pyautogui as pg
import keyboard as kb
from Modulos_quark.data_formatador import formatar_data
from Modulos_quark.edicao_formatador import gerar_edicoes
from Modulos_quark.explorer_utils import verificar_windows 
from pywinauto import Desktop
import Modulos_quark.config as cg

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True
time.sleep(1)

locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")
SISTEMA_OPERACIONAL = verificar_windows()

screen_width, screen_height = pg.size()
center_x = screen_width / 2
center_y = screen_height / 2

edicao_inicial = 8888
quantidade_por_semana = 5
quantidade_repeticoes = 1
data_inicial = datetime(2025, 7, 21) #Precisa ser uma segunda-feira

# ---------------------------- POSIÇÕES DE CLIQUE ----------------------------
# marketing
# x_data = 49.48
# y_data = 23.06
# x_edicao_17 = 44.17
# y_edicao_17 = 12.41
# x_edicao_capa = 13.91
# y_edicao_capa = 41.30

# comercial-3 1366, 768
x_data = 68.45
y_data = 33.20
x_edicao_17 = 41.14
y_edicao_17 = 15.40
x_edicao_capa = 18.74
y_edicao_capa = 58.07

# ---------------------------- FUNÇÕES UTILITÁRIAS ----------------------------
def log(mensagem): 
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {mensagem}")

def atalho_endereço():
    windows = SISTEMA_OPERACIONAL
    return ('ctrl', 'l') if "Windows 11" in windows else ('ctrl', 'd')

def ir_para(específico=None):
    pg.hotkey(*atalho_endereço())
    time.sleep(0.2)
    if específico:
        kb.write(específico) 
    pg.press('enter')
    time.sleep(0.2)

def ajustar_data(data):
    return data + timedelta(days=1) if data.weekday() == 6 else data

def click(x_percent, y_percent):
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

# ---------------------------- EXPLORADOR DE ARQUIVOS ----------------------------
def pasta_esta_aberta(*nomes):
    janelas = Desktop(backend="uia").windows()
    for janela in janelas:
        if janela.class_name() == "CabinetWClass":
            titulo = janela.window_text().lower()
            for nome in nomes:
                if nome.lower() in titulo:
                    return True
    return False

def criar_pasta(nome, em=None):
    if em:
        ir_para(em)
    time.sleep(0.3)
    maximizar_janela()
    time.sleep(0.3)
    pg.click(center_x, center_y)
    pg.hotkey('ctrl', 'shift', 'n')
    time.sleep(0.3)
    kb.write(nome)
    pg.press('enter')
    time.sleep(0.3)

def copiar_modelo_para_pasta(caminho, ed, data_formatada, de=None):
    if de:
        ir_para(de)
    nome_pasta = f"{ed.replace('.', '')} - {data_formatada}"
    pg.click(center_x, center_y)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    time.sleep(0.2)
    ir_para(f"{caminho}\\{nome_pasta}")
    pg.hotkey('ctrl', 'v')
    time.sleep(0.2)

def abrir_pasta(endereco):
    os.startfile(endereco)
    maximizar_janela()
    pg.click(center_x, center_y)

# ---------------------------- FUNÇÕES UTILITÁRIAS (QUARK)----------------------------
def abrir_sugestão():
    time.sleep(0.2)
    pg.press('down')
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(cg.TEMPO_ABERTURA)

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
    kb.write(f"{cg.CAMINHO_ADIANTO}\\{nome_pasta}")
    pg.press('enter')
    pg.write(str(numero))
    abrir_sugestão()
    preencher_data(data_formatada)

def fechar_pagina():
    pg.press('esc', presses=3)
    time.sleep(0.2)
    pg.hotkey('ctrl', 's')
    time.sleep(0.2)
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'f4')
    time.sleep(cg.TEMPO_FECHAMENTO)

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
    abrir_sugestão()
    time.sleep(3)
    selecionar_ferramenta("v")
    click(x_edicao_capa, y_edicao_capa)
    selecionar_ferramenta("t")
    pg.press('t', presses=4)
    pg.press('backspace', presses=5)
    kb.write(f"nº {edicao_formatada} ")
    pg.press('right', presses=2)
    pg.press('backspace')
    kb.write(f"|  {data_formatada}")
    fechar_pagina()

def autodata_edicao_17(edicao_formatada, data_formatada, dia_semana):
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', '0')
    pg.hotkey('ctrl', 'o')
    time.sleep(0.3)
    kb.write(cg.CAMINHO_ADIANTO + '\\' + f"{edicao_formatada.replace('.', '')} - {dia_semana}")
    pg.press('enter')
    time.sleep(0.5)
    kb.write('17')
    abrir_sugestão()
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
    fechar_pagina()

# ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------
def Modelo_diário():
    log(f"📦 Gerando edições...")
    edicao = edicao_inicial
    data = data_inicial
    
    for _ in range(quantidade_repeticoes):
        edicoes = gerar_edicoes(edicao, quantidade_por_semana)

        for ed in edicoes:
            dia_semana = formatar_data(data, tipo='dia_semana')
            pasta_nome = f"{ed.replace('.', '')} - {dia_semana}"
            info = {
            "edicao_formatada": ed,
            "data_formatada": formatar_data(data),
            "dia_semana": formatar_data(data, tipo='dia_semana')
            }
            modelo_path = {
            0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
            5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
            }.get(data.weekday(), r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição')

            # ---------------CRIANDO PASTAS, COPIANDO MODELOS E APLICANDO CABEÇALHO--------
            if pasta_esta_aberta("4 Adianto de novas edições"):
                abrir_pasta(cg.CAMINHO_ADIANTO)
                ir_para(cg.CAMINHO_PAGFLIP)
            elif pasta_esta_aberta("00 Pagflip"):
                abrir_pasta(cg.CAMINHO_PAGFLIP)
            else:
                abrir_pasta(cg.CAMINHO_PAGFLIP)
            criar_pasta(pasta_nome)
            criar_pasta(pasta_nome, cg.CAMINHO_WEB)
            copiar_modelo_para_pasta(cg.CAMINHO_WEB, ed, dia_semana, cg.CAMINHO_MODELO_WEB)
            criar_pasta(pasta_nome, cg.CAMINHO_FOTOS)
            criar_pasta(pasta_nome, cg.CAMINHO_ADIANTO)
            copiar_modelo_para_pasta(cg.CAMINHO_ADIANTO, ed, dia_semana, modelo_path)
            pg.hotkey('alt', 'up')

            # -------------------------------------------------------------------------Aplicando autodata
            abrir_software(1)
            selecionar_ferramenta("v")
            autodata_edicao_17(**info) #prepara o local no quark
            autodata_paginas(**info)
            autodata_edicao_1(**info)
                                       
            log(f"📦 Edição {ed} gerada com sucesso.")
            data += timedelta(days=1)
            data = ajustar_data(data)
        edicao += quantidade_por_semana + 2

if __name__ == "__main__":
    Modelo_diário()