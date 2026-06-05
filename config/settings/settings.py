import os
import sys
import locale
import pyautogui as pg

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(raiz_projeto)

from config.core import gen_randon_numbers as rn
import config.core.data_edition_sync as sy_de
from config.settings.settings_edition_request import edicao_inicial, total_edicoes, quantidade_repeticoes


# ------------------------------------------------------------------------- Caminhos de rede
CAMINHO_FOTOS = r'\\192.168.1.249\fotos'
CAMINHO_WEB = r'\\192.168.1.249\redacao\web'
CAMINHO_MODELO_WEB = r'\\192.168.1.249\redacao\web\00 - Modelo'
CAMINHO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip'
CAMINHO_MODELO_PAGFLIP = r'\\192.168.1.249\redacao\arte\00 Pagflip\00 - Modelo'
CAMINHO_EDD = r'\\192.168.1.249\redacao\diagramacao\edicao'
CAMINHO_MODELO_EDD = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições\00 - modelo'
CAMINHO_MODELO_EDD_0 = r'\\192.168.1.249\redacao\arte\01 Projeto\4 Adianto de novas edições'
CAMINHO_PRINTS = r'\\192.168.1.249\comercial\PRINTS\00 - Auto-prints'


# ------------------------------------------------------------------------- Tempos de espera
TIMETOOPEN = 4
TIMETOCLOSE = 6
TIMEEXPPDF = 7


# ------------------------------------------------------------------------- Barra de tarefas
quark = 1
opera = 2 # any browser
vscode = 3
explorer = 4 

# ------------------------------------------------------------------------- Configurações gerais
screen_width, screen_height = pg.size()
center_x = screen_width / 2
center_y = screen_height / 2
locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")

# ------------------------------------------------------------------------- Pytesseract and regions
already_open_r = (489, 280, 98, 103)
already_open_full_r = (489, 281, 389, 156) 
quark_icon_c_r = (499, 309, 79, 101)
quark_loading = (493, 304, 123, 111)
file_not_fond = (465, 232, 477, 210)
file_not_fond_close = (500, 260, 363, 142)
button_cancel_qk = 829, 419
button_ok_qk = 829, 385

x_data = 850
y_data = 259
x_edicao_17 = 560
y_edicao_17 = 121
x_edicao_capa = 346
y_edicao_capa = 448



# ------------------------------------------------------------------------- Web
acessos_B1 = rn.generate_number(0, 3)
acessos_B2 = int(acessos_B1 / 2 + 1)
acessos_B3 = int(acessos_B2 / 2)
acessos_H1 = 1
acessos_H2 = 2
acessos_H3 = 1

url_target = "https://ohoje.com"
botão_1 = str("ads-728 mx-auto") #principal
botão_2 = "p-3 pb-0" #lateral
botão_3 = "placement_1026570_0_i" #banner rodapé


# ------------------------------------------------------------------------- Prints settings
# addon banner principal 40135
# ad_1_pi = 40135 
ad_1_pi = None 
ad_1_client = "BRAZIL AÇUCAREIRA"
ad_1_folder = f'{ad_1_pi} - Principal - {ad_1_client}'
ad_1 = "section.block-ads:nth-child(2) img[alt='Publicidade']" 
ad_1_link = 'a[href*="https://ohoje.com/2026/05/22/brasil-acucareira-acelera-expansao-nacional-com-logistica-propria-e-operacao-24-horas/"]'

# addon Width (rodapé?)
# ad_2_pi = 40270
ad_2_pi = None
ad_2_client = 'LUIZIÂNIA'
ad_2_folder = f'{ad_2_pi} - Width - {ad_2_client}'
ad_2 = f"section.block-ads:nth-child(5) img[alt='Publicidade']" 
ad_2_link = 'a[href*="https://www.luziania.go.gov.br/"]'

# addon Halfpage (03 a 30)
ad_3_pi = 40347
# ad_3_pi = None
ad_3_client = 'GOV'
ad_3_folder = f'{ad_3_pi} - Halfpage - {ad_3_client}'
ad_3 = "div:nth-child(2) img[alt='Publicidade']"
ad_3_link = "img[src*='https://s0.2mdn.net/simgad/1179575939825349183']"
# ad_3_link = "a[href*='https://adclick.g.doubleclick.net/pcs/click?xai=AKAOjsuLVbYQRSpWltg_GIOZWwGdNi0bORgoXwtJdVPKow9kxu4YS2WUrQgP_EUDHckr4gOgAtUpY5geRzV9fvyh-bUSPW5Tni1eTq5gfYHS0t3qu3EEu9ZjTTLJdMJ6VOFv2AsK4yHAiiF4obXgozJn64V9PtH4s_1EFhoRsT46I_FrSGoPM3FVJylPmH2nC2F3OWBKmd7Sb4vrSYHXL9vnfivqfIy_XKyCiVV3pwIoaRL2W9asH5StC0cm_f3Sq-LUgqMsriVvF27Czgr5lRaL01Eo8sA_ejgmP3cOpLEoY4ftDZba-h2yET2KFV2YF1DwZlE07fpHLT8w-DfI-3HDhpNIle8NkcAmkjWmg_1br9vVZRd6hOvO5SZUuqBP3DBTToNPGmXSpMyM9_gDBon5t-mswPZWZ4C-irpaZe2TmgSxvLCvnUUVHfXOX8_6k2qeIZKBCVwN3Okhk4waY-jAv9p8-auEkdKUW5CBR7nO8jbtnEk1AuOUan3mWhtJnBBkfMbxeFhxrseihxw4NXZNHkHxjc61Fwvh6ZubUPLyZr0fK1VyP7ors4PHIIycZlQacHpGyeQq1czP8nhVxmfbD_rcjY9bL9vqrHdMTnLsaZwM_sqGKsO-Z1YwnM3lIOWTAI6IjpSUFCdUvKwbiToCXrJeKiIXi6Xv2D7v7lWdREt1bk8&sai=AMfl-YTxmTNE5rO2lEwwgH-L1U6FfanAFtsoLoBJZ4pGuP7jnLaQoo8aM__DqPheEQTvFtki1yIHag1S1iW6ImemWDKDhhnv5PUrG3So_YMsG5TyN-VqReXbYLkWHeGj7h2p6-ajFf7PCvJcCzVJhCfdprOOrmvDeF7WGNhOr3SiFcvWuXlwKCmAfD9jofSIQXNam0Wj5cYvRlbOaUakG3lC_vOa05V2_ck5P3obw7sVG5W4kwtVku9o1rLw8Uv368x_C0gflaIxpbIkK2nQNKfCIQ-Q2NwG_UF4EuvCUGYgqJYSb93uADk48iS7XUAyFuG9A4Opd52B9rI4bN2juiEU8eSMa8Z4Lg&sig=Cg0ArKJSzM01HnhcjQ-r&cry=1&fbs_aeid=%5Bgw_fbsaeid%5D&urlfix=1&nx=114&ny=147&dim=300x250&bg=!mJulm8PNAAZQ-7cWcPs7AEcBe5WfOLf4YGuCQ7XsfHm83dvq_cNSF45Kf2DYFblR_fLn_7rHjTraUHETJHXwHJz_slLE8_1tLLB148t7MkwwlHDIJNVRLQ8ABB4CsGVoAQd-AGo9DBnMXnqlfgCsYqYqBraL8IB0l6U_YQEUDOkRApKVKeesxnBM4gLH36uFwbcEYECKFb4muhp3aW_W5rujeXvJWLnKeiDTg3hmjWZPY5JqFksVGKVwO4lrubI0w4aC7EWKJXt9FmSFFd5FmQKPlfwd2TBo1bg71fnTyfW13JLjF6fF6vU-dmCFZvvRoKZqbHNq3pxsZ3vPcAIVouqAQj1d_UNRqylpj56TGCqM5tbdSfLd0cXSvF5lLlh19iM2jNZc8VRdDwUOFG3GWuIcwoxASEntqDGfTeqi1Fm5LluKmkwKYT-C-FFPxlKbmH7aybgfs1DzZsHVf7a_5j_lTQdWolxhRppWm-WE5BwqWrX3CUz6xLT4rLcfRkLDA-r2WtJVUj_UePyBh-Z1HUT7J0sHgCTTSCTtLYol5vjx22qzbYxwE1IPsyTeegoOfihGI_GF4FEKbvJFL_DAZhtcf4TSPIAsKdkXDTbLuEdF2_2tYmdkOw8S1qY-btuthVJ0S8nUlUW90Mlyf1EqVKcAUwMNeQETl92Cevc9HjeIRsNTLIJr1f_IBiv8MxS4Xdb_7fo0yWpFg3EXZRJqZ5i16AdXjrm8FdZX_5B8hHQr54Pf13n1qSCMy4GfFaPfHisYnH1Pp69NzNw0XTWrU_DJIvCL-uE_aYL-PcQDJBO6NDZksZq9FYd9H4Cu2w9Hs-Shp45f583l3C7ltnYQeAKrJ_gGJ0sCRGUCPT0J8CoE1TUJfrQLjBr4IBRxpmsFC6KU7Cvs-tGy8t6ibgUbaw5DqdSQV7TiIxokpQYPPt4VL6GqvhPszNgNvj6UV3LmrbxOokgV-7hYWRwexjLwYxK1FowUconWid_OqlEjPtHdwkGEEtYtsRspdxddtVhc94dN4QBROUgeeUP-0jU-yW3bU22DLEqIm-H8c0yUe05YW_T_09DMY4QdoBm7JJA9m6IzSnhh5A5vWQ74kpsPqMr_ELGqS4o-tpwqJ3ED2GQXGLbmzzFWypVzZXlm3pA-VA&adurl=https://www.gov.br/mds/pt-br/noticias-e-conteudos/desenvolvimento-social/noticias-desenvolvimento-social/com-70-de-publico-feminino-no-brasil-programa-acredita-amplia-renda-de-mulheres-empreendedoras%3Futm_medium%3Dbanner_cpm%26utm_source%3Do_hoje%26utm_campaign%3D2026_always_on_20260009_%26utm_content%3Dempreendedoras-300x250_banner_300x250_cpm%26dclid%3D%25edclid!%26gad_source%3D7%26gad_campaignid%3D23907397852']"


# addon Middle retangle (quadrado?)
ad_4_pi = None
ad_4_client = ''
ad_4_folder = f'{ad_4_pi} - MIDDLE RETANGLE - {ad_4_client}'
ad_4 = "section.block-ads:nth-child(3) img[alt='Publicidade']"  
ad_4_link = ''

#alt addon (when have two ads from the same localization)
ad_alt_pi = None
ad_alt_client = ''
ad_alt_folder = f'{ad_alt_pi} - Halfpage - {ad_alt_client}'
ad_alt_ad = ad_3
ad_alt_link = ''



def stats():
    print(".....")
    print("⚙️  Settings loaded ✔️")
    print(f".. Tamanho da tela: {pg.size()}")
    print(f".. Centro da tela: ({center_x}, {center_y})")
    print(f".. Edição inicial: {edicao_inicial}")
    print(f".. Quantidade de repetições: {quantidade_repeticoes}")
    print(f".. Criando modelo de {total_edicoes} edições")
    print(f".. Última edição: {total_edicoes + edicao_inicial}")
    print(".....")


if __name__ == "__main__":
    stats()
    # print(sy_de.EDD)  