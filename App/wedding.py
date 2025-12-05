import pyautogui as pg
import time
import os
import sys
import tkinter as tk
from tkinter import messagebox

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

import Global.utils as utl
import Global.data_edition_sync as sy_de
import App.modulos_quark.utils_quark as utlq
from Global.FileManager import take_file
from Global.Logs.logs import log

pg.PAUSE = 0.3 
pg.FAILSAFE = True

def wedding(nome_arquivo, paginas):
    # try:
        utl.open_web()
        take_file(nome_arquivo)
        time.sleep(1)
        utl.close_and_open_quark()
        
        # Na máquina Marketing não há permissão para rodar o código
        # utl.error_check()

        for page_number in paginas:
            is_even = page_number % 2 == 0
            utlq.process_page(page_number, is_even)
            # log("Wedding", "SUCESSO", f"Paginas {nome_arquivo} casadas") 
        
    # except Exception as e:
    #     erro_msg = f"Erro ao clicar no botão: {str(e)}"
    #     log("Wedding", "ERRO", erro_msg) 

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

    btn_t = tk.Button(janela, text="Básico completo", command=lambda: fazer_escolha("basico completo"), **estilo_escolhas)
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
