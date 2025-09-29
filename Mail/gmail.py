import time
import keyboard as kb
import pyautogui as pg
from Modulos_gmail.edicao_formatador import gerar_edicoes
import os
import sys

raiz_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_path)

import Global.settings as cg
import Global.utils as ut

# ------------------------------------------------------------------------- CONFIGURAÇÕES
pg.PAUSE = 0.4
pg.FAILSAFE = True
time.sleep(1)

# ------------------------------------------------------------------------- FUNÇÕES DE AUTOMAÇÃO 
def take_emails():
    """Captura os emails de um arquivo no VSCode"""
    pg.hotkey('win', 's')
    pg.hotkey('win', '3')  # Verificar se é o app certo (VSCode)
    pg.click(cg.center_x, cg.center_y)
    time.sleep(0.3)
    pg.hotkey('ctrl', 'o')
    time.sleep(0.3)
    pg.write('ar')
    time.sleep(0.3)
    pg.press('down')
    time.sleep(0.3)
    pg.press('enter')
    pg.write('ema')
    pg.press('down')
    pg.press('enter')
    time.sleep(0.5)
    pg.click(cg.center_x, cg.center_y)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    time.sleep(0.5)
    pg.hotkey('ctrl', 'f4')

def shortcut_send_emails():
    """Atalho para abrir campo de envio no Gmail"""
    pg.press('esc')
    pg.press('c')  # Abrir menu de mensagem
    time.sleep(1.5)
    pg.hotkey('ctrl', 'shift', 'b')
    time.sleep(0.5)

def enviar_emails_para_leitores(edicao):
    """Simula envio de emails com conteúdo da edição"""
    shortcut_send_emails()
    pg.hotkey('ctrl', 'v') # Cola emails
    time.sleep(0.3)  
    pg.press('tab')
    time.sleep(0.3)  
    kb.write(f"Segue edição {edicao} do jornal O Hoje")
    pg.press('esc')
    time.sleep(1)

def enviar_para_grafica(edicao, parte):
    """Simula envio para gráfica com parte específica da edição"""
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

# ------------------------------------------------------------------------- ROTINA PRINCIPAL

def create_draft():
    print("📦 Edições geradas:")
    edicao = cg.edicao_inicial
   
    for _ in range(cg.quantidade_repeticoes):
        edicoes = gerar_edicoes(edicao, cg.quantidade_por_semana)

        for ed in edicoes:
            enviar_para_grafica(ed, "básico")
            enviar_para_grafica(ed, "resto")
            enviar_emails_para_leitores(ed)
            # print(f"→ {ed}")

        edicao += cg.quantidade_por_semana + 2

def create_drafts():
    take_emails()
    ut.open_software(2) #Abrindo Gmail -- ATENÇÃO -- Verificar se está na aba certa do navegador
    create_draft()

if __name__ == "__main__":
    print("teste")
    create_drafts()