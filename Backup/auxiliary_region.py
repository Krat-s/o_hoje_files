import cv2
import numpy as np
import pyautogui
import os
import time
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

pasta_destino = f"{raiz_projeto}\\Backup\\Prints" 
os.makedirs(pasta_destino, exist_ok=True)  

# Faz uma captura da tela inteira
# time.sleep(4)
screenshot = pyautogui.screenshot()
img = np.array(screenshot)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Seleciona área
r = cv2.selectROI("Selecione a área e pressione ENTER", img, False, False)
x, y, w, h = map(int, r)
print(f"Coordenadas selecionadas: (x={x}, y={y}, w={w}, h={h})")

# Salva no local desejado
if w > 0 and h > 0:
    roi = img[y:y+h, x:x+w]
    caminho_arquivo = os.path.join(pasta_destino, "area_selecionada.png")
    cv2.imwrite(caminho_arquivo, roi)
    print(f"🖼️ Imagem salva em: {caminho_arquivo}")
 
cv2.destroyAllWindows()