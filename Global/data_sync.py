import os
import sys
import pyautogui as pg
from datetime import datetime, timedelta
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)
import Global.settings as cg
import Global.utils as ut
from App.Modulos_quark.data_formatador import formatar_data
from App.Modulos_quark.edicao_formatador import gerar_edicoes

# function
def obter_data_por_edicao(edi_numero, edi_inicial=6496, data_inicial=datetime(2024, 8, 26)):
    """
    Retorna a data correspondente à edição informada.
    
    Parâmetros:
      edi_numero     : Número da edição desejada (int).
      edi_inicial    : Número da edição base (default 6496) associada a uma data base.
      data_inicial   : Data da edição base (default 26/05/2025, que deve ser uma segunda-feira).
      
    Observação:
      - Este cálculo considera que cada ciclo de 7 números de edição mapeia para 6 dias úteis:
          * Índices 0 a 4 do ciclo correspondem a segunda a sexta.
          * Índices 5 e 6 correspondem a sábado.
    """
    if edi_numero < edi_inicial:
        raise ValueError("O número da edição não pode ser menor que a edição inicial.")

    diff = edi_numero - edi_inicial  # Quantos números de edição já se passaram.
    ciclos = diff // 7               # Cada ciclo possui 7 identificadores.
    resto = diff % 7

    # Para índices 0-4, o avanço é o próprio índice; para 5 ou 6, utiliza 5 (sábado)
    dias_extra = resto if resto < 5 else 5

    # Cada ciclo completo adiciona 7 dias corridos (que já incluem o domingo “oculto”)
    offset_total = ciclos * 7 + dias_extra

    return data_inicial + timedelta(days=offset_total)

edi = cg.edicao_inicial
data_edicao = obter_data_por_edicao(8900)
quantidade_por_semana = 5

def teste():
    print(f"EDITION SYNC: {edi} é {data_edicao.strftime('%A, %d/%m/%Y')}")
    print(f"EDITION SYNC: {edi} é {formatar_data(data_edicao)}")
       
def main2():
    edicao_ini = cg.edicao_inicial
    data_atual = obter_data_por_edicao(edicao_ini)

    for _ in range(cg.quantidade_repeticoes):
        edicoes = gerar_edicoes(edicao_ini, quantidade_por_semana)
        
        for ed in edicoes:
            dia_semana = formatar_data(data_atual, tipo='dia_semana')
            pasta_nome = f"{ed.replace('.', '')} - {dia_semana}"
            info = {
            "edicao_formatada": ed,
            "data_formatada": formatar_data(data_atual),
            "dia_semana": formatar_data(data_atual, tipo='dia_semana')
            }
            # Extrai o número inteiro da edição:
            num = int(ed.replace('.', '').split('-')[0])
            # Recalcula a data exata para essa edição:
            data_atual = obter_data_por_edicao(num)
            # print(f"📦 EDITION SYNC: {ed}, {formatar_data(data_atual).capitalize()}")
            # print(dia_semana)
            # print(pasta_nome) 
            # Se for edição de fim de semana (p.ex., contém "-"), pula 2 dias; senão, 1 dia:
            passo = 2 if '-' in ed else 1
            data_atual += timedelta(days=passo)
        edicao_ini += quantidade_por_semana + 2

def obter_edicao_por_data(data_alvo, edi_inicial=6496, data_inicial=datetime(2024, 8, 26)):
    if data_alvo < data_inicial:
        raise ValueError("A data não pode ser anterior à data inicial.")

    dias_passados = (data_alvo - data_inicial).days
    edicao_numero = edi_inicial

    while True:
        data_edicao = obter_data_por_edicao(edicao_numero, edi_inicial, data_inicial)
        if data_edicao.date() == data_alvo.date():
            return edicao_numero
        elif data_edicao > data_alvo:
            break
        edicao_numero += 1

    raise ValueError("Data não corresponde a nenhuma edição válida.")

data_edicao

if __name__ == "__main__":
    # teste()
    # main2()
    obter_edicao_por_data(datetime.now())
    print(obter_edicao_por_data(datetime.now()))