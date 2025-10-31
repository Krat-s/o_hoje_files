import cv2
import numpy as np
import pyautogui

# Faz uma captura da tela inteira
screenshot = pyautogui.screenshot()
img = np.array(screenshot)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Permite selecionar área com o mouse
r = cv2.selectROI("Selecione a área com o mouse e pressione ENTER", img, False, False)

x, y, w, h = map(int, r)
print(f"Coordenadas selecionadas: (x={x}, y={y}, w={w}, h={h})")

# Recorta e salva a região
if w > 0 and h > 0:
    roi = img[y:y+h, x:x+w]
    cv2.imwrite("area_selecionada.png", roi)
    print("🖼️ Imagem salva como 'area_selecionada.png'")

cv2.destroyAllWindows()
