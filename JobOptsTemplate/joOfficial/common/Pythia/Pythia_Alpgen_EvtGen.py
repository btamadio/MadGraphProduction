
if runArgs.trfSubstepName == 'afterburn':
  evgenConfig.generators += ["Alpgen"]

include('MC15JobOptions/Pythia_EvtGen.py')
