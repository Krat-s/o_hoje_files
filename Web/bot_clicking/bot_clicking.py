import os
import sys

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Global.daily_task_random_time import daily_task_loop

if __name__ == "__main__":
    daily_task_loop()