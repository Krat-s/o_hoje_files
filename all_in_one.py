from App import wedding as cm
from Global import utils as ut
from App.billhead_editions import auto_billhead_editions
from Mail.gmail import auto_drafts
# from Mail import gmail as gm
# from Tasks import relatorio as rl


# 📌 ------------------------------------------ envio de emails
def auto_drafts_():
    try:
        auto_drafts()
    except Exception as e:
        print(f"Erro ao enviar emails: {e}")


# 📌 ------------------------------------------ casamento
def auto_marriage_():
    try:
        cm.auto_marriage()
    except Exception as e:
        print(f"Erro no casamento: {e}")


# 📌 ------------------------------------------ cabeçalho
def auto_billhead_editions_():
    try:
        auto_billhead_editions()
    except Exception as e:
        print(f"Erro ao enviar fazer o cabeçalho: {e}")




# Importar aplicações
# 📌 Drive Daily
# 📌 billhead_variables
# 📌 relatório
# 📌 click_farmer
# 📌 Gerar interfaçe gráfica de opções de automações

if __name__ == "__main__":
    auto_drafts_()
    auto_marriage_()
    auto_billhead_editions_()