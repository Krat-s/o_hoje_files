import pyautogui as pg
import time

# time.sleep(3)

# print(pyautogui.position())

# # Calculando a posição em porcentagem
# x_percent = (x / screen_width) * 100
# y_percent = (y / screen_height) * 100

# print(f"Posição ({x}, {y}) corresponde a aproximadamente {x_percent:.2f}% do eixo X e {y_percent:.2f}% do eixo Y.")

time.sleep(3)  # Tempo para posicionar o cursor
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

def mover_para_percentual(x_percent, y_percent):
    screen_width, screen_height = pg.size()
    x = int((x_percent / 100) * screen_width)
    y = int((y_percent / 100) * screen_height)
    pg.moveTo(x, y)
    print(f"Movido para ({x}, {y}) que corresponde a {x_percent}% do eixo X e {y_percent}% do eixo Y.")

# Exemplo de uso
if __name__ == "__main__":
    mover_para_percentual(49.48, 23.00)





x_data = 49.48
y_data = 23.06
x_edicao_17 = 44.17
y_edicao_17 = 12.41
x_edicao_capa = 13.91
y_edicao_capa = 41.30

x_data = 68.45
y_data = 33.20
x_edicao_17 = 41.14
y_edicao_17 = 15.40
x_edicao_capa = 18.74
y_edicao_capa = 58.07