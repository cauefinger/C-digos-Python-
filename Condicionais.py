# Calcular nota de aluno
n1 = n2 = 0.0
media = 0.0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) /2
if media >= 6:
    print("você foi aprovado!")
    print("Parabéns!")

else:
    print("Você foi reprovado...")

print("sua média é {}.".format (media))