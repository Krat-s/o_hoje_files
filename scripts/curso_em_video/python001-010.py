def raiz_quadrada(x):
    r = x ** (1/2)
    return (r)


def raiz_cubica(x):
    r = x ** (1/3)
    return (r)

# --------------------------------------


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


def exercício_005():
    n = int(input("Digite um número: "))
    print("O número digitado foi {}, seu antecessor é {} e o sucessor é {}".format(
        n, n - 1, n + 1))


def exercício_006():
    n = int(input("Digite um número: "))
    print("O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}".format(
        n, n * 2, n * 3, n ** (1/2)))


def exercício_007():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    print('A média da nota é: {:.1f}'.format(media).replace('.0', ''))


def exercício_008():
    medida = float(input('Digite a distância em metros: '))
    print('A distancia de {} M corresponde à  \n {} quilômetros \n {} hectômetros \n {} decâmetros \n {} Metros \n {} centimetros \n {} milímetros'.format(
        medida, medida / 1000, medida / 100, medida / 10, medida, medida * 10, medida * 100).replace('.0', ''))


def exercício_009():
    n = int(input("Digite um número: "))
    print("===" * 10 + '\n    Tabuada do {}:\n'.format(n) + "===" * 10)
    for i in range(1, 11):
        multiplo = n * i
        print('  {} x{:>5}:{:>5}'.format(n, i, multiplo))

    print("==="*10)


def exercício_010():
    n = float(input("Digite quantos reais você tem: "))
    dolar = n / 5.14
    print('Você pode comprar $ {:.3} dolares'.format(dolar))


exercício_010()
