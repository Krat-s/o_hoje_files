import random


def exercício_011():
    l = float(input('digite quantos metros de altura a parede tem:'))
    a = float(input('digite quantos metros de largura a parede tem:'))
    area = l * a
    qtdness = area / 2
    print('A área da parede tem {:.0f}M². A quantidade de tinha necessária é {:.1f}L:'.format(
        area, qtdness).replace('.0', ''))


def exercício_012():
    preco = float(input('Digite qual o valor do protuto: '))
    porcentagem = int(input('Digite o desconto em porcentagem: '))
    descontocalc = preco - (preco * porcentagem / 100)
    print('O valor total de {} % de desconto, em um produto de R$ {} reais é de R$ {:.2f}'.format(
        porcentagem, preco, descontocalc).replace('.0', ''))


def exercício_013():
    preco = float(input('Digite qual o valor do serviço: '))
    porcentagem = float(input('Digite a porcentagem de aumento: '))
    descontocalc = preco + (preco * porcentagem / 100)
    print(descontocalc)
    print('O novo salário é de R$ {:.2f} reais'.format(
        descontocalc).replace('.00', '').replace('.0', ''))


def exercício_014():
    c = float(input('Informe a temperatura em ºC: '))
    f = 9 * c / 5 + 32
    print('A temperatura de {} ºC corresponde a: {} ºF'.format(
        c, f))


def exercício_015():
    qntdias = float(input('Por quantos dias alugado? ')) * 60
    qntkmr = float(input('Quantos quilômetros rodados? ')) * 0.15
    print('O valor do aluguel é: R$ {:.2f}'.format(qntdias + qntkmr))


def exercício_016():
    import math
    n = float(input('Digite um número '))
    # x = round(n)
    x = math.trunc(n)

    print('O número real que digitou é: {}'.format(x))


exercício_016()
