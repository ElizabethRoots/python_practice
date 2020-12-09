# This mini project is part of 2020 Advent of Code https://adventofcode.com/2020
# Day 1 (both solutions)

import pandas as pd
import csv


df = pd.read_csv(r'saving_christmas_expense.csv', sep=',')
print(df)

a_expense = df.values.tolist()
b_expense = df.values.tolist()
c_expense = df.values.tolist()
print(a_expense)

total = []
total2 = []
mul_expense = []
sum_expense = 2020
new_num1 = []
new_num2 = []
new_num3 = []
# For each element in the first list
for i in range(len(a_expense)):

    # For each element int he second list
    for j in range(len(b_expense)):

        # Add the two numbers together
        num1 = a_expense[i]
        num2 = b_expense[j]
        total = num1 + num2

        # If the sum between the two numbers equals the sum_expense goal
        if sum(total) == sum_expense:
            print("The two numbers that equals ",
                  sum(total), " are ", num1, num2)

            # List comprehension to multiply the two values and zip the two lists together.
            mul_expense = [num2 * num1 for num2,
                           num1 in zip(a_expense[i], b_expense[j])]

            # Print the multiplied result.
            print("The two numbers multiplied equals: ", mul_expense)

        for k in range(len(c_expense)):
            num3 = c_expense[k]
            total2 = num1 + num2 + num3

            # If the sum between the thee numbers equals the sum_expense goal
            if sum(total2) == sum_expense:
                print("The three numbers added together are: ",
                      sum(total2), " are ", num1, num2, num3)

                mul_expense2 = [num2 * num1 * num3 for num2,
                                num1, num3 in zip(a_expense[i], b_expense[j], c_expense[k])]
                print("The three numbers multiplied together equals: ", mul_expense2)
