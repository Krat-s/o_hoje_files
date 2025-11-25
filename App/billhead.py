import os
import sys
import time
import pyautogui as pg
import keyboard as kb
from dataclasses import dataclass

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as desync

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True

# ---------------------------- DATA CLASS ----------------------------
@dataclass
class EdicaoInfo:
    edicao_formatada: str
    data_formatada: str
    dia_semana: str

# ---------------------------- EXPLORADOR DE ARQUIVOS ----------------------------
def copiar_modelo_para_pasta(caminho, pasta_nome, de=None):
    if de:
        utl.go_to(de)
    time.sleep(2)
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'a')
    time.sleep(1)
    pg.hotkey('ctrl', 'c')
    # utl.safe_copy()
    # if not utl.safe_copy():
    #     raise Exception("Falha ao copiar arquivos — p\\192.168.1.249\redacao\arte\00 Pagflipasta vazia ou nada selecionado.")
    utl.go_to(f"{caminho}\\{pasta_nome}")
    pg.hotkey('ctrl', 'v')
    time.sleep(2)

# ---------------------------- FUNÇÕES UTILITÁRIAS (QUARK) ----------------------------
def preencher_data(info: EdicaoInfo):
    utl.take_tool("v")
    pg.click(cfg.x_data, cfg.y_data)
    utl.take_tool("t")
    utl.press_repeat('t', 2)
    time.sleep(0.4)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.4)
    kb.write(info.data_formatada)

def aplicar_autodata(numero, info: EdicaoInfo):
    utl.press_repeat('esc', 3)
    pg.hotkey('ctrl', 'o')

    nome_pasta = f"{info.edicao_formatada.replace('.', '')} - {info.dia_semana}"
    kb.write(f"{cfg.CAMINHO_MODELO_EDD}\\{nome_pasta}")
    pg.press('enter')
    pg.write(str(numero))
    utl.chose_suggestion(1, cfg.TIMETOOPEN)
    preencher_data(info)


# ---------------------------- AUTODATA ----------------------------
def autodata_paginas(info: EdicaoInfo):
    for i in range(20, 1, -1):
        if i in [17, 18, 19]:
            continue
        aplicar_autodata(i, info)
        utl.close_page()

def autodata_edicao_1(info: EdicaoInfo):
    utl.press_repeat('esc', 3)
    pg.hotkey('ctrl', 'o')
    pg.write('1')
    utl.chose_suggestion(1, 3)
    utl.take_tool("v")
    pg.click(cfg.x_edicao_capa, cfg.y_edicao_capa)
    utl.take_tool("t")
    utl.press_repeat('t', 4)
    utl.press_repeat('backspace', 5)
    kb.write(f"nº {info.edicao_formatada} ")
    utl.press_repeat('right', 2)
    pg.press('backspace')
    kb.write(f"|  {info.data_formatada}")
    utl.close_page()

def autodata_edicao_17(info: EdicaoInfo):
    utl.press_repeat('esc', 3)
    pg.hotkey('ctrl', '0')
    pg.hotkey('ctrl', 'o')
    time.sleep(0.3)
    kb.write(cfg.CAMINHO_MODELO_EDD + '\\' + f"{info.edicao_formatada.replace('.', '')} - {info.dia_semana}")
    time.sleep(0.3)
    pg.press('enter')
    time.sleep(0.5)
    kb.write('17')
    utl.chose_suggestion(1, 1)
    utl.press_repeat('esc', 3)
    preencher_data(info)
    time.sleep(0.4)
    utl.press_repeat('esc', 3)
    utl.take_tool("v")
    pg.hotkey('ctrl', '0')
    pg.click(cfg.x_edicao_17, cfg.y_edicao_17)
    utl.take_tool("t")
    utl.press_repeat('t', 4)
    pg.hotkey('ctrl', 'a')
    kb.write(f"Ano 21 - nº {info.edicao_formatada}")
    utl.close_page()


# ---------------------------- PASTAS ----------------------------
def open_main_folder():
    if utl.folder_is_open("4 Adianto de novas edições"):
        utl.open_folder(cfg.CAMINHO_MODELO_EDD)
        utl.go_to(cfg.CAMINHO_PAGFLIP)
    elif utl.folder_is_open("fotos"):
        utl.open_folder(cfg.CAMINHO_FOTOS)
        utl.go_to(cfg.CAMINHO_PAGFLIP)
    elif utl.folder_is_open("00 Pagflip"):
        utl.open_folder(cfg.CAMINHO_PAGFLIP)
    else:
        utl.open_folder(cfg.CAMINHO_PAGFLIP)

def auto_folders(pasta_nome, modelo_path):
    try:
        open_main_folder()
        utl.make_folder(pasta_nome)
        utl.make_folder(pasta_nome, cfg.CAMINHO_WEB)
        utl.make_folder(pasta_nome, cfg.CAMINHO_FOTOS)
        utl.make_folder(pasta_nome, cfg.CAMINHO_MODELO_EDD)
        copiar_modelo_para_pasta(cfg.CAMINHO_WEB, pasta_nome, cfg.CAMINHO_MODELO_WEB)
        copiar_modelo_para_pasta(cfg.CAMINHO_MODELO_EDD, pasta_nome, modelo_path)
        pg.hotkey('alt', 'up')
        utl.log("billhead-auto_folder", "sucesso", f"Pasta {pasta_nome} criada")
    except Exception as e:
        utl.log("billhead-auto_folder", "ERRO", f"Erro ao criar pasta: {str(e)}")


# ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------
def auto_billhead():
    for item in desync.gerar_edicoes_formatadas():
        try:
            info = EdicaoInfo(
                edicao_formatada=item["edicao_formatada"],
                data_formatada=item["data_formatada"],
                dia_semana=item["dia_semana"],
            )

            weekday = item["dia_semana_padrão"]
            pasta_nome = item["pasta_nome"]

            modelo_path = {
                0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
                5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
            }.get(
                weekday,
                r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição'
            )

            # Criando modelo de pastas
            auto_folders(pasta_nome, modelo_path)

            # ------------------ Aplicando autodata no Quark
            utl.open_software(cfg.quark)
            utl.take_tool("v")

            autodata_edicao_17(info)
            autodata_paginas(info)
            autodata_edicao_1(info)

            utl.log("billhead", "sucesso",
                    f"Modelos da edição {info.edicao_formatada}, {info.dia_semana} criado")

        except Exception as e:
            utl.log(
                "billhead",
                "erro",
                f"Modelos da edição {item['edicao_formatada']}, {item['dia_semana']} não criado. {str(e)}"
            )


if __name__ == "__main__":
    time.sleep(2)
    print('hello')
    auto_billhead()
