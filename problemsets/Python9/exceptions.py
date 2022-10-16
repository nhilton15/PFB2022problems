#!/usr/bin/env python3

import re

fastafile = input('Enter a fasta file name: ')

try:
    print(f'File name: {fastafile}')
    if not fastafile.endswith('.fasta'):
        raise ValueError('Not a fasta file')
    with open(fastafile, 'r') as fastaread:
        for line in fastafile:
            if not re.search('>', line) and re.search(r'^[ATCGN]', line):
                raise ValueError('Sequence contains non ATCGN')

except IndexError:
    print('Please provide a file name')

except IOError as ex:
    print('Can\'t find file:',fastafile,':',ex.strerror)


