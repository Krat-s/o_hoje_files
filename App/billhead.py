import os
import sys
import pyautogui as pg
from dataclasses import dataclass
import time

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as desync
from Global.Logs.logs import log
from Global.FileManager import copy_files, make_folder, open_folder, folder_is_open, go_to
from App.modulos_quark.utils_quark import take_tool
from billhead_one import aply_17, aply_1, auto_pages

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True

# ---------------------------- DATA CLASS ----------------------------
@dataclass
class EdicaoInfo:
    edicao_formatada: str
    data_formatada: str
    dia_semana: str

# ---------------------------- AUTODATA ----------------------------
def autodata_paginas(info: EdicaoInfo):
    for i in range(20, 1, -1):
        if i in [17, 18, 19]:
            continue
        auto_pages(i, info)
        utl.close_page()

# ---------------------------- PASTAS ----------------------------
def open_main_folder():
    if folder_is_open("4 Adianto de novas edições"):
        open_folder(cfg.CAMINHO_MODELO_EDD)
        go_to(cfg.CAMINHO_PAGFLIP)
    elif folder_is_open("fotos"):
        open_folder(cfg.CAMINHO_FOTOS)
        go_to(cfg.CAMINHO_PAGFLIP)
    elif folder_is_open("00 Pagflip"):
        open_folder(cfg.CAMINHO_PAGFLIP)
    else:
        open_folder(cfg.CAMINHO_PAGFLIP)

def auto_folders(pasta_nome, modelo_path):
    try:
        open_main_folder()
        # make_folder(pasta_nome)
        # make_folder(pasta_nome, cfg.CAMINHO_WEB)
        # make_folder(pasta_nome, cfg.CAMINHO_FOTOS)
        make_folder(pasta_nome, cfg.CAMINHO_MODELO_EDD)
        time.sleep(1)

        # copy_files(cfg.CAMINHO_WEB, pasta_nome, cfg.CAMINHO_MODELO_WEB)
        time.sleep(1)
        copy_files(cfg.CAMINHO_MODELO_EDD, pasta_nome, modelo_path)
        pg.hotkey('alt', 'up')
        log("billhead-auto_folder", "sucesso", f"Pasta {pasta_nome} criada")
    except Exception as e:
        log("billhead-auto_folder", "ERRO", f"Erro ao criar pasta: {str(e)}")


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

            # Criando pastas e copiando
            auto_folders(pasta_nome, modelo_path)

            # ------------------ Aplicando autodata no Quark
            utl.open_software(cfg.quark)
            take_tool("v")

            aply_17(info)
            auto_pages(info)
            aply_1(info)
            # print(info.data_formatada)

            log("billhead", "sucesso", 
                    f"Modelos da edição {info.edicao_formatada}, {info.dia_semana} criado")

        except Exception as e:
            log(
                "billhead",
                "erro",
                f"Modelos da edição {item['edicao_formatada']}, {item['dia_semana']} não criado. {str(e)}"
            )


# def teste(info: EdicaoInfo):
#     for i in range(20, 1, -1):
#         if i in [17, 18, 19]:
#             continue
#         print(info)


if __name__ == "__main__":
    # time.sleep(2)
    # print('hello')
    # auto_billhead()
    auto_billhead()



##FIX COPY FILES