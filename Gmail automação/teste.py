def formatar_edicao(inicio, fim):
    """
    Formata dois números de edição removendo a parte repetida do segundo número.
    Ex: 6799-6800 → 6799-6800 (sem repetição)
        6794-6795 → 6794-95 (remove prefixo comum)
    """
    inicio_str = str(inicio)
    fim_str = str(fim)

    # Encontra prefixo comum entre os dois números
    i = 0
    while i < len(inicio_str) and i < len(fim_str) and inicio_str[i] == fim_str[i]:
        i += 1

    # Se os números forem totalmente diferentes, exibe ambos completos
    if i == 0:
        return f"{inicio_str}-{fim_str}"

    # Exibe só o sufixo que muda no segundo número
    return f"{int(inicio_str):,}-{int(fim_str[i:])}".replace(',', '.')


def gerar_edicoes(inicial, quantidade_por_semana):
    """
    Gera uma lista de edições com um ciclo padrão semanal + fim de semana formatado.
    """
    edicoes = []

    # Edições padrão da semana
    for _ in range(quantidade_por_semana):
        edicoes.append(str(inicial))
        inicial += 1

    # Edição de fim de semana — formatada
    edicao_fim_de_semana = formatar_edicao(inicial, inicial + 1)
    edicoes.append(edicao_fim_de_semana)

    return edicoes
    




# 🧪 Teste didático

if __name__ == "__main__":
    edicao_inicial = 6594
    edicoes_por_semana = 5
    quantidade_repeticoes = 2

    print("📦 Edições geradas:")
for _ in range(quantidade_repeticoes):
    edicoes = gerar_edicoes(edicao_inicial, edicoes_por_semana)
    for edicao in edicoes:
           print(edicao)

    edicao_inicial += edicoes_por_semana + 2  # Incrementa para a próxima iteração