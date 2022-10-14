#!/usr/bin/env python3
import re

seqdict = {}
filename = input('Enter file name: ')

with open(filename,'r') as openfile:
    for line in openfile:
        line = line.rstrip()
        if re.search(r'>',line):
            code = line
            seqdict[code] = ''
        else:
            seqdict[code] = seqdict[code]+line

#nucdict = {}

#for gene in seqdict:
#    if gene not in nucdict:
#        nucdict[gene] = {}
#    for nuc in seqdict[gene]:
#        if nuc not in nucdict[gene]:
#            nucdict[gene][nuc] = 1
#        else:
#            nucdict[gene][nuc] +=1

#for gene in nucdict:
#    print(gene+'\t'+str(nucdict[gene]['A'])+'\t'+str(nucdict[gene]['T'])+'\t'+str(nucdict[gene]['G'])+'\t'+str(nucdict[gene]['C']))

codondict = {}

for gene in seqdict:
    if gene not in codondict:
        codondict[gene] = {}
    #split string every three char

