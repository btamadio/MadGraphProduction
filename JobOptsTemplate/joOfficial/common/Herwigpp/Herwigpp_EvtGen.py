## Run EvtGen afterburner on top of Pythia 8
assert hasattr(genSeq, "Herwigpp")
include("MC15JobOptions/EvtGen_Fragment.py")
evgenConfig.auxfiles += ['HerwigppInclusiveP8.pdt']
genSeq.EvtInclusiveDecay.pdtFile = "HerwigppInclusiveP8.pdt"
