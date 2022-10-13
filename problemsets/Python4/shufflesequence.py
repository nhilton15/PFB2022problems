#!/usr/bin/env python3
import sys
import random

#this will create a shuffled sequence (Fisher-Yates shuffle)

seq = input('Enter sequence: ')
seqlen = len(seq)
seq = [loci for loci in seq] #does this need to be in a list? could just do it in a string
shufseq = seq.copy()

for swap in range(seqlen):
    posA = random.randrange(seqlen)
    posB = random.randrange(seqlen)
    hold = shufseq[posA]
    shufseq[posA] = shufseq[posB]
    shufseq[posB] = hold

print(seq)
print(shufseq)
