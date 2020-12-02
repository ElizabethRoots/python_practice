my_list = [1, 3, 14, 22, 29, 43, 89, 102, 256]


def extract_even_numbers_in_list(alist):
    """
    Returns a list of the numbers in the input alist
    that are even numbers

    NOTE: n%2 == 0 if n is even,  n%2 == 1 if n is odd
    """
    result = []
    for elem in alist:
        if elem % 2 == 0:
            result.append(elem)
    return result


def extract_digits_from_string(s):
    """
    Returns a list of all the digits that appear in a string,
    in the order in which they are encountered.
    """
    result = []
    for c in s:
        if c.isdigit():
            result.append(c)
    return result


def make_dict_of_squares(n):
    """
    Returns a dictionary that maps from integers to their squares,
    starting with 0 and ending at one less than the input n
    """
    result = {}
    for i in range(n):
        result[i] = i*i
    return result


# Create new lists that does the same thing the above functions do.
# Accomplish this with list comprehensions only
my_evens = extract_even_numbers_in_list(my_list)
my_evens2 = [elem for elem in my_list if elem % 2 == 0]

# my_evens2 = [extract_even_numbers_in_list(i) for i in my_list if i % 2 == 0]


s = 'The answer is 42, but many people guess 12.'
str_digits = extract_digits_from_string(s)
str_digits2 = [c for c in s if c.isdigit()]


# Create new dictionary that des the same thing as make_dict_of_squares
squares = make_dict_of_squares(10)
squares2 = {x: x**2 for x in range(10)}

# -----------------------
# For list to print out only evens
circles = []
for i in range(10):
    if i % 2 == 0:
        circles.append(i)

print(circles)

# List comprehension that does the same thing
circle = [i for i in range(10) if i % 2 == 0]
print(circle)


# Pass a function as an iterable map()
# Create a shopping list and calculate tax rate


def get_price_with_tax(items, tax_rate):
    total = items + (items * tax_rate)
    total = round(total, 2)
    return total


print(get_price_with_tax(2.43, .08))

# List comprehension that does the same thing as the get_price_with_tax function
tax_with_items = [round(i + (i * r), 2)
                  for i in [2.43] for r in [.08]]
print(tax_with_items)
