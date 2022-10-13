#!/usr/bin/env python3
import sys

#this script will take three numbers, representing homozygous dominant, heterozygous, and homozygous recessive organisms, and give a number representing the probablility that two random organisms will produce an offspring posessing an dominant allele

homd = int(sys.argv[1])
het = int(sys.argv[2])
homr = int(sys.argv[3])

popu = homd + het + homr

#homd and het have dominant alleles, all pairings with homd will produce offspring with dominant alleles, while het pairings will produce dom alleles part of the time

homdp = 1 - (((het+homr)/popu)*((het+homr-1)/(popu-1))) #probability that at least one parent is homd

#het and het pairings
hethet = (het/popu)*((het-1)/(popu-1))
hethet *= 0.75 #75% of these pairings will result in offspring with dominant allele

#het and homr pairings
hethomr = ((het/popu)*((homr-1)/(popu-1)))+((homr/popu)*((het-1)/(popu-1)))
hethomr *= 0.5 #50% of these pairings will result in offspring with dominant allele

print(homdp,hethet,hethomr)
