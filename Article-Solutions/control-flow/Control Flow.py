# Large Power
# Write your large_power function here:
def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False


# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
print(large_power(5000, 1))

# ------------------------------------------

# Over Budget
# Write your over_budget function here:


def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if (budget < (food_bill + electricity_bill + internet_bill + rent)):
        return True
    else:
        return False


# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

# ----------------------------------
# Twice As Large
# Write your twice_as_large function here:


def twice_as_large(num1, num2):
    if num1 > (num2 * 2):
        return True
    else:
        return False


# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True
print(twice_as_large(21, 10))
