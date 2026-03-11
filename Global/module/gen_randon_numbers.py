from datetime import datetime, timedelta
import random


def generate_number(start=0, end=3):
    '''Gera um número aleatório entre os valores de início e fim.'''
    return random.randint(start, end)


def generate_hours(start_h, end_h, max_accesses):

    '''Gera horários aleatórios dentro de um intervalo de horas. O numero máximo de horários gerados é 
    definido por acessos_max.'''

    hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start = hoje + timedelta(hours=start_h)
    end   = hoje + timedelta(hours=end_h)
    total_s = int((end - start).total_seconds())

    horarios = sorted(
        start + timedelta(seconds=random.randint(0, total_s))
        for _ in range(max_accesses)
    )
    return horarios