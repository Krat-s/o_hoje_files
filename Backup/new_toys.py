# import pyautogui as pg  
# import time

# import pytesseract

# pg.size()

# def teste():
#     for i in range(20):
#         print(i)
#         print('asdas')
# teste()


# from PIL import ImageGrab
# # Define uma função que espera até que um texto específico apareça na tela
# def esperar_texto(texto_alvo, timeout=10):
#     # Marca o tempo de início da espera
#     inicio = time.time()

#     # Loop que continua até o tempo limite (timeout) ser atingido
#     while time.time() - inicio < timeout:
#         # Captura uma imagem da tela inteira
#         img = ImageGrab.grab()

#         # Usa OCR para extrair o texto da imagem capturada
#         texto = pytesseract.image_to_string(img)

#         # Verifica se o texto desejado está presente na imagem (ignora maiúsculas/minúsculas)
#         if texto_alvo.lower() in texto.lower():
#             return True  # Texto encontrado, retorna sucesso

#         # Aguarda meio segundo antes de tentar novamente (evita sobrecarga)
#         time.sleep(0.5)

#     # Se o tempo limite for atingido sem encontrar o texto, retorna falso
# esperar_texto(str('ABOBRINHA'))

# while esperar_texto(True):
#         print('achou')





# import random
# import time

# # Lista de ações simuladas
# acoes = ["Principal", "Halfpage", "wide"]

# # Limite de ações a executar
# limite = 2

# # Seleciona ações aleatórias sem repetir
# acoes_escolhidas = random.sample(acoes, limite)

# # Executa cada ação com um intervalo
# for acao in acoes_escolhidas:
#     print(f"Executando: {acao}")
#     time.sleep(random.uniform(1, 2))  # Espera entre 1 e 3 segundos



import random
import time

# Lista de ações com "peso"
acoes = ["Verificar status", "Enviar alerta", "Reiniciar serviço"]
pesos = [0.5, 0.3, 0.2]  # Probabilidades relativas

# Número máximo de execuções
max_execucoes = 5

for _ in range(max_execucoes):
    acao = random.choices(acoes, weights=pesos, k=1)[0]
    print(f"Ação aleatória: {acao}")
    time.sleep(random.uniform(0.5, 2))
    