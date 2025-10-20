import random

numeros = ["4", "5", "6", "7"]
limite = 1

number_random = random.sample(numeros, limite)

for acao in number_random:
    gen_num = acao

if __name__ == "__main__":
    print(gen_num)
