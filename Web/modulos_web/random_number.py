# import random

# inicio = 0
# fim = 3
# limite = 1

# numeros = list(range(inicio, fim + 1))  
# numeros_aleatorios = random.sample(numeros, limite)

# for n in numeros_aleatorios:
#     gen_nc = n




import random

def gerar_numero(inicio=0, fim=3):
    """Gera um número inteiro aleatório dentro de um intervalo."""
    return random.randint(inicio, fim)