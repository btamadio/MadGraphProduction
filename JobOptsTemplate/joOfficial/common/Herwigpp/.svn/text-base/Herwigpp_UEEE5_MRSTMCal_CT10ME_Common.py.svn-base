## Herwig++ config for the MRSTMCal UE-EE-5 tune series with an NLO ME PDF
include("MC15JobOptions/Herwigpp_Base_Fragment.py")

## Construct command set
from Herwigpp_i import config as hw
cmds = hw.energy_cmds(runArgs.ecmEnergy) + hw.base_cmds() \
     + hw.nlo_pdf_cmds("CT10.LHgrid", "MRSTMCal.LHgrid") \
     + hw.ue_tune_cmds("UE-EE-5-LO**")
genSeq.Herwigpp.Commands += cmds.splitlines()
del cmds

evgenConfig.tune = "LO**-UE-EE-5"
