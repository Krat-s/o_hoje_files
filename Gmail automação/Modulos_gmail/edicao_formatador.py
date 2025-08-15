# edicao_formatador.py

def formatar_numero(num):
    return f"{num:,}".replace(",", ".")

def formatar_edicao(inicio, fim):
    inicio_str = str(inicio)
    fim_str = str(fim)

    i = 0
    while i < len(inicio_str) and i < len(fim_str) and inicio_str[i] == fim_str[i]:
        i += 1

    if i == 0:
        return f"{formatar_numero(inicio)}-{formatar_numero(fim)}"

    sufixo_fim = fim_str[i:]
    return f"{formatar_numero(inicio)}-{sufixo_fim}"

def gerar_edicoes(inicial, quantidade_por_semana):
    edicoes = []
    for _ in range(quantidade_por_semana):
        edicoes.append(formatar_numero(inicial))
        inicial += 1

    edicao_fds = formatar_edicao(inicial, inicial + 1)
    edicoes.append(edicao_fds)

    return edicoes