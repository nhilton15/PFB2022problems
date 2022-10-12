#!/usr/bin/env python3
import sys

#this program extracts a substring from a sequence
#it also creates reverse complement, counts G content, and prints all

start = int(sys.argv[1])
stop = int(sys.argv[2])
sequence = sys.argv[3]

subsequence = sequence[start-1:stop]
countG = subsequence.count('G') + subsequence.count('g')

complement = subsequence.replace('A','B')
complement = complement.replace('a','b')
complement = complement.replace('T','A')
complement = complement.replace('t','a')
complement = complement.replace('B','T')
complement = complement.replace('b','t')
complement = complement.replace('G','B')
complement = complement.replace('g','b')
complement = complement.replace('C','G')
complement = complement.replace('c','g')
complement = complement.replace('B','C')
complement = complement.replace('b','c')

revcomp = complement[::-1]

print(f'Original Sequence  5\' {subsequence} 3\'')
print(f'Complement         3\' {complement} 5\'')
print(f'Reverse Complement 5\' {revcomp} 3\'')
print(f'Number of G\'s in subsequence: {countG}')
