def exercício_001():
    print('Hello, World!')


def exercício_002():
    nome = input("Digite seu nome: ")
    print("Seja bem vindo(a), {}!".format(nome))


def exercício_003():
    n1 = input("Digite um número: ")
    n2 = input("Digite outro número: ")
    soma = float(n1) + float(n2)
    if soma.is_integer():
        print("A soma de {} e {} é {}.".format(n1, n2, int(soma)))
        return int(soma)
    print("A soma de {} e {} é {}!".format(n1, n2, soma))


def exercício_004():
    info = input("Digite algo: ")
    print("O tipo primitivo desse valor é {}".format(type(info)))
    print("Só tem espaços? {}".format(info.isspace()))
    print("É um número? {}".format(info.isnumeric()))
    print("É alfabético? {}".format(info.isalpha()))
    print("É alfanumérico? {}".format(info.isalnum()))
    print("Está em maiúsculas? {}".format(info.isupper()))
    print("Está em minúsculas? {}".format(info.islower()))
    print("Está capitalizada? {}".format(info.istitle()))
    print("É decimal? {}".format(info.isdecimal()))
    print("É um dígito? {}".format(info.isdigit()))
    print("É imprimível? {}".format(info.isprintable()))
    print("É um identificador válido? {}".format(info.isidentifier()))
    print("É um espaço em branco? {}".format(info.isspace()))
    print("É printável? {}".format(info.isprintable()))
    print("É um número? {}".format(info.isnumeric()))


exercício_004()
