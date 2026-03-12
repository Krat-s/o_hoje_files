import pyautogui as pg
import time
import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Global.utils import open_software
from Tasks.modulos_tasks import index_numbers as ni

time.sleep(1)
pg.PAUSE = 0.3 
pg.FAILSAFE = True

edicao_inicial = 36500
quantidade_de_numeros = 5


def vigencia(dia):
    open_software(5)
    for i in range (25):
        pg.write(str(dia))
        pg.press("tab")


def pedidos():
    ni.gerar_n(36400)


if __name__ == "__main__":
    print(ni.gerar_n(37000))

##ainda trabalhando em um relatório para o comercial, preciso gerar números e linkar as informações com o banco de dados --- preciso de acesso ao banco de dados para isso, e também preciso de um modelo do relatório para saber quais informações precisam ser linkadas.

