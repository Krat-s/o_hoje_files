import os
import sys
import pyautogui as pg
from datetime import datetime, timedelta
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)
import Global_modulos.settings as cg
from Quark_automações.Modulos_quark.data_formatador import formatar_data
from Quark_automações.Modulos_quark.edicao_formatador import gerar_edicoes

# ---------------------------- CONFIGURAÇÕES ----------------------------
pg.PAUSE = 0.4

# ---------------------------- VARIÁVEIS ----------------------------
def obter_data_por_edicao(edi_numero, edi_inicial_base=6496, data_inicial=datetime(2024, 8, 26)):
    """
    Retorna a data correspondente à edição informada.
    
    Parâmetros:
      edi_numero     : Número da edição desejada (int).
      edi_inicial_base    : Número da edição base (default 6769) associada a uma data base.
      data_inicial   : Data da edição base (default 26/05/2025, que deve ser uma segunda-feira).
      
    Observação:
      - Este cálculo considera que cada ciclo de 7 números de edição mapeia para 6 dias úteis:
          * Índices 0 a 4 do ciclo correspondem a segunda a sexta.
          * Índices 5 e 6 correspondem a sábado.
    """
    if edi_numero < edi_inicial_base:
        raise ValueError("O número da edição não pode ser menor que a edição inicial.")
        
    diff = edi_numero - edi_inicial_base  # Quantos números de edição já se passaram.
    ciclos = diff // 7               # Cada ciclo possui 7 identificadores.
    resto = diff % 7

    # Para índices 0-4, o avanço é o próprio índice; para 5 ou 6, utiliza 5 (sábado)
    dias_extra = resto if resto < 5 else 5

    # Cada ciclo completo adiciona 7 dias corridos (que já incluem o domingo “oculto”)
    offset_total = ciclos * 7 + dias_extra

    return data_inicial + timedelta(days=offset_total)

# Exemplo de uso:
edicao_ini = cg.edicao_inicial #Precisa ser uma segunda-feira
data_edicao = obter_data_por_edicao(edicao_ini)
quantidade_por_semana = 5
data = data_edicao
    
def data():
    
    for _ in range(cg.quantidade_repeticoes):
        edicoes = gerar_edicoes(edicao_ini, quantidade_por_semana)

        for ed in edicoes:
            dia_semana = formatar_data(data, tipo='dia_semana')
            pasta_nome = f"{ed.replace('.', '')} - {dia_semana}"
            info = {
            "edicao_formatada": ed,
            "data_formatada": formatar_data(data),
            "dia_semana": formatar_data(data, tipo='dia_semana')
            }
            # print(f"📦 Criando: {pasta_nome}")
            # print(f"📦 Criando: {ed}, que corresponde a data {formatar_data(data)}")
            data += timedelta(days=1)
        edicao_ini += quantidade_por_semana + 2


print(data)