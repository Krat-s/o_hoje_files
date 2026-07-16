import pyautogui as pg
import time

from App import wedding as cm
from App.billhead_editions import auto_billhead_editions
from Mail.gmail import auto_drafts
from Web.print_ad_by_selector import auto_print_all_ads
from Web.print_ad import auto_prints_all_ads
from config.settings.settings_edition_request import quantidade_repeticoes, edicao_inicial
# from Backup.shutdawns import sleep_computer
    
import tkinter as tk
from tkinter import messagebox



# 📌 ------------------------------------------ making drafts
def auto_drafts_(ed=None, qnt=None):
    try:
        auto_drafts(ed=ed, qnt=qnt)
    except Exception as e:
        print(f'Error creating drafts: {e}')



# 📌 ------------------------------------------ Wedding
def auto_marriage_():
    try:
        cm.auto_marriage()
    except Exception as e:
        print(f'Error in marriage: {e}')



# 📌 ------------------------------------------ making billhead
def auto_billhead_editions_(ed=edicao_inicial, qnt=quantidade_repeticoes):
    try:
        auto_billhead_editions(edicao_inicial=ed, quantidade_repeticoes=qnt)
    except Exception as e:
        print(f'Error creating billhead: {e}')


# 📌 ------------------------------------------ print ads
def auto_print_():
   try:
       auto_print_all_ads()
   except Exception as e:
       print(f'Error printing ads: {e}')

def auto_print_by_link_():
   try:
       auto_prints_all_ads()
   except Exception as e:
       print(f'Error printing ads by link: {e}')

# from config.core import schedule_manager as sm
# # 📌 ------------------------------------------ Sredule
# def scredule_function_():
#     try:
#        sm.schedule_function(auto_prints_all_ads())
#     except Exception as e:
#        print(f'Error printing ads: {e}')

# Importar aplicações
# 📌 Drive Daily
# 📌 billhead_variables
# 📌 relatório
# 📌 click_farmer
# 📌 Gerar interfaçe gráfica de opções de automações


# 📌 ------------------------------------------ Escolhas
def all_in_one_():
    def fazer_escolha(opcao):
        if opcao == "Casamento":
            auto_marriage_()
            janela.destroy()
        elif opcao == "Billhead":
            auto_billhead_editions_(ed_ini, qtd)
            janela.destroy()
        elif opcao == "Rascunhos":
            auto_drafts_(ed_ini, qtd)
            janela.destroy()
        elif opcao == "Print":
            janela.destroy()
            auto_print_()
        elif opcao == "print por link":
            janela.destroy()
            auto_print_by_link_()
        elif opcao == "week_duty":
            janela.destroy()
            sem = pg.prompt("Quantas edições deseja adiantar?")
            semanal = int(sem) * 7
            auto_drafts_(ed_ini, int(semanal))
            auto_billhead_editions_(ed_ini, int(semanal))
            time.sleep(1)
        elif opcao == "Desligar":
            janela.destroy()
            # sleep_computer()
        else:
            messagebox.showerror("Erro", "Opção inválida.")

    janela = tk.Tk() 
    janela.title("Kratos Api")
    janela.geometry("400x350")
    janela.configure(bg="#32395F")
    janela.iconbitmap(r'App\archives\favicon.ico')

    estilo_escolhas = {"font": ("Noto sans", 14), "bg": "#12162B", "fg": "white", "width": 30, "borderwidth": 3, "relief": "raised"}

    btn_x = tk.Button(janela, text="Casamento da edição atual", command=lambda: fazer_escolha("Casamento"), **estilo_escolhas)
    btn_x.pack(pady=5)

    btn_v = tk.Button(janela, text="Cabeçalho das páginas", command=lambda: fazer_escolha("Billhead"), **estilo_escolhas)
    btn_v.pack(pady=5)

    btn_t = tk.Button(janela, text="Rascunhos no Gmail", command=lambda: fazer_escolha("Rascunhos"), **estilo_escolhas)
    btn_t.pack(pady=5)

    btn_y = tk.Button(janela, text="Print de anúncios", command=lambda: fazer_escolha("Print"), **estilo_escolhas)
    btn_y.pack(pady=5)

    btn_z2 = tk.Button(janela, text="Print de anúncio por link", command=lambda: fazer_escolha("print por link"), **estilo_escolhas)
    btn_z2.pack(pady=5)

    btn_z3 = tk.Button(janela, text="Adianto semanal", command=lambda: fazer_escolha("week_duty"), **estilo_escolhas)
    btn_z3.pack(pady=5)

    btn_z4 = tk.Button(janela, text="Desligar tudo", command=lambda: fazer_escolha("Desligar"), **estilo_escolhas)
    btn_z4.pack(pady=5)

    janela.mainloop()

ed_ini = 7168
qtd = 3

if __name__ == "__main__":
    print('All in one executando...')
    all_in_one_()