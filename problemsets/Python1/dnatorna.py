#!/usr/bin/env python3
import sys

#this will convert DNA to RNA

dnaseq = sys.argv[1]

rnaseq = dnaseq.replace('T','U')
rnaseq = rnaseq.replace('t','u')

print(rnaseq)
