import os
import sys

modulo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Global_modulos'))

from .Gmail_automações.gmail import create_drafts
from .Quark_automações.Cabeçalho import Modelo_diário


