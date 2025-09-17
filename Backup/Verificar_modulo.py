import sys
import os

# Caminho absoluto para a pasta Global_modulos
raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(raiz_projeto)


from Global_modulos.teste import tesasdas
# Adiciona ao sys.path

# Importa o módulo

# Testa a função
tesasdas()