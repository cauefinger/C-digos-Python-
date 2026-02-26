# é possível utilizar o Else após um laço While
# Else não é válido se o laço é quebrado (Beak)

string = "Qualquer valor"
i = 0

while i < len(string):
    letra = (string[i])
    print(letra)
    i +=1
    if letra == " ":
        print("Um espaço foi encontrado em sua string")
        break
else:   
    print("Seu laço while terminou.")
    print("Nenhum espaço encontrado.")