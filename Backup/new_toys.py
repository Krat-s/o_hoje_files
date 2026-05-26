# import pyautogui as pg  
# import time
# import pytesseract
# import os
# import sys
# from PIL import Image, ImageDraw, ImageFont

# def get_screen_text(region=None):
#     """Captura a tela (ou região) e retorna o texto detectado."""
#     screenshot = pg.screenshot(region=region)
#     return pytesseract.image_to_string(screenshot)

# def wait_until_text_disappears(text, region=None, check_interval=1):
#     """Espera até que o texto sumir da tela."""
#     print(f"Aguardando '{text}' desaparecer...")
#     img = pg.screenshot(region=region)
#     img = img.convert("L")  # escala de cinza
#     img = img.point(lambda x: 0 if x < 180 else 255)  # binarização
#     text = pytesseract.image_to_string(img)
   
#     while True:
#         screen_text = get_screen_text(region).lower()
#         if text.lower() not in screen_text:
#             print(f"'{text}' não encontrado, continuando o código.")
#             break
#         time.sleep(check_interval)

# def wait_until_text_appears(text, region=None, check_interval=1):
#     """Espera até que o texto apareça na tela."""
#     # print(f"Aguardando '{text}' aparecer...")
#     # img = pg.screenshot(region=region)
#     # img = img.convert("L")  # escala de cinza
#     # img = img.point(lambda x: 0 if x < 180 else 255)  # binarização
#     # text = pytesseract.image_to_string(img)

#     while True:
#         screen_text = get_screen_text(region).lower()
#         if text.lower() in screen_text:
#             print(f"'{text}' detectado! Continuando...")
#             pg.alert('Abobrinha a vista')
#             break
#         time.sleep(check_interval)




# region_png_qk_ldg = 493, 304, 123, 111

# # Exemplo de uso
# print("inicio")
# # wait_until_text_disappears("Loading pages", region=(500, 300, 600, 200))
# wait_until_text_appears("ABOBRINHA", region=region_png_qk_ldg)




# ingredientes1 = {}
# ingredientes2 = {}


# def mostrar_receita(item):
#     receitas = {
#         "1": {"nome": "Ovo Frito", "ingredientes": "Ovo, Sal, Azeite", "preparo": "Frite o ovo."},
#         "2": {"nome": "Misto Quente", "ingredientes": "Pão, Queijo, Presunto", "preparo": "Toste o pão."},
#         "3": {"nome": "Salada", "ingredientes": "Alface, Tomate, Cebola", "preparo": "Combine os ingredientes."}
#     }
    
#     if item in receitas:
#         r = receitas[item]
#         print(f"\n--- {r['nome']} ---")
#         print(f"Ingredientes: {r['ingredientes']}")
#         print(f"Preparo: {r['preparo']}\n")
#     else:
#         print("\nOpção inválida!\n")

# while True:
#     print("Selecione um item:")
#     print("1. Ovo Frito")
#     print("2. Misto Quente")
#     print("3. Sair")
    
#     escolha = input("Digite o número: ")
    
#     if escolha == "3":
#         break
#     else:
#         mostrar_receita(escolha)




from InquirerPy import inquirer

opcao = inquirer.select(
    message="Escolha uma opção:",
    choices=["Iniciar", "Configurações", "Sair"]
).execute()

print(opcao)