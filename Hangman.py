palavras = [
    # FÁCEIS (1–35)
    "cat", "dog", "sun", "moon", "book", "pen", "tree", "car", "ball", "fish",
    "bird", "milk", "water", "house", "door", "chair", "table", "phone", "cup", "shoe",
    "hat", "apple", "banana", "bread", "smile", "happy", "sad", "run", "walk", "jump",
    "sleep", "eat", "drink", "play", "love",

    # MÉDIAS (36–70)
    "computer", "python", "window", "garden", "school", "teacher", "student", "picture", "music", "guitar",
    "football", "kitchen", "bathroom", "bedroom", "language", "country", "weather", "holiday", "friends", "family",
    "internet", "message", "morning", "evening", "market", "restaurant", "history", "science", "problem", "solution",
    "example", "program",

    # DIFÍCEIS (71–100)
    "development", "technology", "algorithm", "architecture", "psychology", "philosophy", "independent", "communication", "environment", "responsibility",
    "imagination", "intelligence", "mathematics", "relationship", "information", "opportunity", "understanding", "consequence", "determination", "achievement",
    "performance", "confidence", "experience", "knowledge", "creativity", "discipline", "motivation", "efficiency", "complexity", "perspective"
]

import random

def pegue_palavra_aleatoria(palavras):
    return random.choice(palavras)

palavra_escolhida = pegue_palavra_aleatoria(palavras)
letras = ["_"] * len(palavra_escolhida)      
tentativas = 6
# ok
while tentativas > 0 and "_" in letras:
    print("\nPalavra:", " " .join(letras))
    print("Tentativas restantes:", tentativas)

    palpite = input("Digite uma letra: ").lower()
# ok
    if len(palpite) != 1 or not palpite.isalpha():
        print("Digite apenas uma letra válida. ")
        continue
    if palpite in palavra_escolhida:
        for i in range(len(palavra_escolhida)):
            if palavra_escolhida[i] == palpite:
                letras[i] = palpite
        print("Boa! Você acertou.")
    else:
        tentativas -= 1
        print("Errou!")
if "_" not in letras:
    print("\n🎉 Você ganhou!")
else:
    print("\n💀 Você perdeu!")

print("A palavra era:", palavra_escolhida)