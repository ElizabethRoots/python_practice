
balance = 100.0
rate = 0.03

print(0, round(balance, 2))
print("Sanity check")
for n in range(1, 11):
    balance = round(balance * (1 + rate), 2)
    print(n, round(balance, 2))

print("---")
print("Compound totals.")


def compound(balance, rate, num_periods):
    """
    Compound totals with interest
    """
    print(0, round(balance, 2))
    for n in range(1, num_periods):
        balance = round(balance * (1 + rate), 2)
        print(n, round(balance, 2))
    return round(balance, 2)


print(compound(100, 0.03, 10))


print("---")
print("Compound by period.")


def compound_by_period(balance, rate, num_periods):
    """
    Compound period over period
    """
    total = []
    print(0, round(balance, 2))
    for n in range(1, num_periods):
        balance = round(balance * (1 + rate), 2)
        total.append(balance)
        print(n, round(balance, 2), round(sum(total), 2))
    # return round(sum(total),2)
    return total


print(compound_by_period(100, 0.03, 10))

print("---")
print("Change per period ")


def change_per_period(balance, rate, num_periods):
    """
    Change per period
    """
    total = []
    diff = []
    prev = []
    print(0, round(balance, 2))
    for n in range(1, num_periods):
        prev = round(balance, 2)
        balance = round(balance * (1 + rate), 2)
        total.append(balance)
        diff = round(balance, 2) - prev
        print(n, round(balance, 2), round(diff, 2))
    return round(diff, 2)


print(change_per_period(100, 0.03, 10))

print("---")
print("Squares")
square = 0


def chess(square):
    total_wheat = []
    grains = 2 ** (square - 1)
    total_wheat = grains
    print(grains)
    return total_wheat


print(chess(64))
