# import sys
# import os

# modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(modulo_path)

# from unittest.mock import patch
# from App.billhead_editions import auto_billhead_editions

# from unittest.mock import Mock

# def fake_edicao():
#     info = Mock()
#     info.edicao_formatada = "6500"
#     info.data_formatada = "26/08/2024"
#     info.dia_semana = "Segunda"
#     info.dia_semana_padrão = 0
#     info.pasta_nome = "6500 - Segunda"
#     return info

# def test_auto_billhead_sucesso():
#     fake_info = fake_edicao()

#     with patch("App.billhead_runner.desync.gerar_edicoes_formatadas", return_value=[fake_info]):
#         with patch("App.billhead_runner.auto_folders") as auto_folders_mock:
#             with patch("App.billhead_runner.utl.open_software") as open_mock:
#                 with patch("App.billhead_runner.aply_17") as aply_17_mock:
#                     with patch("App.billhead_runner.auto_date_all_non_especial_pages") as auto_all_mock:
#                         with patch("App.billhead_runner.aply_1") as aply_1_mock:
#                             with patch("App.billhead_runner.log") as log_mock:
#                                 auto_billhead_editions()





# aply_17_mock.assert_called_once_with(fake_info)
# auto_all_mock.assert_called_once_with(fake_info)
# aply_1_mock.assert_called_once_with(fake_info)

