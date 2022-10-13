#!/usr/bin/env python3

genedict = {}

with open('Python_06.seq.txt','r') as seqread:
    for line in seqread:
        line = line.rstrip()
        geneid,sequence = line.split()
        genedict[geneid] = sequence

for seq in genedict:
    genedict[seq] = genedict[seq][::-1]
    genedict[seq] = genedict[seq].replace('A','B')
    genedict[seq] = genedict[seq].replace('T','A')
    genedict[seq] = genedict[seq].replace('B','T')
    genedict[seq] = genedict[seq].replace('C','B')
    genedict[seq] = genedict[seq].replace('G','C')
    genedict[seq] = genedict[seq].replace('B','G')

print('This is the reverse complement')
for gene in genedict:
    print(f'>{gene}\n{genedict[gene]}')
