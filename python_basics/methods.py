# Built in methods for lists, tuples, and strings
# %run methods.py

print("--LISTS--")
# create and append to a list
movie_list = ["John Wick 2", "John Wick 1", "John Wick 3"]
movie_list.append("kick ass")
print(movie_list)

# Returns first index (position) of element in list
numList = [11, 15, 18]
print(numList.index(18))

# Returns number of times an element occurs in a list
print(movie_list.count("kick ass"))

# Sorts list in-place by altering the data in the list
movie_list.sort()
print("Sorted Movies: ", movie_list)

# Reverses order of list in-place
movie_list.reverse()
print("Reversed Movies: ", movie_list)

# ---------------
print(" ")
print("--TUPLES--")

# Returns first index (position) of element in tuple
days = ("monday", "sunday", "thursday")
startingDay = days.index("monday")
print("The position in the list is: ", startingDay)

# Returns number of times an element occurs in a tuple
print(days.count("monday"))

# ---------------
print(" ")
print("--STRING--")
# Returns True or False depending on whether the string is made up entirely of digits
'142'.isdigit()

# Returns True or False depending on whether the string is all lowercase
'ABCdef'.islower()

# Returns True or False depending on whether the string is all uppercase
'ABCDEF'.isupper()

# Returns a new copy of the string converted to lowercase
'ABCdef'.lower()

# Returns a new copy of the string converted to uppercase
'ABCdef'.upper()

# Returns a new string in which the first character is uppercase and the rest lower
'hello'.capitalize()

# Returns True if a string starts with a specified prefix, False otherwise
'Python'.startswith('Py')

# Returns True if a string ends with a specified suffix, False otherwise
'filename.csv'.endswith('.csv')

# ---------------
print(" ")
print("--DICTIONARIES--")

# create a dict
fruitDict = {
    "name": "apple",
    "color": "red",
    "count": 1
}

# Set of all keys used to map values in a dictionary but in no guaranteed order
print(fruitDict.keys())

# Set of dictionary values in the dictionary mapping
print(fruitDict.values())

# Set of all key-value pairs in the dictionary (each pair is a tuple)
print(fruitDict.items())

# Returns the value associated with a certain key, but can also return a default value if that key does not exist in the dictionary
print(fruitDict.get("name", 0))

# Returns the value from the dictionary associated with a key and removes (or pops) the key-value pair from the dictionary
fruitDict.pop("name")
print(fruitDict)

# Updates existing dictionary with the keys-values from another dictionary
fruits = {
    1: "apples",
    2: "bananas",
    3: "pear"
}

newFruit = {
    2: "orange"
}

fruits.update(newFruit)
print(fruits)

# ---------------
print(" ")
print("--SETS--")

# create a new set
my_set = {"abc", "nbc", "cbs"}
your_set = {"tv", "movie"}

# Returns new set as union of this set and another set
x = my_set
z = your_set
print(x.union(z))

# Returns new set as intersection of this set and another set
y = my_set
print(y.intersection(z))

# Returns new set with everything in this set that is not in another set
a = my_set
print(a.difference(your_set))  # same as my_set - your_set
