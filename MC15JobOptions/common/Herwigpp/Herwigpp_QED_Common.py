## Common job option for gamma gamma processes in Herwig++
## MPI tune is not relevant as the pdf_gammagamma_cmds() function disables MPI
## Contact: Oldrich Kepka
include("MC15JobOptions/Herwigpp_Base_Fragment.py")
from Herwigpp_i import config as hw
cmds = hw.energy_cmds(runArgs.ecmEnergy) + hw.base_cmds() + hw.pdf_gammagamma_cmds()
cmds += "create ThePEG::O1AlphaS /Herwig/AlphaQCD_O1 O1AlphaS.so\n"
cmds += "set /Herwig/Generators/LHCGenerator:StandardModelParameters:QCD/RunningAlphaS /Herwig/AlphaQCD_O1\n"
genSeq.Herwigpp.Commands += cmds.splitlines()
del cmds
