#!/usr/bin/env python3

class Dnaseq(object):
    def __init__(self, sequence, name, organism):
        self.sequence = sequence
        self.name = name
        self.organism = organism
    def getlen(self):
        return len(self.sequence)
    def nuccomp(self):
        nucdict = {}
        nucdict['A'] = self.sequence.count('A')
        nucdict['T'] = self.sequence.count('T')
        nucdict['C'] = self.sequence.count('C')
        nucdict['G'] = self.sequence.count('G')
        return nucdict
    def gccontent(self):
        ccount = self.sequence.count('C')
        gcount = self.sequence.count('G')
        gccont = (ccount+gcount)/len(self.sequence)
        return gccont
    def makefasta(self):
        return '>'+self.name+'\n'+self.sequence
    def seqcompare(self, seq2):
        if self.sequence == seq2.sequence and self.name == seq2.name and self.organism == seq2.organism:
            return True
        else:
            return False


samplegene = Dnaseq('AATTCCGG','Gene 1','Homo sapiens')
samplegene2 = Dnaseq('AATTCCGG','Gene 1','Homo sapiens')

#print(samplegene.sequence,samplegene.name,samplegene.organism)
#print(samplegene.getlen())
#print(samplegene.nuccomp())
#print(samplegene.gccontent())
#print(samplegene.makefasta())

print(samplegene.seqcompare(samplegene2))
