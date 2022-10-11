#!/usr/bin/env python3
import sys
import math

#this script tests if a number is positive or negative

#grabbing input number and converting it to float
input = sys.argv[1]
number = float(input)

#determining if the number has a decimal or not (decimal being false indicates that it's present)
if 0 in math.modf(number):
    decimal = True
else:
    decimal = False

#dealing with the fractions
if number >= 1 or number <= -1:
    number = int(number)
elif number == 0:
    number = int(number)
elif number > 0:
    number = 3
else:
    number = -3

#sorting the numbers into different categories
if number > 0:
    print('positive')
    if number < 50:
        if number%2 == 0 and decimal:
            print('it is an even number that is smaller than 50')
    if number > 50:
        if number%3 == 0 and decimal:
            print('it is larger than 50 and divisible by 3')
elif number == 0:
    print('zero')
else:
    print('negative')

print(input)
