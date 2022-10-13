#!/usr/bin/env python3

cutter = input('The cut site is (include cut as "^"): ')
sequence = input('The sequence is: ')
tofind = cutter.replace('^','')
cutnum = sequence.count(tofind)

sequence = sequence.replace(tofind,cutter)
splitseq = sequence.split('^')

metalist = []
startS = 1
endS = 0
for split in splitseq:
    endS = startS + len(split) - 1
    metalist.append([len(split),split,startS,endS])
    startS = endS + 1

metalist.sort(reverse=True,key=[item[0] for item in metalist])
for sublist in metalist print(f'Fragment {sublist[1]} goes from position {sublist[2]} to {sublist[3]}, and is {sublist[0]}bp long.')

