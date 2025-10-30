import pytesseract
import os

# Se o executável não for encontrado, tenta definir manualmente:
if not os.path.exists(pytesseract.pytesseract.tesseract_cmd):
    possible_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        r"D:\Apps\Tesseract-OCR\tesseract.exe"
    ]
    for path in possible_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            break