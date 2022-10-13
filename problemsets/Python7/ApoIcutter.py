#!/usr/bin/env python3
import re

with open('Python_07_ApoI.fasta','r') as openseq:
    sequence = openseq.read()
sequence = re.sub(r'([CATG])\s',r'\1',sequence)
for site in re.finditer(r'([GA])ATT[CT]',sequence):
#    print(f'Cuts after {site.start(1)-5}')
    sequence = re.sub(r'([GA])ATT([CT])',r'\1^ATT\2',sequence)

sequence = sequence[6:]
fragments = sequence.split('^')

fragments = fragments.sort(key=len)

#print(sequence)
print(fragments)
