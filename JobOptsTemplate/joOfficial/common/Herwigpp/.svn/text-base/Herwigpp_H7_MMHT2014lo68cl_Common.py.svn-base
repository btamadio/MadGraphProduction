## Herwig++ config for the H7-UE-MMHT tune series with an LO ME PDF
include("MC15JobOptions/Herwigpp_Base_Fragment.py")

## Construct command set
from Herwigpp_i import config as hw
cmds = hw.energy_cmds(runArgs.ecmEnergy) + hw.base_cmds() \
    + hw.nlo_pdf_cmds("CT10.LHgrid", "MMHT2014lo68cl.LHpdf") \
    + hw.ue_tune_cmds("H7-UE-MMHT")
genSeq.Herwigpp.Commands += cmds.splitlines()
del cmds

evgenConfig.tune = "H7-UE-MMHT"

