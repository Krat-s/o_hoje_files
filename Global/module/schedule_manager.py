import schedule
from datetime import datetime

from Global.module.gen_randon_numbers import generate_hours
from Global.settings.settings import acessos_H1, acessos_H2, acessos_H3
from Logs.logs import log

def start_daily_schedules(task_function):
    """Gera novos horários todos os dias e os agenda novamente."""
    schedule.clear("execucoes_diarias") # Limpa agendamentos anteriores
    agendas = []
    agendas += generate_hours(6, 16, acessos_H1)   # manhã
    agendas += generate_hours(16, 22, acessos_H2)  # tarde
    agendas += generate_hours(22, 24, acessos_H3)  # noite

    for dt in agendas:
        marcacao = dt.strftime("%H:%M")
        schedule.every().day.at(marcacao).do(task_function).tag("execucoes_diarias")
        print(f"🕒 Execução agendada para: {marcacao}")
    print(f"✅ {len(agendas)} horários configurados para {datetime.now():%Y-%m-%d}")
    log("start_daily_schedules", "SUCESSO", f"Agendamentos configurados com sucesso")
    log("start_daily_schedules", "SUCESSO", f"{len(agendas)} horários agendados para ({datetime.now():%Y-%m-%d})")

    