## Herwig++ config for the CTEQ6L1 UE-EE-5 tune series with NLO events read from an LHEF file
include("MC15JobOptions/Herwigpp_UEEE5_CTEQ6L1_Common.py")

from Herwigpp_i import config as hw
genSeq.Herwigpp.Commands += hw.lhef_cmds(filename="events.lhe", nlo=False).splitlines()
