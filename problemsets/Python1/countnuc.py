#!/usr/bin/env python3
import sys

#counts different numbers of nucleotides in a sequence

#take the sequence
sequence = sys.argv[1]

#initialize A C T Gs
numA = 0
numC = 0
numT = 0
numG = 0

#now, count
numA = sequence.count('A')
numA = numA + sequence.count('a')
numC = sequence.count('C')
numC = numC + sequence.count('c')
numT = sequence.count('T')
numT = numT + sequence.count('t')
numG = sequence.count('G')
numG = numG + sequence.count('g')

#print the numbers
print(numA,numC,numG,numT)
