#!/usr/bin/env python
#-*- coding : utf8 -*-

#Author: GHARBI Houssem / Timothee O'Donnell
"""
Description: Manuelle d'utilisation du programme
"""

def usage():
	usage = ("Ce programme calcul le score avec l'equation de Cornell impliquant les termes non liees, ou avec l'equation de Cornell modifie par ajout de score denergie lie au desolvation entre le fichier pdb du recepteur fixe et les differents orientations du ligand"
	 		"Puis calcul le RMSD entre la struture native et la meilleur structure predite par ce calcul.\n\n"
			"Input = \n"
			"\t-> -in:  repertoire contenant les differents fichiers pdb des solutions du ligand\n"
			"\t-> -out: repertoire qui contiendra les sorties de donnees\n"
			"\t-> -prog: le programme avec le quelle les scores vont etre calculer,cet argument peut prendre l'une de ces 3 valeus: (NewScoringCornell.py, NewScoringCornellAndDesolvation.py, OldScoringCornellAndDesolvation.py)\n"
			"\t-> -pdbR: fichier du recepteur \n"
			"\t-> -pdbC: fichier du complexe natif\n\n"
			
			"Output = \n"
			"\t->RMSD.out= un fichier contenant les differents RMSD calculer \n"
			"\t->complexe_predit_score.pdb: un fichier pdb contenant le meilleur complexe predit \n"
			"\t->tous les fichiers pdb de tous les solutions pour la quelle un score a ete calculer \n"
			"\t->Eners.out: tous les scores calculer non trier\n"
			"\t->InterfaceNatif.pdb: fichier pdb dont les bfactors de tous les atomes sont 0 sauf ceux de l'interface qui vallent 1\n"
			"\t->InterfaceBestScore.pdb: fichier pdb dont les bfactors de tous les atomes vallent 0 sauf ceux de l'interface du complexe Natif qui vallent1\n"
			"\t->Scoring: fichier contenant tous les scores triees dans l'ordre croissant des scores\n\n"
			
			"Argument Obligatoire : -in,-out,-prog, -pdbR\n"
			"Argument Facultatif : -pdbC\n\n"  
			)
	
	print usage
