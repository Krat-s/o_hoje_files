from datetime import datetime, timedelta
from App.Modulos_quark.data_formatador import formatar_data
from App.Modulos_quark.edicao_formatador import gerar_edicoes

# Base fixa para cálculo de data (não precisa ser alterada)
EDICAO_BASE = 6496
DATA_BASE = datetime(2024, 8, 26)  # Segunda-feira

# Parâmetros padrão de geração
QUANTIDADE_POR_SEMANA = 5
REPETICOES_PADRAO = 3

def obter_data_por_edicao(edi_numero, edi_inicial=EDICAO_BASE, data_inicial=DATA_BASE):
    """
    Retorna a data correspondente à edição informada.
    """
    if edi_numero < edi_inicial:
        raise ValueError("O número da edição não pode ser menor que a edição inicial.")

    diff = edi_numero - edi_inicial
    ciclos = diff // 7
    resto = diff % 7

    # Índices 0-4 são dias úteis; 5 e 6 são sábado (pulam domingo)
    dias_extra = resto if resto < 5 else 5
    offset_total = ciclos * 7 + dias_extra

    return data_inicial + timedelta(days=offset_total)

def gerar_edicoes_formatadas(edicao_inicial, quantidade_por_semana=QUANTIDADE_POR_SEMANA, repeticoes=REPETICOES_PADRAO):
    """
    Gera uma lista de edições com data, dia da semana e nome de pasta.
    """
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

            # Extrai número da edição e recalcula a data exata
            num = int(ed.replace('.', '').split('-')[0])
            data_atual = obter_data_por_edicao(num)

            # Se for fim de semana, pula 2 dias; senão, 1
            passo = 2 if '-' in ed else 1
            data_atual += timedelta(days=passo)

        edicao_inicial += quantidade_por_semana + 2

    return resultados

def para_cada_edicao(fazer_algo, edicao_inicial, quantidade_por_semana=QUANTIDADE_POR_SEMANA, repeticoes=REPETICOES_PADRAO):
    """
    Executa uma função para cada edição gerada.
    
    Parâmetro 'fazer_algo' deve ser uma função que recebe um dicionário com:
      - edicao_formatada
      - data_formatada
      - dia_semana
      - pasta_nome
    """
    for item in gerar_edicoes_formatadas(edicao_inicial, quantidade_por_semana, repeticoes):
        fazer_algo(item)