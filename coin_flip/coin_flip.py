import random

num = random.randint(1, 10)


def heads_tails():
    heads = 'heads'
    tails = 'tails'
    money = 100
    total = 0
    coin_guess = input("Choose a side: ")
    bet = int(input("How much to bet? "))
    print(coin_guess)
    print(int(bet))

    coin_flip = random.randint(1, 2)
    print(coin_flip)

    if coin_flip == 1:
        if coin_guess == heads:
            total = (money + bet)
            print("You guessed heads and the coin was " +
                  heads + ". You win!")
            print(total)
        else:
            total = (money - bet)
            print("You guessed heads and the coin was " +
                  tails + ". You lost.")
            print(total)
    if coin_flip == 2:
        if coin_guess == tails:
            total = (money + bet)
            print("You guessed tails and the coin was " +
                  tails + ". You win!")
            print(total)
        else:
            total = (money - bet)
            print("You guessed tails and the coin was " +
                  heads + ". You lost!")
            print(total)


# Call your game of chance functions here
heads_tails()
