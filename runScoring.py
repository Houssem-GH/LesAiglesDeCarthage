#!/usr/bin/env python
#-*- coding : utf8 -*-

#Author: GHARBI Houssem / Timothee O'Donnell
"""
Description: Programme principale qui:
-Calcule les scores des solutions fournis en argument
-Calcule les RMSD
"""

import random, math, numpy, string, sys, glob, os
from pylab import *
import structureTools, ForceField3,usage


#les arguments: 

#repertoire des fichiers correspondant aux coordonnees du ligand pour chacune des 948 solutions de docking
try:
    indir = sys.argv[sys.argv.index("-in")+1]
except:    
    usage.usage1()
    print "ERROR: please, enter the name of the directory input"
    sys.exit()

    
#repertoire de sortie a creer des resultats du calcul de scoring
try:
    outdir = sys.argv[sys.argv.index("-out")+1]
except:    
    usage.usage1()
    print "ERROR: please, enter the name of the directory output"
    sys.exit()


#le programme de scoring a executer 
try:
    Program_Scoring = sys.argv[sys.argv.index("-prog")+1]
    if  Program_Scoring not in ("NewScoringCornell.py","NewScoringCornellAndDesolvation.py","OldScoringCornellAndDesolvation.py"):
		sys.exit() 
except:    
    usage.usage1()
    print "ERROR: please, enter the name of the program to execute among the available programs"
    sys.exit()


#le fichier pdb du recepteur natif
try:
    Receptor = sys.argv[sys.argv.index("-pdbR")+1]
    #Rec_natif_DP.pdb
except:    
    usage.usage1()
    print "ERROR: please, enter the name of the receptor file"
    sys.exit()


#le fichier pdb du ligand natif
try:
    Ligand = sys.argv[sys.argv.index("-pdbL")+1]
    #Lig_natif_DP_aligned.pdb
except:
	Ligand = ""


#la chaine d'acide amine du recepteur
try:
    chaineRec = sys.argv[sys.argv.index("-chainRec")+1]
    #B
except:    
    usage.usage1()
    print "ERROR: please, enter the pdb name of the chain of the receptor"
    sys.exit()


#la chaine d'acide amine du Ligand
try:
    chaineLig = sys.argv[sys.argv.index("-chainLig")+1]
    #D
except:    
    usage.usage1()
    print "ERROR: please, enter the pdb name of the chain of the ligand"
    sys.exit()







#recuperer les noms des fichiers correspondant aux coordonnees du ligand dans une liste
filelist = glob.glob("%s/*DP.pdb"%(indir)) 


#creer le repertoire de sortie
os.system("mkdir -p %s"%(outdir)) 

#creer le repertoire fichier pdb des complexes theoriques
os.system("mkdir -p %s/Rec_Lig_PDB"%(outdir)) 


#boucle de calcul de score de chaque fichier correspondant aux coordonnees du ligand par rapport au recepteur
#qui lui est fixe (Ex:fichier PDB: Rec_natif_DP)
for pdb in filelist : 
    num = pdb.split("/")[-1].split("_")[-2]
    curpdb = "rec_nat_lig_%s.pdb"%(num)
    os.system("cat %s %s > %s/Rec_Lig_PDB/%s"%(Receptor, pdb,outdir, curpdb))
    os.system("python %s -pdb %s/Rec_Lig_PDB/%s -chain1 %s -chain2 %s"%(Program_Scoring, outdir,curpdb,chaineRec,chaineLig))
 
#recuperer les donnees de Scoring dans un nouveau fichier nonTrier
if Program_Scoring == "NewScoringCornell.py":
	nonTrier = "NewScoringCornell.out" 
elif Program_Scoring == "NewScoringCornellAndDesolvation.py":
	nonTrier = "NewScoringCornellAndDesolvation.out"
else:
	nonTrier = "OldScoringCornellAndDesolvation.out"
#lecture du fichier nonTrier
f = open(nonTrier, "r")
lines = f.readlines()
f.close()





#Stocker les resultats dans un dictionnaire
dicoNT= {}
for line in lines:
	line = line.split("/")[2]
	cle,valeur= line.split(" : ") 
	valeur = float(valeur)
	dicoNT[cle] = valeur
	

#Trier par Score les resultats de score dans une liste
ListT=sorted(dicoNT.items(), key=lambda t: t[1])


#Afficher les resultats de scoring par ordre croissant de score dans le fichier Scoring_Cornell
f_out = open("%s/Scoring"%(outdir),"w")

for res in ListT:	
	f_out.write("%s : %f\n"%(res[0],res[1]))
	
f_out.close()


#Creer le fichier du complex Recepteur-ligand selon la methode de calcul 
if Program_Scoring == "NewScoringCornell.py":
	os.system("cat %s/Rec_Lig_PDB/%s > %s/complexe_predit_score1.pdb "%(outdir,ListT[0][0],outdir))
	pdbinfile = "%s/complexe_predit_score1.pdb"%(outdir)
	
elif Program_Scoring == "NewScoringCornellAndDesolvation.py":
	os.system("cat %s/Rec_Lig_PDB/%s > %s/complexe_predit_score2.pdb "%(outdir,ListT[0][0],outdir))
	pdbinfile = "%s/complexe_predit_score2.pdb"%(outdir)
	
elif Program_Scoring == "OldScoringCornellAndDesolvation.py":
	os.system("cat %s/Rec_Lig_PDB/%s > %s/complexe_predit_score3.pdb "%(outdir,ListT[0][0],outdir))
	pdbinfile = "%s/complexe_predit_score3.pdb"%(outdir)


########################


if Ligand <> "" :
	#creeation du fichier Complexe.pdb
	os.system("cat %s %s > %s/Complexe.pdb"%(Receptor,Ligand,outdir))
	Complex="%s/Complexe.pdb"%(outdir)
#Caclul de RMSD

# parses the pdb file
	dPDB_Cplx_BestScore = structureTools.parsePDBMultiChains(pdbinfile)
	dPDB_Cplx_Natif = structureTools.parsePDBMultiChains(Complex)

	dPDB_Lig_Natif={}
	dPDB_Lig_Natif["chains"] = []
	dPDB_Lig_Natif["chains"].append(chaineLig)

	dPDB_Lig_BestScore={}
	dPDB_Lig_BestScore["chains"] = []
	dPDB_Lig_BestScore["chains"].append(chaineLig)

	dPDB_Lig_Natif[chaineLig] = dPDB_Cplx_Natif[chaineLig]
	dPDB_Lig_BestScore[chaineLig] = dPDB_Cplx_BestScore[chaineLig]


	dPDB_Interface_Natif = structureTools.InterfacePDB(dPDB_Cplx_Natif , 5.0 , "atom", chaineRec , chaineLig)

				


	RMSD_full_Cplx_CA = structureTools.RMSD(dPDB_Cplx_BestScore , dPDB_Cplx_Natif,"CA")
	RMSD_full_Cplx_AllAtoms = structureTools.RMSD(dPDB_Cplx_BestScore , dPDB_Cplx_Natif)


	RMSD_Lig_CA = structureTools.RMSD(dPDB_Lig_Natif , dPDB_Lig_BestScore,"CA")
	RMSD_Lig_AllAtoms = structureTools.RMSD(dPDB_Lig_Natif , dPDB_Lig_BestScore)


	RMSD_Interface_Natif_CA = structureTools.RMSD(dPDB_Interface_Natif, dPDB_Cplx_BestScore,"CA")
	RMSD_Interface_Natif_AllAtoms = structureTools.RMSD(dPDB_Interface_Natif, dPDB_Cplx_BestScore)


	#Ecrire les resultats dans un fichier out
	f= open("%s/RMSD.out"%(outdir),"w")

	f.write("Meilleur Solution: %s\n\n"%(ListT[0][0]))

	f.write("-RMSD Complex entier (CA): %f\n -RMSD Complex entier (tous les atomes): %f\n\n"%(RMSD_full_Cplx_CA,RMSD_full_Cplx_AllAtoms))

	f.write("-RMSD Ligand (CA): %f\n -RMSD Ligand (tous les atomes): %f\n\n"%(RMSD_Lig_CA , RMSD_Lig_AllAtoms))

	f.write("-RMSD Interface native (CA): %f\n -RMSD Interface native (tous les atomes): %f\n"%(RMSD_Interface_Natif_CA , RMSD_Interface_Natif_AllAtoms))

	f.close()


	structureTools.initBfactor(dPDB_Cplx_Natif)

	for chain in dPDB_Interface_Natif["chains"]:
		for res in dPDB_Interface_Natif[chain]["reslist"]:
			dPDB_Cplx_Natif[chain][res]["bfactor"] = 1


	structureTools.initBfactor(dPDB_Cplx_BestScore)

	for chain in dPDB_Interface_Natif["chains"]:
		for res in dPDB_Interface_Natif[chain]["reslist"]:
			dPDB_Cplx_BestScore[chain][res]["bfactor"] = 1

	structureTools.writePDB(dPDB_Cplx_Natif,"%s/interfaceNatif.pdb"%(outdir),bfactor = True)
	structureTools.writePDB(dPDB_Cplx_BestScore,"%s/interfaceBestScore.pdb"%(outdir),bfactor = True)

#supprimer le fichier non trie
os.system("rm -f %s"%(nonTrier)) 
