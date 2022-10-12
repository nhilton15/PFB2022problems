#!/usr/bin/env python3
import sys

#this script will find and print the starting nucleotide position within a sequence you give
#as well as the stop site
#give name, site looking for, sequence to search

sitename = sys.argv[1]
site = sys.argv[2]
site = site.upper()
sequence = sys.argv[3]
sequence = sequence.upper()

locusS = sequence.find(site)
locusE = len(site)

print(f'{sitename} startPos:{locusS+1} endPos:{locusE+locusS}')
#print(f'The starting nucleotide position of your site is {locusS+1}.')
#print(f'The ending nucleotide position of your site is {locusE+locusS}.')
