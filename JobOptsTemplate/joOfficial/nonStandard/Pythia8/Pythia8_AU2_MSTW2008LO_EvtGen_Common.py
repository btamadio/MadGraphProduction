## Config for Py8 tune AU2 with MSTW2008LO 
## The default version of this tune fragment include EvtGen for standardised b fragmentation 
## but it is also non standard 

# Reference the non-standard version without EvtGen
include("MC15JobOptions/nonStandard/Pythia8_AU2_MSTW2008LO_Common.py")

# Add EvtGen for b fragmentation.  No EvtGen is available in "nonStandard"
include("MC15JobOptions/Pythia8_EvtGen.py")

