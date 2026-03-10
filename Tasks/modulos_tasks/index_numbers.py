from Tasks.report import quantidade_de_numeros

def formatar_numero(num):
    """Formata número com ponto como separador de milhar: 6794 → 6.794"""
    return f"{num:,}".replace(",", ".")

def gerar_n(inicial):
    """
    Gera uma lista de edições formatadas com ponto,
    e edição de fim de semana usando formatação inteligente.
    """
    edicoes = []

    for _ in range(quantidade_de_numeros):
        edicoes.append(formatar_numero(inicial))
        inicial += 1

    return edicoes


# 🧪 Teste didático
if __name__ == "__main__":
    edicao_inicial = 36400
    quantidade_de_numeros = 5

    print("📦 Edições geradas:")
    def gerar_numeros():
        for _ in range(1):
            edicoes = gerar_n(edicao_inicial)
            for edicao in edicoes:

                print(f"teste: {edicao}")

            edicao_inicial

    gerar_numeros()

