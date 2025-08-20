import os
import time
import locale
from datetime import datetime, timedelta
import pyautogui as pg
import keyboard as kb
from Modulos_quark.data_formatador import formatar_data
from Modulos_quark.edicao_formatador import gerar_edicoes
from Modulos_quark.explorer_utils import verificar_windows 
from pywinauto import Desktop

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.5
pg.FAILSAFE = True
time.sleep(1)

locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")

screen_width, screen_height = pg.size()
center_x = screen_width / 2
center_y = screen_height / 2

edicao_inicial = 8888
quantidade_por_semana = 5
quantidade_repeticoes = 1
data_inicial = datetime(2025, 7, 21) #Precisa ser uma segunda-feira

# ---------------------------- CONSTANTES ----------------------------
SISTEMA_OPERACIONAL = verificar_windows()
CAMINHO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip'
CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
CAMINHO_WEB = r'\\192.168.1.249\redacao\web'
CAMINHO_MODELO_WEB = r'\\192.168.1.249\redacao\web\Modelo páginas casadas'
CAMINHO_FOTOS = r'\\192.168.1.249\fotos'
TEMPO_ABERTURA = 4
TEMPO_FECHAMENTO = 3

# ---------------------------- POSIÇÕES DE CLIQUE ----------------------------
# --MARKETING 1
x_data = 49.48
y_data = 23.06
x_edicao_17 = 44.17
y_edicao_17 = 12.41
x_edicao_capa = 13.91
y_edicao_capa = 41.30

# --COMERCIAL 3
# x_data = 68.45
# y_data = 33.20
# x_edicao_17 = 41.14
# y_edicao_17 = 15.40
# x_edicao_capa = 18.74
# y_edicao_capa = 58.07

# ---------------------------- FUNÇÕES UTILITÁRIAS ----------------------------
def log(mensagem): 
    """Função para registrar mensagens com timestamp. (Não necessário para o funcionamento do script, mas útil para depuração)"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {mensagem}")

def atalho_endereço():
    """Retorna o atalho de teclado para acessar a barra de endereços do explorador de arquivos, dependendo do sistema operacional."""
    windows = SISTEMA_OPERACIONAL
    return ('ctrl', 'l') if "Windows 11" in windows else ('ctrl', 'd')

def acessar_busca(específico=None):
    """Acessa a barra de endereços do explorador de arquivos e, opcionalmente, escreve um caminho específico.""" 
    pg.hotkey(*atalho_endereço())
    time.sleep(0.2)
    if específico:
        kb.write(específico) 

def ajustar_data(data):
    """Ajusta a data para o dia seguinte se for domingo, caso contrário, retorna a data original."""
    return data + timedelta(days=1) if data.weekday() == 6 else data

def click(x_percent, y_percent):
    """Clica em uma posição específica da tela baseada em porcentagens da largura e altura da tela."""
    x = int((x_percent / 100) * screen_width)
    y = int((y_percent / 100) * screen_height)
    pg.click(x, y)

def abrir_software(numero):
    """Abre um software específico usando o atalho do Windows."""
    pg.hotkey('win', 's')
    pg.hotkey('win', str(numero))
    pg.press('enter')
    time.sleep(0.5)

def maximizar_janela():
    """Maximiza a janela ativa usando atalhos de teclado."""
    kb.press_and_release('alt+space')
    time.sleep(0.2)
    kb.press_and_release('x')

# ---------------------------- EXPLORADOR DE ARQUIVOS ----------------------------
def pasta_esta_aberta(nome_pasta):
    """Verifica se uma pasta específica está aberta no explorador de arquivos do Windows."""
    janelas = Desktop(backend="uia").windows()
    for janela in janelas:
        if janela.class_name() == "CabinetWClass":
            titulo = janela.window_text()
            if nome_pasta.lower() in titulo.lower():
                return True
    return False

def criar_pasta(nome):
    """Cria uma nova pasta com o nome especificado no local atual do explorador de arquivos."""
    time.sleep(0.3)
    maximizar_janela()
    time.sleep(0.3)
    pg.click(center_x, center_y)
    pg.hotkey('ctrl', 'shift', 'n')
    time.sleep(0.3)
    kb.write(nome)
    pg.press('enter')
    time.sleep(0.3)

def copiar_modelo_para_pasta(ed, data_formatada):
    """Copia o modelo para a pasta recém-criada."""
    nome_pasta = f"{ed.replace('.', '')} - {data_formatada}"
    pg.click(center_x, center_y)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    time.sleep(0.3)
    acessar_busca()
    kb.write(f"{CAMINHO_ADIANTO}\\{nome_pasta}")
    pg.press('enter')
    pg.hotkey('ctrl', 'v')

def abrir_pasta(endereco):
    """Abre uma pasta específica no explorador de arquivos do Windows."""
    os.startfile(endereco)
    maximizar_janela()
    pg.click(center_x, center_y)

# ---------------------------- FUNÇÕES UTILITÁRIAS (QUARK)----------------------------
def selecionar_ferramenta(tecla):
    """Seleciona uma ferramenta específica no Quark usando a tecla fornecida."""
    time.sleep(0.2)
    pg.click(center_x, 10)
    time.sleep(0.2)
    pg.press("v")
    kb.press(tecla)

def preencher_data(data_formatada):
    """Preenche a data da edição atual no Quark usando a ferramenta de texto."""
    selecionar_ferramenta("v")
    click(x_data, y_data)
    selecionar_ferramenta("t")
    pg.press('t', presses=2)
    time.sleep(0.4)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.4)
    kb.write(data_formatada)

def aplicar_autodata(numero, edicao_formatada, dia_semana, data_formatada):
    """Aplica a autodata para uma edição específica no Quark."""
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'o')
    nome_pasta = f"{edicao_formatada.replace('.', '')} - {dia_semana}"
    kb.write(f"{CAMINHO_ADIANTO}\\{nome_pasta}")
    pg.press('enter')
    pg.write(str(numero))
    time.sleep(0.3)
    pg.press('down')
    time.sleep(0.3)
    pg.press('enter')
    time.sleep(TEMPO_ABERTURA)
    preencher_data(data_formatada)
    time.sleep(0.4)
    pg.press('esc')
    pg.hotkey('ctrl', 's')

def fechar_pagina():
    pg.hotkey('ctrl', 'f4')
    time.sleep(TEMPO_FECHAMENTO)

# ---------------------------- AUTODATA ----------------------------
def autodata_paginas(edicao_formatada, dia_semana, data_formatada):
    """Aplica a autodata e edição para todas as páginas da edição no quark, exceto 1, 17, 18 e 19."""
    for i in range(20, 1, -1):
        if i in [17, 18, 19]:
            continue
        else:
            aplicar_autodata(i, edicao_formatada, dia_semana, data_formatada)
            fechar_pagina()
           
def autodata_edicao_1(edicao_formatada, data_formatada, dia_semana):
    """Aplica a autodata e edição para a capa da edição no quark."""
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', 'o')
    pg.write('1')
    pg.press('down')
    pg.press('enter')
    time.sleep(TEMPO_ABERTURA + 3)
    selecionar_ferramenta("v")
    click(x_edicao_capa, y_edicao_capa)
    selecionar_ferramenta("t")
    pg.press('t', presses=4)
    pg.press('backspace', presses=5)
    kb.write(f"nº {edicao_formatada} ")
    pg.press('right', presses=2)
    pg.press('backspace')
    kb.write(f"|  {data_formatada}")
    pg.press('esc', presses=2)
    pg.hotkey('ctrl', 's')
    time.sleep(0.2)
    fechar_pagina()

def autodata_edicao_17(edicao_formatada, data_formatada, dia_semana):
    """Aplica a autodata e edição para a página 17 da edição no quark."""
    pg.press('esc', presses=3)
    pg.hotkey('ctrl', '0')
    pg.hotkey('ctrl', 'o')
    time.sleep(0.3)
    kb.write(CAMINHO_ADIANTO + '\\' + f"{edicao_formatada.replace('.', '')} - {dia_semana}")
    pg.press('enter')
    time.sleep(0.5)
    kb.write('17')
    pg.press('down')
    pg.press('enter')
    time.sleep(TEMPO_ABERTURA)
    pg.press('esc', presses=3)
    preencher_data(data_formatada)
    time.sleep(0.3)
    pg.press('esc', presses=3)
    selecionar_ferramenta("v")
    pg.hotkey('ctrl', '0')
    click(x_edicao_17, y_edicao_17)
    selecionar_ferramenta("t")
    pg.press('t', presses=4)
    pg.hotkey('ctrl', 'a')
    kb.write(f"Ano 21 - nº {edicao_formatada}")
    time.sleep(0.2)
    pg.hotkey('ctrl', 's')
    time.sleep(0.2)
    pg.press('esc', presses=3)
    fechar_pagina()

# ---------------------------- EXECUÇÃO PRINCIPAL ----------------------------
def Modelo_diário():
    """Função principal para gerar edições diárias no Quark."""
    log(f"📦 Gerando edições...")
    edicao = edicao_inicial
    data = data_inicial
    
    for _ in range(quantidade_repeticoes):
        edicoes = gerar_edicoes(edicao, quantidade_por_semana)

        for ed in edicoes:
            data_formatada = formatar_data(data)
            dia_semana = formatar_data(data, tipo='dia_semana')
            info = {
            "edicao_formatada": ed,
            "data_formatada": formatar_data(data),
            "dia_semana": formatar_data(data, tipo='dia_semana')
            }
            modelo_path = {
            0: r'\\192.168.1.249\redacao\arte\01 Projeto\3 - k Modelo de Segunda-feira',
            5: r'\\192.168.1.249\redacao\arte\01 Projeto\2 - k Modelo de Fim de semana',
            }.get(data.weekday(), r'\\192.168.1.249\redacao\arte\01 Projeto\1 - k Modelo da edição')

            # ---------------CRIANDO PASTAS, COPIANDO MODELOS E APLICANDO CABEÇALHO--------
            if pasta_esta_aberta("4 Adianto de novas edições"):
                abrir_pasta(CAMINHO_ADIANTO)
                acessar_busca(CAMINHO_PAGFLIP)
                pg.press('enter')
                time.sleep(0.1)

            elif pasta_esta_aberta("00 Pagflip"):
                abrir_pasta(CAMINHO_PAGFLIP)
                pg.press('enter')
                time.sleep(0.1)

            else:
                abrir_pasta(CAMINHO_PAGFLIP)

            criar_pasta(f"{ed.replace('.', '')} - {dia_semana}")
            acessar_busca(CAMINHO_WEB)
            pg.press('enter')
            time.sleep(0.1)
            criar_pasta(f"{ed.replace('.', '')} - {dia_semana}")
            acessar_busca(CAMINHO_MODELO_WEB)
            pg.press('enter')
            pg.click(center_x, center_y)
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            pg.hotkey('alt', 'up')
            acessar_busca(f"{CAMINHO_WEB}\\{ed.replace('.', '')} - {dia_semana}")     
            pg.press('enter')
            pg.hotkey('ctrl', 'v')    

            acessar_busca(CAMINHO_FOTOS)
            pg.press('enter')
            time.sleep(0.1)
            criar_pasta(f"{ed.replace('.', '')} - {dia_semana}")

            abrir_pasta(CAMINHO_ADIANTO)
            acessar_busca(CAMINHO_ADIANTO)
            pg.press('enter')
            time.sleep(0.1)
            criar_pasta(f"{ed.replace('.', '')} - {dia_semana}")
            time.sleep(0.4)
            acessar_busca()
            kb.write(modelo_path)
            pg.press('enter')
            copiar_modelo_para_pasta(ed, dia_semana)
            pg.hotkey('alt', 'up')
            time.sleep(0.3)

            # -------------------------------------------------------------------------Aplicando autodata
            abrir_software(1)
            selecionar_ferramenta("v")
            autodata_edicao_17(**info) #prepara o local no quark
            autodata_paginas(**info)
            autodata_edicao_1(**info)
                                       
            log(f"📦 Edição {ed} gerada com sucesso.")
            data += timedelta(days=1)
            data = ajustar_data(data)
        edicao += quantidade_por_semana + 2

if __name__ == "__main__":
    Modelo_diário()
