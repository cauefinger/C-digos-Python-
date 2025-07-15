# mostrar um valor na tela e gerar 5 valores aleatórios de 1 a 100 para cada valor

import random


for valor in range(1,6):
    print(valor)
    for num_aleat in range(5):
        num = random.randint (1,100)
        print(f"Valor: {num}")