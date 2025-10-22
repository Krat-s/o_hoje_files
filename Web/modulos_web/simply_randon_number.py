import random

import random

inicio = 2
fim = 3
limite = 1

numeros = list(range(inicio, fim + 1))  
numeros_aleatorios = random.sample(numeros, limite)

numeros2 = list(range(0, 6 + 1))
numeros_aleatorios2 = random.sample(numeros2, limite)

for n in numeros_aleatorios:
    gen_nc = n

for n2 in numeros_aleatorios2:
    gen_nh = n2


# numero de acessos totais
# numero de visualizações
# numero de acessos por horario (3)
# numerod de acessos por botão