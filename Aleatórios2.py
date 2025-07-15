# função que utiliza laço de repetição for para gerar 5 números aleatórios utilizando randint

import random

for R in range(5):
   aleatórios = random.randint(1,1000)
   print(f"Os números escolhidos de forma aleatória foram: {aleatórios}!\n")
   print(R)
