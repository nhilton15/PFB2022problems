#!/usr/bin/env python3
import sys

#this script will convert T's to U's

sequence = sys.argv[1]

sequence = sequence.replace('T','U')
sequence = sequence.replace('t','u')
print(sequence)
