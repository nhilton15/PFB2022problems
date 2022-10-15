#!/usr/bin/env python3

def gccalc(dnastr):
    cval = dnastr.count('C')
    gval = dnastr.count('G')
    gcper = (gval+cval)/len(dnastr)
    return gcper

def revcomp(dnastr):
    dnastr = dnastr[::-1]
    dnastr = dnastr.replace('A','B')
    dnastr = dnastr.replace('T','A')
    dnastr = dnastr.replace('B','T')
    dnastr = dnastr.replace('C','B')
    dnastr = dnastr.replace('G','C')
    dnastr = dnastr.replace('B','G')
    return dnastr


