import time
import pyautogui as pg  
import pytesseract
import threading

import settings.settings as cfg
import utils as utl
from Logs.logs import log



def get_screen_text(region=None):
    screenshot = pg.screenshot(region=region)
    return pytesseract.image_to_string(screenshot)


def _current_time():
    return time.monotonic()


def wait_until_text_appears(text, region=None, check_interval=1, timeout=None, on_found=None, run_once=False):
    """Waits until text appears, returns False if timeout."""

    # text: string a procurar
    # region: tupla (x, y, w, h) ou None para tela inteira
    # check_interval: tempo entre verificações (em segundos)
    # timeout: tempo máximo de espera (em segundos). None = esperar indefinidamente
    # on_found: callback (função) chamada quando o texto é detectado
    # run_once: se True, garante que on_found seja executado apenas uma vez durante essa chamada

    deadline = None if timeout is None else _current_time() + timeout
    executed = False # flag to control callback execution when run_once=True

    while True:
        screen_text = get_screen_text(region).lower()

        if text.lower() in screen_text:

            log("All_in_One", "SUCESSO", f"Text found: {text}")
            log("Waits_tesseract", "SUCESSO", f"Text found: {text}")

            if on_found and (not run_once or not executed):
                # if there is a callback and either we are not limiting the execution or we have not executed it yet
                try:
                    on_found() # calls the callback function without arguments
                    log("All_in_One", "SUCESSO", f"Callback on_found executado para o texto: {text}")
                    log("Waits_tesseract", "SUCESSO", f"Callback on_found executado para o texto: {text}")  
                except Exception as e:
                    log("All_in_One", "ERRO", f"Erro na função {__name__} callback on_found: {e}")
                    log("Waits_tesseract", "ERRO", f"Erro na função {__name__} callback on_found: {e}")
                executed = True
            return True
        
        if deadline is not None and _current_time() > deadline:
            log("All_in_One", "ERRO", f"Timeout aguardando texto: '{text}'")
            log("Waits_tesseract", "ERRO", f"Timeout aguardando texto: '{text}'")
            print(f"Timeout aguardando texto: '{text}'")
            return False
        time.sleep(check_interval)


def wait_until_text_disappears(text, region=None, check_interval=1, timeout=None):
    """Wait until the text disappears. Returns True if gone, False if timeout."""
    deadline = None if timeout is None else _current_time() + timeout
    while True:
        screen_text = get_screen_text(region).lower()
        if text.lower() not in screen_text:
            return True
        if deadline is not None and _current_time() > deadline:
            return False
        time.sleep(check_interval)


def get_image(img_path, region=None, confidence=0.8):
    """Returns True if the image (file) is found on the screen."""
    try:
        loc = pg.locateOnScreen(img_path, region=region, confidence=confidence)
        return loc is not None
    except Exception as e:
        log("All_in_One", "ERRO", f"Tesseract: Erro ao localizar imagem: {e}")
        log("Waits_tesseract", "ERRO", f"Tesseract: Erro ao localizar imagem: {e}")
        return False


def wait_until_img_appears(img_path, region=None, check_interval=1, timeout=None, on_found=None, run_once=False):
    '''Wait until the image appears on the screen within the timeout. This function allows you to execute other commands if the image is found, False if timeout.'''
    deadline = None if timeout is None else _current_time() + timeout
    executed = False
    time.sleep(0.5)

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
    """Executes target_fn(*args) in thread and calls callback_on_complete(result) when finished.
    target_fn must return a value (True/False)."""
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
    #Tenho uma ideia de onde usar esse daqui mas caso não precise tenho que apagar depois, então deixo aqui por enquanto. Ele é basicamente para rodar as funções de espera sem bloquear o restante do código, e quando a função terminar ele pode chamar um callback com o resultado (True/False) para tomar alguma ação dependendo do resultado da espera.



# ---- função para verificar e resolver mensagens de erro ----
def check_file_status():
    """Verifica se há erros de arquivo usando OCR e retorna um status"""
    check_open = wait_until_text_appears(
        "already open", cfg.already_open_full_r,
        check_interval=0.5, timeout=3,
        on_found=utl.cancel_qk, run_once=True
    )

    check_file = wait_until_text_appears(
        "Arquivo não encontrado", cfg.file_not_fond_close,
        check_interval=0.5, timeout=3,
        on_found=utl.ok_qk, run_once=True
    )

    if check_open:
        print("Página já estava aberta")
        time.sleep(cfg.TIMETOCLOSE)
        return "open"
        
    elif check_file:
        print("Arquivo não encontrado, ignorando e continuando processos...")
        return "not_found"

    print("Nenhum erro detectado, continuando processos...")
    return "ok"