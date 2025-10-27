import pyautogui as pg  
import time
import pytesseract

from PIL import Image, ImageDraw, ImageFont

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Cria uma imagem branca
img = Image.new("RGB", (300, 100), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

# Escreve um texto simples
draw.text((10, 30), "Teste OCR 123", fill=(0, 0, 0))

# (Opcional) Salva a imagem pra ver o que foi criado
img.save("teste_ocr.png")

# Usa o Tesseract para reconhecer o texto da imagem
texto = pytesseract.image_to_string(img, lang="por")  # use "eng" para inglês

print("🧾 Texto reconhecido pelo OCR:")
print(texto)
