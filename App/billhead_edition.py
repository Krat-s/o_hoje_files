import os
import sys
import time
import pyautogui as pg
import keyboard as kb
from dataclasses import dataclass

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

from App.modulos_quark.utils_quark import close_page
import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as desync
from App.billhead import aply_17, aply_1, auto_date_all_non_especial_pages
from Global.FileManager import auto_folders

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True

# ---------------------------- DATA CLASS ----------------------------
target = 6996
target = desync.obter_data_formatada(target)

# ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------
def auto_billhead_edition():
    try:

        # weekday = item["dia_semana_padrão"]
        # pasta_nome = item["pasta_nome"]

        # modelo_path = {
        #     0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
        #     5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
        # }.get(
        #     weekday,
        #     r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição'
        # )

        # # Criando pastas e copiando
        # auto_folders(pasta_nome, modelo_path)
        # time.sleep(1)

        # # ------------------ Aplicando autodata no Quark
        # utl.open_software(cfg.quark)
        
        # aply_17(EdicaoInfo)
        # autodata_paginas(Edi)
        # aply_1(info)
        
        # log("billhead", "sucesso", f"Modelos da edição {info.edicao_formatada}, {info.dia_semana} criado")
        print(target)
    except Exception as e:
        # log("billhead", "erro", f"Modelos da edição {item['edicao_formatada']}, {item['dia_semana']} não criado. {str(e)}")
        print(e)


if __name__ == "__main__":
    auto_billhead_edition()

