from datetime import datetime, timedelta

import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Global.edicao_formatador import gerar_edicoes, formatar_edicao, formatar_numero
from Global.data_formatador import formatar_data
from Global.settings_edition_request import quantidade_repeticoes, edicao_inicial
from Global.edition_info import EdicaoInfo

# Base fixa para cálculo de data
EDICAO_BASE = 6496
DATA_BASE = datetime(2024, 8, 26)  # Segunda-feira
QUANTIDADE_POR_SEMANA = 5

# Parâmetros padrão de geração
REPETICOES_PADRAO = quantidade_repeticoes
EDICAO_INI = edicao_inicial 

def obter_data_por_edicao(edi_numero, edi_inicial=EDICAO_BASE, data_inicial=DATA_BASE):
    """
    Retorna a data formatada para a edição informada
    """
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
    Retorna a edição formatada para a data informada
    """
    if data_alvo < data_inicial:
        raise ValueError("A data não pode ser anterior à data inicial.")

    weekday = data_alvo.weekday() 

    # 1) Fim de semana? retrocede até sexta e formata o range
    if weekday >= 5:
        # quantos dias volto para chegar à sexta (4)
        days_to_friday = weekday - 4
        sexta = data_alvo - timedelta(days=days_to_friday)

        # encontra o número inteiro da edição de sexta
        edi_num = edi_inicial
        while True:
            if obter_data_por_edicao(edi_num).date() == sexta.date():
                edi_sexta = edi_num
                break
            elif obter_data_por_edicao(edi_num) > sexta:
                raise ValueError("Não encontrou edição de sexta-feira.")
            edi_num += 1

        # sábado = edi_sexta+1, domingo = edi_sexta+2
        return formatar_edicao(edi_sexta + 1, edi_sexta + 2)

    # 2) Dia de semana: busca edição exata e formata número simples
    edi_num = edi_inicial
    while True:
        data_edi = obter_data_por_edicao(edi_num)
        if data_edi.date() == data_alvo.date():
            return formatar_numero(edi_num)
        elif data_edi > data_alvo:
            break
        edi_num += 1

    raise ValueError("Data não corresponde a nenhuma edição válida.")

def formatar_edicao_unica(edicao_numero: int) -> EdicaoInfo:
    data = obter_data_por_edicao(edicao_numero)

    edicao_formatada = formatar_numero(edicao_numero)
    dia_semana = formatar_data(data, tipo='dia_semana').capitalize()

    return EdicaoInfo(
        edicao_sem_ponto=edicao_formatada.replace('.', ''),
        edicao_formatada=edicao_formatada,
        data_formatada=formatar_data(data),
        dia_semana=dia_semana,
        dia_semana_padrão=data.weekday(),
        pasta_nome=f"{edicao_formatada.replace('.', '')} - {dia_semana}",
    )

def gerar_edicoes_formatadas(edicao_inicial=EDICAO_INI, quantidade_por_semana=QUANTIDADE_POR_SEMANA, repeticoes=REPETICOES_PADRAO):
    
    resultados: list[EdicaoInfo] = []
    data_atual = obter_data_por_edicao(edicao_inicial)

    for _ in range(repeticoes):
        edicoes = gerar_edicoes(edicao_inicial, quantidade_por_semana)

        for ed in edicoes:
            ed = ed
            dia_semana = formatar_data(data_atual, tipo='dia_semana').capitalize()
            pasta_nome = f"{ed.replace('.', '')} - {dia_semana.capitalize()}"
            edicao_sem_ponto = ed.replace('.', '')

            info = EdicaoInfo(
                edicao_sem_ponto=edicao_sem_ponto,
                edicao_formatada=ed,
                data_formatada=formatar_data(data_atual),
                dia_semana=dia_semana,
                dia_semana_padrão=data_atual.weekday(),
                pasta_nome=pasta_nome,
            )

            resultados.append(info)

            num = int(ed.replace('.', '').split('-')[0])
            data_atual = obter_data_por_edicao(num)
            passo = 2 if '-' in ed else 1
            data_atual += timedelta(days=passo)
        
        edicao_inicial += quantidade_por_semana + 2

    return resultados


def para_cada_edicao(fazer_algo, edicao_inicial=EDICAO_INI, quantidade_por_semana=QUANTIDADE_POR_SEMANA, repeticoes=REPETICOES_PADRAO):
    for item in gerar_edicoes_formatadas(edicao_inicial, quantidade_por_semana, repeticoes):
        fazer_algo(item)

def obter_data_formatada(nume):
    return formatar_data(obter_data_por_edicao(nume)).capitalize()

edicao_0 = obter_edicao_por_data(datetime.now() + timedelta(days=1))
data_0 = formatar_data(datetime.now() + timedelta(days=1), tipo="dia_semana")
EDD = f"{edicao_0.replace('.', '')} - {data_0}"


if __name__ == "__main__":
    teste1 = datetime.now() + timedelta(days=1)
    teste2 = 8001
    print(obter_edicao_por_data(teste1))
    print(formatar_data(obter_data_por_edicao(teste2)))
    print('...')
    