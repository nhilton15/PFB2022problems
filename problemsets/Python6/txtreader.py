#!/usr/bin/env python3

with open('Python_06.txt','r') as txtread, open('Python_06_uc.txt','w') as txtwrite :
    for line in txtread:
        txtwrite.write(line.upper())
