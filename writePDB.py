#!/usr/bin/env python


def writePDB(dPDB, filout = "out.pdb", bfactor = False) :
    """according to the coordinates in dPDB, writes the corresponding PDB file."""

    fout = open(filout, "w")
    #print dPDB["reslist"][1], dPDB[dPDB["reslist"][1]]["C"]["id"]

    for chain in dPDB["chains"]:
        for res in dPDB[chain]["reslist"] :
            for atom in dPDB[chain][res]["atomlist"] :
                if bfactor :
                    #print "bafctor ", dPDB[chain][res]["bfactor"]
                    fout.write("ATOM  %5s  %-4s%3s %s%4s    %8.3f%8.3f%8.3f  1.00%7.3f X X\n"%(dPDB[chain][res][atom]["id"], atom, dPDB[chain][res]["resname"],chain, res,dPDB[chain][res][atom]["x"], dPDB[chain][res][atom]["y"],dPDB[chain][res][atom]["z"],dPDB[chain][res]["bfactor"] ))
                else:
                   fout.write("ATOM  %5s  %-4s%3s %s%4s    %8.3f%8.3f%8.3f  1.00  1.00 X X\n"%(dPDB[chain][res][atom]["id"], atom, dPDB[chain][res]["resname"],chain, res,dPDB[chain][res][atom]["x"], dPDB[chain][res][atom]["y"],dPDB[chain][res][atom]["z"] ))
                    
    fout.close()
