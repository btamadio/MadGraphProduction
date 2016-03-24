## Config for Py8 tune AZ with CTEQ6L1
include("MC15JobOptions/Pythia8_Base_Fragment.py")

genSeq.Pythia8.Commands += [
    "PDF:LHAPDFset = cteq6ll.LHpdf",
    "BeamRemnants:primordialKThard =  1.713",
    "SpaceShower:pT0Ref = 0.586",
    "SpaceShower:alphaSvalue = 0.12374",
    "MultipartonInteractions:pT0Ref = 2.18"]

evgenConfig.tune = "AZ CTEQ6L1"





