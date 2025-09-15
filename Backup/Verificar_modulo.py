import sys
import os

# Caminho absoluto para a pasta Global_modulos
modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Global_modulos'))

# Adiciona ao sys.path
sys.path.append(modulo_path)

# Importa o módulo
import teste

# Testa a função
teste.fteste()