#!/usr/bin/env python3
import re

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

print(enzdict)
