
import os
import sys
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Global.daily_task import iniciar_agendador, gerar_horarios
# import Global.daily_task

if __name__ == "__main__":
    print(gerar_horarios)
