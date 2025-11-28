import pyautogui as pg
import time
import keyboard as kb
import os
import sys
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from App.modulos_quark.data_formatador import formatar_data
import Global.settings as cfg
import Global.utils as utl
import Global.data_edition_sync as sy_de

# ------------------------------------------------------------------------- Constantes
pg.PAUSE = 0.3 
pg.FAILSAFE = True

# ------------------------------------------------------------------------- Funções   
def expdf():
    pg.hotkey('ctrl', 'shift', 's')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(0.2)
    pg.press('left')
    time.sleep(0.2)
    pg.press('enter')
    time.sleep(2)
    pg.hotkey('alt', 'f') #quarkExpress8 hotkey to "file menu" 
    pg.press('e')   #quick select to "export PDF"
    pg.press('enter')
    time.sleep(1)
    pg.press('right')
    time.sleep(1)
    pg.press('backspace', presses=9)
    time.sleep(1)
    pg.press('tab', presses=2)
    time.sleep(1)
    pg.press('enter')
    time.sleep(cfg.TIMEEXPPDF)
    
def exporting_pdf(file):
    utl.open_web()
    utl.take_file(file)
    utl.error_check()


def exp_basic():
    exporting_pdf("17_20")
    exporting_pdf("13_16")
    exporting_pdf("14_15")

def exp_town():
    exporting_pdf("10_11")
    exporting_pdf("9_12")

def basic():
    exp_basic()
    exp_town()

def exp_crumb():
    exporting_pdf("3_6")
    exporting_pdf("4_5")

def exp_complete_crumb():
    exporting_pdf("2_7")    
    exporting_pdf("3_6")
    exporting_pdf("4_5")
    
def exporting_pdf_cape():
    exporting_pdf("1_8")

def wedding_fist_journal():
    exp_complete_crumb()
    # wedding_cape()

def exp_all():
    exp_basic()
    wedding_fist_journal()

# ------------------------------------------------------------------------- Executando 
def auto_exporttpdf():
    def fazer_escolha(opcao):
        if opcao == "Essencia + Classificados":
            time.sleep(5)
            exp_basic()
            pg.alert('Automação finalizada')
        elif opcao == "cidades":
            time.sleep(5)
            exp_town()
            pg.alert('Automação finalizada')
        elif opcao == "o miolo":
            time.sleep(5)
            exp_crumb()
            pg.alert('Automação finalizada')
        elif opcao == "2_7 + miolo":
            time.sleep(5)
            exp_complete_crumb()
            pg.alert('Automação finalizada')
        elif opcao == "primeiro caderno":
            time.sleep(5)
            exp_fist_journal()
            pg.alert('Automação finalizada')
        elif opcao == "basico completo":
            time.sleep(5)
            process_complete_basic()    
            pg.alert('Automação finalizada')  
        elif opcao == "tudo":
            time.sleep(5)
            process_all()    
            pg.alert('Automação finalizada')     
        else:
            messagebox.showerror("Erro", "Opção inválida.")

    # Criar janela principal
    janela = tk.Tk() 
    janela.title("Casamento")
    janela.geometry("600x450")
    janela.configure(bg="#747474")
    janela.iconbitmap(r'App\archives\favicon.ico')

    estilo_títulos = {"font": ("Helvetica", 19, "bold"), "bg": "#585858", "fg": "white", "width": 30, "borderwidth": 3, "relief": "solid"}
    estilo_escolhas = {"font": ("Noto sans", 14), "bg": "#585858", "fg": "white", "width": 20, "borderwidth": 3, "relief": "raised"}

    # Texto de instrução
    label = tk.Label(janela, text=f"Edição: {EDD}", **estilo_títulos)
    label.pack(pady=10)

    # Botões de escolha
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

    # Iniciar a interface
    janela.mainloop()

if __name__ == "__main__":
    auto_marriage()
                    