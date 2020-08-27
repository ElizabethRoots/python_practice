import random

num = random.randint(1, 10)
heads = 'heads'
tails = 'tails'
money = 100
total = 0


def heads_tails():
    coin_guess = input("Choose a side: ")
    bet = int(input("How much to bet? "))
    print("You guessed: " + coin_guess + " and bet: " + str(int(bet)))

    coin_flip = random.randint(1, 2)
    print(coin_flip)

    if (coin_guess == heads) & (coin_flip == 1):
        total = (money + bet)
        print("Congrats, the coin was " + heads + ". You guessed right!")
        print(total)
    elif (coin_flip == 2) & (coin_guess == tails):
        total = (money + bet)
        print("The coin was " + tails + ". Sorry, but no dice!")
        print(total)
    elif (coin_guess == heads) & (coin_flip == 2) | (coin_guess == tails) & (coin_flip == 1):
        total = (money - bet)
        print("You guessed wrong. Just try again.")
        print(total)


# Call your game of chance functions here
heads_tails()
