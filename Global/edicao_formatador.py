def formatar_numero(num):
    """Formata número com ponto como separador de milhar: 6794 → 6.794"""
    return f"{num:,}".replace(",", ".")

def formatar_edicao(inicio, fim):
    """
    Formata dois números de edição com separador de milhar,
    e suprime prefixo comum no segundo número quando apropriado.
    """
    inicio_str = str(inicio)
    fim_str = str(fim)

    # Encontra prefixo comum
    i = 0
    while i < len(inicio_str) and i < len(fim_str) and inicio_str[i] == fim_str[i]:
        i += 1

    if i == 0:
        return f"{formatar_numero(inicio)}-{formatar_numero(fim)}"

    sufixo_fim = fim_str[i:]
    return f"{formatar_numero(inicio)}-{sufixo_fim}"

def gerar_edicoes(inicial, quantidade_por_semana):
    """
    Gera uma lista de edições formatadas com ponto,
    e edição de fim de semana usando formatação inteligente.
    """
    edicoes = []

    for _ in range(quantidade_por_semana):
        edicoes.append(formatar_numero(inicial))
        inicial += 1

    edicao_fds = formatar_edicao(inicial, inicial + 1)
    edicoes.append(edicao_fds)

    return edicoes

# 🧪 Teste didático
if __name__ == "__main__":
    edicao_inicial = 6900
    edicoes_por_semana = 5
    quantidade_repeticoes = 2

    print("📦 Edições geradas:")
    for _ in range(quantidade_repeticoes):
        edicoes = gerar_edicoes(edicao_inicial, edicoes_por_semana)
        for edicao in edicoes:
            print(f"teste: {edicao}")

        edicao_inicial += edicoes_por_semana + 2
