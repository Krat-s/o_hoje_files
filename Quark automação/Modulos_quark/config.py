from datetime import datetime
import pyautogui as pg

# Caminhos de rede
CAMINHO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip'
CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
CAMINHO_WEB = r'\\192.168.1.249\redacao\web'
CAMINHO_FOTOS = r'\\192.168.1.249\fotos'
CAMINHO_MODELO_WEB = r'\\192.168.1.249\redacao\web\Modelo páginas casadas'
CAMINHO_FOTOS = r'\\192.168.1.249\fotos'

# Dados de edição
edicao_inicial = 8888
quantidade_por_semana = 5
quantidade_repeticoes = 1
data_inicial = datetime(2025, 7, 21)  # Precisa ser uma segunda-feira

# Posições de clique (em porcentagem da tela)
# screen_width, screen_height = pyautogui.size()
def clicks():
    if pg.size() == ():
        x_data = 49.48
        y_data = 23.06
        x_edicao_17 = 44.17
        y_edicao_17 = 12.41
        x_edicao_capa = 13.91
        y_edicao_capa = 41.30
        print("Resolução detectada: 1920x1080")
    elif pg.size() == (1366, 768):
        x_data = 68.45
        y_data = 33.20
        x_edicao_17 = 41.14
        y_edicao_17 = 15.40
        x_edicao_capa = 18.74
        y_edicao_capa = 58.07
        print("Resolução detectada: 1366x768")

# Tempos de espera
TEMPO_ABERTURA = 4
TEMPO_FECHAMENTO = 3



# --


if __name__ == "__main__":
    clicks()