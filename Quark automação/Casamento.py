import pyautogui as pg
import time
import keyboard as kb
import os
import tkinter as tk
from tkinter import messagebox

#Contantes
pg.PAUSE = 0.3 
pg.FAILSAFE = True

largura, altura = pg.size()
centro_x = largura / 2
centro_y = altura / 2
TIME1 = 5
TIME2 = 4
TIMETOCLOSE = 6
WAY_EDD = r'\\192.168.1.249\redacao\diagramacao\edicao'
WAY_WEB = r'\\192.168.1.249\redacao\web'

#variáveis
EDD = r"6861 - terça-feira" 

#funções
def max_windows():
    kb.press_and_release('alt+space')
    time.sleep(0.2)
    kb.press_and_release('x')

def take_file(arquivo):
    kb.press_and_release('ctrl+f')
    time.sleep(0.5)
    kb.write(str(arquivo))
    time.sleep(2)
    pg.click(centro_x, centro_y)
    pg.press('down')
    time.sleep(0.3)
    pg.press('down')
    time.sleep(0.3)
    kb.press_and_release('enter')

def open_web():
    os.startfile(WAY_WEB + "\\" + EDD)
    time.sleep(0.3)
    max_windows()

#funções-específicas
def close_and_open_quark():
    pg.hotkey('alt', 'f4')
    pg.hotkey('win', 's')
    pg.hotkey('win', '1')
    time.sleep(TIME2)

def take_tool(tool):
    pg.click(centro_x, 10)
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
    kb.write(WAY_EDD + "\\" + EDD + "\\" + 'Páginas prontas')
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
    time.sleep(TIME2)

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
    time.sleep(TIME1)
    agrupar_e_fechar_agora()
    time.sleep(TIMETOCLOSE)
    time.sleep(TIMETOCLOSE)
    time.sleep(0.3)
    pg.hotkey('ctrl', '0')
    pg.click(centro_x, centro_y)
    pg.hotkey('ctrl', 'v')
    time.sleep(TIME1)
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
    time.sleep(0.3)

def process_casamento_basico():
    process_casamento("13_16", [13, 16])
    process_casamento("14_15", [14, 15])
    process_casamento("17_20", [17, 20])
    process_casamento("10_11", [10, 11])
    process_casamento("9_12", [9, 12])

def process_casamento_miolo():
    process_casamento("4_5", [4, 5])
    process_casamento("3_6", [3, 6])

def process_casamento_capa():
    process_casamento("2_7", [2, 7])    
    process_casamento("1_8", [1, 8])

def process_casamento_primeiro_caderno():
    process_casamento_miolo()
    process_casamento_capa()
    
def process_casamento_completo():
    process_casamento_basico()
    process_casamento_primeiro_caderno()

# --------------------------Executando 


# def fazer_escolha(opcao):
#     EDD = entrada_edicao.get()
#     if EDD.strip() == "":
#         messagebox.showwarning("Atenção", "Por favor, digite o número da edição.")
#         return
#     messagebox.showinfo("Escolha", f"Edição {EDD} selecionada.\nVocê escolheu fazer {opcao}.")

# # Criar janela principal
# janela = tk.Tk() 
# janela.title("Escolha uma opção")
# janela.geometry("300x250")


# # Texto de instrução
# label = tk.Label(janela, text="Vc quer:", font=("Arial", 35))
# label.pack(pady=10)


# # Caixa de entrada para número da edição
# label_edicao = tk.Label(janela, text="Digite o número da edição:")
# label_edicao.pack()
# entrada_edicao = tk.Entry(janela)
# entrada_edicao.pack(pady=5)

# # Botões de escolha
# btn_x = tk.Button(janela, text="Básico", command=lambda: fazer_escolha("o básico"))
# btn_x.pack(pady=5)

# btn_y = tk.Button(janela, text="Miolo", command=lambda: fazer_escolha("o miolo"))
# btn_y.pack(pady=5)

# btn_z = tk.Button(janela, text="Capa", command=lambda: fazer_escolha("a capa"))
# btn_z.pack(pady=5)

# # Iniciar a interface
# janela.mainloop()


# process_casamento_basico()
process_casamento_miolo() 
pg.hotkey('win', 's')
pg.hotkey('win', '3')
print("ACABOU XD")