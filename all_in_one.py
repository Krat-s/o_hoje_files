from App import wedding as cm
from App.billhead_editions import auto_billhead_editions
from Mail.gmail import auto_drafts
from Web.print_ad import auto_print_all_ads
from Global.settings.settings_edition_request import quantidade_repeticoes, edicao_inicial



# 📌 ------------------------------------------ envio de emails
def auto_drafts_(ed=None, qnt=None):
    try:
        auto_drafts(ed=ed, qnt=qnt)
    except Exception as e:
        print(f"Erro ao enviar emails: {e}")



# 📌 ------------------------------------------ casamento
def auto_marriage_():
    try:
        cm.auto_marriage()
    except Exception as e:
        print(f"Erro no casamento: {e}")



# 📌 ------------------------------------------ cabeçalho
def auto_billhead_editions_(ed=edicao_inicial, qnt=quantidade_repeticoes):
    try:
        auto_billhead_editions(edicao_inicial=ed, quantidade_repeticoes=qnt)
    except Exception as e:
        print(f"Erro ao enviar fazer o cabeçalho: {e}")



# 📌 ------------------------------------------ print
def auto_print_():
   try:
       auto_print_all_ads()
   except Exception as e:
       print(f"Erro ao imprimir anúncios: {e}")



# Importar aplicações
# 📌 Drive Daily
# 📌 billhead_variables
# 📌 relatório
# 📌 click_farmer
# 📌 Gerar interfaçe gráfica de opções de automações

ed_ini = 7091
qtd = 3

if __name__ == "__main__":
    print('All in one rodando...')
    auto_print_()
    # auto_marriage_()
    # auto_drafts_(ed_ini, qtd)
    # auto_billhead_editions_(ed_ini, qtd)