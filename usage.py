#!/usr/bin/env python
#-*- coding : utf8 -*-

#Author: GHARBI Houssem / Timothee O'Donnell
"""
Description: Manuelle d'utilisation du programme
"""

def usage1():
	usage1 = ("Ce programme calcul le score avec l'equation de Cornell impliquant les termes non liees, ou avec l'equation de Cornell modifie par ajout de score denergie lie au desolvation entre le fichier pdb du recepteur fixe et les differents orientations du ligand"
	 		"Puis calcul le RMSD entre la struture native et la meilleur structure predite par ce calcul.\n\n"
			"Input = \n"
			"\t-> -in:  repertoire contenant les differents fichiers pdb des solutions du ligand\n"
			"\t-> -out: repertoire qui contiendra les sorties de donnees\n"
			"\t-> -prog: le programme avec le quelle les scores vont etre calculer,cet argument peut prendre l'une de ces 3 valeus: (NewScoringCornell.py, NewScoringCornellAndDesolvation.py, OldScoringCornellAndDesolvation.py)\n"
			"\t-> -pdbR: fichier du recepteur \n"
			"\t-> -pdbL: fichier du Ligand natif aligne\n"
			"\t-> -chainRec: preciser la chaine du recepteur\n"
			"\t-> -chainLig: preciser la chaine du ligand\n\n" 
			"Output = \n"
			"\t->RMSD.out= un fichier contenant les differents RMSD calculer \n"
			"\t->complexe_predit_score.pdb: un fichier pdb contenant le meilleur complexe predit \n"
			"\t->Rec_Lig_PDB: repertoire contenenant tous les complexes theoriques pdb de tous les solutions pour la quelle un score a ete calculer \n"
			"\t->InterfaceNatif.pdb: fichier pdb dont les bfactors de tous les atomes sont 0 sauf ceux de l'interface qui vallent 1\n"
			"\t->InterfaceBestScore.pdb: fichier pdb dont les bfactors de tous les atomes vallent 0 sauf ceux de l'interface du complexe Natif qui vallent 1\n"
			"\t->Scoring: fichier contenant tous les scores triees dans l'ordre croissant des scores\n\n"
			
			"Argument Obligatoire : -in, -out, -prog, -pdbR, -chainRec, -chainLig\n"
			"Argument Facultatif : -pdbL\n\n"  
			)
	
	print usage1





def usage2():
	usage2 = ("Ce programme calcul les RMSD entre le complexe natif en fichier pdb et les differentes solutions presentes dans le repertoire -in fourni\n\n"
			"Input = \n"
			"\t-> -in:  repertoire contenant les differents fichiers pdb des solutions du ligand\n"
			"\t-> -out: repertoire qui contiendra les sorties de donnees\n"
			"\t-> -pdbR: fichier du recepteur natif \n"
			"\t-> -pdbL: fichier du Ligand natif aligne\n"
			"\t-> -chainRec: preciser la chaine du recepteur\n"
			"\t-> -chainLig: preciser la chaine du ligand\n\n" 
			"Output = \n"
			"\t->RMSD_Full.out= un fichier contenant les differentes RMSD calculee en ordre croissant \n"
			"\t->Rec_Lig_PDB: repertoire contenenant tous les complexes theoriques pdb de tous les solutions pour la quelle un RMSD a ete calculer \n\n"
			
			"Argument Obligatoire : -in, -out, -pdbL, -pdbR, -chainRec, -chainLig\n\n" 
			)
	
	print usage2
