# Data containers and how to access them.

# create a list
print("--EXPLORING LISTS--")
fruitList = ["apple", "banana", "cherry"]
print(fruitList)

# print the first item in the list
print('The first item in the list is', fruitList[0])

# add an item to the list
fruitList.append("pear")

# prints list with the new item
print(fruitList)

# prints the last item in the list
print(fruitList[-1])

# get total count of items in list
print(len(fruitList))  # should return 4

# extending the list by adding a fruit by eachletter
fruitList.extend("kiwi")

# prints list and individual letters k i w i
print(fruitList)

# create a new fruit list
more_fruit = ["orange", "starfruit"]

# combine and print both fruitLists and more_fruit on the same line
fruitList.extend(more_fruit)
print(fruitList)

# count the new total of items - should return 10
print(len(fruitList))

# --------------
print(' ')
print("--EXPLORING SETS--")

# create a set
fruitSet = {"apple", "banana", "cherry"}
print(fruitSet)

#  loop through the set and print the set
for x in fruitSet:
    print(x)

# check for a value present in the set. Returns True
print("banana" in fruitSet)

#  add item to a set
fruitSet.add("grape")
print(fruitSet)  # returns grape, apple, banana, cherry

# remove an item from a set
fruitSet.remove("apple")
print(fruitSet)  # returns grape, cherry, banana

# get count (or length) of a set - returns 3
print(len(fruitSet))

# remove the last item from the list
newFruit = ["apple", "orange", "pear"]
x = newFruit.pop()  # returns item removed from the list - pear
print(x)  # prints updated list
print(newFruit)  # prints updated list

# --------------
print(' ')
print("--EXPLORING DICTIONARIES--")

# create a dict
fruitDict = {
    "name": "apple",
    "color": "red",
    "count": 1
}

# print dictionary
print("Dict key-value are: ")
for key, value in fruitDict.items():
    print(key, value)

# print the dictionary using enumerate to get the key/value pair
print("Dict key-value are : ")
for i in enumerate(fruitDict.items()):
    print(i)

# change value
fruitDict["count"] = 2

# return the color value from the key pair - red
print(fruitDict["count"])

# print length of the dictionary
print(len(fruitDict))

# add item to dictionary
fruitDict["size"] = "large"
print(fruitDict)

# --------------
print(' ')
print("--EXPLORING TUPLE--")

# create a tuple
fruitTuple = ("apple", "banana", "cherry")
print(fruitTuple)

# print second item in a tuple
print(fruitTuple[1])

# convert tuple to list
fruitTupleList = list(fruitTuple)
print(fruitTupleList)

fruitTupleList[1] = "kiwi"  # replaces banana with kiwi

fruitTuple = tuple(fruitTupleList)
print(fruitTuple)
print(type(fruitTuple))
print(len(fruitTuple))
