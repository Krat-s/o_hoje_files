import locale
from datetime import datetime, timedelta

# Configura o locale para português do Brasil
locale.setlocale(locale.LC_TIME, "pt_BR.utf8")

# Variáveis auxiliares
marco_babugado = "março"
terca_babugado = "terça-feira, "

# Função auxiliar para verificar fim de semana
def eh_fim_de_semana(data):
    return data.weekday() in [5, 6]  # sábado ou domingo

# Função principal
def formatar_data(data, tipo="completo"):
    dia = int(data.strftime('%d')) 
    dia_formatado = f"{dia}º" if dia == 1 else f"{dia}"
    proximo_dia = int((data + timedelta(days=1)).strftime('%d'))
    proximo_dia_formatado = f"{proximo_dia}º" if proximo_dia == 1 else f"{proximo_dia}"
    mes_de_data = data.strftime('%B')
    proximo_mes = (data + timedelta(days=1)).strftime('%B')
    ano_de_data = data.strftime('%Y')
    virada = (data + timedelta(days=1)).strftime('%Y')

    # Tipo: dia da semana
    if tipo == "dia_semana":
        if eh_fim_de_semana(data):
            return "Fim de semana"
        if data.weekday() == 1:
            return "terça-feira"
        return data.strftime("%A").capitalize()

    # Tipo: mês
    elif tipo == "mes":
        return marco_babugado.capitalize() if data.month == 3 else data.strftime("%B").capitalize()

    # Virada de ano
    if ano_de_data != virada:
        return f"Fim de semana, {dia_formatado} de dezembro de {ano_de_data} e 1º de janeiro {virada}"

    # Mês de março com formatação especial
    if data.month == 3:
        if data.weekday() == 1:
            return f"{terca_babugado}{dia_formatado} de {marco_babugado} de {ano_de_data}"
        elif eh_fim_de_semana(data):
            if mes_de_data != proximo_mes:
                return f"fim de semana, {dia_formatado} de {marco_babugado} e {proximo_dia_formatado} de abril de {ano_de_data}"
            return f"fim de semana, {dia_formatado} e {proximo_dia_formatado} de {marco_babugado} de {ano_de_data}"
        else:
            return f"{data.strftime('%A')}, {dia_formatado} de {marco_babugado} de {ano_de_data}"

    # Fim de semana genérico
    if eh_fim_de_semana(data):
        if mes_de_data != proximo_mes:
            return f"fim de semana, {dia_formatado} de {mes_de_data} e {proximo_dia_formatado} de {proximo_mes} de {ano_de_data}"
        return f"fim de semana, {dia_formatado} e {proximo_dia_formatado} de {mes_de_data} de {ano_de_data}"

    # Terça-feira genérica
    if data.weekday() == 1:
        return f"{terca_babugado}{dia_formatado} de {mes_de_data} de {ano_de_data}"

    # Padrão
    return f"{data.strftime('%A')}, {dia_formatado} de {mes_de_data} de {ano_de_data}"

# --------------------testes---------------------
def main():
    hoje = datetime(2025, 9, 26)
    amanha = hoje + timedelta(days=1)
    ontem = hoje - timedelta(days=1)

    testes = [
        ("Ontem", formatar_data(ontem)),
        ("Hoje", formatar_data(hoje)),
        ("Amanhã", formatar_data(amanha)),
        ("Virada de mar/abr", formatar_data(datetime(2029, 3, 31))),
        ("Virada de ano", formatar_data(datetime(2033, 12, 31))),
        ("Virada de mês random", formatar_data(datetime(2025, 5, 31))),
        ("Dia específico", formatar_data(datetime(2028, 5, 25))),
        ("Mês de março", formatar_data(datetime(2025, 3, 15), tipo="mes")),
        ("Data completa", formatar_data(datetime(2025, 6, 10), tipo="completo")),
        ("Debug 30/09/2025", formatar_data(datetime(2025, 9, 30))),
        ("Debug 30/09/2025", formatar_data(datetime(2025, 9, 1), tipo="dia_semana"))
    ]

    for nome, resultado in testes:
        print(f"{nome}: {resultado}")

if __name__ == "__main__":  
    main()
