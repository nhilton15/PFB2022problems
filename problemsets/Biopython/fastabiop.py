#!/usr/bin/env python3

from Bio import SeqIO

fastafile = input('Enter fasta file name: ')

seqnum = 0
nuctot = 0
shortest = 999999999999999
longest = 0
gccount = 0
lowestgc = 1
highestgc = 0

for openfasta in SeqIO.parse(fastafile,'fasta'):
    seqnum +=1
    nuctot = nuctot + len(openfasta.seq)
    if shortest > len(openfasta.seq):
        shortest = len(openfasta.seq)
    if longest < len(openfasta.seq):
        longest = len(openfasta.seq)
    gccount = gccount + openfasta.seq.count('G') + openfasta.seq.count('C')
    currgc = (openfasta.seq.count('G')+openfasta.seq.count('C'))/len(openfasta.seq)
    if lowestgc > currgc:
        lowestgc = currgc
    if highestgc < currgc:
        highestgc = currgc

avglen = nuctot/seqnum
gccont = gccount/nuctot

print(f'sequence count: {seqnum}')
print(f'total number of nucleotides: {nuctot}')
print(f'avg len: {avglen}')
print(f'shortest len: {shortest}')
print(f'longest len: {longest}')
print(f'avg GC content: {gccont}')
print(f'lowest GC content: {lowestgc}')
print(f'highest GC content: {highestgc}')

