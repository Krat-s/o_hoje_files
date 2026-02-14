import locale
import time
import pyautogui as pg
from datetime import datetime, timedelta

# Configura o locale para português do Brasil
locale.setlocale(locale.LC_TIME, "pt_BR.utf8")

# Variáveis auxiliares
marco_babugado = "março"
terca_babugado = "terça-feira, "

# Função auxiliar para verificar fim de semana
def eh_fim_de_semana(data):
    return data.weekday() in [5]  # saturday

def eh_domingo(data):
    return data.weekday() in [6]

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
        if eh_domingo(data):
            return "Domingo"
        if eh_fim_de_semana(data):
            return "Fim de semana"
        if data.weekday() == 1:
            return "terça-feira"
        return data.strftime("%A").capitalize()

    # Tipo: mês
    elif tipo == "mes":
        return marco_babugado.capitalize() if data.month == 3 else data.strftime("%B").capitalize()

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
         # Virada de ano
        if ano_de_data != virada and data.weekday() == 6:
            return f"Domingão"
        if data.weekday() == 5 and ano_de_data != virada:
            return f"Fim de semana, {dia_formatado} de dezembro de {ano_de_data} e 1º de janeiro {virada}"
        if mes_de_data != proximo_mes:
            return f"fim de semana, {dia_formatado} de {mes_de_data} e {proximo_dia_formatado} de {proximo_mes} de {ano_de_data}"
        return f"fim de semana, {dia_formatado} e {proximo_dia_formatado} de {mes_de_data} de {ano_de_data}"

    # Terça-feira genérica
    if data.weekday() == 1:
        return f"{terca_babugado}{dia_formatado} de {mes_de_data} de {ano_de_data}"

    # Padrão
    return f"{data.strftime('%A')}, {dia_formatado} de {mes_de_data} de {ano_de_data}"

# --------------------testes---------------------
hoje = datetime.now()
amanha = hoje + timedelta(days=1)
def main():
    hoje = datetime.now()
    amanha = hoje + timedelta(days=1)
    ontem = hoje - timedelta(days=1)

    testes = [
        ("Ontem", formatar_data(ontem)),
        ("Hoje", formatar_data(hoje)),
        ("Amanhã", formatar_data(amanha)),
        # ("Virada de mar/abr", formatar_data(datetime(2029, 3, 31))),
        # ("Virada de ano 29", formatar_data(datetime(2029, 12, 31))),
        # ("Virada de ano 29", formatar_data(datetime(2030, 1, 1))),

        ("Virada de ano 30", formatar_data(datetime(2030, 12, 31))),
        ("Virada de ano 30", formatar_data(datetime(2031, 1, 1))),

        ("Virada de ano 31", formatar_data(datetime(2031, 12, 31))),
        ("Virada de ano 31", formatar_data(datetime(2032, 1, 1))),

        ("Virada de ano 32", formatar_data(datetime(2032, 12, 31))),
        ("Virada de ano 32", formatar_data(datetime(2033, 1, 1))),

        ("Virada de ano 33 - FDS", formatar_data(datetime(2033, 12, 31))),
        ("Virada de ano 33", formatar_data(datetime(2034, 1, 1))),


        ("Virada de ano 34", formatar_data(datetime(2034, 12, 31))),
        ("Virada de ano 34", formatar_data(datetime(2035, 1, 1))),

        ("Virada de ano 35", formatar_data(datetime(2035, 12, 31))),
        ("Virada de ano 36", formatar_data(datetime(2036, 12, 31))),
        ("Virada de ano 37", formatar_data(datetime(2037, 12, 31))),
        ("Virada de ano 38", formatar_data(datetime(2038, 12, 31))),
        ("Virada de ano 39 - FDS", formatar_data(datetime(2039, 12, 31))),
        ("Virada de ano 40", formatar_data(datetime(2040, 12, 31))),



        # ("Virada de mês random", formatar_data(datetime(2025, 5, 31))),
        # ("Dia específico", formatar_data(datetime(2028, 5, 25))),
        # ("Mês de março", formatar_data(datetime(2025, 3, 15), tipo="mes")),
        # ("Data completa", formatar_data(datetime(2025, 6, 10), tipo="completo")),
        # ("Debug 30/09/2025", formatar_data(datetime(2025, 9, 30))),
        # ("Debug 30/09/2025", formatar_data(datetime(2025, 9, 30), tipo="dia_semana")),
        ("Debug virada", formatar_data(datetime(2025, 12, 31))),
        ("Debug domingo", formatar_data(datetime(2026, 1, 4)))  
    ]

    for nome, resultado in testes:
        print(f"{nome}: {resultado}")

if __name__ == "__main__":  
    main()