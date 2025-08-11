import pyautogui as pg
import time
import os

# time.sleep(3)

# print(pyautogui.position())


# # conversão para %%


# screen_width, screen_height = pyautogui.size()
# x = 959
# y = 252

# # Calculando a posição em porcentagem
# x_percent = (x / screen_width) * 100
# y_percent = (y / screen_height) * 100

# print(f"Posição ({x}, {y}) corresponde a aproximadamente {x_percent:.2f}% do eixo X e {y_percent:.2f}% do eixo Y.")



time.sleep(0.5)  # Tempo para posicionar o cursor
x, y = pg.position()  # Captura a posição atual do cursor

# Obtendo tamanho da tela
screen_width, screen_height = pg.size()

# Calculando a posição em porcentagem
x_percent = (x / screen_width) * 100
y_percent = (y / screen_height) * 100

# Exibindo os valores no terminal
print(f"Posição: ({x}, {y})")
print(f"Porcentagem: {x_percent:.2f}% do eixo X, {y_percent:.2f}% do eixo Y")

# Gerando o próprio código pronto para copiar e reutilizar
codigo_gerado = f"""
x = {x}, y = {y}
x_percent, y_percent = {x_percent:.2f}, {y_percent:.2f}
"""

print("\nCopie e cole o código abaixo:")
print(codigo_gerado)
# Move o cursor para a posição capturada

DATA = 64.28
EDICAO = 90

screen_width, screen_height = pg.size()
center_x = screen_width / 2
center_y = screen_height / 2

def click(x_percent, y_percent):
    screen_width, screen_height = pg.size()
    x = int((x_percent / 100) * screen_width)
    y = int((y_percent / 100) * screen_height)
    pg.moveTo(x, y)
    print(f"Movido para ({x}, {y}) que corresponde a {x_percent}% do eixo X e {y_percent}% do eixo Y.")

# Exemplo de uso
# click(DATA)

CAMINHO_ADIANTO = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'

def abrir_pasta(endereco):
    os.startfile(endereco)
    pg.click(center_x, center_y)

abrir_pasta(CAMINHO_ADIANTO)