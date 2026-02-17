# Faça um laço que mostre de 0 a 100, porém que pule do 14 ao 27 e quebre no 40.
# Utilize break e continue

numero = 0

while numero <= 100:
    if numero >= 14 and numero <= 27:
        numero += 1
        continue 
    print(numero)
    if numero == 40:
        break
    numero += 1