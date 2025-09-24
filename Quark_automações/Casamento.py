import pyautogui as pg
import time
import keyboard as kb
import os
import sys
import tkinter as tk
from tkinter import messagebox

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)
import Global_modulos.settings as cg
import Global_modulos.utils as ut
import Global_modulos.edition_sync as sc
from Quark_automações.Modulos_quark.data_formatador import formatar_data

# ------------------------------------------------------------------------- Constantes
pg.PAUSE = 0.3 
pg.FAILSAFE = True

# ------------------------------------------------------------------------- Variáveis
# EDD = input("qual o número da edição? Exemplo: 6868 - terça-feira: ")
# EDD = f"{cg.edicao_inicial} - terça-feira" 
EDD = r'6889 - terça-feira'

# ------------------------------------------------------------------------- Funções
def take_file(arquivo):
    kb.press_and_release('ctrl+f')
    time.sleep(0.5)
    kb.write(str(arquivo))
    time.sleep(2)
    pg.click(cg.center_x, cg.center_y)
    pg.press('down')
    time.sleep(0.3)
    pg.press('down')
    time.sleep(0.3)
    kb.press_and_release('enter')

def open_web():
    os.startfile(cg.CAMINHO_WEB + "\\" + EDD)
    time.sleep(0.3)
    ut.max_windows()

# ------------------------------------------------------------------------- Funções específicas
def close_and_open_quark():
    pg.hotkey('alt', 'f4')
    pg.hotkey('win', 's')
    pg.hotkey('win', '1')
    time.sleep(4)

def take_tool(tool):
    pg.click(cg.center_x, 10)
    kb.press(str(tool))

def confirmancia():
    pg.press('down')
    pg.press('enter')
    
def open_paste_page_done():
    pg.press('esc')
    take_tool("v")
    pg.hotkey('ctrl', '0')
    pg.hotkey('ctrl', 'o')
    time.sleep(0.2)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.2)
    kb.write(cg.CAMINHO_EDD + "\\" + EDD + "\\" + 'Páginas prontas')
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(0.2)
    
def agrupar_e_fechar_agora():
    take_tool("v")
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'g')
    time.sleep(0.2)
    pg.hotkey('ctrl', 's')
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(0.2)
    pg.hotkey('ctrl', 'c')
    pg.hotkey('ctrl', 'f4')
    time.sleep(cg.TIMETOCLOSE)

def move_page(left, right):
    pg.hotkey('ctrl', 'shift', 'alt', 'm')
    time.sleep(0.2)
    kb.write(str(left))
    time.sleep(0.2)
    pg.press('tab')
    time.sleep(0.2)
    kb.write(str(right))
    pg.press('enter')
    time.sleep(0.2)
    pg.press('down')
    time.sleep(0.2)
    pg.press('up')
    
def process_page(page_number, is_even):
    time.sleep(0.3)
    open_paste_page_done()
    pg.write(str(page_number))
    confirmancia()
    time.sleep(5)
    agrupar_e_fechar_agora()
    time.sleep(cg.TIMETOCLOSE)
    time.sleep(cg.TIMETOCLOSE)
    time.sleep(0.3)
    pg.hotkey('ctrl', '0')
    pg.click(cg.center_x, cg.center_y)
    pg.hotkey('ctrl', 'v')
    time.sleep(5)
    time.sleep(2)
    if is_even: 
        move_page(10, 20) 
    else: 
        move_page(290, 20)
    pg.hotkey('ctrl', 's')
    time.sleep(0.3)

def process_casamento(nome_arquivo, paginas):
    open_web()
    take_file(nome_arquivo)
    close_and_open_quark()
    for page_number in paginas:
        is_even = page_number % 2 == 0
        process_page(page_number, is_even)
    time.sleep(0.5)

def process_casamento_basico():
    process_casamento("13_16", [13, 16])
    process_casamento("14_15", [14, 15])
    process_casamento("17_20", [17, 20])

def process_casamento_miolo():
    print('miolo')
    process_casamento("10_11", [10, 11])
    process_casamento("9_12", [9, 12])
    process_casamento("3_6", [3, 6])
    process_casamento("4_5", [4, 5])

def process_casamento_capa():
    process_casamento("2_7", [2, 7])    
    process_casamento("1_8", [8, 1])
    print('capa')

def process_casamento_primeiro_caderno():
    process_casamento_miolo()
    process_casamento_capa()
    
def process_casamento_completo():
    process_casamento_basico()
    process_casamento_primeiro_caderno()

# ------------------------------------------------------------------------- Executando 
# time.sleep(5)
# process_casamento_basico()
# process_casamento_miolo() 
# pg.hotkey('win', 's')
# pg.hotkey('win', '3')
print("ACABOU XD")
print(formatar_data(sc.data, tipo='dia_semana'))
print(formatar_data(sc.data))



# def fazer_escolha(opcao):
#     EDD = entrada_edicao.get()
#     if EDD.strip() == "":
#         messagebox.showwarning("Atenção", "Por favor, digite o número da edição.")
#         return EDD
#     messagebox.showinfo("Escolha", f"Edição {EDD} selecionada.\nVocê escolheu fazer {opcao}.")
#     print(EDD)


# # Criar janela principal
# janela = tk.Tk() 
# janela.title("Casamento")
# janela.geometry("300x250")


# # Texto de instrução
# label = tk.Label(janela, text="Edição:", font=("Noto Serif", 20))
# label.pack(pady=10)


# # Caixa de entrada para número da edição
# label_edicao = tk.Label(janela, text="Digite o número da edição:")
# label_edicao.pack()
# entrada_edicao = tk.Entry(janela)
# entrada_edicao.pack(pady=5)

# # Botões de escolha
# btn_x = tk.Button(janela, text="Básico", command=lambda: fazer_escolha("o básico"))
# btn_x.pack(pady=5)

# # btn_y = tk.Button(janela, text="Miolo", command=lambda: fazer_escolha("o miolo"))
# # btn_y.pack(pady=5)

# # btn_z = tk.Button(janela, text="Capa", command=lambda: fazer_escolha("a capa"))
# # btn_z.pack(pady=5)

# # Iniciar a interface
# janela.mainloop()