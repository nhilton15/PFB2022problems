#!/usr/bin/env python3
import sys

#this program will take input in FASTA format of multiple sequences, determine the GC content of each, output the name of the sequence with the highest content, and give the content percent

#input of sequences
sequencelist = sys.argv[1]
seqnum = sequencelist.count('Rosalind_')
altseq = sequencelist

#create a dictionary from list of sequences
seqdict = {}

for i in range(0,seqnum):
    positionS = sequencelist.find('Rosalind_')
    positionE = -1
    for j in range(0, 2)
        positionE = altseq.find('Rosalind_', positionE + 1)
    seqdict[sequencelist[positionS:positionS+12].append(positionS+13:positionE-2)
    altseq.replace('Rosalind_','Done',1)

#evaluate GC content in dictionary


#determine highest content


#display highest sequence name and content
