## Herwig++ config for the CTEQ6L1 UE-EE-5 tune series with an LO ME PDF
include("MC15JobOptions/Herwigpp_Base_Fragment.py")

## Construct command set
from Herwigpp_i import config as hw
cmds = hw.energy_cmds(int(runArgs.ecmEnergy)) + hw.base_cmds() \
    + hw.lo_pdf_cmds("cteq6ll.LHpdf") \
    + hw.ue_tune_cmds("UE-EE-5-CTEQ6L1")
genSeq.Herwigpp.Commands += cmds.splitlines()
del cmds

evgenConfig.tune = "CTEQ6L1-UE-EE-5"
