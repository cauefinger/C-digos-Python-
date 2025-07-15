# abrir laçoes de repetição dentro de um laço de repetição

for contador_externo in range (1,6):
    print(f"/n Rodada: {contador_externo}")
    for contador_interno in range (5,0,-1):
        print(f"{contador_interno}")
print("Fim dos laços.")
