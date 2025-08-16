# Faça um programa que leia 4 notas, mostre as notas e a média na tela.
# O programa não deve ter notas negativas 

notas = []
total = 0

for i in range(4):
    nota = float(input("Digite a sua nota: "))

    if nota <=0:
        print("Não é possível inserir notas negativas! Tente outra nota.")
    else:
        notas.append(nota)
        total = total + nota


print("As suas notas gerais são: ")
for nota in notas:
    print(nota)

media = total / len(notas) 
print("A média de suas notas é: ")
print(f"{media}")



