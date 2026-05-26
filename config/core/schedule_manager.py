import schedule
from datetime import datetime

import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(raiz_projeto)

from Global.module.gen_randon_numbers import generate_hours
from Global.settings.settings import acessos_H1, acessos_H2, acessos_H3
from Global.Logs.logs import log



def start_daily_schedules(task_function_):
    """Generates new schedules every day and schedules them again."""
    try:
        schedule.clear("daily_executions") # Limpa agendamentos anteriores
        hours = []
        hours += generate_hours(6, 16, acessos_H1)   # manhã
        hours += generate_hours(16, 22, acessos_H2)  # tarde
        hours += generate_hours(22, 24, acessos_H3)  # noite

        for dt in hours:
            marcacao = dt.strftime("%H:%M")
            schedule.every().day.at(marcacao).do(task_function_).tag("daily_executions")
        
            log("start_daily_schedules", "SUCESSO", 
            f"Agendamentos configurados: {len(hours)} horários agendados para ({datetime.now():%Y-%m-%d})")
        
    except Exception as e:
        erro_msg = f"Erro ao agewndar tarefas: {str(e)}"
        log("All_in_one", "ERRO", erro_msg)
        log("start_daily_schedules", "ERRO", erro_msg)