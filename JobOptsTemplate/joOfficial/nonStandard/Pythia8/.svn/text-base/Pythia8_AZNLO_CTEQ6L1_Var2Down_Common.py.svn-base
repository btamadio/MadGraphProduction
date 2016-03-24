## Config for Py8 tune AZNLO with CTEQ6L1
include("MC15JobOptions/Pythia8_Base_Fragment.py")

genSeq.Pythia8.Commands += [
        "Tune:pp = 5",
        "PDF:useLHAPDF = on",
        "PDF:LHAPDFset = cteq6ll.LHpdf",
        "BeamRemnants:primordialKThard = 1.737",
        "SpaceShower:alphaSorder = 2",
        "SpaceShower:alphaSvalue = 0.118",
        "SpaceShower:pT0Ref = 2.004",
        "MultipartonInteractions:pT0Ref = 2.002887"
        ]

evgenConfig.tune = "AZNLO CTEQ6L1"

# needs Pythia8 Main31 matching
include('MC15JobOptions/Pythia8_Powheg_Main31.py')

genSeq.Pythia8.UserModes += ['Main31:NFinal = 1',
                             'Main31:pTHard = 0',
                             'Main31:pTdef = 2'
                             ]
