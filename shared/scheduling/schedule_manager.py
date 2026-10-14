import schedule
from datetime import datetime
import time as tm
from datetime import datetime, time

from shared.gen_randon_numbers import generate_hours
from settings.settings import acessos_H1, acessos_H2, acessos_H3
from shared.logging.logs import log


def wait_Idle_session_timeout():
    # Define os horários de início e fim do bloqueio
    inicio_bloqueio = time(23, 57)  # 23:57
    fim_bloqueio = time(0, 3)       # 00:03

    while True:
        agora = datetime.now().time()

        # Como o intervalo passa da meia-noite, a lógica usa 'or' (ou)
        # Bloqueia se for depois das 23:58 OU antes das 00:02
        if agora >= inicio_bloqueio or agora <= fim_bloqueio:
            print(
                f"[{datetime.now().strftime('%H:%M:%S')}] Dentro do horário de pausa. Aguardando...")
            tm.sleep(30)  # Verifica novamente a cada 30 segundos
        else:
            print("Fora do horário de pausa. Continuando a execução do script...")
            break


def start_daily_schedules(task_function_):
    """Generates new schedules every day and schedules them again."""
    try:
        schedule.clear("daily_executions")  # Limpa agendamentos anteriores
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
