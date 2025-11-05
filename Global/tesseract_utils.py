import pyautogui as pg  
import time
import pytesseract
import os
import sys
from PIL import Image, ImageDraw, ImageFont
import threading
import pytesseract

import os
import sys
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)
import Global.settings as cfg

def get_screen_text(region=None):
    screenshot = pg.screenshot(region=region)
    return pytesseract.image_to_string(screenshot)

def _current_time():
    return time.monotonic()

def wait_until_text_appears(text, region=None, check_interval=1, timeout=None, on_found=None, run_once=False):
    """Espera até o texto aparecer. Retorna True se encontrado, False se timeout.
    on_found: função chamada quando encontrado: on_found() ou on_found(match_text) se quiser.
    run_once: se True, on_found só é executado na primeira detecção (útil se for chamada repetidamente)."""

    # text: string a procurar
    # region: tupla (x, y, w, h) ou None para tela inteira
    # check_interval: tempo entre verificações (em segundos)
    # timeout: tempo máximo de espera (em segundos). None = esperar indefinidamente
    # on_found: callback (função) chamada quando o texto é detectado
    # run_once: se True, garante que on_found seja executado apenas uma vez durante essa chamada

    deadline = None if timeout is None else _current_time() + timeout
    executed = False # flag para controlar execução do callback quando run_once=True
    while True:
        screen_text = get_screen_text(region).lower()
        if text.lower() in screen_text:
            if on_found and (not run_once or not executed):
                # se existir um callback e ou não estamos limitando a execução ou ainda não executamos
                try:
                    on_found() # chama a função de callback sem argumentos
                except Exception as e:
                    print(f"Erro no callback on_found: {e}")
                executed = True
            return True
        if deadline is not None and _current_time() > deadline:
            return False
        time.sleep(check_interval)

def wait_until_text_disappears(text, region=None, check_interval=1, timeout=None):
    """Espera até o texto desaparecer. Retorna True se desapareceu, False se timeout."""
    deadline = None if timeout is None else _current_time() + timeout
    while True:
        screen_text = get_screen_text(region).lower()
        if text.lower() not in screen_text:
            return True
        if deadline is not None and _current_time() > deadline:
            return False
        time.sleep(check_interval)

def get_image(img_path, region=None, confidence=0.8):
    """Retorna True se a imagem (arquivo) for encontrada na tela."""
    try:
        loc = pg.locateOnScreen(img_path, region=region, confidence=confidence)
        return loc is not None
    except Exception as e:
        print(f"Erro ao localizar imagem: {e}")
        return False

def wait_until_img_appears(img_path, region=None, check_interval=1, timeout=None, on_found=None, run_once=False):
    deadline = None if timeout is None else _current_time() + timeout
    executed = False
    while True:
        if get_image(img_path, region):
            if on_found and (not run_once or not executed):
                try:
                    on_found()
                except Exception as e:
                    print(f"Erro no callback on_found: {e}")
                executed = True
            return True
        if deadline is not None and _current_time() > deadline:
            return False
        time.sleep(check_interval)

def wait_until_img_disappears(img_path, region=None, check_interval=1, timeout=None):
    deadline = None if timeout is None else _current_time() + timeout
    while True:
        if not get_image(img_path, region):
            return True
        if deadline is not None and _current_time() > deadline:
            return False
        time.sleep(check_interval)

# ---- execução não bloqueante (background) ----
def start_background_wait(target_fn, *args, callback_on_complete=None, daemon=True):
    """Executa target_fn(*args) em thread e chama callback_on_complete(result) quando terminar.
    target_fn deve retornar um valor (True/False)."""
    def _worker():
        result = None
        try:
            result = target_fn(*args)
        except Exception as e:
            print(f"Erro no worker: {e}")
            result = False
        if callback_on_complete:
            try:
                callback_on_complete(result)
            except Exception as e:
                print(f"Erro no callback_on_complete: {e}")

    t = threading.Thread(target=_worker, daemon=daemon)
    t.start()
    return t




if __name__ == "__main__":
    def cancel_qk():
        # pg.moveTo(829, 419)
        # time.sleep(0.2)
        # pg.click()
        print("teste")
        time.sleep(0.1)

    ok = wait_until_text_appears("already open", cfg.already_open_full_r, check_interval=0.8, timeout=10, on_found=cancel_qk, run_once=True)
    if ok:
        print("Evento ocorreu dentro do timeout")
    else:
        print("Timeout: texto não apareceu")
        
        
    