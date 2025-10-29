import pyautogui as pg  
import time
import pytesseract
import os

from PIL import Image, ImageDraw, ImageFont

os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

# Cria uma imagem branca
img = Image.new("RGB", (300, 100), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Escreve um texto simples
draw.text((10, 30), "Teste OCR 123", fill=(0, 0, 0))

# (Opcional) Salva a imagem pra ver o que foi criado
img.save("teste_ocr.jpeg")

# Usa o Tesseract para reconhecer o texto da imagem
texto = pytesseract.image_to_string(img, lang="eng")  # use "eng" para inglês

print("🧾 Texto reconhecido pelo OCR:")
print(texto)


