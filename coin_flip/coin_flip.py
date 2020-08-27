import random

num = random.randint(1, 10)
heads = 'heads'
tails = 'tails'
money = 100
total = 0


def heads_tails():
    coin_guess = input("Choose a side: ")
    bet = int(input("How much to bet? "))
    print(coin_guess)
    print(int(bet))

    coin_flip = random.randint(1, 2)
    print(coin_flip)

    if (coin_guess == heads) & (coin_flip == 1):
        total = (money + bet)
        print("You guessed heads and the coin was " + heads + ". You win!")
        print(total)
    elif (coin_flip == 2) & (coin_guess == tails):
        total = (money + bet)
        print("You guessed tails and the coin was " + tails + ". You win!")
        print(total)
    elif (coin_guess == heads) & (coin_flip == 2) | (coin_guess == tails) & (coin_flip == 1):
        total = (money - bet)
        print("You guessed wrong.")
        print(total)


# Call your game of chance functions here
heads_tails()
