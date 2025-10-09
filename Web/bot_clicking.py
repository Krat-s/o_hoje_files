from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from threading import Thread
import time
import schedule

import os
import sys
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Global.daily_task import abrir_navegador_e_clickar, gerar_horarios


# 1. Gere todos os horários do dia
agendas = []
agendas += gerar_horarios(6,  9, 5)   # manhã
agendas += gerar_horarios(12, 17, 8)  # tarde
agendas += gerar_horarios(18, 22, 3)  # noite

# 2. Agende cada execução
for dt in agendas:
    marcacao = dt.strftime("%H:%M")
    schedule.every().day.at(marcacao).do(abrir_navegador_e_clickar)

# 3. Loop principal
while True:
    schedule.run_pending()
    time.sleep(30)
