
import os
import sys
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Global.daily_task import iniciar_agendador

if __name__ == "__main__":
    iniciar_agendador()
