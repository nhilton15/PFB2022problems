#!/usr/bin/env python3

dnaseq = input('Input a sequence of dna: ')

def stringcut60(dna):
    cutdna = ''
    newcut = 0
    for nuc in range(len(dna)):
        if (nuc)%60 == 0 and nuc != 0:
            oldcut = newcut
            newcut = nuc
            cutdna = cutdna +'\n'+dna[oldcut:newcut]
    cutdna = cutdna +'\n'+dna[newcut:]
    return cutdna

print(stringcut60(dnaseq))

