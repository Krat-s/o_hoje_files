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
import Global.utils as utl
import Global.data_edition_sync as desync

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True

# ---------------------------- EXPLORADOR DE ARQUIVOS ----------------------------
def copiar_modelo_para_pasta(caminho, pasta_nome, de=None):
    if de:
        utl.ir_para(de)
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    time.sleep(0.2)
    utl.ir_para(f"{caminho}\\{pasta_nome}")
    pg.hotkey('ctrl', 'v')
    time.sleep(1)

# ---------------------------- FUNÇÕES UTILITÁRIAS (QUARK)----------------------------
def preencher_data(data_formatada):
    utl.take_tool("v")
    pg.click(cfg.x_data, cfg.y_data)
    utl.take_tool("t")
    utl.press_repeat('t', 2)
    time.sleep(0.4)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.4)
    kb.write(data_formatada)

def aplicar_autodata(numero, edicao_formatada, dia_semana, data_formatada):
    utl.press_repeat('esc', 3)
    pg.hotkey('ctrl', 'o')
    nome_pasta = f"{edicao_formatada.replace('.', '')} - {dia_semana}"
    kb.write(f"{cfg.CAMINHO_MODELO_EDD}\\{nome_pasta}")
    pg.press('enter')
    pg.write(str(numero))
    utl.chose_suggestion(1, cfg.TIMETOOPEN)
    preencher_data(data_formatada)

# ---------------------------- AUTODATA ----------------------------
def autodata_paginas(edicao_formatada, dia_semana, data_formatada):
    for i in range(20, 1, -1):
        if i in [17, 18, 19]:
            continue
        else:
            aplicar_autodata(i, edicao_formatada, dia_semana, data_formatada)
            utl.close_page()
           
def autodata_edicao_1(edicao_formatada, data_formatada, dia_semana=None):
    utl.press_repeat('esc', 3)
    pg.hotkey('ctrl', 'o')
    pg.write('1')
    utl.chose_suggestion(1, 3)
    utl.take_tool("v")
    pg.click(cfg.x_edicao_capa, cfg.y_edicao_capa)
    utl.take_tool("t")
    utl.press_repeat('t', 4)
    utl.press_repeat('backspace', 5)
    kb.write(f"nº {edicao_formatada} ")
    utl.press_repeat('right', 2)
    pg.press('backspace')
    kb.write(f"|  {data_formatada}")
    utl.close_page()

def autodata_edicao_17(edicao_formatada, data_formatada, dia_semana):
    utl.press_repeat('esc', 3)
    pg.hotkey('ctrl', '0')
    pg.hotkey('ctrl', 'o')
    time.sleep(0.3)
    kb.write(cfg.CAMINHO_MODELO_EDD + '\\' + f"{edicao_formatada.replace('.', '')} - {dia_semana}")
    time.sleep(0.3)
    pg.press('enter')
    time.sleep(0.5)
    kb.write('17')
    utl.chose_suggestion(1, 1)
    utl.press_repeat('esc', 3)
    preencher_data(data_formatada)
    time.sleep(0.4)
    utl.press_repeat('esc', 3)
    utl.take_tool("v")
    pg.hotkey('ctrl', '0')
    pg.click(cfg.x_edicao_17, cfg.y_edicao_17)
    utl.take_tool("t")
    utl.press_repeat('t', 4)
    pg.hotkey('ctrl', 'a')
    kb.write(f"Ano 21 - nº {edicao_formatada}")
    utl.close_page()

def abrir_janela_unica():
    if utl.folder_is_open("4 Adianto de novas edições"):
        utl.abrir_pasta(cfg.CAMINHO_MODELO_EDD)
        utl.ir_para(cfg.CAMINHO_PAGFLIP)
    elif utl.folder_is_open("fotos"):
        utl.abrir_pasta(cfg.CAMINHO_FOTOS)
        utl.ir_para(cfg.CAMINHO_PAGFLIP)
    elif utl.folder_is_open("00 Pagflip"):
        utl.abrir_pasta(cfg.CAMINHO_PAGFLIP)
    else:
        utl.abrir_pasta(cfg.CAMINHO_PAGFLIP)
    
def auto_pastas(pasta_nome, modelo_path):
    try:
        abrir_janela_unica()
        utl.criar_pasta(pasta_nome)
        utl.criar_pasta(pasta_nome, cfg.CAMINHO_WEB)
        copiar_modelo_para_pasta(cfg.CAMINHO_WEB, pasta_nome, cfg.CAMINHO_MODELO_WEB)
        utl.criar_pasta(pasta_nome, cfg.CAMINHO_FOTOS)
        utl.criar_pasta(pasta_nome, cfg.CAMINHO_MODELO_EDD)
        copiar_modelo_para_pasta(cfg.CAMINHO_MODELO_EDD, pasta_nome, modelo_path)
        pg.hotkey('alt', 'up')
        utl.log(str("billhead-auto_folder"), "sucesso", f"Pasta {pasta_nome} criada")
    except Exception as e:
        erro_msg = f"Erro ao criar pasta: {str(e)}"
        utl.log(str("billhead-auto_folder"), "ERRO", erro_msg)

# ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------
def auto_billhead():
    for item in desync.gerar_edicoes_formatadas():
        try:
        #     #----------------------------------------📌verificar se existe uma forma melhor de chamar as variaveis
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
                "dia_semana": dia_semana,
                "data_formatada": data_formatada,
                }
            
            # ---------------CRIANDO PASTAS, COPIANDO MODELOS E APLICANDO CABEÇALHO--------
            auto_pastas(pasta_nome, modelo_path)

            # -------------------------------------------------------------------------Aplicando autodata
            utl.open_software(cfg.quark)
            utl.take_tool("v")
            autodata_edicao_17(**info) #prepara o local no quark
            autodata_paginas(**info)
            autodata_edicao_1(**info)               
            
            utl.log(str("billhead"), "sucesso", f"Modelos da edição {ed}, {dia_semana} criado")    
        except Exception as e:
            erro_msg = f"Erro: {str(e)}"
            utl.log(str("billhead"), "erro", f"Modelos da edição {ed}, {dia_semana} não criado. {erro_msg}")      

if __name__ == "__main__":
    time.sleep(1)
    print('hello')
    auto_billhead()