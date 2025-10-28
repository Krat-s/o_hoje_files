import os
import sys
import time
from datetime import datetime, timedelta
import pyautogui as pg
import keyboard as kb
from pywinauto import Desktop

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

from App.modulos_quark.data_formatador import formatar_data
from App.modulos_quark.edicao_formatador import gerar_edicoes
import Global.settings as cfg
import Global.utils as ut
import Global.data_edition_sync as desync

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True
time.sleep(1)

# ---------------------------- FUNÇÕES UTILITÁRIAS ----------------------------
ver = "v1.2.1"
def log(mensagem): 
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {mensagem}")

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

def copiar_modelo_para_pasta(caminho, ed, data_formatada, de=None):
    if de:
        ut.ir_para(de)
    nome_pasta = f"{ed.replace('.', '')} - {data_formatada}"
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    time.sleep(0.2)
    ut.ir_para(f"{caminho}\\{nome_pasta}")
    pg.hotkey('ctrl', 'v')
    time.sleep(1)

# ---------------------------- FUNÇÕES UTILITÁRIAS (QUARK)----------------------------
def abrir_sugestão():
    time.sleep(0.2)
    pg.press('down')
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(cfg.TEMPO_ABERTURA)

def selecionar_ferramenta(tecla):
    time.sleep(0.2)
    pg.click(cfg.center_x, 10)   
    time.sleep(0.2)
    pg.press("v")
    kb.press(tecla)

def preencher_data(data_formatada):
    selecionar_ferramenta("v")
    pg.click(cfg.x_data, cfg.y_data)
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
    kb.write(f"{cfg.CAMINHO_MODELO_EDD}\\{nome_pasta}")
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
    time.sleep(cfg.TEMPO_FECHAMENTO)

# ---------------------------- AUTODATA ----------------------------
def autodata_paginas(edicao_formatada, dia_semana, data_formatada):
    for i in range(20, 1, -1):
        if i in [17, 18, 19]:
            continue
        else:
            aplicar_autodata(i, edicao_formatada, dia_semana, data_formatada)
            fechar_pagina()
           
def autodata_edicao_1(edicao_formatada, data_formatada, dia_semana=None):
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'o')
    pg.write('1')
    abrir_sugestão()
    time.sleep(3)
    selecionar_ferramenta("v")
    pg.click(cfg.x_edicao_capa, cfg.y_edicao_capa)
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
    kb.write(cfg.CAMINHO_MODELO_EDD + '\\' + f"{edicao_formatada.replace('.', '')} - {dia_semana}")
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
    pg.click(cfg.x_edicao_17, cfg.y_edicao_17)
    selecionar_ferramenta("t")
    pg.press('t', presses=4)
    pg.hotkey('ctrl', 'a')
    kb.write(f"Ano 21 - nº {edicao_formatada}")
    fechar_pagina()

def abrir_janela_unica():
    if pasta_esta_aberta("4 Adianto de novas edições"):
        ut.abrir_pasta(cfg.CAMINHO_MODELO_EDD)
        ut.ir_para(cfg.CAMINHO_PAGFLIP)
    elif pasta_esta_aberta("fotos"):
        ut.abrir_pasta(cfg.CAMINHO_FOTOS)
        ut.ir_para(cfg.CAMINHO_PAGFLIP)
    elif pasta_esta_aberta("00 Pagflip"):
        ut.abrir_pasta(cfg.CAMINHO_PAGFLIP)
    else:
        ut.abrir_pasta(cfg.CAMINHO_PAGFLIP)
    
def auto_pastas(pasta_nome, ed, dia_semana, modelo_path):
    abrir_janela_unica()
    ut.criar_pasta(pasta_nome)
    ut.criar_pasta(pasta_nome, cfg.CAMINHO_WEB)
    copiar_modelo_para_pasta(cfg.CAMINHO_WEB, ed, dia_semana, cfg.CAMINHO_MODELO_WEB)
    ut.criar_pasta(pasta_nome, cfg.CAMINHO_FOTOS)
    ut.criar_pasta(pasta_nome, cfg.CAMINHO_MODELO_EDD)
    copiar_modelo_para_pasta(cfg.CAMINHO_MODELO_EDD, ed, dia_semana, modelo_path)
    pg.hotkey('alt', 'up')

# ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------
def auto_billhead():
    log(f"📦 Gerando edições ({ver})...")
    for item in desync.gerar_edicoes_formatadas():
        #----------------------------------------📌verificar se existe uma forma melhor de chamar as variaveis
        ed = item["edicao_formatada"]
        data_formatada = item["data_formatada"]
        weekday = item["dia_semana_padrão"]
        dia_semana = item["dia_semana"]
        pasta_nome = item["pasta_nome"]

        modelo_path = {
            0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
            5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
            }.get(weekday, r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição')

        info = {
            "edicao_formatada": ed,
            "data_formatada": data_formatada,
            "dia_semana": dia_semana,
            }
        
        # ---------------CRIANDO PASTAS, COPIANDO MODELOS E APLICANDO CABEÇALHO--------
        auto_pastas(pasta_nome, ed, dia_semana, modelo_path)

        # -------------------------------------------------------------------------Aplicando autodata
        ut.open_software(cfg.quark)
        selecionar_ferramenta("v")
        autodata_edicao_17(**info) #prepara o local no quark
        autodata_paginas(**info)
        autodata_edicao_1(**info)               
        
        log(f"📦 Modelos da edição {ed} gerados. -->> {data_formatada.capitalize()}, {dia_semana}")        

if __name__ == "__main__":
    print('hello')
    auto_cabecalho()