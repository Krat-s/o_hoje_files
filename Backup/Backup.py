# Cabeccalho
# import os
# import time
# import locale
# from datetime import datetime, timedelta
# import pyautogui as pg
# import keyboard as kb
# from Modulos.data_formatador import formatar_data
# from Modulos.edicao_formatador import gerar_edicoes

# ---------------------------- CONFIGURAÇÕES ----------------------------
# pg.PAUSE = 0.5
# pg.FAILSAFE = True
# time.sleep(1)

# locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")

# screen_width, screen_height = pg.size()
# center_x = screen_width / 2
# center_y = screen_height / 2

# edicao_inicial = 6794
# quantidade_por_semana = 5
# quantidade_repeticoes = 2
# data_inicial = datetime(2025, 7, 21) #Precisa ser uma segunda-feira

# ---------------------------- CONSTANTES ----------------------------
# CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
# EDD_PADRAO = "0000 - TESTE"
# TEMPO_ABERTURA = 4
# TEMPO_FECHAMENTO = 3

# ---------------------------- POSIÇÕES DE CLIQUE ----------------------------
# x_data = int(screen_width * 0.6428)
# y_data = int(screen_height * 0.3255)
# x_edicao_17 = int(screen_width * 0.4173)
# y_edicao_17 = int(screen_height * 0.1536)
# x_edicao_capa = int(screen_width * 0.1740)
# y_edicao_capa = int(screen_height * 0.4648)

# ---------------------------- FUNÇÕES UTILITÁRIAS ----------------------------
# def ajustar_data(data):
#     return data + timedelta(days=1) if data.weekday() == 6 else data

# def abrir_software(numero):
#     pg.hotkey('win', 's')
#     pg.hotkey('win', str(numero))
#     pg.press('enter')
#     time.sleep(0.5)

# def maximizar_janela():
#     kb.press_and_release('alt+space')
#     time.sleep(0.2)
#     kb.press_and_release('x')

# def selecionar_ferramenta(tecla):
#     pg.click(center_x, 10)
#     kb.press(tecla)

# def criar_pasta(nome):
#     time.sleep(0.5)
#     maximizar_janela()
#     time.sleep(0.5)
#     pg.click(center_x, center_y)
#     pg.hotkey('ctrl', 'shift', 'n')
#     time.sleep(0.5)
#     kb.write(nome)
#     pg.press('enter')

# def copiar_modelo_para_pasta(ed, data_formatada):
#     nome_pasta = f"{ed.replace('.', '')} - {data_formatada}"
#     pg.click(center_x, center_y)
#     pg.hotkey('ctrl', 'a')
#     pg.hotkey('ctrl', 'c')
#     time.sleep(0.3)
#     pg.hotkey('alt', 'd')
#     kb.write(f"{CAMINHO_ADIANTO}\\{nome_pasta}")
#     pg.press('enter')
#     pg.hotkey('ctrl', 'v')

# def preencher_data(data_formatada):
#     selecionar_ferramenta("v")
#     pg.click(x_data, y_data)
#     selecionar_ferramenta("t")
#     pg.press('t', presses=2)
#     time.sleep(0.3)
#     pg.hotkey('ctrl', 'a')
#     time.sleep(0.3)
#     kb.write(data_formatada)

# def aplicar_autodata(numero, edicao_formatada, data_formatada):
#     pg.press('esc', presses=3)
#     pg.hotkey('ctrl', 'o')
#     nome_pasta = f"{edicao_formatada.replace('.', '')} - {str(data_formatada, tipo='dia_semana')}"
#     kb.write(f"{CAMINHO_ADIANTO}\\{nome_pasta}")
#     pg.press('enter')
#     pg.write(str(numero))
#     time.sleep(0.3)
#     pg.press('down')
#     time.sleep(0.3)
#     pg.press('enter')
#     time.sleep(TEMPO_ABERTURA)
#     preencher_data()
#     time.sleep(0.4)
#     pg.press('esc')
#     pg.hotkey('ctrl', 's')

# def fechar_pagina():
#     pg.hotkey('ctrl', 'f4')
#     time.sleep(TEMPO_FECHAMENTO)

# ---------------------------- AUTODATA ----------------------------
# def autodata_paginas():
#     for i in range(20, 1, -1):
#         if i != 17:
#             aplicar_autodata(i)
#             fechar_pagina()

# def autodata_edicao_1(edicao_formatada, data_formatada):
#     pg.press('esc', presses=3)
#     pg.hotkey('ctrl', 'o')
#     kb.write(f"{CAMINHO_ADIANTO}\\{EDD_PADRAO}")
#     pg.press('enter')
#     pg.write('1')
#     pg.press('down')
#     pg.press('enter')
#     time.sleep(TEMPO_ABERTURA + 3)
#     selecionar_ferramenta("v")
#     pg.click(x_edicao_capa, y_edicao_capa)
#     selecionar_ferramenta("t")
#     pg.press('t', presses=4)
#     time.sleep(0.3)
#     pg.press('backspace', presses=5)
#     kb.write(f"nº {edicao_formatada}")
#     time.sleep(0.4)
#     pg.press('right')
#     pg.press('del')
#     kb.write(f" | {data_formatada} ")
    
# def autodata_edicao_17(edicao_formatada, data_formatada):
#     aplicar_autodata(17, edicao_formatada, data_formatada)
#     selecionar_ferramenta("v")
#     pg.hotkey('ctrl', '0')
#     pg.click(x_edicao_17, y_edicao_17)
#     pg.hotkey('ctrl', 'a')
#     kb.write(f"Ano 21 - nº {edicao_formatada}")
#     time.sleep(0.2)
#     pg.hotkey('ctrl', 's')
#     time.sleep(0.2)
#     pg.press('esc', presses=3)
#     pg.hotkey('ctrl', 'f4')
#     time.sleep(TEMPO_FECHAMENTO)

# def cabeçalho(edicao_formatada):
#     autodata_edicao_17(edicao_formatada)
#     autodata_paginas(edicao_formatada)
#     autodata_edicao_1(edicao_formatada)

# ---------------------------- EXPLORADOR DE ARQUIVOS ----------------------------
# def abrir_pasta(endereco):
#     os.startfile(endereco)
#     maximizar_janela()
#     pg.click(center_x, center_y)

# def fechar_explorer():
#     pg.click(center_x, center_y)
#     pg.hotkey('alt', 'f4')

# def voltar_pasta():
#     pg.click(center_x, center_y)
#     pg.hotkey('alt', 'up')

# ---------------------------- TESTE ----------------------------
# def teste(edicao_formatada, data_formatada):
#     print(f"{data_formatada}, {edicao_formatada}")
#     print(data_formatada)
#     print(str(edicao_formatada).replace('.', ''), data_formatada)

# ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------
# abrir_pasta()
# pg.hotkey('win', 's')
# pg.hotkey('win', '1')

# aplicar_autodata(5)
# abrir_pasta(CAMINHO_ADIANTO)


# def main():
#     print("📦 Edições geradas:")
#     edicao = edicao_inicial
#     data = data_inicial

#     for _ in range(quantidade_repeticoes):
#         edicoes = gerar_edicoes(edicao, quantidade_por_semana)

#         for ed in edicoes:
#             data_formatada = formatar_data(data)
#             info = {
#             "edicao_formatada": ed,
#             "data_formatada": formatar_data(data)
#             }
#             modelo_path = {
#             0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
#             5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
#             }.get(data.weekday(), r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição')

#             teste(**info)

# --------------------------------------------------------------------------Criando modelo da edicão
#             criar_pasta(f"{ed.replace('.', '')} - {formatar_data(data, tipo='dia_semana')}")
#             time.sleep(0.3)
#             pg.hotkey('alt', 'd')
#             kb.write(modelo_path)
#             pg.press('enter')
#             copiar_modelo_para_pasta(ed, formatar_data(data, tipo='dia_semana'))
#             voltar_pasta()
#             time.sleep(0.3)

# --------------------------------------------------------------------------Preprarando area de operação
#             abrir_software(1)
#             time.sleep(0.5)
#             pg.press('esc', presses=3)
#             pg.hotkey('ctrl', '0')
#             pg.hotkey('ctrl', 'o')
#             kb.write(CAMINHO_ADIANTO + '\\' + f"{ed.replace('.', '')} - {formatar_data(data, tipo='dia_semana')}")
#             time.sleep(0.3)
#             pg.press('enter')
#             pg.press('esc', presses=3)
#             autodata_edicao_17(**info)





#             autodata_paginas()
            

# ----------------------------------------------------Verificar parte de baixo e adaptar para última sugestão do copilot
            

#              autodata_edicao_17()
#             abrir_software(4)  # Explorer
#             pg.hotkey('alt', 'up')
#             pg.click(center_x, center_y)

#             Se quiser aplicar cabeçalho apenas nos dias úteis:
#             if data_da_edicao.weekday() < 5:
#                 cabeçalho()
        
                      
#             print(f"📦 {ed} - {data_formatada}")
#             data += timedelta(days=1)
#             data = ajustar_data(data)
#         edicao += quantidade_por_semana + 2

# if __name__ == "__main__":
#     main()
    



#     \\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições\6794 - Segunda-feira




# -------explorer_verifiquer
# import os
# import pygetwindow as gw
# import pyautogui as pg
# from pywinauto import Desktop
# import time

# CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'

# def abrir_pasta(endereco):
#     os.startfile(endereco) 

# def explorer_aberto():
#     janelas = Desktop(backend="uia").windows()
#     for janela in janelas:
#         if janela.class_name() == "CabinetWClass":
#                 return True
#     return False

# def pasta_esta_aberta(nome_pasta):
#     janelas = Desktop(backend="uia").windows()
#     for janela in janelas:
#         if janela.class_name() == "CabinetWClass":
#             titulo = janela.window_text()
#             if nome_pasta.lower() in titulo.lower():
#                 return True
#     return False

# if pasta_esta_aberta("4 Adianto de novas edições"):
#     print("CAMINHO_ADIANTO está aberto.")
# else:
#     print("CAMINHO_ADIANTO não está aberto.")

# if explorer_aberto():
#         print("explorer já está aberto.")
# else:
#         print("explorer não está aberto.")




# def fazer_w():
#     messagebox.showinfo("Qual o número da ", "EDIÇÃO?", "?")
#     # process_casamento_basico()

# def fazer_x():
#     messagebox.showinfo("Escolha", "Você escolheu fazer o básico.")
#     # process_casamento_basico()

# def fazer_y():
#     messagebox.showinfo("Escolha", "Você escolheu fazer o 'miolo'.")
#     # process_casamento_miolo()

# def fazer_z():
#     messagebox.showinfo("Escolha", "Você escolheu fazer a capa.")
#     # process_casamento_capa()

# Criar janela principal
# janela = tk.Tk()
# janela.title("Escolha uma opção")
# janela.geometry("800x600")

# # Texto de instrução
# label = tk.Label(janela, text="Vc quer:", font=("Arial", 35))
# label.pack(pady=25)

# # Botões de escolha
# btn_x = tk.Button(janela, text="Básico", font=("Arial", 25), command=fazer_x)
# btn_x.pack(pady=15)

# btn_y = tk.Button(janela, text="Miolo", font=("Arial", 25), command=fazer_y)
# btn_y.pack(pady=15)

# btn_z = tk.Button(janela, text="Capa", font=("Arial", 25), command=fazer_z)
# btn_z.pack(pady=15)

# # Iniciar a interface
# janela.mainloop()



# Teste de execução de edição_data_sync


# from datetime import datetime, timedelta
# from data_edition_sync import EdicaoDataSync
# import os
# import sys
# raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(raiz_projeto)
# import Global.settings as cg
# import Global.utils as ut
# from App.Modulos_quark.data_formatador import formatar_data

# sync = EdicaoDataSync(edicao_inicial=6496, data_inicial=datetime(2024, 8, 26))

# # Obter data por edição
# data = sync.obter_data_por_edicao(8900)
# print("📅 Data da edição 8900:", data.strftime('%d/%m/%Y'))

# # Obter edição por data
# edicao = sync.obter_edicao_por_data(datetime(2025, 9, 26))
# edicao_amanha = sync.obter_edicao_por_data(datetime.now() + timedelta(days=1))
# print("📰 Edição correspondente à data:", edicao_amanha)

# # Gerar várias edições e datas
# # lista = sync.gerar_edicoes_e_datas(15)
# # for ed, dt in lista:
# #     print(f"Edição {ed} → {dt.strftime('%A, %d/%m/%Y')}")
#     # print(f"{data}")

# print(f"..")
# print(f"..")
# print(f"..")

# data = sync.obter_data_por_edicao(6895)
# hoje = datetime.now()
# data_amanha = hoje + timedelta(days=1)
# print("📅 Data da edição de amanha:", formatar_data(data_amanha, tipo="dia_semana"))

# edicao_data_sync.py - VERSÃO COM CLASSE
# from datetime import datetime, timedelta
# import os
# import sys
# from datetime import datetime, timedelta
# raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(raiz_projeto)
# import Global.settings as cg
# import Global.utils as ut
# from App.Modulos_quark.data_formatador import formatar_data



# def ajustar_data(data):
#     return data + timedelta(days=1) if data.weekday() == 6 else data

# class EdicaoDataSync:
#     """
#     Classe para sincronizar edições com datas e vice-versa.
#     """

#     def __init__(self, edicao_inicial=6496, data_inicial=datetime(2024, 8, 26)):
#         """
#         Inicializa com uma edição base e sua data correspondente.

#         edicao_inicial: número da edição base (int)
#         data_inicial: data da edição base (datetime)
#         """
#         self.edicao_inicial = edicao_inicial
#         self.data_inicial = data_inicial

#     def obter_data_por_edicao(self, edi_numero):
#         """
#         Retorna a data correspondente à edição informada.
#         """
        

#         if edi_numero < self.edicao_inicial:
#             raise ValueError("O número da edição não pode ser menor que a edição inicial.")

#         diff = edi_numero - self.edicao_inicial
#         ciclos = diff // 7
#         resto = diff % 7
#         dias_extra = resto if resto < 5 else 5
#         offset_total = ciclos * 7 + dias_extra
#         ajustar_data(self.data_inicial)
#         return self.data_inicial + timedelta(days=offset_total)

#     def obter_edicao_por_data(self, data_alvo):
#         """
#         Retorna o número da edição correspondente à data informada.
#         """
#         if data_alvo < self.data_inicial:
#             raise ValueError("A data não pode ser anterior à data inicial.")
        

#         dias_passados = (data_alvo - self.data_inicial).days
#         edicao_numero = self.edicao_inicial

#         while True:
#             data_edicao = self.obter_data_por_edicao(edicao_numero)
#             if data_edicao.date() == data_alvo.date():
#                 return edicao_numero
            
#             elif data_edicao > data_alvo:
#                 break
#             edicao_numero += 1

#         raise ValueError("Data não corresponde a nenhuma edição válida.")

#     def gerar_edicoes_e_datas(self, quantidade, passo=1):
#         """
#         Gera uma lista de edições e suas datas correspondentes.

#         quantidade: número de edições a gerar
#         passo: incremento entre edições (default 1)
#         """
#         edicoes_datas = []
#         for i in range(quantidade):
#             edicao = self.edicao_inicial + i * passo
#             data = self.obter_data_por_edicao(edicao)
#             edicoes_datas.append((edicao, data))
#         return edicoes_datas
       
    


# Settings usando classe no edition data sync
# import pyautogui as pg
# import os
# import sys
# from datetime import datetime, timedelta
# raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(raiz_projeto)
# import Global.settings as cg
# import Global.utils as ut
# from App.Modulos_quark.data_formatador import formatar_data
# from Global.data_edition_sync import EdicaoDataSync

# # ------------------------------------------------------------------------- Caminhos de rede
# CAMINHO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip'
# CAMINHO_MODELO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip\Modelo'
# CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
# CAMINHO_MODELO_WEB = r'\\192.168.1.249\redacao\web\Modelo páginas casadas'
# CAMINHO_WEB = r'\\192.168.1.249\redacao\web'
# CAMINHO_FOTOS = r'\\192.168.1.249\fotos'
# CAMINHO_EDD = r'\\192.168.1.249\redacao\diagramacao\edicao'

# screen_width, screen_height = pg.size()
# center_x = screen_width / 2
# center_y = screen_height / 2

# # ------------------------------------------------------------------------- Dados para Casamento
# sync = EdicaoDataSync(edicao_inicial=6496, data_inicial=datetime(2024, 8, 26))
# hoje = datetime.now()
# amanha = hoje + timedelta(days=1)

# print(f"...settings loading sucess")
# print(f"...")
# proxima_edicao = sync.obter_edicao_por_data(datetime.now() + timedelta(days=1))

# # ------------------------------------------------------------------------- Dados de edição
# quantidade_repeticoes = 2
# edicao_inicial = 6888

# # ------------------------------------------------------------------------- Posições de clique (em porcentagem da tela)
# # if pg.size() == (1366, 768):
# #     x_data = 49.48
# #     y_data = 23.06
# #     x_edicao_17 = 44.17
# #     y_edicao_17 = 12.41
# #     x_edicao_capa = 13.91
# #     y_edicao_capa = 41.30
# # elif pg.size() == (1920, 1080):
# #     x_data = 68.45
# #     y_data = 33.20
# #     x_edicao_17 = 41.14
# #     y_edicao_17 = 15.40
# #     x_edicao_capa = 18.74
# #     y_edicao_capa = 58.07

# # ------------------------------------------------------------------------- Tempos de espera
# TEMPO_ABERTURA = 4
# TEMPO_FECHAMENTO = 3
# TIMETOCLOSE = 6


# # x_data = 49.48
# # y_data = 23.06
# # x_edicao_17 = 44.17
# # y_edicao_17 = 12.41
# # x_edicao_capa = 13.91
# # y_edicao_capa = 41.30

# # ------------------------------------------------------------------------- Ativar isso se quiser usar posições absolutas(essas funcionam na maquina do comercial)
# x_data = 850
# y_data = 259
# x_edicao_17 = 560
# y_edicao_17 = 121
# x_edicao_capa = 346
# y_edicao_capa = 448

# if __name__ == "__main__":
#     # print(f"Tamanho da tela: {pg.size()}")
#     # print(f"Centro da tela: ({center_x}, {center_y})")
    
#     print(f"Edição inicial: {edicao_inicial}")








# casamento ok
# import pyautogui as pg
# import time
# import keyboard as kb
# import os
# import sys
# import tkinter as tk
# from tkinter import messagebox
# from datetime import datetime, timedelta

# raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(raiz_projeto)

# from App.Modulos_quark.data_formatador import formatar_data
# import Global.settings as cfg
# import Global.utils as utl
# import Global.data_edition_sync as sy_de

# # ------------------------------------------------------------------------- Constantes
# pg.PAUSE = 0.3 
# pg.FAILSAFE = True

# # sync = syde.EdicaoDataSync(edicao_inicial=6496, data_inicial=datetime(2024, 8, 26))
# # amanha = datetime.now() + timedelta(days=1)
# # dia_x = formatar_data(amanha, tipo="dia_semana")
# # edicao_x = sync.obter_edicao_por_data(amanha)
# # EDD = f"{edicao_x} - {dia_x}" 
# EDD = f"6897 - Quarta-feira"

# # ------------------------------------------------------------------------- Funções
# def take_file(arquivo):
#     kb.press_and_release('ctrl+f')
#     time.sleep(0.5)
#     kb.write(str(arquivo))
#     time.sleep(2)
#     pg.click(cfg.center_x, cfg.center_y)
#     pg.press('down')
#     time.sleep(0.3)
#     pg.press('down')
#     time.sleep(0.3)
#     kb.press_and_release('enter')

# def open_web():
#     os.startfile(cfg.CAMINHO_WEB + "\\" + EDD)
#     time.sleep(0.3)
#     utl
# # ------------------------------------------------------------------------- Funções específicas
# def close_and_open_quark():
#     pg.hotkey('alt', 'f4')
#     pg.hotkey('win', 's')
#     pg.hotkey('win', '1')
#     time.sleep(4)

# def take_tool(tool):
#     pg.click(cfg.center_x, 10)
#     kb.press(str(tool))

# def confirmancia():
#     pg.press('down')
#     pg.press('enter')
    
# def open_paste_page_done():
#     pg.press('esc')
#     take_tool("v")
#     pg.hotkey('ctrl', '0')
#     pg.hotkey('ctrl', 'o')
#     time.sleep(0.2)
#     pg.hotkey('ctrl', 'a')
#     time.sleep(0.2)
#     kb.write(cfg.CAMINHO_EDD + "\\" + EDD + "\\" + 'Páginas prontas')
#     time.sleep(0.2)
#     pg.press('enter')
#     time.sleep(0.2)
    
# def agrupar_e_fechar_agora():
#     take_tool("v")
#     pg.hotkey('ctrl', 'a')
#     pg.hotkey('ctrl', 'g')
#     time.sleep(0.2)
#     pg.hotkey('ctrl', 's')
#     time.sleep(0.2)
#     pg.press('enter')
#     time.sleep(0.2)
#     pg.hotkey('ctrl', 'c')
#     pg.hotkey('ctrl', 'f4')
#     time.sleep(cfg.TIMETOCLOSE)

# def move_page(left, right):
#     pg.hotkey('ctrl', 'shift', 'alt', 'm')
#     time.sleep(0.2)
#     kb.write(str(left))
#     time.sleep(0.2)
#     pg.press('tab')
#     time.sleep(0.2)
#     kb.write(str(right))
#     pg.press('enter')
#     time.sleep(0.2)
#     pg.press('down')
#     time.sleep(0.2)
#     pg.press('up')
    
# def process_page(page_number, is_even):
#     time.sleep(0.3)
#     open_paste_page_done()
#     pg.write(str(page_number))
#     confirmancia()
#     time.sleep(5)
#     agrupar_e_fechar_agora()
#     time.sleep(cfg.TIMETOCLOSE)
#     time.sleep(cfg.TIMETOCLOSE)
#     time.sleep(0.3)
#     pg.hotkey('ctrl', '0')
#     pg.click(cfg.center_x, cfg.center_y)
#     pg.hotkey('ctrl', 'v')
#     time.sleep(5)
#     time.sleep(2)
#     if is_even: 
#         move_page(10, 20) 
#     else: 
#         move_page(290, 20)
#     pg.hotkey('ctrl', 's')
#     time.sleep(0.3)

# def process_casamento(nome_arquivo, paginas):
#     open_web()
#     take_file(nome_arquivo)
#     close_and_open_quark()
#     for page_number in paginas:
#         is_even = page_number % 2 == 0
#         process_page(page_number, is_even)
#     time.sleep(0.5)

# def process_casamento_basico():
#     process_casamento("13_16", [13, 16])
#     process_casamento("14_15", [14, 15])
#     process_casamento("17_20", [17, 20])

# def process_casamento_miolo():
#     print('miolo')
#     process_casamento("10_11", [10, 11])
#     process_casamento("9_12", [9, 12])
#     process_casamento("3_6", [3, 6])
#     process_casamento("4_5", [4, 5])

# def process_casamento_capa():
#     process_casamento("2_7", [2, 7])    
#     process_casamento("1_8", [8, 1])
#     print('capa')

# def process_casamento_primeiro_caderno():
#     process_casamento_miolo()
#     process_casamento_capa()
    
# def process_casamento_completo():
#     process_casamento_basico()
#     process_casamento_primeiro_caderno()

# # ------------------------------------------------------------------------- Executando 
# time.sleep(5)
# process_casamento_basico()
# # process_casamento_miolo() 
# # pg.hotkey('win', 's')
# # pg.hotkey('win', '3')
# print("ACABOU XD")
# # print(formatar_data(sc.data, tipo='dia_semana'))
# # print(formatar_data(sc.data))



# # def fazer_escolha(opcao):
# #     EDD = entrada_edicao.get()
# #     if EDD.strip() == "":
# #         messagebox.showwarning("Atenção", "Por favor, digite o número da edição.")
# #         return EDD
# #     messagebox.showinfo("Escolha", f"Edição {EDD} selecionada.\nVocê escolheu fazer {opcao}.")
# #     print(EDD)


# # # Criar janela principal
# # janela = tk.Tk() 
# # janela.title("Casamento")
# # janela.geometry("300x250")


# # # Texto de instrução
# # label = tk.Label(janela, text="Edição:", font=("Noto Serif", 20))
# # label.pack(pady=10)


# # # Caixa de entrada para número da edição
# # label_edicao = tk.Label(janela, text="Digite o número da edição:")
# # label_edicao.pack()
# # entrada_edicao = tk.Entry(janela)
# # entrada_edicao.pack(pady=5)

# # # Botões de escolha
# # btn_x = tk.Button(janela, text="Básico", command=lambda: fazer_escolha("o básico"))
# # btn_x.pack(pady=5)

# # # btn_y = tk.Button(janela, text="Miolo", command=lambda: fazer_escolha("o miolo"))
# # # btn_y.pack(pady=5)

# # # btn_z = tk.Button(janela, text="Capa", command=lambda: fazer_escolha("a capa"))
# # # btn_z.pack(pady=5)

# # # Iniciar a interface
# # janela.mainloop()




# cabeçlho 01/10


# import os
# import sys
# import time
# import locale
# from datetime import datetime, timedelta
# import pyautogui as pg
# import keyboard as kb
# from Modulos_quark.data_formatador import formatar_data
# from Modulos_quark.edicao_formatador import gerar_edicoes
# from Modulos_quark.explorer_utils import verificar_windows 
# from pywinauto import Desktop

# modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(modulo_path)
# import Global.edition_sync as sc
# import Global.settings as cg
# import Global.utils as ut

# # ---------------------------- CONFIGURAÇÕES ----------------------------
# pg.PAUSE = 0.5
# pg.FAILSAFE = True
# time.sleep(1)

# locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")
# SISTEMA_OPERACIONAL = verificar_windows()

# # ---------------------------- FUNÇÕES UTILITÁRIAS ----------------------------
# def log(mensagem): 
#     print(f"[{datetime.now().strftime('%H:%M:%S')}] {mensagem}")

# def atalho_endereço():
#     windows = SISTEMA_OPERACIONAL
#     return ('ctrl', 'l') if "Windows 11" in windows else ('ctrl', 'l')

# def ir_para(específico=None):
#     pg.hotkey(*atalho_endereço())
#     time.sleep(0.2)
#     if específico:
#         kb.write(específico) 
#     pg.press('enter')
#     time.sleep(0.2)

# # ---------------------------- EXPLORADOR DE ARQUIVOS ----------------------------
# def pasta_esta_aberta(*nomes):
#     janelas = Desktop(backend="uia").windows()
#     for janela in janelas:
#         if janela.class_name() == "CabinetWClass":
#             titulo = janela.window_text().lower()
#             for nome in nomes:
#                 if nome.lower() in titulo:
#                     return True
#     return False

# def criar_pasta(nome, em=None):
#     if em:
#         ir_para(em)
#     time.sleep(0.3)
#     ut.max_windows()
#     time.sleep(0.3)
#     pg.click(cg.center_x, cg.center_y)
#     pg.hotkey('ctrl', 'shift', 'n')
#     time.sleep(0.3)
#     kb.write(nome)
#     pg.press('enter')
#     time.sleep(0.3)

# def copiar_modelo_para_pasta(caminho, ed, data_formatada, de=None):
#     if de:
#         ir_para(de)
#     nome_pasta = f"{ed.replace('.', '')} - {data_formatada}"
#     pg.click(cg.center_x, cg.center_y)
#     pg.hotkey('ctrl', 'a')
#     pg.hotkey('ctrl', 'c')
#     time.sleep(0.2)
#     ir_para(f"{caminho}\\{nome_pasta}")
#     pg.hotkey('ctrl', 'v')
#     time.sleep(0.5)

# def abrir_pasta(endereco):
#     os.startfile(endereco)
#     ut.max_windows()
#     pg.click(cg.center_x, cg.center_y)

# # ---------------------------- FUNÇÕES UTILITÁRIAS (QUARK)----------------------------
# def abrir_sugestão():
#     time.sleep(0.2)
#     pg.press('down')
#     time.sleep(0.2)
#     pg.press('enter')
#     time.sleep(cg.TEMPO_ABERTURA)

# def selecionar_ferramenta(tecla):
#     time.sleep(0.2)
#     pg.click(cg.center_x, 10)   
#     time.sleep(0.2)
#     pg.press("v")
#     kb.press(tecla)

# def preencher_data(data_formatada):
#     selecionar_ferramenta("v")
#     pg.click(cg.x_data, cg.y_data)
#     selecionar_ferramenta("t")
#     pg.press('t', presses=2)
#     time.sleep(0.4)
#     pg.hotkey('ctrl', 'a')
#     time.sleep(0.4)
#     kb.write(data_formatada)

# def aplicar_autodata(numero, edicao_formatada, dia_semana, data_formatada):
#     pg.press('esc', presses=3)
#     pg.hotkey('ctrl', 'o')
#     nome_pasta = f"{edicao_formatada.replace('.', '')} - {dia_semana}"
#     kb.write(f"{cg.CAMINHO_ADIANTO}\\{nome_pasta}")
#     pg.press('enter')
#     pg.write(str(numero))
#     abrir_sugestão()
#     preencher_data(data_formatada)

# def fechar_pagina():
#     pg.press('esc', presses=3)
#     time.sleep(0.2)
#     pg.hotkey('ctrl', 's')
#     time.sleep(0.2)
#     pg.press('esc', presses=3)
#     pg.hotkey('ctrl', 'f4')
#     time.sleep(cg.TEMPO_FECHAMENTO)

# # ---------------------------- AUTODATA ----------------------------
# def autodata_paginas(edicao_formatada, dia_semana, data_formatada):
#     for i in range(20, 1, -1):
#         if i in [17, 18, 19]:
#             continue
#         else:
#             aplicar_autodata(i, edicao_formatada, dia_semana, data_formatada)
#             fechar_pagina()
           
# def autodata_edicao_1(edicao_formatada, data_formatada, dia_semana=None):
#     pg.press('esc', presses=3)
#     pg.hotkey('ctrl', 'o')
#     pg.write('1')
#     abrir_sugestão()
#     time.sleep(3)
#     selecionar_ferramenta("v")
#     pg.click(cg.x_edicao_capa, cg.y_edicao_capa)
#     selecionar_ferramenta("t")
#     pg.press('t', presses=4)
#     pg.press('backspace', presses=5)
#     kb.write(f"nº {edicao_formatada} ")
#     pg.press('right', presses=2)
#     pg.press('backspace')
#     kb.write(f"|  {data_formatada}")
#     fechar_pagina()

# def autodata_edicao_17(edicao_formatada, data_formatada, dia_semana):
#     pg.press('esc', presses=3)
#     pg.hotkey('ctrl', '0')
#     pg.hotkey('ctrl', 'o')
#     time.sleep(0.3)
#     kb.write(cg.CAMINHO_ADIANTO + '\\' + f"{edicao_formatada.replace('.', '')} - {dia_semana}")
#     pg.press('enter')
#     time.sleep(0.5)
#     kb.write('17')
#     abrir_sugestão()
#     pg.press('esc', presses=3)
#     preencher_data(data_formatada)
#     time.sleep(0.3)
#     pg.press('esc', presses=3)
#     selecionar_ferramenta("v")
#     pg.hotkey('ctrl', '0')
#     pg.click(cg.x_edicao_17, cg.y_edicao_17)
#     selecionar_ferramenta("t")
#     pg.press('t', presses=4)
#     pg.hotkey('ctrl', 'a')
#     kb.write(f"Ano 21 - nº {edicao_formatada}")
#     fechar_pagina()

# # ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------
# def Modelo_diário():
#     log(f"📦 Gerando edições...")
#     data = datetime.now() + timedelta(days=1)
    
#     for _ in range(cg.quantidade_repeticoes):
#         edicoes = gerar_edicoes(cg.edicao_inicial, 5)

#         for ed in edicoes:
#             dia_semana = formatar_data(data, tipo='dia_semana')
#             pasta_nome = f"{ed.replace('.', '')} - {dia_semana.capitalize()}"
#             info = {
#             "edicao_formatada": ed,
#             "data_formatada": formatar_data(data),
#             "dia_semana": formatar_data(data, tipo='dia_semana')
#             }
#             modelo_path = {
#             0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
#             5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
#             }.get(data.weekday(), r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição')

#             # ---------------CRIANDO PASTAS, COPIANDO MODELOS E APLICANDO CABEÇALHO--------
#             # if pasta_esta_aberta("4 Adianto de novas edições"):
#             #     abrir_pasta(cg.CAMINHO_ADIANTO)
#             #     ir_para(cg.CAMINHO_PAGFLIP)
#             # elif pasta_esta_aberta("fotos"):
#             #     abrir_pasta(cg.CAMINHO_FOTOS)
#             #     ir_para(cg.CAMINHO_PAGFLIP)
#             # elif pasta_esta_aberta("00 Pagflip"):
#             #     abrir_pasta(cg.CAMINHO_PAGFLIP)
#             # else:
#             #     abrir_pasta(cg.CAMINHO_PAGFLIP)
            
#             # criar_pasta(pasta_nome)

#             # criar_pasta(pasta_nome, cg.CAMINHO_WEB)
#             # copiar_modelo_para_pasta(cg.CAMINHO_WEB, ed, dia_semana, cg.CAMINHO_MODELO_WEB)

#             # criar_pasta(pasta_nome, cg.CAMINHO_FOTOS)
        
#             # criar_pasta(pasta_nome, cg.CAMINHO_ADIANTO).capitalize()
#             # copiar_modelo_para_pasta(cg.CAMINHO_ADIANTO, ed, dia_semana, modelo_path)
#             # pg.hotkey('alt', 'up')

#             # # -------------------------------------------------------------------------Aplicando autodata
#             # ut.open_software(1) #Abrindo Quark
#             # selecionar_ferramenta("v")
#             # autodata_edicao_17(**info) #prepara o local no quark
#             # autodata_paginas(**info)
#             # autodata_edicao_1(**info)               
#             log(f"📦 Edição {ed} gerada com sucesso. Data referente -->> {formatar_data(data).capitalize()}")
#             data += timedelta(days=1)
#             data = ut.ajustar_data(data)
#         cg.edicao_inicial += 7

# if __name__ == "__main__":
#     Modelo_diário()
#     ut.open_software(4) #Abrindo Vscode
#     print('acabou')
    

# def create_models(): #vou exportar essa função para o all_in_one para executar tudo de uma vez
#     Modelo_diário()