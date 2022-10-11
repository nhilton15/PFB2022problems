#!/usr/bin/env python3
import sys

#this program takes a sequence of DNA and prints the reverse complement

sequence = sys.argv[1]

#this creates the complement strand in 3' to 5' order
complement = sequence.replace('A','B')
complement = complement.replace('a','b')
complement = complement.replace('T','A')
complement = complement.replace('t','a')
complement = complement.replace('B','T')
complement = complement.replace('b','t')

complement = complement.replace('C','B')
complement = complement.replace('c','b')
complement = complement.replace('G','C')
complement = complement.replace('g','c')
complement = complement.replace('B','G')
complement = complement.replace('b','g')

#now, the reverse
def reverse(s):
    str = ''
    for i in s:
        str = i + str
    return str

print(reverse(complement))
