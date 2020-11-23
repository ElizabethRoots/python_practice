
# 2
# contains_a = lambda word: "a" in word
import random
def contains_a(word): return "a" in word


print contains_a("banana")
print contains_a("apple")
print contains_a("cherry")


# 3
# long_string = lambda word: len(word) > 12
def long_string(word): return len(word) > 12


print long_string("short")
print long_string("photosynthesis")


# 4
# ends_in_a = lambda str: "a" in str[-1]
def ends_in_a(str): return "a" in str[-1]


print ends_in_a("data")
print ends_in_a("aardvark")


# 5
# double_or_zero = lambda num: num * 2 if num > 10 else 0
def double_or_zero(num): return num * 2 if num > 10 else 0


print double_or_zero(15)
print double_or_zero(5)


# 6
# even_or_odd = lambda num: "even" if num % 2 == 0 else "odd"
def even_or_odd(num): return "even" if num % 2 == 0 else "odd"


print even_or_odd(10)
print even_or_odd(5)


# 7
# multiple_of_three = lambda num: "multiple of three" if num % 3 == 0 else "not a multiple"
def multiple_of_three(
    num): return "multiple of three" if num % 3 == 0 else "not a multiple"


print multiple_of_three(9)
print multiple_of_three(10)


# 8
# rate_movie = lambda rating: "I liked this movie" if rating > 8.5 else "This movie was not very good"
def rate_movie(
    rating): return "I liked this movie" if rating > 8.5 else "This movie was not very good"


print rate_movie(9.2)
print rate_movie(7.2)


# 9
# ones_place = lambda num: num % 10
def ones_place(num): return num % 10


print ones_place(123)
print ones_place(4)


# 10
#double_square = lambda num: 2 * num * num
def double_square(num): return 2 * num * num


print double_square(5)
print double_square(3)


# 11
# import random
# add_random = lambda num: num + 1
def add_random(num): return num + 1


print add_random(5)
print add_random(100)
