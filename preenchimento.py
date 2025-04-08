import keyboard as kb
import time
import pyautogui as pg
import pandas as pd

pg.PAUSE = 0.5
pg.FAILSAFE = True

time.sleep(1)

# pg.press('win')
# pg.write('Opera GX')
# pg.press('enter')   
# pg.press('c') #atalho para abrir menu de mensagem no gmail
pg.write('Segue PDF completo da edição', 6.722, 'do jornal O Hoje')




flag
import keyboard as kb
import time
import pyautogui as pg


pg.PAUSE = 0.5
pg.FAILSAFE = True

time.sleep(1) 
# NEDICAO = pg.prompt('Qual o número da edição?')

# pg.press('win')
# pg.write('Opera GX')
# pg.press('enter')   
# pg.press('c') #atalho para abrir menu de mensagem no gmail
# kb.write('Segue PDF completo da edição ')
# kb.write(NEDICAO)
# pg.write(' do jornal O Hoje')


# def gerar_edicoes(inicial, quantidade):
#     edicoes = []
    
#     for _ in range(quantidade):
#         edicoes.append(inicial)
#         inicial += 1
    
#     # Junta as edições de fim de semana
#     edicoes.append(f"{inicial}-{inicial+1}")
    
#     return edicoes

# # Exemplo de uso
# numero_inicial = 6710
# quantidade_semanal = 5

# edicoes_geradas = gerar_edicoes(numero_inicial, quantidade_semanal)

# for edicao in edicoes_geradas:
#     print(edicao)



def gerar_edicoes(inicial, quantidade):
    edicoes = []
    
    for _ in range(quantidade):
        edicoes.append(str(inicial))
        inicial += 1
    
    edicoes.append(f"{inicial}-{inicial+1}")
    
    return edicoes

# Exemplo de uso
numero_inicial = 6710
quantidade_semanal = 6

edicoes_geradas = gerar_edicoes(numero_inicial, quantidade_semanal)

# Agora, você pode pegar cada número de edição de forma isolada
for edicao in edicoes_geradas:
    print(f"Edição: {edicao}")

