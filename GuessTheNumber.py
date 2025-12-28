import random

def guess(x):
    random_number = random.randint(1, x) # gera um número aleatório
    guess = 0
    while guess != random_number: # cria um loop que roda enquanto o número for o errado
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low. ")
        elif guess > random_number:
            print("Sorry, guess again. Too high. ")
    print(f"Yay, congrats! You have the guessed number! {random_number}" )

guess(10) # o X recebe o valor de 10.