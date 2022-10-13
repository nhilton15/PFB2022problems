#!/usr/bin/env python3
import re

with open('Python_07_nobody.txt','r') as nobodyread, open('Billy.txt','w') as billywrite:
#    for line in nobodyread:
#        for find in re.finditer(r'Nobody', line):
#            print(find.start()+1,find.end())
    nobody = nobodyread.read()
    billy = re.sub(r'Nobody', r'Billy', nobody)
    billywrite.write(billy)
