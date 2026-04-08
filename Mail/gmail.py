import os
import sys
import time
import keyboard as kb
import pyautogui as pg

raiz_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_path)

import Global.settings.settings as cfg
import Global.utils as ut
import Global.data_edition_sync as desync
from Global.Logs.logs import log

# ------------------------------------------------------------------------- Settings
pg.PAUSE = 0.7
pg.FAILSAFE = True

# ------------------------------------------------------------------------- Functions 
def take_receivers():
    """Capture emails from a file in VSCode"""
    try:
        ut.open_software(cfg.vscode)  # Check if it's the right app (VSCode)
        time.sleep(1.2)
        pg.click(cfg.center_x, cfg.center_y)
        pg.hotkey('ctrl', 'o')
        pg.write('archives')
        pg.press('down')
        pg.press('enter')
        pg.write('emails_alterado')
        pg.press('down')
        pg.press('enter')
        time.sleep(0.5)
        pg.click(cfg.center_x, cfg.center_y)
        pg.hotkey('ctrl', 'a')
        pg.hotkey('ctrl', 'c')
        time.sleep(0.5)
        pg.hotkey('ctrl', 'f4')
        
        log("All_in_one", "SUCESSO", "Emails copiados")
        log("gmail", "SUCESSO", "Emails copiados")

    except Exception as e:
        erro_msg = f"Falha ao pegar emails: {str(e)}"
        log("All_in_one", "ERRO", erro_msg)
        log("gmail", "ERRO", erro_msg)


def shortcut_send_emails():
    """Atalho para abrir campo de envio no Gmail"""
    pg.press('esc')
    pg.press('c')  # Abrir menu de mensagem
    time.sleep(1.5)
    pg.hotkey('ctrl', 'shift', 'b')
    time.sleep(0.5)


def send_emails_to_readers(edicao):
    """Simula envio de emails com conteúdo da edição"""
    try:    
        shortcut_send_emails()
        pg.hotkey('ctrl', 'v')
        time.sleep(0.9)  
        pg.press('tab')
        time.sleep(0.3)  
        kb.write(f"Segue edição {edicao} do jornal O Hoje")
        pg.press('esc')
        time.sleep(1)

        log("All_in_one", "SUCESSO", "Rascunhos para leitore criados")
        log("gmail", "SUCESSO", "Rascunhos para leitores criados")

    except Exception as e:
        erro_msg = f"Falha ao criar rascunhos para leitores: {str(e)}"
        log("All_in_one", "ERRO", erro_msg)
        log("gmail", "ERRO", erro_msg)


def send_for_graphic(edicao, parte):
    """Simula envio para gráfica com parte específica da edição"""
    try: 
        pg.press('c')
        shortcut_send_emails()
        kb.write('contas')
        pg.press('enter')
        pg.write('grafica')
        pg.press('enter')
        time.sleep(0.3)
        pg.press('tab')
        kb.write(f"Segue {parte} da edição {edicao}")
        pg.press('esc')
        time.sleep(1)

        log("All_in_one", "SUCESSO", "Rascunhos para gráfica criados")
        log("gmail", "SUCESSO", "Rascunhos para gráfica criados")

    except Exception as e:
        erro_msg = f"Falha ao criar rascunhos da gráfica: {str(e)}"
        log("All_in_one", "ERRO", erro_msg)
        log("gmail", "ERRO", erro_msg)


def auto_drafts(ed=None, qnt=None):
    take_receivers()
    ut.open_software(cfg.opera)

    if ed is None or qnt is None:
        for info in desync.gerar_edicoes_formatadas():
            ed = info.edicao_formatada
            send_for_graphic(ed, "básico")
            send_for_graphic(ed, "resto")
            send_emails_to_readers(ed)
            time.sleep(1)

    else:
        for info in desync.gerar_edicoes_formatadas(ed, qnt):

            ed = info.edicao_formatada
            send_for_graphic(ed, "básico")
            send_for_graphic(ed, "resto")
            send_emails_to_readers(ed)
            time.sleep(1)