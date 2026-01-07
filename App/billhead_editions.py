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
from Global.FileManager import auto_folders
from App.modulos_quark.utils_quark import close_page
from App.billhead import aply_17, aply_1, auto_pages

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
        close_page()

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
            time.sleep(1)

            # ------------------ Aplicando autodata no Quark
            utl.open_software(cfg.quark)
            
            aply_17(info)
            autodata_paginas(info)
            aply_1(info)
            
            log("billhead", "sucesso", f"Modelos da edição {info.edicao_formatada}, {info.dia_semana} criado")

        except Exception as e:
            log("billhead", "erro", f"Modelos da edição {item['edicao_formatada']}, {item['dia_semana']} não criado. {str(e)}")

if __name__ == "__main__":
    auto_billhead()

