# Peça uma frase ao usuário e conte quantas palavras existem 
# Mostre qual palavra aparece mais vezes

frase = input("Escreva uma frase para a contagem de palavras: ")

palavras = frase.split()
contador = len(palavras)

mais_frequente = " "
maior_contagem = 0 

for palavra in palavras: 
    contagem = 0
    for p in palavras:
        if p == palavra:
            contagem += 1
    if contagem > maior_contagem:
        maior_contagem = contagem
        mais_frequente = palavra
print("Quantidade de palavras:", contador)
print("Palavra mais frequente:", mais_frequente)
