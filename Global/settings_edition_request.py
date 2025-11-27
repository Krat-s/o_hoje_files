from Logs.logs import log 
quantidade_repeticoes = 10
edicao_inicial = 6965 


total_edicoes = quantidade_repeticoes * 6
edição_final = total_edicoes + edicao_inicial

log("edition_info", "Registro", f"{total_edicoes} criadas, última edição: {edição_final}")
log("All_in_one", "Registro", f"{total_edicoes} criadas, última edição: {edição_final}")
