#!/usr/bin/env python3
import sys

height = float(input("Enter your height in the format: ft.in "))
inches = height * 12

dvd = 7.48
creditCard = 3.375
iPadAir = 9.4

select = int(
    input("Select unit of measurement: 1 = DVD case, 2 = Credit Cards, 3 = iPad Air Gen-One "))


def divide(inches, select):
    formatted_float = "{:.2f}".format(inches / select)
    return formatted_float


if select == 1:
    print("You are", divide(inches, dvd), "DVD cases tall.")

if select == 2:
    print("You are", divide(inches, creditCard),
          "Credit cards tall.")

if select == 3:
    print("You are", divide(inches, iPadAir),
          "iPad Air gen-one's tall.")

else:
    print("Not a valid input.")
