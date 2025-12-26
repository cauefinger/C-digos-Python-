# imprima na tela os padrões de 1 a 5

lista = []
numero = 0

while numero < 5:
    numero += 1
    
    lista.append(numero)
    
    for elemento in lista:
        print(elemento, end = " ")
    print()
