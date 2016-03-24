## Base configuration for HERWIG
from Herwig_i.Herwig_iConf import Herwig
genSeq += Herwig()
evgenConfig.generators += ["Herwig"]

## HERWIG common config/EW parameters

genSeq.Herwig.HerwigCommand = [
    # Weak mixing angle
    "swein 0.23113",
    # Masses and widths
    "rmass 6 172.5",    # TOP mass
    "rmass 198 80.399", # PDG2010 W mass
    "rmass 199 80.399", # PDG2010 W mass
    "rmass 200 91.1876",# PDG2010 Z0 mass
    "gamw 2.085",       # PDG2010 W width
    "gamz 2.4952",      # PDG2010 Z0 width
    # Main JIMMY MPI switches
    "jmueo 1",          # Underlying event option (2->2 QCD)
    "msflag 1",         # Turn on multiple interactions
    "jmbug 0",
    # Fragmentation
    "clpow 1.20",       # Fix the ratio of mesons to baryons in B decays
    # Others
    "pltcut 0.0000000000333", # Make Ks and Lambda stable
    "ptmin 10.",        # (D=10.) Min pT in hadronic jet production
    "mixing 1",         # (D=1) Include neutral B meson mixing
    "maxpr 5"           # Print out event record for first 5 events
    ]
