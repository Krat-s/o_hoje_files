import sys
import os

raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)

from Web.modulos_web.simply_randon_number import acao

acessos_B1 = int(acao)
acessos_B2 = int(acessos_B1 / 2)
acessos_B3 = int(acessos_B2 / 2 + 1)

# print(acessos_B1)
# print(acessos_B2)
# print(acessos_B3)
