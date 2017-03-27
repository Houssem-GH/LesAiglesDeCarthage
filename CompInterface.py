#!/usr/bin/env python

import random, math, numpy, string, sys
from pylab import *
import structureTools



########################################################################################################
#
#                   FUNCTIONS
#
########################################################################################################


def usage():
    print """

     obligatory:
     ===========

     -pdb     -> pdb file

    blablabla

  """



#####################################################################################
#
#                       MAIN
#
#####################################################################################

def compInter(dPDB, threshold, mode) :

    nbresInter = 0
    structureTools.initBfactor(dPDB)
    print dPDB["chains"]
    
    for chainidi in range(len(dPDB["chains"])-1) :
        chaini = dPDB["chains"][chainidi]
        chainidj = chainidi + 1
        chainj = dPDB["chains"][chainidj]
        print "dealing chains %s and %s"%(chaini, chainj)
        for chainidj in range(0, len(dPDB["chains"])):
            for resi in dPDB[chaini]["reslist"] :
                for resj in dPDB[chainj]["reslist"] :
                    dist = structureTools.computeDist_dico(dPDB[chaini][resi], dPDB[chainj][resj], mode = mode)
                    if dist <= threshold :# means, the two residues belong to the interface
                        if dPDB[chaini][resi]["bfactor"] == 0 :
                            nbresInter +=1
                        if dPDB[chainj][resj]["bfactor"] == 0 :
                            nbresInter +=1
                        dPDB[chaini][resi]["bfactor"] = 1
                        dPDB[chainj][resj]["bfactor"] = 1
                        #print "bfactor ", dPDB[chaini][resi]["bfactor"]
                        #print "%s %s VS %s %s = %s"%(chaini, resi, chainj, resj, dist)


    return nbresInter                       

# Get Arguments
#===============

try:
    infile = sys.argv[sys.argv.index("-pdb")+1]
    print "pdb to treat:", infile
except:    
    usage()
    print "ERROR: please, enter the name of the pdb input"
    sys.exit()

try:
    threshold = float(sys.argv[sys.argv.index("-th")+1])
except:    
    threshold = 5.0

    
try:
    mode = sys.argv[sys.argv.index("-mode")+1]
    print "the mode of calculation for the distance is:", mode
except:    
    mode = "atom"

# Computes distances between the two proteins
#============================================


# parses the pdb file
dPDB = structureTools.parsePDBMultiChains(infile)
print "the distance threshold is:", threshold

print "nb res ", len(dPDB[dPDB["chains"][0]]["reslist"])
print "nb of chains: %s"%(len(dPDB["chains"]))
#print dPDB[dPDB["chains"][0]]["reslist"]
#print dPDB[dPDB["chains"][0]][dPDB[dPDB["chains"][0]]["reslist"][0]]


# computes interface

nbresInter = compInter(dPDB, threshold, mode)

print "nb of residues in the interface:",nbresInter

structureTools.writePDB(dPDB, filout = "interface.pdb", bfactor = True) 
