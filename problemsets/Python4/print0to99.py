#!/usr/bin/env python3
import sys

startN = int(sys.argv[1])
endN = int(sys.argv[2])

for num in range(endN-startN+1):
    if (startN+num) %2 != 0:
        print(startN+num)

