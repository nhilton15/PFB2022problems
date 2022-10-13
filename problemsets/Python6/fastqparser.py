#!/usr/bin/env python3

fastqdict = {}
linecount = 1

with open('Python_06.fastq','r') as fastqread:
    for line in fastqread:
        line = line.rstrip()
        if (linecount+3)%4 == 0:
            tempkey = line
        if (linecount+2)%4 == 0:
            fastqdict[tempkey] = line
        linecount += 1

print(fastqdict)
