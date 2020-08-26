import random

money = 100
num = random.randint(1, 10)


def heads_tails(coin_guess, bet):
    heads = 1
    tails = -1
    coin_guess = input("Choose a side: ")
    bet = input("How much to bet?")
    print(coin_guess, bet)

    result = 0
    coin_flip = random.randint(1, 2)

    if coin_flip == 1:
        if coin_guess == heads:
            result = 1

        else:
            result = -1
    if coin_flip == 2:
        if coin_guess == tails:
            result = -1

    if money <= 0:
        print('Sorry! Not enough money to bet.')

# Call your game of chance functions here
