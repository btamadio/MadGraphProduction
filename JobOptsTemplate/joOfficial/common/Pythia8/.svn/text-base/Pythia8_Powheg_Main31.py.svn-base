## Configure Pythia 8 to shower PoWHEG input using Main31 shower veto
include("MC15JobOptions/Pythia8_Powheg.py")
genSeq.Pythia8.Commands += [ 'SpaceShower:pTmaxMatch = 2',
                             'TimeShower:pTmaxMatch = 2'  ]
genSeq.Pythia8.UserHook = 'Main31'
