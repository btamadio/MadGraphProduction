## Config for Py8 tune A2 with CTEQ6L1
include("MC15JobOptions/Pythia8_Base_Fragment.py")

genSeq.Pythia8.Commands += [
    "Tune:pp = 5",
    "PDF:useLHAPDF = on",
    "PDF:LHAPDFset = MSTW2008lo68cl.LHgrid",
    "MultipartonInteractions:bProfile = 4",
    "MultipartonInteractions:a1 = 0.01",
    "MultipartonInteractions:pT0Ref = 1.87",
    "MultipartonInteractions:ecmPow = 0.28",
    "BeamRemnants:reconnectRange = 5.32",
    "SpaceShower:rapidityOrder=0"]
evgenConfig.tune = "AU2 MSTW2008LO"
