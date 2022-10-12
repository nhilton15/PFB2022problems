#!/usr/bin/env python3

dnalist = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

#for seq in dnalist:
#    print(len(seq),seq,sep='\t')

dnanested = [(dnalist.index(seq)+1,len(seq),seq) for seq in dnalist]
print(dnanested)
