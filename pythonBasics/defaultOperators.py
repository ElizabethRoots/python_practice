myname = 'My' + ' ' + 'Name'
print(myname)

# print your name by passing values


def add_two_strings_with_separator(first, second, separator):
    message = first + separator + second
    return message


yourname = add_two_strings_with_separator('Your', 'Name', ' ')
print(yourname)

# print her name


def add_two_strings(first, second, separator=' '):
    msg = first + separator + second
    return msg


hername = add_two_strings('Her', 'Name')
print(hername)
her_name = add_two_strings('Her', 'Name', '_')
print(her_name)

# In order to get all the tests to pass,
# I had to pass the structure of the string (line 14)
# to a variable.

# It would be fewer lines of code if I just printed
# the statement, because then I wouldn't need the print() lines.

# Here is an example (but this wouldn't pass the tests
# def add_two_strings(first, second, separator = ' '):
#   print(first + separator + second)
#
# hername = add_two_strings('Her', 'Name')

# Section 2 of 3
result1 = add_two_strings(first='My', second='Name')
result2 = add_two_strings(second='My', first='Name')
print(result1)
print(result2)
