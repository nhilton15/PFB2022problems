#!/usr/bin/env python3
import sys

#this script calculates the factorial of a number

number = sys.argv[1]
number = int(number)
factorial = 1

while number > 0:
    factorial = number * factorial
    number-=1

print(factorial)
