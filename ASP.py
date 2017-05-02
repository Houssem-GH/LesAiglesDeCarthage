#!/usr/bin/env python


##Author: GHARBI Houssem / Timothee O'Donnell
"""
implementation de parametres de atomique de deslovation necessaire au calcule de l'Energie de Desolvation

"""

def Atomic_solvation_parameter ():

	dASP = {}
	dASP["C"] = -0.00143
	dASP["CA"] = -0.00143
	dASP["CM"] = -0.00143
	dASP["Cs"] = -0.00143
	dASP["CT"] = -0.00143
	dASP["H"] = 0.00051
	dASP["H1"] = 0.00051
	dASP["H2"] = 0.00051
	dASP["H3"] = 0.00051
	dASP["H4"] = 0.00051
	dASP["H5"] = 0.00051
	dASP["HA"] = 0.00051
	dASP["HC"] = 0.00051
	dASP["HO"] = 0.00051
	dASP["HP"] = 0.00051
	dASP["HS"] = 0.00051
	dASP["HW"] = 0.00051
	dASP["N2m"] = -0.00162
	dASP["N3n"] = -0.00162
	dASP["O"] = -0.00251
	dASP["O2"] = -0.00251
	dASP["OH"] = -0.00251
	dASP["OS"] = -0.00251
	dASP["OW"] = -0.00251
	dASP["S"] = -0.00214
	dASP["SH"] = -0.00214





	dAtomic_solvation_parameter = {}
	dAtomic_solvation_parameter["GLY"] = {}
	dAtomic_solvation_parameter["GLY"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["GLY"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["GLY"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["GLY"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["GLY"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["GLY"]["HA2"] = dASP["H1"]
	dAtomic_solvation_parameter["GLY"]["HA3"] = dASP["H1"]

	dAtomic_solvation_parameter["ALA"] = {}
	dAtomic_solvation_parameter["ALA"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["ALA"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["ALA"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["ALA"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["ALA"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["ALA"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["ALA"]["HB1"] = dASP["HC"]
	dAtomic_solvation_parameter["ALA"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["ALA"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["ALA"]["HA"] = dASP["H1"]

	dAtomic_solvation_parameter["ASP"] = {}
	dAtomic_solvation_parameter["ASP"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["ASP"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["ASP"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["ASP"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["ASP"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["ASP"]["CG"] = dASP["C"]
	dAtomic_solvation_parameter["ASP"]["OD1"] = dASP["O2"]
	dAtomic_solvation_parameter["ASP"]["OD2"] = dASP["O2"]
	dAtomic_solvation_parameter["ASP"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["ASP"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["ASP"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["ASP"]["HB3"] = dASP["HC"]


	dAtomic_solvation_parameter["GLU"] = {}
	dAtomic_solvation_parameter["GLU"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["GLU"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["GLU"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["GLU"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["GLU"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["GLU"]["CG"] = dASP["CT"]
	dAtomic_solvation_parameter["GLU"]["CD"] = dASP["C"]
	dAtomic_solvation_parameter["GLU"]["OE1"] = dASP["O2"]
	dAtomic_solvation_parameter["GLU"]["OE2"] = dASP["O2"]
	dAtomic_solvation_parameter["GLU"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["GLU"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["GLU"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["GLU"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["GLU"]["HG2"] = dASP["HC"]
	dAtomic_solvation_parameter["GLU"]["HG3"] = dASP["HC"]


	dAtomic_solvation_parameter["LEU"] = {}
	dAtomic_solvation_parameter["LEU"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["LEU"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["LEU"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["LEU"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["LEU"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["LEU"]["CG"] = dASP["CT"]
	dAtomic_solvation_parameter["LEU"]["CD1"] = dASP["CT"]
	dAtomic_solvation_parameter["LEU"]["CD2"] = dASP["CT"]
	dAtomic_solvation_parameter["LEU"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["LEU"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["LEU"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["LEU"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["LEU"]["HG"] = dASP["HC"]
	dAtomic_solvation_parameter["LEU"]["HD11"] = dASP["HC"]
	dAtomic_solvation_parameter["LEU"]["HD12"] = dASP["HC"]
	dAtomic_solvation_parameter["LEU"]["HD13"] = dASP["HC"]
	dAtomic_solvation_parameter["LEU"]["HD21"] = dASP["HC"]
	dAtomic_solvation_parameter["LEU"]["HD22"] = dASP["HC"]
	dAtomic_solvation_parameter["LEU"]["HD23"] = dASP["HC"]

	dAtomic_solvation_parameter["ASN"] = {}
	dAtomic_solvation_parameter["ASN"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["ASN"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["ASN"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["ASN"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["ASN"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["ASN"]["CG"] = dASP["C"]
	dAtomic_solvation_parameter["ASN"]["ND2"] = dASP["N2m"]
	dAtomic_solvation_parameter["ASN"]["OD1"] = dASP["O"]
	dAtomic_solvation_parameter["ASN"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["ASN"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["ASN"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["ASN"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["ASN"]["HD21"] = dASP["H"]
	dAtomic_solvation_parameter["ASN"]["HD22"] = dASP["H"]


	dAtomic_solvation_parameter["GLN"] = {}
	dAtomic_solvation_parameter["GLN"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["GLN"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["GLN"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["GLN"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["GLN"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["GLN"]["CG"] = dASP["CT"]
	dAtomic_solvation_parameter["GLN"]["CD"] = dASP["C"]
	dAtomic_solvation_parameter["GLN"]["NE2"] = dASP["N2m"]
	dAtomic_solvation_parameter["GLN"]["OE1"] = dASP["O"]
	dAtomic_solvation_parameter["GLN"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["GLN"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["GLN"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["GLN"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["GLN"]["HG2"] = dASP["HC"]
	dAtomic_solvation_parameter["GLN"]["HG3"] = dASP["HC"]
	dAtomic_solvation_parameter["GLN"]["HE21"] = dASP["H"]
	dAtomic_solvation_parameter["GLN"]["HE22"] = dASP["H"]


	dAtomic_solvation_parameter["ILE"] = {}
	dAtomic_solvation_parameter["ILE"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["ILE"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["ILE"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["ILE"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["ILE"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["ILE"]["CG1"] = dASP["CT"]
	dAtomic_solvation_parameter["ILE"]["CG2"] = dASP["CT"]
	dAtomic_solvation_parameter["ILE"]["CD1"] = dASP["CT"]
	dAtomic_solvation_parameter["ILE"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["ILE"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["ILE"]["HB"] = dASP["HC"]
	dAtomic_solvation_parameter["ILE"]["HG12"] = dASP["HC"]
	dAtomic_solvation_parameter["ILE"]["HG13"] = dASP["HC"]
	dAtomic_solvation_parameter["ILE"]["HG21"] = dASP["HC"]
	dAtomic_solvation_parameter["ILE"]["HG22"] = dASP["HC"]
	dAtomic_solvation_parameter["ILE"]["HG23"] = dASP["HC"]
	dAtomic_solvation_parameter["ILE"]["HD11"] = dASP["HC"]
	dAtomic_solvation_parameter["ILE"]["HD12"] = dASP["HC"]
	dAtomic_solvation_parameter["ILE"]["HD13"] = dASP["HC"]

	dAtomic_solvation_parameter["VAL"] = {}
	dAtomic_solvation_parameter["VAL"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["VAL"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["VAL"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["VAL"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["VAL"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["VAL"]["CG1"] = dASP["CT"]
	dAtomic_solvation_parameter["VAL"]["CG2"] = dASP["CT"]
	dAtomic_solvation_parameter["VAL"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["VAL"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["VAL"]["HB"] = dASP["HC"]
	dAtomic_solvation_parameter["VAL"]["HG11"] = dASP["HC"]
	dAtomic_solvation_parameter["VAL"]["HG12"] = dASP["HC"]
	dAtomic_solvation_parameter["VAL"]["HG13"] = dASP["HC"]
	dAtomic_solvation_parameter["VAL"]["HG21"] = dASP["HC"]
	dAtomic_solvation_parameter["VAL"]["HG22"] = dASP["HC"]
	dAtomic_solvation_parameter["VAL"]["HG23"] = dASP["HC"]


	dAtomic_solvation_parameter["SER"] = {}
	dAtomic_solvation_parameter["SER"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["SER"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["SER"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["SER"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["SER"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["SER"]["OG"] = dASP["OH"]
	dAtomic_solvation_parameter["SER"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["SER"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["SER"]["HB2"] = dASP["H1"]
	dAtomic_solvation_parameter["SER"]["HB3"] = dASP["H1"]
	dAtomic_solvation_parameter["SER"]["HG"] = dASP["HO"]



	dAtomic_solvation_parameter["THR"] = {}
	dAtomic_solvation_parameter["THR"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["THR"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["THR"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["THR"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["THR"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["THR"]["OG1"] = dASP["OH"]
	dAtomic_solvation_parameter["THR"]["CG2"] = dASP["CT"]
	dAtomic_solvation_parameter["THR"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["THR"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["THR"]["HB"] = dASP["H1"]
	dAtomic_solvation_parameter["THR"]["HG1"] = dASP["HO"]
	dAtomic_solvation_parameter["THR"]["HG21"] = dASP["HC"]
	dAtomic_solvation_parameter["THR"]["HG22"] = dASP["HC"]
	dAtomic_solvation_parameter["THR"]["HG23"] = dASP["HC"]



	dAtomic_solvation_parameter["CYS"] = {}
	dAtomic_solvation_parameter["CYS"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["CYS"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["CYS"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["CYS"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["CYS"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["CYS"]["SG"] = dASP["SH"]
	dAtomic_solvation_parameter["CYS"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["CYS"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["CYS"]["HB1"] = dASP["H1"]
	dAtomic_solvation_parameter["CYS"]["HB2"] = dASP["H1"]
	dAtomic_solvation_parameter["CYS"]["HG"] = dASP["HS"]


	dAtomic_solvation_parameter["PRO"] = {}
	dAtomic_solvation_parameter["PRO"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["PRO"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["PRO"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["PRO"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["PRO"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["PRO"]["CG"] = dASP["CT"]
	dAtomic_solvation_parameter["PRO"]["CD"] = dASP["CT"]
	dAtomic_solvation_parameter["PRO"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["PRO"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["PRO"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["PRO"]["HG2"] = dASP["HC"]
	dAtomic_solvation_parameter["PRO"]["HG3"] = dASP["HC"]
	dAtomic_solvation_parameter["PRO"]["HD2"] = dASP["H1"]
	dAtomic_solvation_parameter["PRO"]["HD3"] = dASP["H1"]



	dAtomic_solvation_parameter["ARG"] = {}
	dAtomic_solvation_parameter["ARG"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["ARG"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["ARG"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["ARG"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["ARG"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["ARG"]["CG"] = dASP["CT"]
	dAtomic_solvation_parameter["ARG"]["CD"] = dASP["CT"]
	dAtomic_solvation_parameter["ARG"]["NE"] = dASP["N2m"]
	dAtomic_solvation_parameter["ARG"]["CZ"] = dASP["CA"]
	dAtomic_solvation_parameter["ARG"]["NH1"] = dASP["N2m"]
	dAtomic_solvation_parameter["ARG"]["NH2"] = dASP["N2m"]
	dAtomic_solvation_parameter["ARG"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["ARG"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["ARG"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["ARG"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["ARG"]["HG2"] = dASP["HC"]
	dAtomic_solvation_parameter["ARG"]["HG3"] = dASP["HC"]
	dAtomic_solvation_parameter["ARG"]["HD2"] = dASP["H1"]
	dAtomic_solvation_parameter["ARG"]["HD3"] = dASP["H1"]
	dAtomic_solvation_parameter["ARG"]["HE"] = dASP["H"]
	dAtomic_solvation_parameter["ARG"]["HH11"] = dASP["H"]
	dAtomic_solvation_parameter["ARG"]["HH12"] = dASP["H"]
	dAtomic_solvation_parameter["ARG"]["HH21"] = dASP["H"]  
	dAtomic_solvation_parameter["ARG"]["HH22"] = dASP["H"]


	dAtomic_solvation_parameter["LYS"] = {}
	dAtomic_solvation_parameter["LYS"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["LYS"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["LYS"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["LYS"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["LYS"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["LYS"]["CG"] = dASP["CT"]
	dAtomic_solvation_parameter["LYS"]["CD"] = dASP["CT"] 
	dAtomic_solvation_parameter["LYS"]["CE"] = dASP["CT"]
	dAtomic_solvation_parameter["LYS"]["NZ"] = dASP["N3n"] 
	dAtomic_solvation_parameter["LYS"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["LYS"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["LYS"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["LYS"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["LYS"]["HG2"] = dASP["HC"]
	dAtomic_solvation_parameter["LYS"]["HG3"] = dASP["HC"]
	dAtomic_solvation_parameter["LYS"]["HD2"] = dASP["HC"]
	dAtomic_solvation_parameter["LYS"]["HD3"] = dASP["HC"]
	dAtomic_solvation_parameter["LYS"]["HE2"] = dASP["HP"]
	dAtomic_solvation_parameter["LYS"]["HE3"] = dASP["HP"]
	dAtomic_solvation_parameter["LYS"]["HZ2"] = dASP["H"]
	dAtomic_solvation_parameter["LYS"]["HZ1"] = dASP["H"]   
	dAtomic_solvation_parameter["LYS"]["HZ3"] = dASP["H"]


	dAtomic_solvation_parameter["HIE"] = {}
	dAtomic_solvation_parameter["HIE"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["HIE"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["HIE"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["HIE"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["HIE"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["HIE"]["CG"] = dASP["CA"]
	dAtomic_solvation_parameter["HIE"]["ND1"] = dASP["N2m"]
	dAtomic_solvation_parameter["HIE"]["CE1"] = dASP["CA"]
	dAtomic_solvation_parameter["HIE"]["NE2"] = dASP["N2m"]
	dAtomic_solvation_parameter["HIE"]["CD2"] = dASP["CA"]
	dAtomic_solvation_parameter["HIE"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["HIE"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["HIE"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["HIE"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["HIE"]["HE1"] = dASP["H5"]
	dAtomic_solvation_parameter["HIE"]["HE2"] = dASP["H"]
	dAtomic_solvation_parameter["HIE"]["HD2"] = dASP["H4"]

	dAtomic_solvation_parameter["HID"] = {}
	dAtomic_solvation_parameter["HID"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["HID"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["HID"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["HID"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["HID"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["HID"]["CG"] = dASP["CA"]
	dAtomic_solvation_parameter["HID"]["ND1"] = dASP["N2m"]
	dAtomic_solvation_parameter["HID"]["CE1"] = dASP["CA"]
	dAtomic_solvation_parameter["HID"]["NE2"] = dASP["N2m"]
	dAtomic_solvation_parameter["HID"]["CD2"] = dASP["CA"]
	dAtomic_solvation_parameter["HID"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["HID"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["HID"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["HID"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["HID"]["HE1"] = dASP["H5"]
	dAtomic_solvation_parameter["HID"]["HD1"] = dASP["H"]
	dAtomic_solvation_parameter["HID"]["HD2"] = dASP["H4"]

	dAtomic_solvation_parameter["MET"] = {}
	dAtomic_solvation_parameter["MET"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["MET"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["MET"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["MET"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["MET"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["MET"]["CG"] = dASP["CT"]
	dAtomic_solvation_parameter["MET"]["SD"] = dASP["S"]
	dAtomic_solvation_parameter["MET"]["CE"] = dASP["CT"]
	dAtomic_solvation_parameter["MET"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["MET"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["MET"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["MET"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["MET"]["HG2"] = dASP["H1"]
	dAtomic_solvation_parameter["MET"]["HG3"] = dASP["H1"]
	dAtomic_solvation_parameter["MET"]["HE2"] = dASP["H1"]
	dAtomic_solvation_parameter["MET"]["HE3"] = dASP["H1"]
	dAtomic_solvation_parameter["MET"]["HE1"] = dASP["H1"]



	dAtomic_solvation_parameter["PHE"] = {}
	dAtomic_solvation_parameter["PHE"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["PHE"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["PHE"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["PHE"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["PHE"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["PHE"]["CG"] = dASP["CA"]
	dAtomic_solvation_parameter["PHE"]["CD1"] = dASP["CA"]
	dAtomic_solvation_parameter["PHE"]["CD2"] = dASP["CA"]
	dAtomic_solvation_parameter["PHE"]["CE1"] = dASP["CA"]
	dAtomic_solvation_parameter["PHE"]["CE2"] = dASP["CA"]
	dAtomic_solvation_parameter["PHE"]["CZ"] = dASP["CA"]
	dAtomic_solvation_parameter["PHE"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["PHE"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["PHE"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["PHE"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["PHE"]["HD1"] = dASP["HA"]
	dAtomic_solvation_parameter["PHE"]["HD2"] = dASP["HA"]
	dAtomic_solvation_parameter["PHE"]["HE1"] = dASP["HA"]
	dAtomic_solvation_parameter["PHE"]["HE2"] = dASP["HA"]
	dAtomic_solvation_parameter["PHE"]["HZ"] = dASP["HA"]




	dAtomic_solvation_parameter["TYR"] = {}
	dAtomic_solvation_parameter["TYR"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["TYR"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["TYR"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["TYR"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["TYR"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["TYR"]["CG"] = dASP["CA"]
	dAtomic_solvation_parameter["TYR"]["CD1"] =  dASP["CA"]
	dAtomic_solvation_parameter["TYR"]["CD2"] =  dASP["CA"]
	dAtomic_solvation_parameter["TYR"]["CE1"] = dASP["CA"]
	dAtomic_solvation_parameter["TYR"]["CE2"] = dASP["CA"]
	dAtomic_solvation_parameter["TYR"]["CZ"] = dASP["CA"]
	dAtomic_solvation_parameter["TYR"]["OH"] = dASP["OH"]
	dAtomic_solvation_parameter["TYR"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["TYR"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["TYR"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["TYR"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["TYR"]["HD1"] = dASP["HA"]
	dAtomic_solvation_parameter["TYR"]["HD2"] = dASP["HA"]
	dAtomic_solvation_parameter["TYR"]["HE1"] = dASP["HA"]
	dAtomic_solvation_parameter["TYR"]["HE2"] = dASP["HA"]
	dAtomic_solvation_parameter["TYR"]["HH"] = dASP["HO"]




	dAtomic_solvation_parameter["TRP"] = {}
	dAtomic_solvation_parameter["TRP"]["N"] = dASP["N2m"]
	dAtomic_solvation_parameter["TRP"]["CA"] = dASP["CT"]
	dAtomic_solvation_parameter["TRP"]["C"] = dASP["C"]
	dAtomic_solvation_parameter["TRP"]["O"] = dASP["O"]
	dAtomic_solvation_parameter["TRP"]["CB"] = dASP["CT"]
	dAtomic_solvation_parameter["TRP"]["CG"] = dASP["CA"]
	dAtomic_solvation_parameter["TRP"]["CD1"] = dASP["CA"]
	dAtomic_solvation_parameter["TRP"]["CD2"] = dASP["CA"]
	dAtomic_solvation_parameter["TRP"]["NE1"] = dASP["N2m"]
	dAtomic_solvation_parameter["TRP"]["CE2"] = dASP["CA"]
	dAtomic_solvation_parameter["TRP"]["CE3"] = dASP["CA"]
	dAtomic_solvation_parameter["TRP"]["CZ2"] = dASP["CA"]
	dAtomic_solvation_parameter["TRP"]["CZ3"] = dASP["CA"]
	dAtomic_solvation_parameter["TRP"]["CH2"] = dASP["CA"]
	dAtomic_solvation_parameter["TRP"]["H"] = dASP["H"]
	dAtomic_solvation_parameter["TRP"]["HA"] = dASP["H1"]
	dAtomic_solvation_parameter["TRP"]["HB2"] = dASP["HC"]
	dAtomic_solvation_parameter["TRP"]["HB3"] = dASP["HC"]
	dAtomic_solvation_parameter["TRP"]["HD1"] = dASP["H4"]
	dAtomic_solvation_parameter["TRP"]["HE1"] = dASP["H"]
	dAtomic_solvation_parameter["TRP"]["HE3"] = dASP["HA"]
	dAtomic_solvation_parameter["TRP"]["HZ2"] = dASP["HA"]
	dAtomic_solvation_parameter["TRP"]["HZ3"] = dASP["HA"]
	dAtomic_solvation_parameter["TRP"]["HH2"] = dASP["HA"]

	return dAtomic_solvation_parameter
