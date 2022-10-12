#!/usr/bin/env python3
import sys

#this script calculates the AT content of a DNA string
#and now it calculates GC content!

sequence = sys.argv[1]

seqlen = len(sequence)
totalAT = sequence.count('A') + sequence.count('T')
percentAT = totalAT / seqlen * 100
totalGC = sequence.count('G') + sequence.count('C')
percentGC = totalGC / seqlen * 100

print(f'The percent AT content is {percentAT:.2f}% and the percent GC content is {percentGC:.2f}%.')
