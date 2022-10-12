#!/usr/bin/env python3
import sys

#this script counts the number of different bases, regardless of case

sequence = sys.argv[1]

sequence = sequence.upper()
countA = sequence.count('A')
countT = sequence.count('T')
countC = sequence.count('C')
countG = sequence.count('G')

print(f'The number of A\'s is {countA}, the number of T\'s is {countT}, the number of C\'s is {countC}, and the number of G\'s is {countG}.')
