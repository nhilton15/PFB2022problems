#!/usr/bin/env python3
import sys

#this script takes two strings of equal length and computes the Hamming distance, which is the number of corresponding symbols that differ

#taking in the two strings
sequence1 = sys.argv[1]
sequence2 = sys.argv[2]

#adding up differences
hamming = 0
for i in range(0,len(sequence1)):
    if sequence1[i] != sequence2[i]:
        hamming += 1

print(hamming)
