import pyautogui as pg
import time
import tkinter as tk
from tkinter import simpledialog

pg.FAILSAFE = True

# --- FUNÇÕES DE AÇÃO ---
def ajuda():
    
    # Pergunta os dados antes de começar a automação
    linhas = simpledialog.askinteger("Entrada", "Quantas linhas?")
    dados = simpledialog.askinteger("Entrada", "Quantos dados por linha?")


    if linhas and dados:
        pg.hotkey('alt', 'tab', 'tab')      
        for i in range(linhas):
            for _ in range(dados):
                pg.press('del')
                pg.press('tab')
                pg.hotkey('ctrl', 'right')
            pg.press('right')
            pg.press('down')
            pg.press('left')

def so_tab():
    dados = simpledialog.askinteger("Entrada", "Quantas vezes?")
    if dados:
        pg.hotkey('alt', 'tab', 'tab')
        for _ in range(dados):
            pg.press('tab')
            pg.hotkey('ctrl', 'right')
    

# --- INTERFACE GRÁFICA ---
def criar_interface():
    janela = tk.Tk()
    janela.title("Ação")
    janela.geometry("300x150") # Aumentei um pouco para caber os botões
    janela.configure(bg="#4B2A6A")

    # estilo_titulos = {"font": ("Helvetica", 19, "bold"), "bg": "#585858", "fg": "white", "width": 30, "borderwidth": 3, "relief": "solid"}
    estilo_escolhas = {"font": ("Noto sans", 14), "bg": "#585858", "fg": "white", "width": 20, "borderwidth": 3, "relief": "raised"}

    btn_x = tk.Button(janela, text="Só Tab", command=so_tab, **estilo_escolhas)
    btn_x.pack(pady=5)

    btn_v = tk.Button(janela, text="Completo", command=ajuda, **estilo_escolhas)
    btn_v.pack(pady=5)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
