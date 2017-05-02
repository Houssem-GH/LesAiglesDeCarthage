#!/usr/bin/env python
#-*- coding : utf8 -*-

#Author: GHARBI Houssem / Timothee O'Donnell
"""
Description: Programme qui:
- calcule RMSD pour toutes les solutions et rend un fichier trier par ordre croissant 
"""

import random, math, numpy, string, sys, glob, os
from pylab import *
import structureTools, ForceField3,usage


#les arguments: 

#repertoire des fichiers correspondant aux coordonnees du ligand pour chacune des 948 solutions de docking
try:
    indir = sys.argv[sys.argv.index("-in")+1]
except:    
    usage.usage2()
    print "ERROR: please, enter the name of the directory input"
    sys.exit()

    
#repertoire de sortie a creer des resultats du calcul de scoring
try:
    outdir = sys.argv[sys.argv.index("-out")+1]
except:    
    usage.usage2()
    print "ERROR: please, enter the name of the directory output"
    sys.exit()

#le fichier pdb du recepteur natif
try:
    Receptor = sys.argv[sys.argv.index("-pdbR")+1]
    #Rec_natif_DP.pdb
except:    
    usage.usage2()
    print "ERROR: please, enter the name of the receptor file"
    sys.exit()

#le fichier pdb du ligand natif
try:
    Ligand = sys.argv[sys.argv.index("-pdbL")+1]
    #Lig_natif_DP_aligned.pdb
except:
	usage.usage2()
	print "ERROR: please, enter the pdb name of the ligand PDF FILE"
	sys.exit()

#la chaine d'acide amine du recepteur
try:
    chaineRec = sys.argv[sys.argv.index("-chainRec")+1]
    #B
except:    
    usage.usage2()
    print "ERROR: please, enter the pdb name of the chain of the receptor"
    sys.exit()


#la chaine d'acide amine du Ligand
try:
    chaineLig = sys.argv[sys.argv.index("-chainLig")+1]
    #D
except:    
    usage.usage2()
    print "ERROR: please, enter the pdb name of the chain of the ligand"
    sys.exit()


#recuperer les noms des fichiers correspondant aux coordonnees du ligand dans une liste
filelist = glob.glob("%s/*DP.pdb"%(indir)) 

#creer le repertoire de sortie
os.system("mkdir -p %s"%(outdir)) 

#creer le repertoire fichier pdb des complexes theoriques
os.system("mkdir -p %s/Rec_Lig_PDB"%(outdir)) 

#creeation du fichier Complexe.pdb
os.system("cat %s %s > %s/Complexe.pdb"%(Receptor,Ligand,outdir))
Complex="%s/Complexe.pdb"%(outdir)


#boucle de calcul de score de chaque fichier correspondant aux coordonnees du ligand par rapport au recepteur 
#qui lui est fixe (Ex:fichier PDB: Rec_natif_DP)
dPDB_Cplx_Natif = structureTools.parsePDBMultiChains(Complex)
dPDB_Lig_Natif={}
dPDB_Lig_Natif["chains"] = []
dPDB_Lig_Natif["chains"].append(chaineLig)
dPDB_Lig_Natif[chaineLig] = dPDB_Cplx_Natif[chaineLig]

for pdb in filelist :
	num = pdb.split("/")[-1].split("_")[-2]
	curpdb = "rec_nat_lig_%s.pdb"%(num)
	os.system("cat %s %s > %s/Rec_Lig_PDB/%s"%(Receptor, pdb,outdir, curpdb))
	dPDB_Cplx_BestScore = structureTools.parsePDBMultiChains("%s/Rec_Lig_PDB/%s"%(outdir, curpdb))
	dPDB_Lig_BestScore={}
	dPDB_Lig_BestScore["chains"] = []
	dPDB_Lig_BestScore["chains"].append(chaineLig)

	dPDB_Lig_BestScore[chaineLig] = dPDB_Cplx_BestScore[chaineLig]
	dPDB_Interface_Natif = structureTools.InterfacePDB(dPDB_Cplx_Natif , 5.0 , "atom", chaineRec , chaineLig)

	RMSD_full_Cplx_CA = structureTools.RMSD(dPDB_Cplx_BestScore , dPDB_Cplx_Natif,"CA")
	RMSD_full_Cplx_AllAtoms = structureTools.RMSD(dPDB_Cplx_BestScore , dPDB_Cplx_Natif)

	RMSD_Lig_CA = structureTools.RMSD(dPDB_Lig_Natif , dPDB_Lig_BestScore,"CA")
	RMSD_Lig_AllAtoms = structureTools.RMSD(dPDB_Lig_Natif , dPDB_Lig_BestScore)

	RMSD_Interface_Natif_CA = structureTools.RMSD(dPDB_Interface_Natif, dPDB_Cplx_BestScore,"CA")
	RMSD_Interface_Natif_AllAtoms = structureTools.RMSD(dPDB_Interface_Natif, dPDB_Cplx_BestScore)


	#Ecrire les resultats dans un fichier out
	f= open("%s/RMSD.out"%(outdir),"a")
	f.write("%s    RMSD Complex entier (CA) : %f\n"%(curpdb,RMSD_full_Cplx_CA))
	f.close()
    
 
nonTrier = "%s/RMSD.out"%(outdir) #recuperer les donnees de Scoring dans un nouveau fichier nonTrier


#lecture du fichier nonTrier
f = open(nonTrier, "r")
lines = f.readlines()
f.close()



#Stocker les resultats dans un dictionnaire
dicoNT= {}
for line in lines:
	cle,valeur= line.split(" : ") 
	valeur = float(valeur)
	dicoNT[cle] = valeur
	
#Trier par Score les resultats de score dans une liste
ListT=sorted(dicoNT.items(), key=lambda t: t[1])

#Afficher les resultats de scoring par ordre croissant de score dans le fichier RMSD_Full.out
f_out = open("%s/RMSD_Full.out"%(outdir),"w")

for res in ListT:	
	f_out.write("%s : %f\n"%(res[0],res[1]))
	
f_out.close()

 #supprimer le fichier non trie
os.system("rm -f %s/RMSD.out"%(outdir))


