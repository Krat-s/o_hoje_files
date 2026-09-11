import shared.file_manager as fm
from shared.utils import max_windows
from shared.logging.logs import log
import os
import sys
import time
import pyautogui as pg
import settings.settings as cfg
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
from shared.automation.web_diver import wait_d

screen_date = f'{datetime.now().strftime("%Y - %m - %d")}'


def print_task(adon_link, adon_name_folder, gif=None, insta=None):
    """Abre o navegador, clica no botão e registra o resultado."""
    # print(f"🌐 Acessando {cfg.url_target}")
    # print(f"📅 data: {screen_date}")

    # chrome_options = Options()
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--disable-notifications")
    # chrome_options.add_argument("--no-sandbox")

    # try:
    #     driver = webdriver.Chrome(options=chrome_options)
    #     max_windows()

    # except Exception as e:
    #     erro_msg = f"Falha ao iniciar ChromeDriver: {str(e)}"
    #     log("All_in_one", "ERRO", erro_msg)
    #     log("print_ad", "ERRO", erro_msg)
    #     return
    # driver.get(cfg.url_target)

    # wait_d(driver, By.TAG_NAME, "body",)
    # # wait_d(driver, By.CSS_SELECTOR, adon_link)
    # print(  f"✅ Anúncio encontrado")
    # time.sleep(0.5)

    def button_print(adon_link):
        print(f"🖨️ Imprimindo anúncio: {adon_name_folder}")
        # ad = wait_d(driver, By.CSS_SELECTOR, adon_link)

        # time.sleep(3)
        # driver.execute_script(
        #     """
        #     document.body.style.zoom='70%';
        #     const element = arguments[0];
        #     const yOffset = -150;
        #     const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
        #     window.scrollTo({top: y});
        #     """, ad
        # )

        # time.sleep(2)

        fm.make_folder_print(adon_name_folder)

        if gif is not None:
            print('gif print')
            # gifs_folder = f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\gifs"
            # os.makedirs(gifs_folder, exist_ok=True)
            # time.sleep(1.5)
            # pg.screenshot(f"{gifs_folder}\\{screen_date} - gif 1.png")
            # time.sleep(3.5)
            # pg.screenshot(f"{gifs_folder}\\{screen_date} - gif 2.png")
            # time.sleep(3.5)
            # pg.screenshot(f"{gifs_folder}\\{screen_date} - gif 3.png")

        if insta is not None:
            print('intagram print')
            # time.sleep(.5)
            # pg.hotkey('ctrl', 'l')
            # time.sleep(.5)
            # pg.write(f"{cfg.url_target_intagram}")
            # time.sleep(.5)
            # pg.press('enter')
            # time.sleep(3)
            # pg.screenshot(f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\Instagram - {screen_date}.png")

        print('print normal')
        pg.screenshot(
            f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\{screen_date}.png")
        frames_folder = f"{cfg.CAMINHO_PRINTS}\\{adon_name_folder}\\frames"
        os.makedirs(frames_folder, exist_ok=True)
        time.sleep(0.5)
        for i in range(1, 4):
            print(f'Capturando frame {i} do gif...')
            time.sleep(.5)
            pg.screenshot(f"{frames_folder}\\{screen_date} - frame {i}.png")

    try:
        button_print(adon_link)

    except Exception as e:
        erro_msg = f"Falha ao salvar imagem: {str(e)}"
        log("All_in_one", "ERRO", erro_msg)
        log("print_ad", "ERRO", erro_msg)

    finally:
        time.sleep(2)
        # driver.quit()
        log("All_in_one", "RELATÓRIO", "Drive fechado após execução da tarefa")
        log("print_ad", "RELATÓRIO", "Drive fechado após execução da tarefa")


# ------n8n trigger
def run_print_ad(ad=None, folder=None):
    print_task(ad, folder)


# ------------------manual trigger
def auto_prints_all_ads(gif=None, insta=None):
    '''verifica quais anúncios estão configurados e executa a função de print para cada um deles'''
    if cfg.ad_1_pi != None:
        print_task(cfg.ad_1_link, cfg.ad_1_folder,
                   gif=cfg.ad_1_gif, insta=cfg.ad_1_insta)

    if cfg.ad_2_pi != None:
        print_task(cfg.ad_2_link, cfg.ad_2_folder,
                   gif=cfg.ad_2_gif, insta=cfg.ad_2_insta)

    if cfg.ad_3_pi != None:
        print_task(cfg.ad_3_link, cfg.ad_3_folder,
                   gif=cfg.ad_3_gif, insta=cfg.ad_3_insta)

    if cfg.ad_4_pi != None:
        print_task(cfg.ad_4_link, cfg.ad_4_folder,
                   gif=cfg.ad_4_gif, insta=cfg.ad_4_insta)

    if cfg.ad_alt_pi != None:
        print('Printando anúncio alternativo...')
        time.sleep(60 * 6)
        print_task(cfg.ad_alt_link, cfg.ad_alt_folder,
                   gif=cfg.ad_alt_gif, insta=cfg.ad_alt_insta)
        time.sleep(60)
        print_task(cfg.ad_alt_link, f'{cfg.ad_alt_folder}_retry',
                   gif=cfg.ad_alt_gif, insta=cfg.ad_alt_insta)


if __name__ == "__main__":
    print('Print ad rodando...')
    # time.sleep(60 * 60 * 3)
    auto_prints_all_ads()
    # print('Print ad finalizado.')
