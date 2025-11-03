import pyautogui as pg  
import time
import pytesseract
import os
import sys
from PIL import Image, ImageDraw, ImageFont

def get_screen_text(region=None):
    """Captura a tela (ou região) e retorna o texto detectado."""
    screenshot = pg.screenshot(region=region)
    return pytesseract.image_to_string(screenshot)

def wait_until_text_disappears(text, region=None, check_interval=1):
    """Espera até que o texto sumir da tela."""
    print(f"Aguardando '{text}' desaparecer...")
    img = pg.screenshot(region=region)
    img = img.convert("L")  # escala de cinza
    img = img.point(lambda x: 0 if x < 180 else 255)  # binarização
    text = pytesseract.image_to_string(img)
   
    while True:
        screen_text = get_screen_text(region).lower()
        if text.lower() not in screen_text:
            print(f"'{text}' não encontrado, continuando o código.")
            break
        time.sleep(check_interval)

def wait_until_text_appears(text, region=None, check_interval=1):
    """Espera até que o texto apareça na tela."""
    # print(f"Aguardando '{text}' aparecer...")
    # img = pg.screenshot(region=region)
    # img = img.convert("L")  # escala de cinza
    # img = img.point(lambda x: 0 if x < 180 else 255)  # binarização
    # text = pytesseract.image_to_string(img)

    while True:
        screen_text = get_screen_text(region).lower()
        if text.lower() in screen_text:
            print(f"'{text}' detectado! Continuando...")
            pg.alert('Abobrinha a vista')
            break
        time.sleep(check_interval)




region_png_qk_ldg = x=493, y=304, w=123, h=111

# Exemplo de uso
print("inicio")
# wait_until_text_disappears("Loading pages", region=(500, 300, 600, 200))
wait_until_text_appears("ABOBRINHA", region=region_png_qk_ldg)

