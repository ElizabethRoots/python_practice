'''
Description: Enter in a word and the tool counts the appearance of letters and the total T9 score. 
T9 texting decypher. Why? For no reason in particular.
'''

cypher = {"a": 2, "b": 2, "c": 2, "d": 3, "e": 3, "f": 3, "g": 4, "h": 4, "i": 4, "j": 5, "k": 5,
          "l": 5, "m": 6, "n": 6, "o": 6, "p": 7, "q": 7, "r": 7, "s": 7, "t": 8, "u": 8, "v": 8, "w": 9, "x": 9, "y": 9, "z": 9}

new_word = input("Enter a word: ")
#total = []


# def CountLetters(new_word):
def CountLetters(word):
    dict = {}
    for letter in word:
        charcount = dict.keys()
        if letter in charcount:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict


def decypher(dict):
    for letter in dict:
        if letter in cypher:
            dict[letter] = dict[letter] * cypher[letter]
    return dict


my_word = CountLetters(new_word)
print("The count of each letter is: ", my_word)
my_words = decypher(my_word)
print("The T9 code is: ", my_words, " and the total is: ", sum(my_words.values()))

'''
------------------------------------------------------------
Enter a number and a word that equals that total is listed. 
'''

catalog = {"cat": 12, "dog": 13, "fire": 17, "apple": 17, "music": 27}


def findWord(listOfWords, number):
    #print("You entered: ", number)
    listOfKeys = []
    listOfItems = listOfWords.items()
    for item in listOfItems:
        if item[1] == number:
            listOfKeys.append(item[0])
    return listOfKeys


#listOfKeys = [key for (key, value) in catalog.items() if value == pickedNumber]
test_word = findWord(catalog, 17)
print(test_word)

pickedNumber = input("Enter a number: ")
insertWord = findWord(catalog, int(pickedNumber))
print(insertWord)
# problem = function not accepting number that was picked
