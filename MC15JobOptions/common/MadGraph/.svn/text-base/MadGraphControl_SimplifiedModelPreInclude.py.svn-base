# Generator transform pre-include
#  Gets us ready for on-the-fly SUSY SM generation

# Simple variable setups
njets = -1
masses = {}
decays = {}

# Event multipliers for getting more events out of madgraph to feed through athena (esp. for filters)
evt_multiplier = 2.0

# Useful definitions
squarks = []
squarksl = []
for anum in [1,2,3,4]:
    squarks += [str(1000000+anum),str(-1000000-anum),str(2000000+anum),str(-2000000-anum)]
    squarksl += [str(1000000+anum),str(-1000000-anum)]
dict_index_syst = {0:'scalefactup',
                   1:'scalefactdown',
                   2:'alpsfactup',
                   3:'alpsfactdown',
                   4:'moreFSR',
                   5:'lessFSR',
                   6:'qup',
                   7:'qdown'}

# Basic settings for production and filters
SLHAonly = False
syst_mod=None

if hasattr(runArgs,'EventMultiplier'): evt_multiplier=runArgs.EventMultiplier
if runArgs.maxEvents>0:
    nevts=runArgs.maxEvents*evt_multiplier
else:
    nevts=5000*evt_multiplier
evt_multiplier=-1

# in case someone needs to be able to keep the output directory for testing
keepOutput = False

include("MC15JobOptions/Pythia8_A14_NNPDF23LO_EvtGen_Common.py")
include("MC15JobOptions/Pythia8_MadGraph.py")
