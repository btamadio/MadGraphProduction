## Config for Py8 tune A2 with MSTW2008LO
## This is the version without EvtGen, but the default is to use EvtGen
## The default version is in common/Pythia8/Pythia8_A2_MSTW2008LO_Common.py

include("MC15JobOptions/Pythia8_Base_Fragment.py")
	
genSeq.Pythia8.Commands += [
    "Tune:pp = 5",
    "PDF:useLHAPDF = on",
    "PDF:LHAPDFset = MSTW2008lo68cl.LHgrid",
    "MultipartonInteractions:bProfile = 4",
    "MultipartonInteractions:a1 = 0.03",
    "MultipartonInteractions:pT0Ref = 1.90",
    "MultipartonInteractions:ecmPow = 0.30",
    "BeamRemnants:reconnectRange = 2.28",
    "SpaceShower:rapidityOrder=0"]
evgenConfig.tune = "A2 MSTW2008LO"
