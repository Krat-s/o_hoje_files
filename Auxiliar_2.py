import os
from pywinauto import Desktop

CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
NOME_PASTA = "4 Adianto de novas edições"

def abrir_pasta(endereco):
    """Abre a pasta no Explorer."""
    os.startfile(endereco)

def verificar_explorer(nome_pasta=None):
    """Verifica se o Explorer está aberto e se a pasta está entre as janelas."""
    janelas = Desktop(backend="uia").windows()
    explorer_aberto = False
    pasta_encontrada = False

    for janela in janelas:
        if janela.class_name() == "CabinetWClass":
            explorer_aberto = True
            if nome_pasta and nome_pasta.lower() in janela.window_text().lower():
                pasta_encontrada = True

    return explorer_aberto, pasta_encontrada

# Verificação
explorer, pasta = verificar_explorer(NOME_PASTA)

verificar_explorer(NOME_PASTA) 
if True: print(f"Explorer aberto: {explorer}, Pasta encontrada: {pasta}")
if not explorer:
        print("Explorer não está aberto. Abrindo pasta...")
