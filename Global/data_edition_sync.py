# edicao_data_sync.py
from datetime import datetime, timedelta
import os
import sys
from datetime import datetime, timedelta
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)
import Global.settings as cg
import Global.utils as ut
from App.Modulos_quark.data_formatador import formatar_data

def ajustar_data(data):
    return data + timedelta(days=1) if data.weekday() == 6 else data

class EdicaoDataSync:
    """
    Classe para sincronizar edições com datas e vice-versa.
    """

    def __init__(self, edicao_inicial=6496, data_inicial=datetime(2024, 8, 26)):
        """
        Inicializa com uma edição base e sua data correspondente.

        edicao_inicial: número da edição base (int)
        data_inicial: data da edição base (datetime)
        """
        self.edicao_inicial = edicao_inicial
        self.data_inicial = data_inicial

    def obter_data_por_edicao(self, edi_numero):
        """
        Retorna a data correspondente à edição informada.
        """
        

        if edi_numero < self.edicao_inicial:
            raise ValueError("O número da edição não pode ser menor que a edição inicial.")

        diff = edi_numero - self.edicao_inicial
        ciclos = diff // 7
        resto = diff % 7
        dias_extra = resto if resto < 5 else 5
        offset_total = ciclos * 7 + dias_extra
        ajustar_data(self.data_inicial)
        return self.data_inicial + timedelta(days=offset_total)

    def obter_edicao_por_data(self, data_alvo):
        """
        Retorna o número da edição correspondente à data informada.
        """
        if data_alvo < self.data_inicial:
            raise ValueError("A data não pode ser anterior à data inicial.")
        

        dias_passados = (data_alvo - self.data_inicial).days
        edicao_numero = self.edicao_inicial

        while True:
            data_edicao = self.obter_data_por_edicao(edicao_numero)
            if data_edicao.date() == data_alvo.date():
                return edicao_numero
            
            elif data_edicao > data_alvo:
                break
            edicao_numero += 1

        raise ValueError("Data não corresponde a nenhuma edição válida.")

    def gerar_edicoes_e_datas(self, quantidade, passo=1):
        """
        Gera uma lista de edições e suas datas correspondentes.

        quantidade: número de edições a gerar
        passo: incremento entre edições (default 1)
        """
        edicoes_datas = []
        for i in range(quantidade):
            edicao = self.edicao_inicial + i * passo
            data = self.obter_data_por_edicao(edicao)
            edicoes_datas.append((edicao, data))
        return edicoes_datas
       
    


