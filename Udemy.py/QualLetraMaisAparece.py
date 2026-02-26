letra_mais_apareceu = ""
apareceu_mais_vezes = 0
i = 0

while i < len(frase):
    letra = frase[i]
    
    quantas_vezes_letra_apaceceu = frase.count(letra)

    if quantas_vezes_letra_apaceceu > apareceu_mais_vezes:
        apareceu_mais_vezes = quantas_vezes_letra_apaceceu
        letra_mais_apareceu = letra

    i += 1

print(f"A letra que apareceu mais vezes foi '{letra_mais_apareceu}' e apareceu {apareceu_mais_vezes} vezes.")