## Base configuration for PYTHIA 6
from Pythia_i.Pythia_iConf import Pythia
genSeq += Pythia()
evgenConfig.generators += ["Pythia"]

genSeq.Pythia.PythiaCommand = [
    # initializations
    "pyinit pylisti 12",
    "pyinit pylistf 1",
    "pystat 1 3 4 5",
    "pyinit dumpr 1 5",
    # Weak mixing angle
    "pydat1 paru 102 0.23113",
    # Masses
    "pydat2 pmas 6 1 172.5",     # Top mass
    "pydat2 pmas 24 1 80.399",   # PDG2010 W mass
    "pydat2 pmas 23 1 91.1876",  # PDG2010 Z0 mass
    # Widths (these have no effect since widths are calculated perturbatively in PYTHIA)
    #"pydat2 pmas 24 2 2.085",   # PDG2010 W width
    #"pydat2 pmas 23 2 2.4952",  # PDG2010 Z0 width
    ]
