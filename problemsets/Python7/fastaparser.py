#!/usr/bin/env python3
import re

fastadict = {}
seqdict = {}

with open('Python_07.fasta','r') as fastaread:
    for line in fastaread:
        if re.search(r'(^>\S+)( (.*))?',line):
            search = re.search(r'(^>\S+) ?(.*)',line)
            iden = search.group(1)
            fastadict[iden] = search.group(2)
            combline = ''
        else:
            combline = combline + line.replace('\n','')
            seqdict[iden] = combline

print(fastadict)
print(seqdict)
