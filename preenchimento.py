import keyboard as kb
import time
import pyautogui as pg
import csv

pg.PAUSE = 0.3
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
with open("emails_alterado.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        emails.append(linha[0])
        time.sleep(0.2)  # Pegando apenas a coluna de e-mail

# Exemplo de uso
numero_inicial = 6730 
quantidade_semanal = 1

edicoes_geradas = gerar_edicoes(numero_inicial, quantidade_semanal)

pg.hotkey('win', '2')

for edicao in edicoes_geradas:
    pg.press('c')  
    time.sleep(1.5)  # Atalho para abrir menu de mensagem no Gmail
    pg.hotkey('ctrl', 'shift', 'b') # Atalho para abrir menu de contatos em sigilo

    # Adicionando os e-mails automaticamente
    for email in emails:
        kb.write(email + "; ")
        time.sleep(0.2)
        pg.press('tab')
        time.sleep(0.2)  # Adiciona os e-mails separados por ponto e vírgula

    # Adicionando a mensagem com a edição
    time.sleep(0.5)
    pg.press('tab')  
    kb.write(f"Segue PDF completo da edição {edicao} do jornal O Hoje")
    pg.press('esc')
    time.sleep(1)