from App import wedding as cm
from Global import utils as ut
from App import billhead_editions as be_all
from Mail import gmail as gm
# from Mail import gmail as gm
# from Tasks import relatorio as rl

# 📌 ------------------------------------------ envio de emails
try:
    gm.auto_emails()
except Exception as e:
    print(f"Erro ao enviar emails: {e}")

# 📌 ------------------------------------------ casamento
# try:
#     cm.auto_marriage()
# except Exception as e:
#     print(f"Erro no casamento: {e}")


# 📌 Drive Daily 
# 📌 ------------------------------------------ cabeçalho
# cç.auto_billhead()
try:
    be_all.auto_billhead()
except Exception as e:
    print(f"Erro ao enviar emails: {e}")


# Importar aplicações
# 📌 relatório
# 📌 click_farmer

# Gerar interfaçe gráfica de opções de automações
print('cabo')