from datetime import datetime

# Definindo datas no formato dia/mês/ano
ad_fist = "01/01/2024"
ad_last = "05/01/2024"

data_inicial = datetime.strptime(ad_fist, "%d/%m/%Y")
data_final = datetime.strptime(ad_last, "%d/%m/%Y")

# Calculando diferença
diferenca = data_final - data_inicial

print(f"A diferença é de {diferenca.days} dias.")




from itertools import cycle

adon_var = ['primeiro', 'segundo', 'terceiro']

for i, adon in zip(range(1, 10), cycle(adon_var)):
    print(f"Processando anúncio {i} - {adon}...")
