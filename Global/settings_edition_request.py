import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Global.Logs.logs import log

quantidade_repeticoes = 2
edicao_inicial = 7056

total_edicoes = quantidade_repeticoes * 6
edição_final = total_edicoes + edicao_inicial

log("edition_info", "Registro", f"{total_edicoes} criadas, última edição: {edição_final}")
