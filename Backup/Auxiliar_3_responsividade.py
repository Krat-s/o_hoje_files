# import Auxiliar
import pyautogui as pg  
pg.size()

def clicks():
    if pg.size() == (1920, 1080):
        x_data = 49.48
        y_data = 23.06
        x_edicao_17 = 44.17
        y_edicao_17 = 12.41
        x_edicao_capa = 13.91
        y_edicao_capa = 41.30


        # x_data = 49.48
        # y_data = 23.06
        # x_edicao_17 = 44.17
        # y_edicao_17 = 12.41
        # x_edicao_capa = 13.91
        # y_edicao_capa = 41.30
        print("Resolução detectada: 1920x1080")
    elif pg.size() == (1366, 768):
        x_data = 68.45
        y_data = 33.20
        x_edicao_17 = 41.14
        y_edicao_17 = 15.40
        x_edicao_capa = 18.74
        y_edicao_capa = 58.07


        # x_data = 68.45
        # y_data = 33.20
        # x_edicao_17 = 41.14
        # y_edicao_17 = 15.40
        # x_edicao_capa = 18.74
        # y_edicao_capa = 58.07
        print("Resolução detectada: 1366x768")
    else: 
        return print("não sei")

# Tempos de espera
TEMPO_ABERTURA = 4
TEMPO_FECHAMENTO = 3


if __name__ == "__main__":
    clicks()

    # pg.moveTo(x_data)