import keyboard as kb
import time
import pyautogui as pg
import pandas as pd


pg.PAUSE = 0.5
pg.FAILSAFE = True

time.sleep(1)

def gerar_edicoes(inicial, quantidade):
    edicoes = []
    
    for _ in range(quantidade):
        edicoes.append(inicial)
        inicial += 1
    edicoes.append(f"{inicial}-{inicial+1}")
    
    return edicoes

# Exemplo de uso
numero_inicial = 6710
quantidade_semanal = 3

edicoes_geradas = gerar_edicoes(numero_inicial, quantidade_semanal)

# pg.hotkey('win', '3')
  
for edicao in edicoes_geradas:
    pg.press('c') 
    time.sleep(1) #atalho para abrir menu de mensagem no gmail
    pg.hotkey('ctrl', 'shift', 'b') #Atalhgo para abrir o menu de contatos em sigilo
    #adicionar emaisl
    pg.press('tab') 
    time.sleep(0.3)
    kb.write('Segue PDF completo da edição ' + (str(edicao)) + ' do jornal O Hoje')
    pg.press('enter')
    pg.press('esc')