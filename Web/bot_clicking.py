import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Global.daily_task_random_time import agendamento, gerar_horarios

if __name__ == "__main__":
    agendamento()
    # print(gerar_horarios)
