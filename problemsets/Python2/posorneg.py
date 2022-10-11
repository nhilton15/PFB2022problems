#!/usr/bin/env python3
import sys
import math

#this script tests if a number is positive or negative

input = sys.argv[1]
number = float(input)

if 0 in math.modf(number):
    decimal = True
else:
    decimal = False

number = int(number)

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
