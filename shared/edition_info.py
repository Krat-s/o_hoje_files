from dataclasses import dataclass

@dataclass
class EdicaoInfo:
    edicao_sem_ponto: str
    edicao_formatada: str
    data_formatada: str
    dia_semana: str
    dia_semana_padrão: int
    pasta_nome: str