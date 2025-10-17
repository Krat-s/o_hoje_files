from App import casamento as cm
from Global import utils as ut
from App import cabeçalho as cç
from Mail import gmail as gm
# from Mail import gmail as gm
# from Tasks import relatorio as rl

# 📌 ------------------------------------------ envio de emails

# 📌 ------------------------------------------ casamento
cm.auto_casamento()

def mds ():
    gm.auto_emails()
    cç.auto_cabecalho()

# 📌 ------------------------------------------ cabeçalho
# Importar aplicações
# 📌 relatório
# 📌 click_farmer
# 📌 Drive Daily 

# Gerar interfaçe gráfica de opções de automações
print('cabo')