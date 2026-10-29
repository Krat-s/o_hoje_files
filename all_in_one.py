import pyautogui as pg
import time

from settings.settings_edition_request import quantidade_repeticoes, edicao_inicial
from departments.editorial import wedding as cm
from departments.editorial.billhead_editions import auto_billhead_editions
from departments.mail.gmail import auto_drafts
from departments.commercial.word_converter import _watch_folder_converter
from departments.commercial.print_ad import auto_prints_all_ads
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
def auto_print_by_link_():
    try:
        auto_prints_all_ads()
    except Exception as e:
        print(f'Error printing ads by link: {e}')


# 📌 ------------------------------------------ converter word
def auto_watch_folder():
    try:
        _watch_folder_converter()
    except Exception as e:
        print(f'Error watching folder: {e}')


# # 📌 ------------------------------------------ Sredule
# def scredule_function_():
# from config.core import schedule_manager as sm
#     try:
#        sm.schedule_function(auto_prints_all_ads())
#     except Exception as e:
#        print(f'Error printing ads: {e}')
# 📌 Drive Daily
# 📌 billhead_variables
# 📌 relatório
# 📌 click_farmer
# 📌 Gerar interfaçe gráfica de opções de automações


# 📌 ------------------------------------------ Escolhas
def all_in_one_():
    def choise(option):
        if option == "Casamento":
            auto_marriage_()
            janela.destroy()
        elif option == "Billhead":
            auto_billhead_editions_(ed_ini, qtd)
            janela.destroy()
        elif option == "Rascunhos":
            auto_drafts_(ed_ini, qtd)
            janela.destroy()
        elif option == "ad-print":
            janela.destroy()
            auto_print_by_link_()
        elif option == "week_duty":
            janela.destroy()
            sem = pg.prompt("Quantas edições deseja adiantar?")
            semanal = int(sem) * 7
            auto_drafts_(ed_ini, int(semanal))
            auto_billhead_editions_(ed_ini, int(semanal))
            time.sleep(1)
        elif option == "monitorar_conversao":
            janela.destroy()
            auto_watch_folder()
            # sleep_computer()
        else:
            messagebox.showerror("Erro", "Opção inválida.")

    janela = tk.Tk()
    janela.title("Kratos Api")
    janela.geometry("600x700")
    janela.configure(bg="#32395F")
    janela.iconbitmap(r'storage\\img\\favicon.ico')

    style_button = {"font": ("Noto sans", 14), "bg": "#12162B",
                    "fg": "white", "width": 30, "borderwidth": 3, "relief": "raised"}

    btn_x = tk.Button(janela, text="Casamento da edição atual",
                      command=lambda: choise("Casamento"), **style_button)
    btn_x.pack(pady=5)

    btn_v = tk.Button(janela, text="Cabeçalho das páginas",
                      command=lambda: choise("Billhead"), **style_button)
    btn_v.pack(pady=5)

    btn_t = tk.Button(janela, text="Rascunhos no Gmail",
                      command=lambda: choise("Rascunhos"), **style_button)
    btn_t.pack(pady=5)

    btn_z2 = tk.Button(janela, text="Print de anúncios",
                       command=lambda: choise("ad-print"), **style_button)
    btn_z2.pack(pady=5)

    btn_z3 = tk.Button(janela, text="Adianto semanal",
                       command=lambda: choise("week_duty"), **style_button)
    btn_z3.pack(pady=5)

    btn_z4 = tk.Button(janela, text="Monitorar pasta de conversão",
                       command=lambda: choise("monitorar_conversao"), **style_button)
    btn_z4.pack(pady=5)

    janela.mainloop()


ed_ini = 7280
qtd = 4

if __name__ == "__main__":
    print('All in one executando...')

    all_in_one_()
