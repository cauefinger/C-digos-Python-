# 3 exercícios básicos em for
# 1. Use for + range() para imprimir os números de 1 até 10.

numeros = list(range(11))
for numero in numeros:
    print(numero)

#
print("=" * 60) 
# 2. Use for para imprimir apenas os números pares entre 0 e 20.

numeros = list(range(21))
for numero in numeros:
    if numero %2 == 0:
        print(numero)

#
print("=" * 60) 
# 3. Use for para imprimir a frase: Olá, Ana Olá, Carlos Olá, João, Olá Marina

nomes = ["Ana", "Carlos", "João", "Marina"]
for nome in nomes:
    print(f"Olá, {nome}!")

