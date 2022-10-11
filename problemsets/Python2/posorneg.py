#!/usr/bin/env python3
import sys
import math

#this script tests if a number is positive or negative

#grabbing input number and converting it to float
input = sys.argv[1]
number = float(input)

#sorting the numbers into different categories
if number > 0.0:
    print('positive')
    if number < 50.0:
        if number%2.0 == 0.0:
            print('it is an even number that is smaller than 50')
    if number > 50.0:
        if number%3.0 == 0.0:
            print('it is larger than 50 and divisible by 3')
elif number == 0.0:
    print('zero')
else:
    print('negative')

print(input)
