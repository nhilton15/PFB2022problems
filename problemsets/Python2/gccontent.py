#!/usr/bin/env python3
import sys

#this program will take input in FASTA format of multiple sequences, determine the GC content of each, output the name of the sequence with the highest content, and give the content percent

#input sequences into string
filepath = sys.argv[1]
sequencefile = open(filepath,'r') #opens file in read mode
sequencelist = sequencefile.read()
sequencelist = sequencelist.replace('\n','')
sequencefile.close()
seqnum = sequencelist.count('>')
altseq = sequencelist

#create a dictionary from list of sequences
seqdict = {}
for i in range(0,seqnum):
    positionS = altseq.find('>')
    altseq = altseq.replace('>','Z',1)
    positionE = altseq.find('>')
    if i == seqnum-1:
        positionE = len(altseq)+1
    seqdict[sequencelist[positionS+1:positionS+14]] = sequencelist[positionS+14:positionE] #addingelements to keys in dictionary, since seqdict is an empty dictionary, keys will be created

print(seqdict)

#evaluate GC content in dictionary
gcdict = {}
for i in range(0,seqnum):
    gcdict[seqdict[i]] = 

#determine highest content


#display highest sequence name and content
