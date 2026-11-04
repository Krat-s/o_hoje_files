"""Carregador central das configurações do projeto.

Os valores fixos ficam em arquivos TOML. Configurações dinâmicas, como
resolução da tela e contagens aleatórias, continuam sendo calculadas em Python.
"""

import locale
import tomllib
from pathlib import Path

import pyautogui as pg

from shared import gen_randon_numbers as rn
import shared.data_sync.data_edition_sync as desync


_CONFIG_DIR = Path(__file__).resolve().parent


def _load_toml(filename: str) -> dict:
    """Carrega um arquivo TOML localizado na pasta settings/."""
    path = _CONFIG_DIR / filename
    with path.open("rb") as file:
        return tomllib.load(file)


# Configurações estruturadas, para módulos novos.
PATHS = _load_toml("paths.toml")
TIMINGS = _load_toml("timings.toml")
WEB = _load_toml("web.toml")
QUARK = _load_toml("quark.toml")
ADS = _load_toml("ads.toml")


# -------------------------------------------------------------------------
# Compatibilidade com os nomes antigos.
# Mantém os imports cfg.CAMINHO_..., cfg.ad_1_..., cfg.quark etc. funcionando.

CAMINHO_FOTOS = PATHS["network"]["photos"]
CAMINHO_WEB = PATHS["network"]["web"]
CAMINHO_MODELO_WEB = PATHS["templates"]["web"]
CAMINHO_PAGFLIP = PATHS["network"]["pagflip"]
CAMINHO_MODELO_PAGFLIP = PATHS["templates"]["pagflip"]
CAMINHO_EDD = PATHS["network"]["edd"]
CAMINHO_MODELO_EDD = PATHS["templates"]["edd"]
CAMINHO_MODELO_EDD_0 = PATHS["templates"]["edd_base"]
CAMINHO_PRINTS = PATHS["prints"]["output"]

# Barra de tarefas: centralizada em paths.toml por ser compartilhada.
quark = PATHS["taskbar"]["quark"]
opera = PATHS["taskbar"]["opera"]
vscode = PATHS["taskbar"]["vscode"]
explorer = PATHS["taskbar"]["explorer"]

TIMETOOPEN = TIMINGS["quark"]["open"]
TIMETOCLOSE = TIMINGS["quark"]["close"]
TIMEEXPPDF = TIMINGS["quark"]["pdf_export"]

# Valores dependentes do ambiente continuam no Python.
screen_width, screen_height = pg.size()
center_x = screen_width / 2
center_y = screen_height / 2

try:
    locale.setlocale(locale.LC_TIME, "pt_BR.utf-8")
except locale.Error:
    # O identificador disponível varia entre Windows e outras plataformas.
    # Não impede a inicialização da automação se esse locale não estiver instalado.
    pass

# Regiões e coordenadas do Quark/OCR.
already_open_r = tuple(QUARK["ocr_regions"]["already_open"])
already_open_full_r = tuple(QUARK["ocr_regions"]["already_open_full"])
quark_icon_c_r = tuple(QUARK["ocr_regions"]["quark_icon"])
quark_loading = tuple(QUARK["ocr_regions"]["quark_loading"])
file_not_fond = tuple(QUARK["ocr_regions"]["file_not_found"])
file_not_fond_close = tuple(QUARK["ocr_regions"]["file_not_found_close"])
button_cancel_qk = tuple(QUARK["click_positions"]["button_cancel"])
button_ok_qk = tuple(QUARK["click_positions"]["button_ok"])

x_data = QUARK["click_positions"]["data_x"]
y_data = QUARK["click_positions"]["data_y"]
x_edicao_17 = QUARK["click_positions"]["edition_17_x"]
y_edicao_17 = QUARK["click_positions"]["edition_17_y"]
x_edicao_capa = QUARK["click_positions"]["edition_cover_x"]
y_edicao_capa = QUARK["click_positions"]["edition_cover_y"]

# Web.
acessos_B1 = rn.generate_number(
    WEB["access_counts"]["b1_min"],
    WEB["access_counts"]["b1_max"],
)
acessos_B2 = int(acessos_B1 / 2 + 1)
acessos_B3 = int(acessos_B2 / 2)
acessos_H1 = WEB["access_counts"]["h1"]
acessos_H2 = WEB["access_counts"]["h2"]
acessos_H3 = WEB["access_counts"]["h3"]

url_target = WEB["site"]["target_url"]
url_target_intagram = WEB["site"]["instagram_url"]
botão_1 = WEB["selectors"]["button_1"]
botão_2 = WEB["selectors"]["button_2"]
botão_3 = WEB["selectors"]["button_3"]


def _ad_value(ad_id: str) -> dict:
    """Retorna a tabela de anúncio correspondente ao identificador."""
    return next(ad for ad in ADS["ads"] if ad["id"] == ad_id)


def _publish_legacy_ad_names(prefix: str, ad: dict) -> None:
    """Expõe os campos de anúncios com os nomes usados pelo código existente."""
    globals()[f"{prefix}_pi"] = ad["pi"]
    globals()[f"{prefix}_client"] = ad["client"]
    globals()[f"{prefix}_folder"] = (
        f'{ad["pi"]} - {ad["position"]} - {ad["client"]}'
    )
    globals()[prefix if prefix != "ad_alt" else "ad_alt_ad"] = ad["selector"]
    globals()[f"{prefix}_link"] = ad["link_selector"]
    globals()[f"{prefix}_gif"] = ad["gif"]
    globals()[f"{prefix}_insta"] = ad["instagram"]


for _ad_id in ("ad_1", "ad_2", "ad_3", "ad_4", "ad_alt"):
    _publish_legacy_ad_names(_ad_id, _ad_value(_ad_id))

# O código legado usa ad_alt_ad como seletor alternativo, e não ad_alt.
ad_alt_ad = _ad_value("ad_alt")["selector"]