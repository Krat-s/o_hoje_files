import keyboard as kb
import time
import pyautogui as pg
import csv

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

# Lendo e-mails do CSV
emails = []
with open("emails.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor, None)  # Ignorar cabeçalho, caso exista
    for linha in leitor:
        emails.append(linha[1])  # Pegando apenas a coluna de e-mail

# Exemplo de uso
numero_inicial = 6710
quantidade_semanal = 3

edicoes_geradas = gerar_edicoes(numero_inicial, quantidade_semanal)

for edicao in edicoes_geradas:
    pg.press('c')  
    time.sleep(1)  # Atalho para abrir menu de mensagem no Gmail
    pg.hotkey('ctrl', 'shift', 'b')  # Atalho para abrir menu de contatos em sigilo

    # Adicionando os e-mails automaticamente
    for email in emails:
        kb.write(email + "; ")  # Adiciona os e-mails separados por ponto e vírgula
    pg.press('enter')

    # Adicionando a mensagem com a edição
    pg.press('tab')  
    time.sleep(0.3)
    kb.write(f"Segue PDF completo da edição {edicao} do jornal O Hoje")
    pg.press('enter')
    pg.press('esc')