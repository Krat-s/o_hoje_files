import pyautogui as pg  
import time
import pytesseract
import os
import sys
from PIL import Image, ImageDraw, ImageFont

import os
import sys
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(raiz_projeto)

import Global.settings as cfg

def get_screen_text(region=None):
    """Captura a tela (ou região) e retorna o texto detectado."""
    screenshot = pg.screenshot(region=region)
    return pytesseract.image_to_string(screenshot)

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

def get_image(img, region=None):
    img = pg.screenshot(region=region)
    img = img.convert("L")  # escala de cinza
    img = img.point(lambda x: 0 if x < 180 else 255)  # binarização
    if pg.locateOnScreen(img, region, confidence=0.8): 
        return True
    
# def wait_until_img_apper(img):
#     get_image(img)

def wait_until_img_desappears(img, region=None):
    while get_image(img, region) is True:
        time.sleep(2)
        print('aguardando imagem desaparecer')
    else: 
        pg.alert("imagem desapareceu")

if __name__ == "__main__":
    wait_until_img_desappears("already_open x=489, y=280, w=98, h=103 selecionado em15h30.png", cfg.already_open_full_r)