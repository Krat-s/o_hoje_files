import os
import time
import locale
from datetime import datetime, timedelta
import pyautogui as pg
import keyboard as kb
from Modulos.data_formatador import formatar_data
from Modulos.edicao_formatador import gerar_edicoes

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True
time.sleep(1)

locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")

screen_width, screen_height = pg.size()
center_x = screen_width / 2
center_y = screen_height / 2

edicao_inicial = 6794
quantidade_por_semana = 5
quantidade_repeticoes = 2
data_inicial = datetime(2025, 7, 21) #Precisa ser uma segunda-feira

# ---------------------------- CONSTANTES ----------------------------
CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
EDD_PADRAO = "0000 - TESTE"
TEMPO_ABERTURA = 4
TEMPO_FECHAMENTO = 3

# ---------------------------- POSIÇÕES DE CLIQUE ----------------------------
x_data = int(screen_width * 0.6428)
y_data = int(screen_height * 0.3255)
x_edicao_17 = int(screen_width * 0.4173)
y_edicao_17 = int(screen_height * 0.1536)
x_edicao_capa = int(screen_width * 0.1740)
y_edicao_capa = int(screen_height * 0.4648)

# ---------------------------- FUNÇÕES UTILITÁRIAS ----------------------------
def ajustar_data(data):
    return data + timedelta(days=1) if data.weekday() == 6 else data

def abrir_software(numero):
    pg.hotkey('win', 's')
    pg.hotkey('win', str(numero))
    pg.press('enter')
    time.sleep(0.5)

def maximizar_janela():
    kb.press_and_release('alt+space')
    time.sleep(0.2)
    kb.press_and_release('x')

def selecionar_ferramenta(tecla):
    pg.click(center_x, 10)
    kb.press(tecla)

def criar_pasta(nome):
    time.sleep(0.5)
    maximizar_janela()
    time.sleep(0.5)
    pg.click(center_x, center_y)
    pg.hotkey('ctrl', 'shift', 'n')
    time.sleep(0.5)
    kb.write(nome)
    pg.press('enter')

def copiar_modelo_para_pasta(ed, data_formatada):
    nome_pasta = f"{ed.replace('.', '')} - {data_formatada}"
    pg.click(center_x, center_y)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    time.sleep(0.3)
    pg.hotkey('alt', 'd')
    kb.write(f"{CAMINHO_ADIANTO}\\{nome_pasta}")
    pg.press('enter')
    pg.hotkey('ctrl', 'v')

def preencher_data(data_formatada):
    selecionar_ferramenta("v")
    pg.click(x_data, y_data)
    selecionar_ferramenta("t")
    pg.press('t', presses=2)
    time.sleep(0.3)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.3)
    kb.write(data_formatada)

def aplicar_autodata(numero, edicao_formatada, data_formatada):
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'o')
    nome_pasta = f"{edicao_formatada.replace('.', '')} - {str(data_formatada, tipo='dia_semana')}"
    kb.write(f"{CAMINHO_ADIANTO}\\{nome_pasta}")
    pg.press('enter')
    pg.write(str(numero))
    time.sleep(0.3)
    pg.press('down')
    time.sleep(0.3)
    pg.press('enter')
    time.sleep(TEMPO_ABERTURA)
    preencher_data()
    time.sleep(0.4)
    pg.press('esc')
    pg.hotkey('ctrl', 's')

def fechar_pagina():
    pg.hotkey('ctrl', 'f4')
    time.sleep(TEMPO_FECHAMENTO)

# ---------------------------- AUTODATA ----------------------------
def autodata_paginas():
    for i in range(20, 1, -1):
        if i != 17:
            aplicar_autodata(i)
            fechar_pagina()

def autodata_edicao_1(edicao_formatada, data_formatada):
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'o')
    kb.write(f"{CAMINHO_ADIANTO}\\{EDD_PADRAO}")
    pg.press('enter')
    pg.write('1')
    pg.press('down')
    pg.press('enter')
    time.sleep(TEMPO_ABERTURA + 3)
    selecionar_ferramenta("v")
    pg.click(x_edicao_capa, y_edicao_capa)
    selecionar_ferramenta("t")
    pg.press('t', presses=4)
    time.sleep(0.3)
    pg.press('backspace', presses=5)
    kb.write(f"nº {edicao_formatada}")
    time.sleep(0.4)
    pg.press('right')
    pg.press('del')
    kb.write(f" | {data_formatada} ")
    
def autodata_edicao_17(edicao_formatada, data_formatada):
    aplicar_autodata(17, edicao_formatada, data_formatada)
    selecionar_ferramenta("v")
    pg.hotkey('ctrl', '0')
    pg.click(x_edicao_17, y_edicao_17)
    pg.hotkey('ctrl', 'a')
    kb.write(f"Ano 21 - nº {edicao_formatada}")
    time.sleep(0.2)
    pg.hotkey('ctrl', 's')
    time.sleep(0.2)
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'f4')
    time.sleep(TEMPO_FECHAMENTO)

def cabeçalho(edicao_formatada):
    autodata_edicao_17(edicao_formatada)
    autodata_paginas(edicao_formatada)
    autodata_edicao_1(edicao_formatada)

# ---------------------------- EXPLORADOR DE ARQUIVOS ----------------------------
def abrir_pasta(endereco):
    os.startfile(endereco)
    maximizar_janela()
    pg.click(center_x, center_y)

def fechar_explorer():
    pg.click(center_x, center_y)
    pg.hotkey('alt', 'f4')

def voltar_pasta():
    pg.click(center_x, center_y)
    pg.hotkey('alt', 'up')

# ---------------------------- TESTE ----------------------------
def teste(edicao_formatada, data_formatada):
    # print(f"{data_formatada}, {edicao_formatada}")
    # print(data_formatada)
    print(str(edicao_formatada).replace('.', ''), data_formatada)

# ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------
# abrir_pasta()
# pg.hotkey('win', 's')
# pg.hotkey('win', '1')

# aplicar_autodata(5)
abrir_pasta(CAMINHO_ADIANTO)


def main():
    print("📦 Edições geradas:")
    edicao = edicao_inicial
    data = data_inicial

    for _ in range(quantidade_repeticoes):
        edicoes = gerar_edicoes(edicao, quantidade_por_semana)

        for ed in edicoes:
            data_formatada = formatar_data(data)
            info = {
            "edicao_formatada": ed,
            "data_formatada": formatar_data(data)
            }
            modelo_path = {
            0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
            5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
            }.get(data.weekday(), r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição')

            # teste(**info)

#--------------------------------------------------------------------------Criando modelo da edicão
            # criar_pasta(f"{ed.replace('.', '')} - {formatar_data(data, tipo='dia_semana')}")
            # time.sleep(0.3)
            # pg.hotkey('alt', 'd')
            # kb.write(modelo_path)
            # pg.press('enter')
            # copiar_modelo_para_pasta(ed, formatar_data(data, tipo='dia_semana'))
            # voltar_pasta()
            # time.sleep(0.3)

#--------------------------------------------------------------------------Preprarando area de operação
            abrir_software(1)
            time.sleep(0.5)
            # pg.press('esc', presses=3)
            # pg.hotkey('ctrl', '0')
            # pg.hotkey('ctrl', 'o')
            # kb.write(CAMINHO_ADIANTO + '\\' + f"{ed.replace('.', '')} - {formatar_data(data, tipo='dia_semana')}")
            # time.sleep(0.3)
            # pg.press('enter')
            # pg.press('esc', presses=3)
            autodata_edicao_17(**info)





            # autodata_paginas()
            

#----------------------------------------------------Verificar parte de baixo e adaptar para última sugestão do copilot
            # 

            #  autodata_edicao_17()
            # abrir_software(4)  # Explorer
            # pg.hotkey('alt', 'up')
            # pg.click(center_x, center_y)

            # Se quiser aplicar cabeçalho apenas nos dias úteis:
            # if data_da_edicao.weekday() < 5:
            #     cabeçalho()
        
                      
            # print(f"📦 {ed} - {data_formatada}")
            data += timedelta(days=1)
            data = ajustar_data(data)
        edicao += quantidade_por_semana + 2

if __name__ == "__main__":
    main()
    



    # \\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições\6794 - Segunda-feira