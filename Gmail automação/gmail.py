import keyboard as kb
import time
import pyautogui as pg
from datetime import timedelta

pg.PAUSE = 0.3
pg.FAILSAFE = True

time.sleep(1)

largura, altura = pg.size()
centro_x = largura / 2
centro_y = altura / 2

EDICAO_DE_INICIO = 6794

quantidade_semanal = 5  # Número de edições por semana 5
quantidade_repeticoes = 2  # quantidade de semanas que vai repetir o ciclo

# ----------------------------------------------------- Functions
def take_emails():
    pg.hotkey('win', 's')
    pg.hotkey('win', '3') #verificar se é o app certo (VScode)
    pg.hotkey('ctrl', 'o')
    pg.write('ar')
    pg.press('down')
    pg.press('enter')
    pg.write('ema')
    pg.press('down')
    pg.press('enter')
    time.sleep(0.5)
    pg.click(y=centro_y, x=centro_x)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    time.sleep(0.5)
 
def Shortcut_send_emails():
    pg.press('esc')
    pg.press('c')  # Atalho para abrir menu de mensagem no Gmail
    time.sleep(1.5)  
    pg.hotkey('ctrl', 'shift', 'b')
    time.sleep(0.5)

def open_gmail():
    pg.hotkey('win', 's')
    pg.hotkey('win', '2') #verificar se é o app e página certo (Navegador - Gmail)
    time.sleep(0.5)

def gerar_edicoes(inicial, quantidade):
    edicoes = []
    for _ in range(quantidade_semanal):
        edicoes.append(str(inicial))
        inicial += 1
    
    edicoes.append(f"{int(inicial):,}-{int(inicial+1):,}".replace(',', '.'))
    return edicoes

# take_emails()
for _ in range(quantidade_repeticoes):
    edicoes_geradas = gerar_edicoes(EDICAO_DE_INICIO, quantidade_semanal)
    
    for edicao in edicoes_geradas:
        inical = int(edicao)
        # open_gmail()
        # pg.press('c')  # Cola os emails copiados
        # Shortcut_send_emails()
        # pg.hotkey('ctrl', 'v')  # Cola os emails copiados
        # pg.press('tab')  
        # kb.write(f"Segue PDF completo da edição {edicao} do jornal O Hoje")
        # pg.press('esc')
        # time.sleep(1)

        # # ----------------------------------------------------- Para a Gráfica
        # pg.press('c')
        # Shortcut_send_emails()
        # kb.write('contas')
        # pg.press('enter')
        # pg.write('grafica')
        # pg.press('enter')
        # time.sleep(0.3)
        # pg.press('tab')  
        # kb.write(f"Segue essência e classificados da edição {edicao} do jornal O Hoje")
        # pg.press('esc')
        # time.sleep(1)
        # Shortcut_send_emails()
        # kb.write('contas')
        # pg.press('enter')
        # pg.write('grafica')
        # pg.press('enter')
        # time.sleep(0.3)
        # pg.press('tab')  
        # kb.write(f"Segue resto da edição {edicao} do jornal O Hoje")
        # pg.press('esc')
        # time.sleep(1)
        print(edicao)

    EDICAO_DE_INICIO += quantidade_semanal + 2