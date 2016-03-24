## Config for Py8 tune A14 with MSTW2008LO
include("MC15JobOptions/Pythia8_Base_Fragment.py")

genSeq.Pythia8.Commands += [
    "Tune:ee = 7", 
    "Tune:pp = 14",
    "PDF:useLHAPDF = on",
    "PDF:LHAPDFset = MSTW2008lo68cl",
    "SpaceShower:rapidityOrder = on",
    "SigmaProcess:alphaSvalue = 0.140",
    "SpaceShower:pT0Ref = 1.62",
    "SpaceShower:pTmaxFudge = 0.92",
    "SpaceShower:pTdampFudge = 1.14",
    "SpaceShower:alphaSvalue = 0.129",
    "TimeShower:alphaSvalue = 0.129",
    "BeamRemnants:primordialKThard = 1.82",
    "MultipartonInteractions:pT0Ref = 2.22",
    "MultipartonInteractions:alphaSvalue = 0.127",
    "BeamRemnants:reconnectRange = 1.87"]

evgenConfig.tune = "A14 MSTW2008LO"
