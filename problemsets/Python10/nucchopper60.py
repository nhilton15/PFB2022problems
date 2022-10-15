#!/usr/bin/env python3

def stringcut60(dna, length):
    cutdna = ''
    newcut = 0
    dna = dna.replace('\n','')
    for nuc in range(len(dna)):
        if (nuc)%int(length) == 0 and nuc != 0:
            oldcut = newcut
            newcut = nuc
            cutdna = cutdna +'\n'+dna[oldcut:newcut]
    cutdna = cutdna +'\n'+dna[newcut:]
    cutdna = cutdna[1:]
    return cutdna

dnaseq = input('Enter a fasta file name: ')
dnalen = input('Enter a length: ')

with open(dnaseq,'r') as fastaread:
    chunk = ''
    for line in fastaread:
        if line.find('>') != -1:
            print(stringcut60(chunk, dnalen), end='')
            chunk = ''
            print(line, end='')
        else:
            chunk = chunk + line
    print(stringcut60(chunk, dnalen))

