#!/usr/bin/env python3

favdict = {}

while True:
    favq = input('Name a type of thing: ')
    fava = input('What is your favorite?: ')
    if favq == 'done' or fava == 'done':
        break
    else:
        favdict[favq] = fava

for item in favdict:
    print(f'{item}\t{favdict[item]}')
