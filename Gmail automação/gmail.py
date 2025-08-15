import time
import keyboard as kb
import pyautogui as pg
from Modulos_gmail.edicao_formatador import gerar_edicoes

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.3
pg.FAILSAFE = True
time.sleep(1)

largura, altura = pg.size()
centro_x = largura / 2
centro_y = altura / 2

edicao_inicial = 6794
quantidade_por_semana = 5
quantidade_repeticoes = 2

# ---------------------------- FUNÇÕES DE AUTOMAÇÃO ----------------------------
def take_emails():
    """Captura os emails de um arquivo no VSCode"""
    pg.hotkey('win', 's')
    pg.hotkey('win', '3')  # Verificar se é o app certo (VSCode)
    pg.hotkey('ctrl', 'o')
    pg.write('ar')
    pg.press('down')
    pg.press('enter')
    pg.write('ema')
    pg.press('down')
    pg.press('enter')
    time.sleep(0.5)
    pg.click(x=centro_x, y=centro_y)
    pg.hotkey('ctrl', 'a')
    pg.hotkey('ctrl', 'c')
    time.sleep(0.5)

def shortcut_send_emails():
    """Atalho para abrir campo de envio no Gmail"""
    pg.press('esc')
    pg.press('c')  # Abrir menu de mensagem
    time.sleep(1.5)
    pg.hotkey('ctrl', 'shift', 'b')
    time.sleep(0.5)

def open_gmail():
    """Atalho para abrir navegador no Gmail"""
    pg.hotkey('win', 's')
    pg.hotkey('win', '2')  # Verificar se é o navegador correto
    time.sleep(0.5)

def enviar_emails_para_leitores(edicao):
    """Simula envio de emails com conteúdo da edição"""
    open_gmail()
    shortcut_send_emails()
    pg.hotkey('ctrl', 'v')  # Cola emails
    pg.press('tab')
    kb.write(f"Segue PDF completo da edição {edicao} do jornal O Hoje")
    pg.press('esc')
    time.sleep(1)

def enviar_para_grafica(edicao, parte):
    """Simula envio para gráfica com parte específica da edição"""
    pg.press('c')
    shortcut_send_emails()
    kb.write('contas')
    pg.press('enter')
    pg.write('grafica')
    pg.press('enter')
    time.sleep(0.3)
    pg.press('tab')
    kb.write(f"Segue {parte} da edição {edicao} do jornal O Hoje")
    pg.press('esc')
    time.sleep(1)

# ---------------------------- ROTINA PRINCIPAL ----------------------------
def main():
    print("📦 Edições geradas:")
    edicao = edicao_inicial

    for _ in range(quantidade_repeticoes):
        edicoes = gerar_edicoes(edicao, quantidade_por_semana)

        for ed in edicoes:
            print(f"→ {ed}")
            # enviar_emails_para_leitores(ed)
            # enviar_para_grafica(ed, "essência e classificados")
            # enviar_para_grafica(ed, "resto")

        edicao += quantidade_por_semana + 2

if __name__ == "__main__":
    main()
