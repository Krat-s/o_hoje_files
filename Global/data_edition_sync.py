from datetime import datetime, timedelta

import os
import sys
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from App.Modulos_quark.data_formatador import formatar_data
import Global.settings as cg
import Global.utils as ut
from App.Modulos_quark.edicao_formatador import gerar_edicoes
from App.Modulos_quark.data_formatador import formatar_data

# Base fixa para cálculo de data
EDICAO_BASE = 6496
DATA_BASE = datetime(2024, 8, 26)  # Segunda-feira

# Parâmetros padrão de geração
QUANTIDADE_POR_SEMANA = 5
REPETICOES_PADRAO = cg.quantidade_repeticoes

def obter_data_por_edicao(edi_numero, edi_inicial=EDICAO_BASE, data_inicial=DATA_BASE):
    if edi_numero < edi_inicial:
        raise ValueError("O número da edição não pode ser menor que a edição inicial.")

    diff = edi_numero - edi_inicial
    ciclos = diff // 7
    resto = diff % 7

    dias_extra = resto if resto < 5 else 5
    offset_total = ciclos * 7 + dias_extra

    return data_inicial + timedelta(days=offset_total)

def obter_edicao_por_data(data_alvo, edi_inicial=EDICAO_BASE, data_inicial=DATA_BASE):
    """
    Retorna o número da edição correspondente à data informada.
    """
    if data_alvo < data_inicial:
        raise ValueError("A data não pode ser anterior à data inicial.")

    edicao_numero = edi_inicial

    # Busca progressiva até encontrar a data exata ou ultrapassar
    while True:
        data_edicao = obter_data_por_edicao(edicao_numero)
        if data_edicao.date() == data_alvo.date():
            return edicao_numero
        elif data_edicao > data_alvo:
            break
        edicao_numero += 1

    raise ValueError("Data não corresponde a nenhuma edição válida.")

def gerar_edicoes_formatadas(edicao_inicial, quantidade_por_semana=QUANTIDADE_POR_SEMANA, repeticoes=REPETICOES_PADRAO):
    resultados = []
    data_atual = obter_data_por_edicao(edicao_inicial)

    for _ in range(repeticoes):
        edicoes = gerar_edicoes(edicao_inicial, quantidade_por_semana)

        for ed in edicoes:
            dia_semana = formatar_data(data_atual, tipo='dia_semana')
            pasta_nome = f"{ed.replace('.', '')} - {dia_semana}"

            info = {
                "edicao_formatada": ed,
                "data_formatada": formatar_data(data_atual),
                "dia_semana": dia_semana,
                "pasta_nome": pasta_nome
            }

            resultados.append(info)

            num = int(ed.replace('.', '').split('-')[0])
            data_atual = obter_data_por_edicao(num)
            passo = 2 if '-' in ed else 1
            data_atual += timedelta(days=passo)

        edicao_inicial += quantidade_por_semana + 2

    return resultados

def para_cada_edicao(fazer_algo, edicao_inicial, quantidade_por_semana=QUANTIDADE_POR_SEMANA, repeticoes=REPETICOES_PADRAO):
    for item in gerar_edicoes_formatadas(edicao_inicial, quantidade_por_semana, repeticoes):
        fazer_algo(item)


def obter_data_formatada(nume):
    return formatar_data(obter_data_por_edicao(nume))
    
# obter_data_por_edicao = formatar_data(obter_data_por_edicao(6896))
def teste_syed():
    print(obter_data_formatada(6897))
    
if __name__ == "__main__":
    teste_syed()