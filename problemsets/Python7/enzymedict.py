#!/usr/bin/env python3
import re
import sys

skipper = 1
enzdict = {}

with open('bionet.txt') as bioread:
    for line in bioread:
        linest = line.strip()
        if skipper > 10 and len(linest) > 2:
            finder = re.match(r'(.{3,}[\)\w])\s{3,}(\S{4,})',linest)
            if finder:
                name = finder.group(1)
                seq = finder.group(2)
                enzdict[name] = seq
        else:
            skipper +=1

#print(enzdict)

enzname = sys.argv[1]
seqtocut = sys.argv[2]

basedict = {'R':'[AG]','Y':'[CT]','S':'[GC]','W':'[AT]','K':'[GT]','M':'[AC]','B':'[CGT]','D':'[AGT]','H':'[ACT]','V':'[ACG]','N':'[ACTG]'}

if enzname in enzdict:
    cutsearch = enzdict[enzname]
    if re.search(r'\^',cutsearch):
        cutsite = cutsearch.find('^')
    for base in range(len(cutsearch)):
        if cutsearch[base] in basedict:
           cutsearch = cutsearch.replace(cutsearch[base],basedict[cutsearch[base]])
    seqclean = cutsearch.replace('^','')
    if re.search(seqclean,seqtocut):
        for found in re.finditer(seqclean,seqtocut):
            seqtocut = seqtocut[:found.start(0)+cutsite]+'^'+seqtocut[found.start(0)+cutsite:]
        print(seqtocut)
        seqsplit = seqtocut.split('^')
        print(len(seqsplit), 'fragments')
        print(seqsplit)
        seqsplit = sorted(seqsplit, key=len, reverse = True)
        print(seqsplit)
    else:
        print('No cut sites')
