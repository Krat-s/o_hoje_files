import sys
import os

# Caminho absoluto para a pasta Global_modulos
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Global_modulos.utils import verificar_windows