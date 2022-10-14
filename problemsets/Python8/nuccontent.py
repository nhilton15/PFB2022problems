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
    codondict[gene] = []
    for frame in range(6):
        codondict[gene].append([])
        seqret = seqdict[gene]
        if frame >= 3:
            seqret = seqret[::-1]
            seqret = seqret.replace('A','B')
            seqret = seqret.replace('T','A')
            seqret = seqret.replace('B','T')
            seqret = seqret.replace('G','B')
            seqret = seqret.replace('C','G')
            seqret = seqret.replace('B','C')
        spacer = 1 + frame
        codon = ''
        for nt in seqret:
            codon = codon + nt
            if spacer%3 == 0:
                codondict[gene][frame].append(codon)
                codon = ''
            spacer +=1
        codondict[gene][frame].append(codon)

with open('Python_08.codons-6frames.nt','w') as codonfile:
    for gene in codondict:
        counter = 1
        for frames in codondict[gene]:
            codonfile.write(f'{gene} Frame{counter}\n')
            counter +=1
            for codonlist in frames:
                codonfile.write(codonlist+' ')
            codonfile.write('\n')

