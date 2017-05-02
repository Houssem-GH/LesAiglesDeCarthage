#!/usr/bin/env python


##Author: GHARBI Houssem / Timothee O'Donnell
"""
implementation de parametres volume necessaire au calcule de l'Energie de Desolvation

"""

def Volume ():

	dV = {}
	dV["C"] = 33.5103
	dV["CA"] = 33.5103
	dV["CM"] = 33.5103
	dV["Cs"] = 33.5103
	dV["CT"] = 33.5103
	dV["H"] = 0
	dV["H1"] = 0
	dV["H2"] = 0
	dV["H3"] = 0
	dV["H4"] = 0
	dV["H5"] = 0
	dV["HA"] = 0
	dV["HC"] = 0
	dV["HO"] = 0
	dV["HP"] = 0
	dV["HS"] = 0
	dV["HW"] = 0
	dV["N2m"] = 22.4493
	dV["N3n"] = 22.4493
	dV["O"] = 17.1573
	dV["O2"] = 17.1573
	dV["OH"] = 17.1573
	dV["OS"] = 17.1573
	dV["OW"] = 17.1573
	dV["S"] = 33.5103
	dV["SH"] =33.5103





	dVolume = {}
	dVolume["GLY"] = {}
	dVolume["GLY"]["N"] = dV["N2m"]
	dVolume["GLY"]["CA"] = dV["CT"]
	dVolume["GLY"]["C"] = dV["C"]
	dVolume["GLY"]["O"] = dV["O"]
	dVolume["GLY"]["H"] = dV["H"]
	dVolume["GLY"]["HA2"] = dV["H1"]
	dVolume["GLY"]["HA3"] = dV["H1"]

	dVolume["ALA"] = {}
	dVolume["ALA"]["N"] = dV["N2m"]
	dVolume["ALA"]["CA"] = dV["CT"]
	dVolume["ALA"]["C"] = dV["C"]
	dVolume["ALA"]["O"] = dV["O"]
	dVolume["ALA"]["CB"] = dV["CT"]
	dVolume["ALA"]["H"] = dV["H"]
	dVolume["ALA"]["HB1"] = dV["HC"]
	dVolume["ALA"]["HB2"] = dV["HC"]
	dVolume["ALA"]["HB3"] = dV["HC"]
	dVolume["ALA"]["HA"] = dV["H1"]

	dVolume["ASP"] = {}
	dVolume["ASP"]["N"] = dV["N2m"]
	dVolume["ASP"]["CA"] = dV["CT"]
	dVolume["ASP"]["C"] = dV["C"]
	dVolume["ASP"]["O"] = dV["O"]
	dVolume["ASP"]["CB"] = dV["CT"]
	dVolume["ASP"]["CG"] = dV["C"]
	dVolume["ASP"]["OD1"] = dV["O2"]
	dVolume["ASP"]["OD2"] = dV["O2"]
	dVolume["ASP"]["H"] = dV["H"]
	dVolume["ASP"]["HA"] = dV["H1"]
	dVolume["ASP"]["HB2"] = dV["HC"]
	dVolume["ASP"]["HB3"] = dV["HC"]


	dVolume["GLU"] = {}
	dVolume["GLU"]["N"] = dV["N2m"]
	dVolume["GLU"]["CA"] = dV["CT"]
	dVolume["GLU"]["C"] = dV["C"]
	dVolume["GLU"]["O"] = dV["O"]
	dVolume["GLU"]["CB"] = dV["CT"]
	dVolume["GLU"]["CG"] = dV["CT"]
	dVolume["GLU"]["CD"] = dV["C"]
	dVolume["GLU"]["OE1"] = dV["O2"]
	dVolume["GLU"]["OE2"] = dV["O2"]
	dVolume["GLU"]["H"] = dV["H"]
	dVolume["GLU"]["HA"] = dV["H1"]
	dVolume["GLU"]["HB2"] = dV["HC"]
	dVolume["GLU"]["HB3"] = dV["HC"]
	dVolume["GLU"]["HG2"] = dV["HC"]
	dVolume["GLU"]["HG3"] = dV["HC"]


	dVolume["LEU"] = {}
	dVolume["LEU"]["N"] = dV["N2m"]
	dVolume["LEU"]["CA"] = dV["CT"]
	dVolume["LEU"]["C"] = dV["C"]
	dVolume["LEU"]["O"] = dV["O"]
	dVolume["LEU"]["CB"] = dV["CT"]
	dVolume["LEU"]["CG"] = dV["CT"]
	dVolume["LEU"]["CD1"] = dV["CT"]
	dVolume["LEU"]["CD2"] = dV["CT"]
	dVolume["LEU"]["H"] = dV["H"]
	dVolume["LEU"]["HA"] = dV["H1"]
	dVolume["LEU"]["HB2"] = dV["HC"]
	dVolume["LEU"]["HB3"] = dV["HC"]
	dVolume["LEU"]["HG"] = dV["HC"]
	dVolume["LEU"]["HD11"] = dV["HC"]
	dVolume["LEU"]["HD12"] = dV["HC"]
	dVolume["LEU"]["HD13"] = dV["HC"]
	dVolume["LEU"]["HD21"] = dV["HC"]
	dVolume["LEU"]["HD22"] = dV["HC"]
	dVolume["LEU"]["HD23"] = dV["HC"]

	dVolume["ASN"] = {}
	dVolume["ASN"]["N"] = dV["N2m"]
	dVolume["ASN"]["CA"] = dV["CT"]
	dVolume["ASN"]["C"] = dV["C"]
	dVolume["ASN"]["O"] = dV["O"]
	dVolume["ASN"]["CB"] = dV["CT"]
	dVolume["ASN"]["CG"] = dV["C"]
	dVolume["ASN"]["ND2"] = dV["N2m"]
	dVolume["ASN"]["OD1"] = dV["O"]
	dVolume["ASN"]["H"] = dV["H"]
	dVolume["ASN"]["HA"] = dV["H1"]
	dVolume["ASN"]["HB2"] = dV["HC"]
	dVolume["ASN"]["HB3"] = dV["HC"]
	dVolume["ASN"]["HD21"] = dV["H"]
	dVolume["ASN"]["HD22"] = dV["H"]


	dVolume["GLN"] = {}
	dVolume["GLN"]["N"] = dV["N2m"]
	dVolume["GLN"]["CA"] = dV["CT"]
	dVolume["GLN"]["C"] = dV["C"]
	dVolume["GLN"]["O"] = dV["O"]
	dVolume["GLN"]["CB"] = dV["CT"]
	dVolume["GLN"]["CG"] = dV["CT"]
	dVolume["GLN"]["CD"] = dV["C"]
	dVolume["GLN"]["NE2"] = dV["N2m"]
	dVolume["GLN"]["OE1"] = dV["O"]
	dVolume["GLN"]["H"] = dV["H"]
	dVolume["GLN"]["HA"] = dV["H1"]
	dVolume["GLN"]["HB2"] = dV["HC"]
	dVolume["GLN"]["HB3"] = dV["HC"]
	dVolume["GLN"]["HG2"] = dV["HC"]
	dVolume["GLN"]["HG3"] = dV["HC"]
	dVolume["GLN"]["HE21"] = dV["H"]
	dVolume["GLN"]["HE22"] = dV["H"]


	dVolume["ILE"] = {}
	dVolume["ILE"]["N"] = dV["N2m"]
	dVolume["ILE"]["CA"] = dV["CT"]
	dVolume["ILE"]["C"] = dV["C"]
	dVolume["ILE"]["O"] = dV["O"]
	dVolume["ILE"]["CB"] = dV["CT"]
	dVolume["ILE"]["CG1"] = dV["CT"]
	dVolume["ILE"]["CG2"] = dV["CT"]
	dVolume["ILE"]["CD1"] = dV["CT"]
	dVolume["ILE"]["H"] = dV["H"]
	dVolume["ILE"]["HA"] = dV["H1"]
	dVolume["ILE"]["HB"] = dV["HC"]
	dVolume["ILE"]["HG12"] = dV["HC"]
	dVolume["ILE"]["HG13"] = dV["HC"]
	dVolume["ILE"]["HG21"] = dV["HC"]
	dVolume["ILE"]["HG22"] = dV["HC"]
	dVolume["ILE"]["HG23"] = dV["HC"]
	dVolume["ILE"]["HD11"] = dV["HC"]
	dVolume["ILE"]["HD12"] = dV["HC"]
	dVolume["ILE"]["HD13"] = dV["HC"]

	dVolume["VAL"] = {}
	dVolume["VAL"]["N"] = dV["N2m"]
	dVolume["VAL"]["CA"] = dV["CT"]
	dVolume["VAL"]["C"] = dV["C"]
	dVolume["VAL"]["O"] = dV["O"]
	dVolume["VAL"]["CB"] = dV["CT"]
	dVolume["VAL"]["CG1"] = dV["CT"]
	dVolume["VAL"]["CG2"] = dV["CT"]
	dVolume["VAL"]["H"] = dV["H"]
	dVolume["VAL"]["HA"] = dV["H1"]
	dVolume["VAL"]["HB"] = dV["HC"]
	dVolume["VAL"]["HG11"] = dV["HC"]
	dVolume["VAL"]["HG12"] = dV["HC"]
	dVolume["VAL"]["HG13"] = dV["HC"]
	dVolume["VAL"]["HG21"] = dV["HC"]
	dVolume["VAL"]["HG22"] = dV["HC"]
	dVolume["VAL"]["HG23"] = dV["HC"]


	dVolume["SER"] = {}
	dVolume["SER"]["N"] = dV["N2m"]
	dVolume["SER"]["CA"] = dV["CT"]
	dVolume["SER"]["C"] = dV["C"]
	dVolume["SER"]["O"] = dV["O"]
	dVolume["SER"]["CB"] = dV["CT"]
	dVolume["SER"]["OG"] = dV["OH"]
	dVolume["SER"]["H"] = dV["H"]
	dVolume["SER"]["HA"] = dV["H1"]
	dVolume["SER"]["HB2"] = dV["H1"]
	dVolume["SER"]["HB3"] = dV["H1"]
	dVolume["SER"]["HG"] = dV["HO"]



	dVolume["THR"] = {}
	dVolume["THR"]["N"] = dV["N2m"]
	dVolume["THR"]["CA"] = dV["CT"]
	dVolume["THR"]["C"] = dV["C"]
	dVolume["THR"]["O"] = dV["O"]
	dVolume["THR"]["CB"] = dV["CT"]
	dVolume["THR"]["OG1"] = dV["OH"]
	dVolume["THR"]["CG2"] = dV["CT"]
	dVolume["THR"]["H"] = dV["H"]
	dVolume["THR"]["HA"] = dV["H1"]
	dVolume["THR"]["HB"] = dV["H1"]
	dVolume["THR"]["HG1"] = dV["HO"]
	dVolume["THR"]["HG21"] = dV["HC"]
	dVolume["THR"]["HG22"] = dV["HC"]
	dVolume["THR"]["HG23"] = dV["HC"]



	dVolume["CYS"] = {}
	dVolume["CYS"]["N"] = dV["N2m"]
	dVolume["CYS"]["CA"] = dV["CT"]
	dVolume["CYS"]["C"] = dV["C"]
	dVolume["CYS"]["O"] = dV["O"]
	dVolume["CYS"]["CB"] = dV["CT"]
	dVolume["CYS"]["SG"] = dV["SH"]
	dVolume["CYS"]["H"] = dV["H"]
	dVolume["CYS"]["HA"] = dV["H1"]
	dVolume["CYS"]["HB1"] = dV["H1"]
	dVolume["CYS"]["HB2"] = dV["H1"]
	dVolume["CYS"]["HG"] = dV["HS"]


	dVolume["PRO"] = {}
	dVolume["PRO"]["N"] = dV["N2m"]
	dVolume["PRO"]["CA"] = dV["CT"]
	dVolume["PRO"]["C"] = dV["C"]
	dVolume["PRO"]["O"] = dV["O"]
	dVolume["PRO"]["CB"] = dV["CT"]
	dVolume["PRO"]["CG"] = dV["CT"]
	dVolume["PRO"]["CD"] = dV["CT"]
	dVolume["PRO"]["HA"] = dV["H1"]
	dVolume["PRO"]["HB2"] = dV["HC"]
	dVolume["PRO"]["HB3"] = dV["HC"]
	dVolume["PRO"]["HG2"] = dV["HC"]
	dVolume["PRO"]["HG3"] = dV["HC"]
	dVolume["PRO"]["HD2"] = dV["H1"]
	dVolume["PRO"]["HD3"] = dV["H1"]



	dVolume["ARG"] = {}
	dVolume["ARG"]["N"] = dV["N2m"]
	dVolume["ARG"]["CA"] = dV["CT"]
	dVolume["ARG"]["C"] = dV["C"]
	dVolume["ARG"]["O"] = dV["O"]
	dVolume["ARG"]["CB"] = dV["CT"]
	dVolume["ARG"]["CG"] = dV["CT"]
	dVolume["ARG"]["CD"] = dV["CT"]
	dVolume["ARG"]["NE"] = dV["N2m"]
	dVolume["ARG"]["CZ"] = dV["CA"]
	dVolume["ARG"]["NH1"] = dV["N2m"]
	dVolume["ARG"]["NH2"] = dV["N2m"]
	dVolume["ARG"]["H"] = dV["H"]
	dVolume["ARG"]["HA"] = dV["H1"]
	dVolume["ARG"]["HB2"] = dV["HC"]
	dVolume["ARG"]["HB3"] = dV["HC"]
	dVolume["ARG"]["HG2"] = dV["HC"]
	dVolume["ARG"]["HG3"] = dV["HC"]
	dVolume["ARG"]["HD2"] = dV["H1"]
	dVolume["ARG"]["HD3"] = dV["H1"]
	dVolume["ARG"]["HE"] = dV["H"]
	dVolume["ARG"]["HH11"] = dV["H"]
	dVolume["ARG"]["HH12"] = dV["H"]
	dVolume["ARG"]["HH21"] = dV["H"]  
	dVolume["ARG"]["HH22"] = dV["H"]


	dVolume["LYS"] = {}
	dVolume["LYS"]["N"] = dV["N2m"]
	dVolume["LYS"]["CA"] = dV["CT"]
	dVolume["LYS"]["C"] = dV["C"]
	dVolume["LYS"]["O"] = dV["O"]
	dVolume["LYS"]["CB"] = dV["CT"]
	dVolume["LYS"]["CG"] = dV["CT"]
	dVolume["LYS"]["CD"] = dV["CT"] 
	dVolume["LYS"]["CE"] = dV["CT"]
	dVolume["LYS"]["NZ"] = dV["N3n"] 
	dVolume["LYS"]["H"] = dV["H"]
	dVolume["LYS"]["HA"] = dV["H1"]
	dVolume["LYS"]["HB2"] = dV["HC"]
	dVolume["LYS"]["HB3"] = dV["HC"]
	dVolume["LYS"]["HG2"] = dV["HC"]
	dVolume["LYS"]["HG3"] = dV["HC"]
	dVolume["LYS"]["HD2"] = dV["HC"]
	dVolume["LYS"]["HD3"] = dV["HC"]
	dVolume["LYS"]["HE2"] = dV["HP"]
	dVolume["LYS"]["HE3"] = dV["HP"]
	dVolume["LYS"]["HZ2"] = dV["H"]
	dVolume["LYS"]["HZ1"] = dV["H"]   
	dVolume["LYS"]["HZ3"] = dV["H"]


	dVolume["HIE"] = {}
	dVolume["HIE"]["N"] = dV["N2m"]
	dVolume["HIE"]["CA"] = dV["CT"]
	dVolume["HIE"]["C"] = dV["C"]
	dVolume["HIE"]["O"] = dV["O"]
	dVolume["HIE"]["CB"] = dV["CT"]
	dVolume["HIE"]["CG"] = dV["CA"]
	dVolume["HIE"]["ND1"] = dV["N2m"]
	dVolume["HIE"]["CE1"] = dV["CA"]
	dVolume["HIE"]["NE2"] = dV["N2m"]
	dVolume["HIE"]["CD2"] = dV["CA"]
	dVolume["HIE"]["H"] = dV["H"]
	dVolume["HIE"]["HA"] = dV["H1"]
	dVolume["HIE"]["HB2"] = dV["HC"]
	dVolume["HIE"]["HB3"] = dV["HC"]
	dVolume["HIE"]["HE1"] = dV["H5"]
	dVolume["HIE"]["HE2"] = dV["H"]
	dVolume["HIE"]["HD2"] = dV["H4"]

	dVolume["HID"] = {}
	dVolume["HID"]["N"] = dV["N2m"]
	dVolume["HID"]["CA"] = dV["CT"]
	dVolume["HID"]["C"] = dV["C"]
	dVolume["HID"]["O"] = dV["O"]
	dVolume["HID"]["CB"] = dV["CT"]
	dVolume["HID"]["CG"] = dV["CA"]
	dVolume["HID"]["ND1"] = dV["N2m"]
	dVolume["HID"]["CE1"] = dV["CA"]
	dVolume["HID"]["NE2"] = dV["N2m"]
	dVolume["HID"]["CD2"] = dV["CA"]
	dVolume["HID"]["H"] = dV["H"]
	dVolume["HID"]["HA"] = dV["H1"]
	dVolume["HID"]["HB2"] = dV["HC"]
	dVolume["HID"]["HB3"] = dV["HC"]
	dVolume["HID"]["HE1"] = dV["H5"]
	dVolume["HID"]["HD1"] = dV["H"]
	dVolume["HID"]["HD2"] = dV["H4"]

	dVolume["MET"] = {}
	dVolume["MET"]["N"] = dV["N2m"]
	dVolume["MET"]["CA"] = dV["CT"]
	dVolume["MET"]["C"] = dV["C"]
	dVolume["MET"]["O"] = dV["O"]
	dVolume["MET"]["CB"] = dV["CT"]
	dVolume["MET"]["CG"] = dV["CT"]
	dVolume["MET"]["SD"] = dV["S"]
	dVolume["MET"]["CE"] = dV["CT"]
	dVolume["MET"]["H"] = dV["H"]
	dVolume["MET"]["HA"] = dV["H1"]
	dVolume["MET"]["HB2"] = dV["HC"]
	dVolume["MET"]["HB3"] = dV["HC"]
	dVolume["MET"]["HG2"] = dV["H1"]
	dVolume["MET"]["HG3"] = dV["H1"]
	dVolume["MET"]["HE2"] = dV["H1"]
	dVolume["MET"]["HE3"] = dV["H1"]
	dVolume["MET"]["HE1"] = dV["H1"]



	dVolume["PHE"] = {}
	dVolume["PHE"]["N"] = dV["N2m"]
	dVolume["PHE"]["CA"] = dV["CT"]
	dVolume["PHE"]["C"] = dV["C"]
	dVolume["PHE"]["O"] = dV["O"]
	dVolume["PHE"]["CB"] = dV["CT"]
	dVolume["PHE"]["CG"] = dV["CA"]
	dVolume["PHE"]["CD1"] = dV["CA"]
	dVolume["PHE"]["CD2"] = dV["CA"]
	dVolume["PHE"]["CE1"] = dV["CA"]
	dVolume["PHE"]["CE2"] = dV["CA"]
	dVolume["PHE"]["CZ"] = dV["CA"]
	dVolume["PHE"]["H"] = dV["H"]
	dVolume["PHE"]["HA"] = dV["H1"]
	dVolume["PHE"]["HB2"] = dV["HC"]
	dVolume["PHE"]["HB3"] = dV["HC"]
	dVolume["PHE"]["HD1"] = dV["HA"]
	dVolume["PHE"]["HD2"] = dV["HA"]
	dVolume["PHE"]["HE1"] = dV["HA"]
	dVolume["PHE"]["HE2"] = dV["HA"]
	dVolume["PHE"]["HZ"] = dV["HA"]




	dVolume["TYR"] = {}
	dVolume["TYR"]["N"] = dV["N2m"]
	dVolume["TYR"]["CA"] = dV["CT"]
	dVolume["TYR"]["C"] = dV["C"]
	dVolume["TYR"]["O"] = dV["O"]
	dVolume["TYR"]["CB"] = dV["CT"]
	dVolume["TYR"]["CG"] = dV["CA"]
	dVolume["TYR"]["CD1"] =  dV["CA"]
	dVolume["TYR"]["CD2"] =  dV["CA"]
	dVolume["TYR"]["CE1"] = dV["CA"]
	dVolume["TYR"]["CE2"] = dV["CA"]
	dVolume["TYR"]["CZ"] = dV["CA"]
	dVolume["TYR"]["OH"] = dV["OH"]
	dVolume["TYR"]["H"] = dV["H"]
	dVolume["TYR"]["HA"] = dV["H1"]
	dVolume["TYR"]["HB2"] = dV["HC"]
	dVolume["TYR"]["HB3"] = dV["HC"]
	dVolume["TYR"]["HD1"] = dV["HA"]
	dVolume["TYR"]["HD2"] = dV["HA"]
	dVolume["TYR"]["HE1"] = dV["HA"]
	dVolume["TYR"]["HE2"] = dV["HA"]
	dVolume["TYR"]["HH"] = dV["HO"]




	dVolume["TRP"] = {}
	dVolume["TRP"]["N"] = dV["N2m"]
	dVolume["TRP"]["CA"] = dV["CT"]
	dVolume["TRP"]["C"] = dV["C"]
	dVolume["TRP"]["O"] = dV["O"]
	dVolume["TRP"]["CB"] = dV["CT"]
	dVolume["TRP"]["CG"] = dV["CA"]
	dVolume["TRP"]["CD1"] = dV["CA"]
	dVolume["TRP"]["CD2"] = dV["CA"]
	dVolume["TRP"]["NE1"] = dV["N2m"]
	dVolume["TRP"]["CE2"] = dV["CA"]
	dVolume["TRP"]["CE3"] = dV["CA"]
	dVolume["TRP"]["CZ2"] = dV["CA"]
	dVolume["TRP"]["CZ3"] = dV["CA"]
	dVolume["TRP"]["CH2"] = dV["CA"]
	dVolume["TRP"]["H"] = dV["H"]
	dVolume["TRP"]["HA"] = dV["H1"]
	dVolume["TRP"]["HB2"] = dV["HC"]
	dVolume["TRP"]["HB3"] = dV["HC"]
	dVolume["TRP"]["HD1"] = dV["H4"]
	dVolume["TRP"]["HE1"] = dV["H"]
	dVolume["TRP"]["HE3"] = dV["HA"]
	dVolume["TRP"]["HZ2"] = dV["HA"]
	dVolume["TRP"]["HZ3"] = dV["HA"]
	dVolume["TRP"]["HH2"] = dV["HA"]

	return dVolume
