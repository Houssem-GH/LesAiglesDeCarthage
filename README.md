#Groupe: Les aigles de Carthage
#Projet: Docking
#Version: Python 2.7
#Auteurs: GHARBI HOUSSEM-EDDINE et O'DONNELL TIMOTHEE
#Date de mise en ligne: 02/05/2017


#Fonction Programme runScoring.py et RMSDFull.py

L'objectif du programme RunScoring.py est d'implémenter une fonction de scoring sur un groupe de solutions préselectionnées afin de déterminer la conformation d'un complexe ligand recepteur la plus probable.
Il y a trois 3 algorithmes de scoring differents qui devront etre preciser en argument.

Un second programme calcule les RMSDFull.py entre le complexe natif en fichier pdb et les differentes solutions presentes dans le repertoire fourni en argument, ce programme determine si la meilleur solution a été trouver par l'un des algorithmes.
On note que ce programme n'est executable que s'il on a le ligand natif.
 
#Argument et output runScoring.py:

Pour executer ce programme, il suffit d'executer le programme nommer runScoring.py et mettre comme arguments:

```
INput:
	-in:  repertoire contenant les differents fichiers pdb des solutions du ligand
	-out: repertoire qui contiendra les sorties de donnees
	-prog: le programme avec le quelle les scores vont etre calculer,cet argument peut prendre l'une de ces 3 valeus:
	(NewScoringCornell.py,NewScoringCornellAndDesolvation.py, OldScoringCornellAndDesolvation.py)
	-pdbR: fichier du recepteur
	-pdbL: fichier du ligand natif 
	-chainRec: preciser la chaine du recepteur
	-chainLig: preciser la chaine du ligand

Output:
	complexe_predit_score.pdb: un fichier pdb contenant le meilleur complexe predit
	Rec_Lig_PDB: repertoire contenenant tous les complexes theoriques pdb de tous les solutions pour la quelle un score a ete calculer
	Scoring: fichier contenant tous les scores triees dans l'ordre croissant des scores

Output supplementaire si argument -pdbL ajoute: 
	InterfaceNatif.pdb: fichier pdb dont les bfactors de tous les atomes sont 0 sauf ceux de l'interface qui vallent 1
	InterfaceBestScore.pdb: fichier pdb dont les bfactors de tous les atomes vallent 0 sauf ceux de l'interface du complexe Natif qui 					vallent 1
	Complexe.pdb: fichier reunissant le recepteur et le ligand fourni en argument
	RMSD.out= un fichier contenant les differents RMSD calculer
	Argument Obligatoire : -in, -out, -prog, -pdbR, -chainRec, -chainLig
	Argument Facultatif : -pdbL
```
Exemple de code: 
python runScoring.py -in confs_withH/ -out ScoringCornell -prog NewScoringCornell.py -pdbR Rec_natif_DP.pdb -pdbL Lig_natif_DP_aligned.pdb -chainRec B -chainLig D


 
#Argument et output RMSDFull.py:

Pour executer ce programme, il suffit d'executer le programme nommer RMSDFull.py et mettre comme arguments:

```
Input:
	-in:  repertoire contenant les differents fichiers pdb des solutions du ligand
	out: repertoire qui contiendra les sorties de donnees
	-pdbR: fichier du recepteur natif
	-pdbL: fichier du ligand natif
	-chainRec: preciser la chaine du recepteur
	-chainLig: preciser la chaine du ligand
Output:
	RMSD_Full.out= un fichier contenant les differentes RMSD calculee en ordre croissant
	Rec_Lig_PDB: repertoire contenenant tous les complexes theoriques pdb de tous les solutions pour la quelle un RMSD a ete calculer
	Complexe.pdb: fichier reunissant le recepteur et le ligand fourni en argument
	
Argument Obligatoire : -in, -out, -pdbL, -pdbR, -chainRec, -chainLig 

```
Exemple de code: python runRMSDFull.py -in confs_withH/ -out RMSDFull -pdbR Rec_natif_DP.pdb -pdbL Lig_natif_DP_aligned.pdb -chainRec B -chainLig D


