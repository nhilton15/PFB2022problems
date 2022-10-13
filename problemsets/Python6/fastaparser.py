#!/usr/bin/env python3

culen = 0
linecount = 0

with open('Python_06.fastq','r') as fastaread:
    for line in fastaread:
        line = line.rstrip()
        culen += len(line)
        linecount += 1

print(linecount,culen,culen/linecount)
