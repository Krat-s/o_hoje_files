

# from datetime import datetime, timedelta
# from data_edition_sync import EdicaoDataSync
# import os
# import sys
# raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(raiz_projeto)
# import Global.settings as cg
# import Global.utils as ut
# from App.Modulos_quark.data_formatador import formatar_data

# sync = EdicaoDataSync(edicao_inicial=6496, data_inicial=datetime(2024, 8, 26))

# # Obter data por edição
# data = sync.obter_data_por_edicao(8900)
# print("📅 Data da edição 8900:", data.strftime('%d/%m/%Y'))

# # Obter edição por data
# edicao = sync.obter_edicao_por_data(datetime(2025, 9, 24))
# edicao_amanha = sync.obter_edicao_por_data(datetime.now() + timedelta(days=1))
# print("📰 Edição correspondente à data:", edicao_amanha)

# # Gerar várias edições e datas
# # lista = sync.gerar_edicoes_e_datas(15)
# # for ed, dt in lista:
# #     print(f"Edição {ed} → {dt.strftime('%A, %d/%m/%Y')}")
#     # print(f"{data}")



# data = sync.obter_data_por_edicao(7000)
# data_formatada = formatar_data(data)
# hoje = datetime.now()
# data_amanha = hoje + timedelta(days=1)
# # print(data_formatada)
# # print("📅 Data da edição de amanha:", formatar_data(data_amanha, tipo="dia_semana"))

# # print(f"..")
# # print(f"..")
# # print(f"..")


# edicao = sync.obter_edicao_por_data(datetime.now() + timedelta(days=1))
# edicao_hoje = sync.obter_edicao_por_data(datetime.now() + timedelta(days=1))
# # print("📰 Edição correspondente à data:", edicao_hoje)





import sys
print(sys.executable)