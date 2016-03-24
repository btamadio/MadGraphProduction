include("MC15JobOptions/Herwigpp_Base_Fragment.py")

from Herwigpp_i import config as hw
cmds = hw.energy_cmds(runArgs.ecmEnergy) + hw.base_cmds() \
    + hw.nlo_pdf_cmds("CT10f4.LHgrid", "cteq6ll.LHpdf") \
    + hw.ue_tune_cmds("UE-EE-5-CTEQ6L1") \
    + hw.lhef_cmds(filename="events.lhe", nlo=True) 
genSeq.Herwigpp.Commands += cmds.splitlines()
del cmds
