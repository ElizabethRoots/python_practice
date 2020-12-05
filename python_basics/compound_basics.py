
balance = 100.0
rate = 0.03

print(0, round(balance, 2))
for n in range(1, 11):
    balance = round(balance * (1 + rate), 2)
    print(n, round(balance, 2))

print(" ")
print("Compound")


def compound(balance, rate, num_periods):
    """
    Compound 
    """
    print(0, round(balance, 2))
    for n in range(1, num_periods):
        balance = balance * (rate + 1)
        current_balance = balance
        print(n, round(current_balance, 2))
    return (n, round(current_balance, 2))


print(compound(100, 0.03, 11))

print(" ")
print("Compound by period")


def compound_by_period(balance, rate, num_periods):
    """
    Compound by period
    """
    yr_balance = []
    print(0, round(balance, 2))
    for n in range(1, num_periods):
        balance = (rate + 1) * balance + 1
        yr_balance.append(balance)
        print(n, round(sum(yr_balance), 2))
    return yr_balance


print(compound_by_period(100, 0.03, 11))

print(" ")
print("Change per period")


def change_per_period(balance, rate, num_periods):
    """
    Change per period
    """
    total = []
    diff = []
    prev = []
    for n in range(1, num_periods):
        prev = round(balance, 2)
        balance = round(balance * (1 + rate), 2)
        total.append(balance)
        diff = round(balance, 2) - prev
    return total


print(change_per_period(100, 0.03, 11))

print(" ")
print("Wheat")
wheat = compound_by_period(1, 1, 64)
print(wheat)
total_wheat = wheat.pop()
print(total_wheat)
