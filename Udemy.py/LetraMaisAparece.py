# Encontre a letra que mais se repete na frase
# Diga quantas vezes ela se repetiu

frase = "frase sobre alguma coisa"
i = 0
qtd_apareceu_mais = 0
letra_apareceu_mais = " "

while i < len(frase):
    letra = frase[i]

    if letra == " ":
        i += 1
        continue
        

    qtd_apareceu_mais_atual = frase.count(letra) # mostra quantas vezes cada letra aparece

    if qtd_apareceu_mais_atual > qtd_apareceu_mais:
        qtd_apareceu_mais = qtd_apareceu_mais_atual
        letra_apareceu_mais = letra
    i += 1

print(qtd_apareceu_mais)
print(letra_apareceu_mais)