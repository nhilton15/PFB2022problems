#!/usr/bin/env python3
import sys

#this program will take input in FASTA format of multiple sequences, determine the GC content of each, output the name of the sequence with the highest content, and give the content percent

#input of sequences
sequencelist = sys.argv[1]

#create a dictionary from list of sequences
seqdict = {}
seqnum = sequencelist.count('Rosalind_')
for i in (0,seqnum):
    
