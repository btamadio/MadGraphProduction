## Herwig++ config for the CTEQ6L1 UE-EE-5 tune series with a NNPDF3.0 NLO ME PDF
include("MC15JobOptions/Herwigpp_Base_Fragment.py")

## Construct command set
from Herwigpp_i import config as hw
cmds = hw.energy_cmds(runArgs.ecmEnergy) + hw.base_cmds() \
    + hw.nlo_pdf_cmds("NNPDF30_nlo_as_0118.LHgrid", "cteq6ll.LHpdf") \
    + hw.ue_tune_cmds("UE-EE-5-CTEQ6L1")
genSeq.Herwigpp.Commands += cmds.splitlines()
del cmds

evgenConfig.tune = "CTEQ6L1-UE-EE-5"
