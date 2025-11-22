import pyautogui as pg
import time
import keyboard as kb
import os
import sys
import tkinter as tk
from tkinter import messagebox

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as sy_de

# ------------------------------------------------------------------------- Constantes
pg.PAUSE = 0.3 
pg.FAILSAFE = True

# ------------------------------------------------------------------------- Funções   
def open_paste_page_done():
    pg.press('esc')
    utl.take_tool("v")
    pg.hotkey('ctrl', '0')
    pg.hotkey('ctrl', 'o')
    time.sleep(0.2)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.2)
    kb.write(cfg.CAMINHO_EDD + "\\" + sy_de.EDD + "\\" + 'Páginas prontas')
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(0.2)
    
def cg_close():
    utl.take_tool("v")
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'g')
    time.sleep(0.2)
    pg.hotkey('ctrl', 's')
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(0.2)
    pg.hotkey('ctrl', 'c')
    pg.hotkey('ctrl', 'f4')
    time.sleep(cfg.TIMETOCLOSE)

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
    utl.chose_suggestion()
    # utl.error_check()
    time.sleep(cfg.TIMETOOPEN)
    cg_close()
    time.sleep(cfg.TIMETOCLOSE + 4)
    pg.hotkey('ctrl', '0')
    pg.click(cfg.center_x, cfg.center_y)
    pg.hotkey('ctrl', 'v')
    time.sleep(5)
    if is_even: 
        move_page(10, 20) 
    else: 
        move_page(290, 20)
    pg.hotkey('ctrl', 's')
    time.sleep(1)

def wedding(nome_arquivo, paginas):
    utl.open_web()
    utl.take_file(nome_arquivo)
    utl.close_and_open_quark()
    
    # Na máquina Marketing não há permissão para rodar o código
    # utl.error_check()

    for page_number in paginas:
        is_even = page_number % 2 == 0
        process_page(page_number, is_even)
    time.sleep(0.5)
    pg.hotkey('ctrl', 'f4')
    time.sleep(0.5)

def process_basic():
    wedding("17_20", [17, 20])
    wedding("13_16", [13, 16])
    wedding("14_15", [14, 15])

def process_town():
    wedding("10_11", [10, 11])
    wedding("9_12", [9, 12])

def process_crumb():
    wedding("3_6", [3, 6])
    wedding("4_5", [4, 5])

def wedding_cape():
    wedding("1_8", [8, 1])

# ------------------------------------------------------------------------- Executando 
def auto_marriage():
    def fazer_escolha(opcao):
        if opcao == "Essencia + Classificados":
            time.sleep(5)
            process_basic()
            pg.alert('Essencia + Classificados OK')
        elif opcao == "cidades":
            time.sleep(5)
            process_town()
            pg.alert('Cidades OK')
        elif opcao == "primeiro caderno":
            time.sleep(5)
            wedding("2_7", [2, 7])    
            process_crumb()
            wedding_cape()
            pg.alert('Primeiro caderno OK')
        elif opcao == "basico completo":
            time.sleep(5)
            process_basic()
            process_town()    
            pg.alert('Básico completo OK')  
        elif opcao == "o miolo":
            time.sleep(5)
            process_crumb()
            pg.alert('Miolo OK')
        elif opcao == "2_7 + miolo":
            time.sleep(5)
            wedding("2_7", [2, 7])    
            process_crumb()
            pg.alert('2_7 + miolo OK')
        elif opcao == "tudo":
            time.sleep(5)
            process_basic()
            process_town() 
            process_crumb()
            wedding("2_7", [2, 7])    
            wedding_cape()    
            pg.alert('Tudo OK')     
        else:
            messagebox.showerror("Erro", "Opção inválida.")

    janela = tk.Tk() 
    janela.title("Casamento")
    janela.geometry("600x450")
    janela.configure(bg="#747474")
    janela.iconbitmap(r'App\archives\favicon.ico')

    estilo_títulos = {"font": ("Helvetica", 19, "bold"), "bg": "#585858", "fg": "white", "width": 30, "borderwidth": 3, "relief": "solid"}
    estilo_escolhas = {"font": ("Noto sans", 14), "bg": "#585858", "fg": "white", "width": 20, "borderwidth": 3, "relief": "raised"}

    label = tk.Label(janela, text=f"Edição: {sy_de.EDD}", **estilo_títulos)
    label.pack(pady=10)

    btn_x = tk.Button(janela, text="Essencia + Classificados", command=lambda: fazer_escolha("Essencia + Classificados"), **estilo_escolhas)
    btn_x.pack(pady=5)

    btn_t = tk.Button(janela, text="Básico completo", command=lambda: fazer_escolha("Básico completo"), **estilo_escolhas)
    btn_t.pack(pady=5)

    btn_v = tk.Button(janela, text="Caderno de cidades", command=lambda: fazer_escolha("cidades"), **estilo_escolhas)
    btn_v.pack(pady=5)

    btn_y = tk.Button(janela, text="Miolo", command=lambda: fazer_escolha("o miolo"), **estilo_escolhas)
    btn_y.pack(pady=5)

    btn_w = tk.Button(janela, text="Primeiro caderno", command=lambda: fazer_escolha("primeiro caderno"), **estilo_escolhas)
    btn_w.pack(pady=5)

    btn_z = tk.Button(janela, text="miolo completo", command=lambda: fazer_escolha("2_7 + miolo"), **estilo_escolhas)
    btn_z.pack(pady=5)

    btn_u = tk.Button(janela, text="Tudo", command=lambda: fazer_escolha("tudo"), **estilo_escolhas)
    btn_u.pack(pady=5)

    janela.mainloop()

if __name__ == "__main__":
    auto_marriage()

    #Faltando corrigir o check_status na máquina do marketing
