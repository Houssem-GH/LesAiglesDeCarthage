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
    usage.usage()
    print "ERROR: please, enter the name of the directory input"
    sys.exit()

    
#repertoire de sortie a creer des resultats du calcul de scoring
try:
    outdir = sys.argv[sys.argv.index("-out")+1]
except:    
    usage.usage()
    print "ERROR: please, enter the name of the directory output"
    sys.exit()


#le programme de scoring a executer 
try:
    Program_Scoring = sys.argv[sys.argv.index("-prog")+1]
except:    
    usage.usage()
    print "ERROR: please, enter the name of the program to execute"
    sys.exit()

try:
    Receptor = sys.argv[sys.argv.index("-pdbR")+1]
    #Rec_natif_DP.pdb
except:    
    usage.usage()
    print "ERROR: please, enter the name of the receptor file"
    sys.exit()

try:
    Complex = sys.argv[sys.argv.index("-pdbC")+1]
    #cplx_natif.pdb
except:
	Complex = ""






filelist = glob.glob("%s/*DP.pdb"%(indir)) #recuperer les noms des fichiers correspondant aux coordonnees du ligand dans une liste


os.system("rm -rf %s"%(outdir)) #suprimer la repertoire de sortie si elle existe


os.system("mkdir %s"%(outdir)) #creer la repertoire de sortie



#boucle de calcul de score de chaque fichier correspondant aux coordonnees du ligand par rapport au recepteur 
#qui lui est fixe (Ex:fichier PDB: Rec_natif_DP)
for pdb in filelist : 
    num = pdb.split("/")[-1].split("_")[-2]
    curpdb = "rec_nat_lig_%s.pdb"%(num)
    os.system("cat %s %s > %s/%s"%(Receptor, pdb,outdir, curpdb))
    os.system("python %s -pdb %s/%s -chain1 B -chain2 D"%(Program_Scoring, outdir,curpdb))
 

#mettre les resultats de calcul de scoring dans Eners.out   
os.system("cat ener.out >> %s/Eners.out  > %s/Eners.out"%(outdir,outdir))
os.system("rm -f ener.out") #supprimer le fichier de score temporaire


nonTrier = "%s/Eners.out"%(outdir) #recuperer les donnees de Scoring dans un nouveau fichier nonTrier


#lecture du fichier nonTrier
f = open(nonTrier, "r")
lines = f.readlines()
f.close()


#Stocker les resultats dans un dictionnaire
dicoNT= {}
for line in lines:
	cle= "%s"%(line[0:24]).strip()
	valeur = float(line[28:50])
	dicoNT[cle] = valeur
	

#Trier par Score les resultats de score dans une liste
ListT=sorted(dicoNT.items(), key=lambda t: t[1])


#Afficher les resultats de scoring par ordre croissant de score dans le fichier Scoring_Cornell
f_out = open("%s/Scoring"%(outdir),"w")

for res in ListT:	
	f_out.write("%s    %f\n"%(res[0],res[1]))
	
f_out.close()


#Creer le fichier du complex Recepteur-ligand selon la methode de calcul 
if Program_Scoring == "NewScoringCornell.py":
	os.system("cat %s > %s/complexe_predit_score1.pdb "%(ListT[0][0],outdir))
	pdbinfile = "%s/complexe_predit_score1.pdb"%(outdir)
	
elif Program_Scoring == "NewScoringCornellAndDesolvation.py":
	os.system("cat %s > %s/complexe_predit_score2.pdb "%(ListT[0][0],outdir))
	pdbinfile = "%s/complexe_predit_score2.pdb"%(outdir)
	
elif Program_Scoring == "OldScoringCornellAndDesolvation.py":
	os.system("cat %s > %s/complexe_predit_score3.pdb "%(ListT[0][0],outdir))
	pdbinfile = "%s/complexe_predit_score3.pdb"%(outdir)

########################

if Complex <> "" :
#Caclul de RMSD

# parses the pdb file
	dPDB_Cplx_BestScore = structureTools.parsePDBMultiChains(pdbinfile)
	dPDB_Cplx_Natif = structureTools.parsePDBMultiChains("%s"%(Complex))

	dPDB_Lig_Natif={}
	dPDB_Lig_Natif["chains"] = []
	dPDB_Lig_Natif["chains"].append("D")

	dPDB_Lig_BestScore={}
	dPDB_Lig_BestScore["chains"] = []
	dPDB_Lig_BestScore["chains"].append("D")

	dPDB_Lig_Natif["D"] = dPDB_Cplx_Natif["D"]
	dPDB_Lig_BestScore["D"] = dPDB_Cplx_BestScore["D"]


	dPDB_Interface_Natif = structureTools.InterfacePDB(dPDB_Cplx_Natif , 5.0 , "atom", "B" , "D")

				


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
