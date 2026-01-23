import os
import sys
import time
import pyautogui as pg

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as desync
from App.billhead import aply_17, aply_1, auto_date_all_non_especial_pages
from Global.FileManager import auto_folders
from Global.data_formatador import formatar_data
from Global.Logs.logs import log

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True

# ---------------------------- vari ----------------------------
target = 8000
target_data = desync.obter_data_formatada(target)
target_weekday = formatar_data(desync.obter_data_por_edicao(target), tipo="dia_semana")
pasta_nome = str(f"{target} - {target_weekday}")
target_weekday_standard = desync.obter_data_por_edicao(target).weekday()

# ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------

def auto_billhead_edition():
    try:
        info = desync.formatar_edicao_unica(target)
        modelo_path = {
            0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
            5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
        }.get(
            info.dia_semana_padrão,
            r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição'
        )

        auto_folders(info.pasta_nome, modelo_path)
        time.sleep(1)
        utl.open_software(cfg.quark)
        aply_17(info)
        auto_date_all_non_especial_pages(info)
        aply_1(info)

        log("billhead", "sucesso", f"Modelos da edição {info.edicao_formatada} - {info.dia_semana} criado")
        log("All_in_one", "sucesso", f"Modelos da edição {info.edicao_formatada} - {info.dia_semana} criado")
        pg.alert("Automação encerrada")

    except Exception as e:
        log("billhead", "erro", f"Modelos da edição {info.edicao_formatada} - {info.dia_semana} não criado. {str(e)}")
        log("All_in_one", "erro", f"Modelos da edição {info.edicao_formatada} - {info.dia_semana} não criado. {str(e)}")

if __name__ == "__main__":
    auto_billhead_edition()