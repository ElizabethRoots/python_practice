import numpy as np
import timeit

a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
print(a)

print(" ")
print("Question 2")
lastrow = a[-1]
print(lastrow)
print(type(lastrow))

print(" ")
print("Question 3")
firstcol = a[:, 0]
print(firstcol)
print(len(firstcol))

print(a[1:, 2:])

print(" ")
print("Question 4")
a_gt_5 = a > 5
print(a_gt_5)

print(" ")
print("Question 5")
elements_gt_5 = a[a_gt_5]

print(elements_gt_5)
