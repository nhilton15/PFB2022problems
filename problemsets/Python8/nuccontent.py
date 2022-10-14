#!/usr/bin/env python3
import re

seqdict = {}
filename = input('Enter file name: ')

with open(filename,'r') as openfile:
    for line in openfile:
        line = line.rstrip()
        if re.search(r'>',line):
            code = line
            seqdict[code] = ''
        else:
            seqdict[code] = seqdict[code]+line

#nucdict = {}

#for gene in seqdict:
#    if gene not in nucdict:
#        nucdict[gene] = {}
#    for nuc in seqdict[gene]:
#        if nuc not in nucdict[gene]:
#            nucdict[gene][nuc] = 1
#        else:
#            nucdict[gene][nuc] +=1

#for gene in nucdict:
#    print(gene+'\t'+str(nucdict[gene]['A'])+'\t'+str(nucdict[gene]['T'])+'\t'+str(nucdict[gene]['G'])+'\t'+str(nucdict[gene]['C']))

codondict = {}

for gene in seqdict:
    codondict[gene] = []
    for frame in range(6):
        codondict[gene].append([])
        seqret = seqdict[gene]
        if frame >= 3:
            seqret = seqret[::-1]
            seqret = seqret.replace('A','B')
            seqret = seqret.replace('T','A')
            seqret = seqret.replace('B','T')
            seqret = seqret.replace('G','B')
            seqret = seqret.replace('C','G')
            seqret = seqret.replace('B','C')
        spacer = 1 + frame
        codon = ''
        for nt in seqret:
            codon = codon + nt
            if spacer%3 == 0:
                codondict[gene][frame].append(codon)
                codon = ''
            spacer +=1
        codondict[gene][frame].append(codon)

#with open('Python_08.codons-6frames.nt','w') as codonfile:
#    for gene in codondict:
#        counter = 1
#        for frames in codondict[gene]:
#            codonfile.write(f'{gene} Frame{counter}\n')
#            counter +=1
#            for codonlist in frames:
#                codonfile.write(codonlist)
#            codonfile.write('\n')

translation_table = { 'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'AAT':'N', 'AAC':'N', 'GAT':'D', 'GAC':'D', 'TGT':'C', 'TGC':'C', 'CAA':'Q', 'CAG':'Q', 'GAA':'E', 'GAG':'E', 'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'CAT':'H', 'CAC':'H', 'ATT':'I', 'ATC':'I', 'ATA':'I', 'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L', 'AAA':'K', 'AAG':'K', 'ATG':'M', 'TTT':'F', 'TTC':'F', 'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S', 'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'TGG':'W', 'TAT':'Y', 'TAC':'Y', 'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V', 'TAA':'*', 'TGA':'*', 'TAG':'*' }

transldict = {}

for gene in codondict:
    transldict[gene] = []
    for frame in range(6):
        transldict[gene].append([])
        for codon in range(len(codondict[gene][frame])):
            if len(codondict[gene][frame][codon]) == 3:
                transldict[gene][frame].append(translation_table[codondict[gene][frame][codon]])

#with open('Python_08.translated.aa','w') as translatedfile:
#    for gene in transldict:
#        counter = 1
#        for frames in transldict[gene]:
#            translatedfile.write(f'{gene} Frame{counter}\n')
#            counter +=1
#            for aalist in frames:
#                translatedfile.write(aalist)
#            translatedfile.write('\n')

peptdict = {}

for gene in transldict:
    peptdict[gene] = []
    for frame in range(6):
        peptide = ''
        for residue in range(len(transldict[gene][frame])):
            peptide = peptide + transldict[gene][frame][residue]
        peptdict[gene].append(peptide)

longpepdict = {}

for gene in peptdict:
    longpepdict[gene] = []
    for frame in range(6):
        longpepdict[gene].append(' ')
        for orf in re.finditer(r'M\w*\*', peptdict[gene][frame]):
            if (orf.end(0)-orf.start(0)) > len(longpepdict[gene][frame]):
                longpepdict[gene][frame] = orf.group(0)

#with open('Python_08.translated-longest.aa','w') as longestwrite:
#    for gene in longpepdict:
#        counter = 1
#        for frames in longpepdict[gene]:
#            longestwrite.write(f'{gene} Frame{counter}\n')
#            counter +=1
#            longestwrite.write(frames+'\n')

creamofthecrop = {}

for gene in longpepdict:
    creamofthecrop[gene] = ''
    for frame in range(6):
        if len(longpepdict[gene][frame]) > len(creamofthecrop[gene]):
            creamofthecrop[gene] = longpepdict[gene][frame]

with open('Python_08.orf-longest.nt','w') as creamwrite:
    for gene in creamofthecrop:
        creamwrite.write(f'{gene}\n{creamofthecrop[gene]}\n')


