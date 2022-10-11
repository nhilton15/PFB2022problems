#!/usr/bin/env python3
import sys

#this script will find the number of rabbit pairs present after n months if mature rabbits produce k pairs of baby rabbits (gives number of PAIRS) (we start with babies)

#getting months and pair production
months = sys.argv[1]
production = sys.argv[2]
months = int(months)
production = int(production)

#initial state
babies = 1
adults = 0
babies = int(babies)
adults = int(adults)

#math to calculate production
for i in range(0,months):
    newadults = babies
    babies = production * adults
    adults = adults + newadults
    i += 1

#give answer
print('Number of babies:',end=' ')
print(babies)
print('Number of adults:',end=' ')
print(adults)
