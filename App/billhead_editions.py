import os
import sys
import pyautogui as pg
import time

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as desync
from Global.Logs.logs import log
from Global.FileManager import auto_folders
from App.billhead import aply_17, aply_1, auto_date_all_non_especial_pages
from Global.edition_info import EdicaoInfo

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True

# ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------
def auto_billhead_editions():
    for info in desync.gerar_edicoes_formatadas():
        try:
            weekday = info.dia_semana_padrão
            pasta_nome = info.pasta_nome

            modelo_path = {
                0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
                5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
            }.get(
                weekday,
                r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição'
            )
            auto_folders(pasta_nome, modelo_path)
            time.sleep(1)
            
            utl.open_software(cfg.quark)
            aply_17(info)
            auto_date_all_non_especial_pages(info)
            aply_1(info)
            
            log("billhead", "sucesso", f"Modelos da edição {info.edicao_formatada}, {info.dia_semana} criado")

        except Exception as e:
            log("billhead", "erro", f"Modelos da edição {info.edicao_formatada}, {info.dia_semana} não criado. {str(e)}")

if __name__ == "__main__":
    auto_billhead_editions()