import keyboard as kb
import time
import pyautogui as pg

pg.FAILSAFE = True
pg.PAUSE = 0.3
center_x, center_y = pg.size()

time.sleep(0.5)

def gerar_edicoes(inicial, quantidade):
    edicoes = []
    
    for _ in range(quantidade):
        edicoes.append(str(inicial))
        inicial += 1
    
    edicoes.append(f"{inicial}-{inicial+1}")
    
    return edicoes

# Configuração inicial
numero_inicial = 6727
quantidade_semanal = 5
quantidade_repeticoes = 2  # Número de repetições

pg.hotkey('ctrl', 'p')
kb.write('emails_alterado.csv')
pg.press('down')
pg.press('enter')
time.sleep(0.5)
pg.click(center_x / 2, center_y / 2)
pg.hotkey('ctrl', 'a')
pg.hotkey('ctrl', 'c')
pg.hotkey('win', '3')

for _ in range(quantidade_repeticoes):
    edicoes_geradas = gerar_edicoes(numero_inicial, quantidade_semanal)
    
    for edicao in edicoes_geradas:
        pg.press('c')  
        time.sleep(1.5)  # Atalho para abrir menu de mensagem no Gmail
        pg.hotkey('ctrl', 'shift', 'b')  # Atalho para abrir menu de contatos em sigilo
        pg.hotkey('ctrl', 'v')
        pg.press('tab') 
        time.sleep(0.5)
        kb.write(f"Segue PDF completo da edição {edicao} do jornal O Hoje")
        pg.press('esc')
        time.sleep(1)
        numero_inicial += quantidade_semanal


# ----Backup
#     import keyboard as kb
# import time
# import pyautogui as pg
# import csv

# pg.PAUSE = 0.3
# pg.FAILSAFE = True

# time.sleep(0.5)

# def gerar_edicoes(inicial, quantidade):
#     edicoes = []
    
#     for _ in range(quantidade):
#         edicoes.append(inicial)
#         inicial += 1
#     edicoes.append(f"{inicial}-{inicial+1}")
    
#     return edicoes

# # Lendo e-mails do CSV
# # emails = []
# # with open("emails_alterado.csv", newline="", encoding="utf-8") as arquivo:
# #     leitor = csv.reader(arquivo)
# #     for linha in leitor:
# #         emails.append(linha[0])  # Pegando apenas a coluna de e-mail

# # Exemplo de uso
# numero_inicial = 6730 
# quantidade_semanal = 0

# edicoes_geradas = gerar_edicoes(numero_inicial, quantidade_semanal)

# pg.hotkey('win', '3')

# for edicao in edicoes_geradas:
#     pg.press('c')  
#     time.sleep(1.5)  # Atalho para abrir menu de mensagem no Gmail
#     pg.hotkey('ctrl', 'shift', 'b') # Atalho para abrir menu de contatos em sigilo

#     # Adicionando os e-mails automaticamente
#     # for email in emails:
#     #     kb.write(email + ", ")
#     #     time.sleep(0.2)
#     #     pg.press('tab')
#     #     time.sleep(0.2)
        
#     # Adicionando a mensagem com a edição
#     pg.press('esc')
#     pg.press('tab') 
#     time.sleep(0.5)
#     kb.write(f"Segue PDF completo da edição {edicao} do jornal O Hoje")
#     pg.press('esc')
#     time.sleep(1)
#     print(f"Mensagem enviada para a edição {edicao} com sucesso!")


#backup pegar edições correto
# import keyboard as kb
# import time
# import pyautogui as pg

# pg.PAUSE = 0.2
# pg.FAILSAFE = True

# time.sleep(1) 
# # NEDICAO = pg.prompt('Qual o número da edição?')

# # pg.press('win')
# # pg.write('Opera GX')
# # pg.press('enter')   
# # pg.press('c') #atalho para abrir menu de mensagem no gmail
# # kb.write('Segue PDF completo da edição ')
# # kb.write(NEDICAO)
# # pg.write(' do jornal O Hoje')


# # def gerar_edicoes(inicial, quantidade):
# #     edicoes = []
    
# #     for _ in range(quantidade):
# #         edicoes.append(inicial)
# #         inicial += 1
    
# #     # Junta as edições de fim de semana
# #     edicoes.append(f"{inicial}-{inicial+1}")
    
# #     return edicoes

# # # Exemplo de uso
# # numero_inicial = 6720
# # quantidade_semanal = 5

# # edicoes_geradas = gerar_edicoes(numero_inicial, quantidade_semanal)

# # for edicao in edicoes_geradas:
# #     print(edicao)



# import time
# import pyautogui as pg

# def gerar_edicoes(inicial, quantidade):
#     edicoes = []
    
#     for _ in range(quantidade):
#         edicoes.append(str(inicial))
#         inicial += 1
    
#     edicoes.append(f"{inicial}-{inicial+1}")
    
#     return edicoes

# # Configuração inicial
# numero_inicial = 6720
# quantidade_semanal = 5
# quantidade_repeticoes = 4  # Número de repetições

# for _ in range(quantidade_repeticoes):
#     edicoes_geradas = gerar_edicoes(numero_inicial, quantidade_semanal)
    
#     for edicao in edicoes_geradas:
#         print(f"Edição: {edicao}")
#         # time.sleep(2)
#         pg.hotkey('ctrl', 'c')  # Simulação da cópia
    
#     numero_inicial += quantidade_semanal  # Atualiza para a próxima sequência
