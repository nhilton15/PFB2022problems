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

if enzname in enzdict:
    seqclean = enzdict[enzname].replace('^','')
    if re.search(seqclean,seqtocut):
        seqout = re.sub(seqclean,enzdict[enzname],seqtocut)
        print(seqout)
        seqsplit = seqout.split('^')
        print(len(seqsplit), 'fragments')
        print(seqsplit)
        seqsplit = sorted(seqsplit, key=len, reverse = True)
        print(seqsplit)
    else:
        print('No cut sites')
