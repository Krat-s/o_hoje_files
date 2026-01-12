import sys
import os

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(modulo_path)

from unittest.mock import Mock, patch
from App.billhead import auto_date, aply_1, auto_pages

def test_auto_date_escreve_data():
    info = Mock()
    info.data_formatada = "26 de agosto de 2024"

    with patch("App.billhead.kb.write") as write_mock:
        with patch("App.billhead.pg") as pg_mock:
            with patch("App.billhead.utlq"):
                with patch("App.billhead.utl"):
                    auto_date(info)

    write_mock.assert_called_with("26 de agosto de 2024")

def test_aply_1_escreve_edicao_e_data():
    info = Mock()
    info.edicao_formatada = "6500"
    info.data_formatada = "26/08/2024"

    with patch("App.billhead.kb.write") as write_mock:
        with patch("App.billhead.pg"):
            with patch("App.billhead.utl"):
                with patch("App.billhead.utlq"):
                    aply_1(info)

    chamadas = [c.args[0] for c in write_mock.call_args_list]

    assert "nº 6500 " in chamadas
    assert "|  26/08/2024" in chamadas

def test_auto_pages_caminho_pasta():
    info = Mock()
    info.edicao_formatada = "6500"
    info.dia_semana = "Segunda"

    with patch("App.billhead.kb.write") as write_mock:
        with patch("App.billhead.pg"):
            with patch("App.billhead.utl"):
                with patch("App.billhead.auto_date"):
                    auto_pages(3, info)

    caminho = write_mock.call_args_list[0].args[0]
    assert "6500 - Segunda" in caminho

test_aply_1_escreve_edicao_e_data()