## EvtGen fragment for Herwig/Jimmy
## EvtGen is run in a separate afterburn substep, so we need an if... else

if runArgs.trfSubstepName == 'generate' :
  runArgs.maxEvents = int(runArgs.maxEvents * 1.05 + 1)
  evgenConfig.generators += ["EvtGen"]

if runArgs.trfSubstepName == 'afterburn':
  evgenConfig.generators += ["Herwig"]
  include("MC15JobOptions/EvtGen_Fragment.py")
  genSeq.EvtInclusiveDecay.outputKeyName = "GEN_EVENT"
  genSeq.EvtInclusiveDecay.readExisting = True
  evgenConfig.auxfiles += ['inclusiveP8DsDPlus.pdt']
  genSeq.EvtInclusiveDecay.pdtFile = "inclusiveP8DsDPlus.pdt"
