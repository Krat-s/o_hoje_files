import random
import math


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
    n = float(input('Digite um número ').replace(',', '.'))
    print('O número natural que digitou é: {}'.format(math.trunc(n)))


def exercício_017():
    cat_oposto = float(input('Digite o valor do cateto oposto '))
    cat_adjacente = float(input('Digite o valor do cateto adjacente '))
    hypotenusa = math.hypot(cat_oposto, cat_adjacente)

    if cat_oposto or cat_adjacente != None:
        print('A soma da hipotenusa é: {}'.format(hypotenusa))
    else:
        print('erro')


def exercício_018():
    angulo = float(input('Digite o valor do ângulo '))
    seno = math.sin(angulo)
    cosseno = math.cos(angulo)
    tangente = math.tan(angulo)
    print('O valor de Seno é: {:.2f}, O cosseno é: {:.2f}, e a tangênte é: {:.2f}'.format(
        seno, cosseno, tangente))


def exercício_019():
    n_sorteado = random.randrange(1, 5)
    for x in range(1, 5):
        nome = str(input('Digite o nome de um aluno '))
        if x == n_sorteado:
            novon = nome
            pass
    print('O Aluno sorteado é: {}'.format(novon))


exercício_019()
