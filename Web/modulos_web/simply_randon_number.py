import random
import time

# Lista de ações simuladas
numeros = ["5", "6", "7", "8", "9"]

# Limite de ações a executar
limite = 1

# Seleciona ações aleatórias sem repetir
acoes_escolhidas = random.sample(numeros, limite)

# Executa cada ação com um intervalo
for acao in acoes_escolhidas:
    acessos_B1 = acao

acessos_B1 = int(acao)
acessos_B2 = int(acessos_B1 / 2)
acessos_B3 = int(acessos_B2 / 2 + 1)


if __name__ == "__main__":
    print(acessos_B1)
    print(acessos_B2)
    print(acessos_B3)
