import os
import sys

import pyautogui as pg
import time

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

from Global.wait import wait_until
from pywinauto import Desktop


pg.PAUSE = 0.5
pg.FAILSAFE = True


def wait_explorer_open(min=0.3, timeout=10):
    '''Espera até que o Explorador de Arquivos esteja aberto. Retorna True se aberto, False se timeout.'''
    time.sleep(min)
    return wait_until(
        lambda: any(
            w.class_name() == "CabinetWClass"
            for w in Desktop(backend="uia").windows()
        ), 
        condition="'Explorador open'",
        timeout=timeout
    )


def wait_folder_open(nome_pasta, timeout=10):
    '''Espera até que uma pasta específica esteja aberta no Explorador de Arquivos. Retorna True se aberto, False se timeout.'''
    nome = nome_pasta.lower()
    time.sleep(0.3)
    return wait_until(
        lambda: any(
            nome in w.window_text().lower()
            for w in Desktop(backend="uia").windows()
            if w.class_name() == "CabinetWClass"
        ), 
        condition="'Specific folder is open'",
        timeout=timeout
    )


def wait_file(path, timeout=10):
    '''Espera até que um arquivo exista no caminho especificado dentro do timeout. Retorna True se encontrado, False se timeout.'''
    return wait_until(
        lambda: os.path.exists(path), 
        condition="'File exists'",
        timeout=timeout
    )


def wait_image(image_path, region=None, timeout=10, confidence=0.9):
    '''Espera até que a imagem apareça na tela dentro do timeout. Retorna True se encontrada, False se timeout.'''
    return wait_until(
        lambda: pg.locateOnScreen(image_path, region=region, confidence=confidence) is not None,
        condition="'Image found'",
        timeout=timeout
    )


#-------------------logic status waits
# def wait_quark_ready():
#     return wait_until(
#         lambda: not kb.is_pressed('esc'),
#         condition="'Quark is ready'",
#         timeout=5
#     )


if __name__ == "__main__":
    print('Waits_checks module test')
    wait_explorer_open()
    # wait_text_visible('PERA')