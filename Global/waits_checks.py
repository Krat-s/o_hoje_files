import pyautogui as pg
import keyword as kb
import os

from Global.wait import wait_until
from pywinauto import Desktop
import Global.waits_tesseract as tutl


#-------------------Explorer-waits
def wait_explorer_open(timeout=10):
    return wait_until(
        lambda: any(
            w.class_name() == "CabinetWClass"
            for w in Desktop(backend="uia").windows()
        ),
        timeout=timeout
    )

def wait_folder_open(nome_pasta, timeout=10):
    nome = nome_pasta.lower()

    return wait_until(
        lambda: any(
            nome in w.window_text().lower()
            for w in Desktop(backend="uia").windows()
            if w.class_name() == "CabinetWClass"
        ),
        timeout=timeout
    )


#-------------------file exist waits
def wait_file(path, timeout=10):
    return wait_until(
        lambda: os.path.exists(path),
        timeout=timeout
    )


#-------------------image waits
def image_visible(path, timeout=10):
    return wait_until(
        lambda: pg.locateOnScreen(path) is not None,
        timeout
    )

def wait_image(image_path, timeout=10, confidence=0.9):
    return wait_until(
        lambda: pg.locateOnScreen(image_path, confidence=confidence) is not None,
        timeout=timeout
    )


#-------------------logic status waits
def wait_quark_ready():
    return wait_until(
        lambda: not kb.is_pressed('esc'),
        timeout=5
    )


def text_visible(text, timeout=10):
    return wait_until(
        lambda: text.lower() in tutl.read_screen().lower(),
        timeout
    )