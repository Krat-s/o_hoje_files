import pyautogui as pg
import datetime

# ------------------------------ #4 D1
# nome = input("Digite seu nome: ")
# print(f"Seja bem vindo(a) {nome}!")

# ------------------------------ #4 D2
# def desafio_2_my():
#     day = input("Digite o dia do seu nascimento: ")
#     month = input("Digite o mês do seu nascimento: ")
#     year = input("Digite o ano do seu nascimento: ")
#     if datetime.datetime.now() < datetime.datetime(int(year), int(month), int(day)):
#         print("Data de nascimento inválida. Por favor, insira uma data válida.")
#         return
#     if datetime.datetime.now().month < int(month) or (datetime.datetime.now().month == int(month) and datetime.datetime.now().day < int(day)):
#         years_old = datetime.datetime.now().year - int(year) - 1
#     else:
#         years_old = datetime.datetime.now().year - int(year)

#     print(f"Você nasceu em {day}/{month}/{year} e tem {years_old} anos.")


# def desafio_2_my2():
#     day = input("Digite o dia do seu nascimento: ")
#     month = input("Digite o mês do seu nascimento: ")
#     year = input("Digite o ano do seu nascimento: ")
#     if datetime.datetime.now() < datetime.datetime(int(year), int(month), int(day)):
#         print("Data de nascimento inválida. Por favor, insira uma data válida.")
#         return
#     if datetime.datetime.now().month < int(month) or (datetime.datetime.now().month == int(month) and datetime.datetime.now().day < int(day)):
#         years_old = datetime.datetime.now().year - int(year) - 1
#     else:
#         years_old = datetime.datetime.now().year - int(year)

#     button = pg.confirm(
#         "Deseja formatar a data de nascimento?", buttons=["Sim", "Não"])
#     if button == "Sim":
#         print(
#             f"Você nasceu em {datetime.date(int(year), int(month), int(day))} e tem {years_old} anos.")
#     else:
#         print(f"Você nasceu em {day}/{month}/{year} e tem {years_old} anos.")


# def desafio_2():
#     day = input("Digite o dia do seu nascimento: ")
#     month = input("Digite o mês do seu nascimento: ")
#     year = input("Digite o ano do seu nascimento: ")
#     print(f"Você nasceu em {datetime.date(int(year), int(month), int(day))}.")


# ------------------------------  # 4 D3


# def somar_numeros():
# n1 = input("Digite um número: ")
# n2 = input("Digite outro número: ")
# soma = float(n1) + float(n2)
# if soma.is_integer():
#     print(f"A soma de {n1} e {n2} é {int(soma)}.")
#     return int(soma)
# print(f"A soma de {n1} e {n2} é {soma}.")


# -----PRECEDENCIA
# 1 ()
# 2 ** --potencias
# 3 *, /, // divisão inteira, % resto
# 4 +, -

def raiz_quadrada(x):
    r = x ** (1/2)
    return (r)


def raiz_cubica(x):
    r = x ** (1/3)
    return (r)


def printexemplos():
    n = 1500
    n2 = 1500
    s = n2 + n
    m = n * n2
    d = n2 / n2
    di = n2 // n
    e = n ** n2
    print('exemplos {}'.format(n))
    print('exemplos {:20}!'.format(n))
    print('exemplos {:>20}!'.format(n))
    print('exemplos {:<20}!'.format(n))
    print('exemplos {:^20}!'.format(n))
    print('exemplos {:.^20}!'.format(n))
    print('exemplos {:=^20}!'.format(n))
    print('A soma de é {} o produto é {} e a divisão é {:.3f}'.format(s, m, d))
    print('Divisão inteira é {}, e potência'.format(di, e))


printexemplos()
